1. The challenge provided a firmware file and a remote IP and port.

2. After connecting to the machine, it asked for some credentials.

```shell-session
$ nc 68.183.47.198 31878
��������
hwtheneedle-501669-66f7bc65c9-fbvn9 login:
```

3. We can use the `binwalk --extract` to extract files in the binary.

4. Then, we used the plaintext "login" to search for the possible files.

```
$ grep -r "login" .          
grep: ./busybox: binary file matches
grep: ./libc.so: binary file matches
./config_generate:              set system.@system[-1].ttylogin='0'
./login.sh:[ "$(uci get system.@system[0].ttylogin)" == 1 ] || exec /bin/ash --login
./login.sh:exec /bin/login
grep: ./rpcd: binary file matches
./inittab:::askconsole:/usr/libexec/login.sh
grep: ./dropbear: binary file matches
./busybox.list:/bin/login
./profile:in order to prevent unauthorized SSH logins.
grep: ./pppd: binary file matches
./99_10_failsafe_login:failsafe_netlogin () {
./99_10_failsafe_login: ash --login
./99_10_failsafe_login: echo "Please reboot system when done with failsafe network logins"
./99_10_failsafe_login:boot_hook_add failsafe failsafe_netlogin
grep: ./squashfs-root/lib/libc.so: binary file matches
./squashfs-root/lib/upgrade/common.sh:                          *procd*|*ash*|*init*|*watchdog*|*ssh*|*dropbear*|*telnet*|*login*|*hostapd*|*wpa_supplicant*|*nas*|*relayd*) : ;;
./squashfs-root/lib/preinit/99_10_failsafe_login:failsafe_netlogin () {
./squashfs-root/lib/preinit/99_10_failsafe_login:       ash --login
./squashfs-root/lib/preinit/99_10_failsafe_login:       echo "Please reboot system when done with failsafe network logins"
./squashfs-root/lib/preinit/99_10_failsafe_login:boot_hook_add failsafe failsafe_netlogin
grep: ./squashfs-root/sbin/rpcd: binary file matches
grep: ./squashfs-root/bin/busybox: binary file matches
./squashfs-root/bin/config_generate:            set system.@system[-1].ttylogin='0'
./squashfs-root/usr/lib/lua/luci/model/cbi/admin_system/admin.lua:ra = s:option(Flag, "RootPasswordAuth", translate("Allow root logins with password"),
./squashfs-root/usr/lib/lua/luci/model/cbi/admin_system/admin.lua:      translate("Allow the <em>root</em> user to login with password"))
./squashfs-root/usr/lib/opkg/info/busybox.list:/bin/login
./squashfs-root/usr/lib/opkg/info/base-files.list:/usr/libexec/login.sh
./squashfs-root/usr/lib/opkg/info/base-files.list:/lib/preinit/99_10_failsafe_login
grep: ./squashfs-root/usr/sbin/dropbear: binary file matches
grep: ./squashfs-root/usr/sbin/pppd: binary file matches
./squashfs-root/usr/share/rpcd/acl.d/unauthenticated.json:                              "login"
./squashfs-root/usr/libexec/login.sh:[ "$(uci get system.@system[0].ttylogin)" == 1 ] || exec /bin/ash --login
./squashfs-root/usr/libexec/login.sh:exec /bin/login
./squashfs-root/etc/inittab:::askconsole:/usr/libexec/login.sh
./squashfs-root/etc/config/rpcd:config login
./squashfs-root/etc/scripts/telnetd.sh: if [ -f "/usr/sbin/login" ]; then
./squashfs-root/etc/scripts/telnetd.sh:         telnetd -l "/usr/sbin/login" -u Device_Admin:$sign      -i $lf &
./squashfs-root/etc/profile:in order to prevent unauthorized SSH logins.
./common.sh:                       *procd*|*ash*|*init*|*watchdog*|*ssh*|*dropbear*|*telnet*|*login*|*hostapd*|*wpa_supplicant*|*nas*|*relayd*) : ;;
./admin.lua:ra = s:option(Flag, "RootPasswordAuth", translate("Allow root logins with password"),
./admin.lua:    translate("Allow the <em>root</em> user to login with password"))
./unauthenticated.json:                         "login"
./telnetd.sh:   if [ -f "/usr/sbin/login" ]; then
./telnetd.sh:           telnetd -l "/usr/sbin/login" -u Device_Admin:$sign      -i $lf &
./base-files.list:/usr/libexec/login.sh
./base-files.list:/lib/preinit/99_10_failsafe_login
```

5. The content in `squashfs-root/etc/scripts/telnetd.sh` seems promising. And we also found `$sign` in `squashfs-root//etc/config/sign` as `qS6-X/n]u>fVfAt!` 

```
$ cat squashfs-root/etc/scripts/telnetd.sh
#!/bin/sh
sign=`cat /etc/config/sign`
TELNETD=`rgdb
TELNETD=`rgdb -g /sys/telnetd`
if [ "$TELNETD" = "true" ]; then
        echo "Start telnetd ..." > /dev/console
        if [ -f "/usr/sbin/login" ]; then
                lf=`rgbd -i -g /runtime/layout/lanif`
                telnetd -l "/usr/sbin/login" -u Device_Admin:$sign      -i $lf &
        else
                telnetd &
        fi
fi 
```

6. Use `Device_Admin:qS6-X/n]u>fVfAt!` and we log in to the machine.