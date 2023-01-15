1. We visited the page. On this page, we got two seemingly attractive information `/964430b4cdd199af19b986eaf2193b21f32542d0/bootstrap/css/bootstrap.min.css` and an administrator name `Reese`.

```
HTTP/1.1 200 OK
Accept-Ranges: bytes
Content-Length: 2214
Content-Type: text/html; charset=utf-8
Last-Modified: Tue, 27 Oct 2020 15:51:14 GMT
Date: Sat, 14 Jan 2023 17:58:46 GMT

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Phonebook - Login</title>

    <!-- Bootstrap core CSS -->

<link href="/964430b4cdd199af19b986eaf2193b21f32542d0/bootstrap/css/bootstrap.min.css" rel="stylesheet">

<meta name="theme-color" content="#563d7c">

    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>

    <!-- Custom styles for this template -->
    <link href="/964430b4cdd199af19b986eaf2193b21f32542d0/login.css" rel="stylesheet">
  </head>
  <body class="text-center">

    <form class="form-signin" action="/login" method="post">
      <div class="alert alert-danger" role="alert" id="message" style="visibility: hidden;"></div>
<script>
  const queryString = window.location.search;
if (queryString) {
  const urlParams = new URLSearchParams(queryString);
  const message = urlParams.get('message');
  if (message) {
    document.getElementById("message").innerHTML = message;
    document.getElementById("message").style.visibility = "visible";
    }
  }
</script>
  <img class="mb-4" src="/964430b4cdd199af19b986eaf2193b21f32542d0/phone-icon.png" alt="" width="72" height="72">
  <h1 class="h3 mb-3 font-weight-normal">Please login</h1>
  <input type="text" id="username" name="username" class="form-control" placeholder="Username" required autofocus>
  <input type="password" id="password" name="password" class="form-control" placeholder="Password" required>
  <br />
  <div class="checkbox mb-3">
    <label>
      <input type="checkbox" value="remember-me"> Remember me
    </label>
  </div>
  <button class="btn btn-lg btn-primary btn-block" type="submit">Login</button>

  <br /> <br />

  <div class="alert alert-info" role="alert">
  New (9.8.2020): You can now login using the workstation username and password! - Reese
  </div>

</form>
</body>
</html>
```

1. We first tried to look for another page. However, there is nothing.

```
$ gobuster dir -u http://161.35.161.184:30688 -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 64
===============================================================
Gobuster v3.3
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://161.35.161.184:30688
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.3
[+] Timeout:                 10s
===============================================================
2023/01/14 09:31:49 Starting gobuster in directory enumeration mode
===============================================================
/login                (Status: 200) [Size: 2214]

```

2. We then tried to SQL injection. We filled in `admin") -- ` in the username field, and then the response became `500 Internal Server Error`. It could be a sign of SQLi working.

3. After many tries, we discovered that we could use `*` as a password to log in. In other words, the wildcard was enabled in the SQL.

4. After login, we could search the users (`reese` was there), but there was nothing like the flag. Thus, we decided to log in again using `*:HTB{*}` and it worked. It meant the flag is the password. 

5. We can write a script to brute force the password then.