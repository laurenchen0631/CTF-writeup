> A Junior Developer just switched to a new source control platform. Can you find the secret token?

1. We checked the `config.json` and there was a base64 string: `UmVkIEhlcnJpbmcsIHJlYWQgdGhlIEpTIGNhcmVmdWxseQ==`. After decoding, it showed `Red Herring, read the JS carefully`.
   
2. We checked the `bot.js, and unfortunately, there was nothing that could show us the token.

3. We checkout the directory with `ls -al`, and there was `.git` directory, and thus we can check the commit logs.

```
$ ls -al
total 16
drwxrwxr-x@  5 lorne  staff   160 May 30  2019 .
drwx------+ 15 lorne  staff   480 Jan  4 09:57 ..
drwxrwxr-x@ 14 lorne  staff   448 Jan  4 10:04 .git
-rw-rw-r--@  1 lorne  staff  2635 May 30  2019 bot.js
-rw-rw-r--@  1 lorne  staff   199 May 30  2019 config.json

$ git log
commit edc5aabf933f6bb161ceca6cf7d0d2160ce333ec (HEAD -> master)
Author: SherlockSec <dan@lights.htb>
Date:   Fri May 31 14:16:43 2019 +0100
 
    Added some whitespace for readability!
 
commit 47241a47f62ada864ec74bd6dedc4d33f4374699
Author: SherlockSec <dan@lights.htb>
Date:   Fri May 31 12:00:54 2019 +0100
 
    Thanks to contributors, I removed the unique token as it was a security risk. Thanks for reporting responsibly!
 
commit ddc606f8fa05c363ea4de20f31834e97dd527381
Author: SherlockSec <dan@lights.htb>
Date:   Fri May 31 09:14:04 2019 +0100
 
    Added some more comments for the lovely contributors! Thanks for helping out!
 
commit 335d6cfe3cdc25b89cae81c50ffb957b86bf5a4a
Author: SherlockSec <dan@lights.htb>
Date:   Thu May 30 22:16:02 2019 +0100
 
    Moving to Git, first time using it. First Commit!
```

4. The commit with message "Thanks to contributors, I removed the unique token as it was a security risk. Thanks for reporting responsibly!" could contain the token and thus we check out to that commit and check the config again.

```
$ git show 47241a47f62ada864ec74bd6dedc4d33f4374699
commit 47241a47f62ada864ec74bd6dedc4d33f4374699
Author: SherlockSec <dan@lights.htb>
Date:   Fri May 31 12:00:54 2019 +0100
 
    Thanks to contributors, I removed the unique token as it was a security risk. Thanks for reporting responsibly!
 
diff --git a/config.json b/config.json
index 316dc21..6735aa6 100644
--- a/config.json
+++ b/config.json
@@ -1,6 +1,6 @@
 {
 
-       "token": "SFRCe3YzcnNpMG5fYzBudHIwbF9hbV9JX3JpZ2h0P30=",
+       "token": "Replace me with token when in use! Security Risk!",
        "prefix": "~",
        "lightNum": "1337",
        "username": "UmVkIEhlcnJpbmcsIHJlYWQgdGhlIEpTIGNhcmVmdWxseQ==",
```

5. `SFRCe3YzcnNpMG5fYzBudHIwbF9hbV9JX3JpZ2h0P30` is base64-encoded token that we were looking for.
