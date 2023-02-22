1. We ran the program to test first, and it asked for password.

```
$ ./exatlon_v1             

███████╗██╗  ██╗ █████╗ ████████╗██╗      ██████╗ ███╗   ██╗       ██╗   ██╗ ██╗
██╔════╝╚██╗██╔╝██╔══██╗╚══██╔══╝██║     ██╔═══██╗████╗  ██║       ██║   ██║███║
█████╗   ╚███╔╝ ███████║   ██║   ██║     ██║   ██║██╔██╗ ██║       ██║   ██║╚██║
██╔══╝   ██╔██╗ ██╔══██║   ██║   ██║     ██║   ██║██║╚██╗██║       ╚██╗ ██╔╝ ██║
███████╗██╔╝ ██╗██║  ██║   ██║   ███████╗╚██████╔╝██║ ╚████║███████╗╚████╔╝  ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═══╝   ╚═╝


[+] Enter Exatlon Password  :
```

2. We extracted readable strings from the program, and it seemed it is encrypted using [UPX packer](https://upx.github.io/).

```
$ strings -n 20 exatlon_v1
 !#9999$`ab9999cdef9999ghij9999klmn9999opqr9999stuv9999wxyz9999{|}~9999
ST9999UVWX9999YZ[\9999]^_
 !rrrr"#$%rrrr&'()rrrr*+,-rrrr./01rrrr2345rrrr6789rrrr:;<=rrrr>?@ArrrrBCDErrrrFGHIrrrrJKLMrrrrNOPQ
T9999UVWX9999YZ[\7S89]^3
 rrrr!"#$rrrr%&'(rrrr)*+,rrrr-./0rrrr1234rrrr5678rrrr9;<=rrrr>@ABrrrrCDFJrrrrKLMNrrrrOPRSrrrrTUVWrrrrXYZ[rrrr\]^_rrrr`abcrrrrdefgrrrrhijkrrrrlmnorrrrpqrsrrrrtuvwrrrrxyz{rrrr|}~
 !"9999#$%&9999'()*9999+,-.9999/012999934569999789:9999;<=>9999?@AB9999CDEF9999GHIJ9999KLMN9999OPQR9999STUV9999WXYZ9999[\]^9999_`ab9999cdef9999ghij9999klmn9999opqr9999stuv9999wxyz9999{|}~9999
.NNNN6>FNNNNNV^fnNNNNv~
PROT_EXEC|PROT_WRITE failed.
$Info: This file is packed with the UPX executable packer http://upx.sf.net $
$Id: UPX 3.95 Copyright (C) 1996-2018 the UPX Team. All Rights Reserved. $
GCC: (Debian 9.2.1-21)
o>trPKSt9<R_infoS1_PPv
```

3. Then we used `upx -d` to unpack the program but some of informtaion was also lost during the process.

4. We put the program into [Ghidra](https://ghidra-sre.org/) to execute some basic analysis, and we search for `Enter Exatlon Password` in the program. The comparison code is at address `0x00404d37`.

```c
undefined4 main(void)

{
  bool bVar1;
  basic_ostream *pbVar2;
  undefined4 unaff_R12D;
  basic_string_char_std__char_traits_char__std__allocator_char__ local_58 [32];
  basic_string local_38 [32];
  
  do {
    std::operator__((basic_ostream *)std::cout,"\n");
    std::operator__((basic_ostream *)std::cout,&DAT_0054b018);
    std::operator__((basic_ostream *)std::cout,&DAT_0054b0d8);
    sleep(1);
    std::operator__((basic_ostream *)std::cout,&DAT_0054b1a8);
    std::operator__((basic_ostream *)std::cout,&DAT_0054b260);
    sleep(1);
    std::operator__((basic_ostream *)std::cout,&DAT_0054b320);
    sleep(1);
    std::operator__((basic_ostream *)std::cout,&DAT_0054b400);
    sleep(1);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string
              (local_58);
                    /* try { // try from 00404cfe to 00404dce has its CatchHandler @ 00404def */
    std::operator__((basic_ostream *)std::cout,"[+] Enter Exatlon Password  : ");
    std::operator__((basic_istream *)std::cin,(basic_string *)local_58);
    exatlon(local_38);
    bVar1 = std::operator__(local_38,
                            "1152 1344 1056 1968 1728 816 1648 784 1584 816 1728 1520 1840 1664 784 1632 1856 1520 1728 816 1632 1856 1520 784 1760 1840 1824 816 1584 1856 784 1776 1760 528 528 2000 "
                           );
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::_basic_string
              ((basic_string_char_std__char_traits_char__std__allocator_char__ *)local_38);
    if (bVar1 == false) {
      bVar1 = std::operator__((basic_string *)local_58,"q");
      if (bVar1 == false) {
        pbVar2 = std::operator__((basic_ostream *)std::cout,"[-] ;(\n");
        std::basic_ostream<char,std::char_traits<char>>::operator__
                  ((basic_ostream_char_std__char_traits_char__ *)pbVar2,
                   std::endl_char_std__char_traits_char__);
        bVar1 = true;
      }
      else {
        unaff_R12D = 0;
        bVar1 = false;
      }
    }
    else {
      pbVar2 = std::operator__((basic_ostream *)std::cout,"[+] Looks Good ^_^ \n\n\n");
      std::basic_ostream<char,std::char_traits<char>>::operator__
                ((basic_ostream_char_std__char_traits_char__ *)pbVar2,
                 std::endl_char_std__char_traits_char__);
      unaff_R12D = 0;
      bVar1 = false;
    }
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::_basic_string
              (local_58);
  } while (bVar1);
  return unaff_R12D;
}
```

5. We didn't understand what `1152 1344 1056 1968 1728 816 1648 784 1584 816 1728 1520 1840 1664 784 1632 1856 1520 1728 816 1632 1856 1520 784 1760 1840 1824 816 1584 1856 784 1776 1760 528 528 2000` is, and thus we decided to run the program in gdb.

```
$ gdb exatlon_v1
GNU gdb (Debian 12.1-3) 12.1
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
GEF for linux ready, type `gef' to start, `gef config' to configure
90 commands loaded and 5 functions added for GDB 12.1 in 0.00ms using Python engine 3.10
Reading symbols from exatlon_v1...
(No debugging symbols found in exatlon_v1)
gef➤  b *0x00404d37
Breakpoint 1 at 0x404d37
```

```
gef➤  r
Starting program: /home/kali/Desktop/exatlon_v1 
[*] Failed to find objfile or not a valid file format: [Errno 2] No such file or directory: 'system-supplied DSO at 0x7ffff7ffd000'

███████╗██╗  ██╗ █████╗ ████████╗██╗      ██████╗ ███╗   ██╗       ██╗   ██╗ ██╗
██╔════╝╚██╗██╔╝██╔══██╗╚══██╔══╝██║     ██╔═══██╗████╗  ██║       ██║   ██║███║
█████╗   ╚███╔╝ ███████║   ██║   ██║     ██║   ██║██╔██╗ ██║       ██║   ██║╚██║
██╔══╝   ██╔██╗ ██╔══██║   ██║   ██║     ██║   ██║██║╚██╗██║       ╚██╗ ██╔╝ ██║
███████╗██╔╝ ██╗██║  ██║   ██║   ███████╗╚██████╔╝██║ ╚████║███████╗╚████╔╝  ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═══╝   ╚═╝


[+] Enter Exatlon Password  : A

Breakpoint 1, 0x0000000000404d37 in main ()
[ Legend: Modified register | Code | Heap | Stack | String ]
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$rax   : 0x007fffffffdc30  →  0x007fffffffdc40  →  0x00002030343031 ("1040 "?)
$rbx   : 0x00000000400548  →   add BYTE PTR [rax], al
$rcx   : 0x20303430        
$rdx   : 0x007fffffffdb88  →  0x007fffffffdc21  →  0xc400000000005900
$rsp   : 0x007fffffffdc10  →  0x007fffffffdc20  →  0x00000000590041  →  <__EH_FRAME_BEGIN__+150281> (bad) 
$rbp   : 0x007fffffffdc60  →  0x0000000049eb50  →  <__libc_csu_init+0> push r15
$rsi   : 0x0000000054b4f0  →  "1152 1344 1056 1968 1728 816 1648 784 1584 816 172[...]"
$rdi   : 0x007fffffffdc30  →  0x007fffffffdc40  →  0x00002030343031 ("1040 "?)
$rip   : 0x00000000404d37  →  <main+267> call 0x4050fa <_ZSteqIcSt11char_traitsIcESaIcEEbRKNSt7__cxx1112basic_stringIT_T0_T1_EEPKS5_>
$r8    : 0x007fffffffdbd0  →  0x0000002030343000
$r9    : 0x0               
$r10   : 0x007fffffffd834  →  0x29ab940030343031 ("1040"?)
$r11   : 0x0               
$r12   : 0x0000000049ebe0  →  <__libc_csu_fini+0> push rbp
$r13   : 0x0               
$r14   : 0x000000005a8018  →  0x000000004d6f10  →  <__rawmemchr_avx2+0> mov ecx, edi
$r15   : 0x0               
$eflags: [zero carry parity adjust sign trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x33 $ss: 0x2b $ds: 0x00 $es: 0x00 $fs: 0x00 $gs: 0x00 
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0x007fffffffdc10│+0x0000: 0x007fffffffdc20  →  0x00000000590041  →  <__EH_FRAME_BEGIN__+150281> (bad)    ← $rsp
0x007fffffffdc18│+0x0008: 0x0000000000000001
0x007fffffffdc20│+0x0010: 0x00000000590041  →  <__EH_FRAME_BEGIN__+150281> (bad) 
0x007fffffffdc28│+0x0018: 0x0000000049ebc4  →  <__libc_csu_init+116> add rbx, 0x1
0x007fffffffdc30│+0x0020: 0x007fffffffdc40  →  0x00002030343031 ("1040 "?)       ← $rax, $rdi
0x007fffffffdc38│+0x0028: 0x0000000000000005
0x007fffffffdc40│+0x0030: 0x00002030343031 ("1040 "?)
0x007fffffffdc48│+0x0038: 0x0000000049ebe0  →  <__libc_csu_fini+0> push rbp
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:64 ────
     0x404d29 <main+253>       lea    rax, [rbp-0x30]
     0x404d2d <main+257>       lea    rsi, [rip+0x1467bc]        # 0x54b4f0
     0x404d34 <main+264>       mov    rdi, rax
 →   0x404d37 <main+267>       call   0x4050fa <_ZSteqIcSt11char_traitsIcESaIcEEbRKNSt7__cxx1112basic_stringIT_T0_T1_EEPKS5_>
   ↳    0x4050fa <bool+0>         push   rbp
        0x4050fb <bool+0>         mov    rbp, rsp
        0x4050fe <bool+0>         sub    rsp, 0x10
        0x405102 <bool+0>         mov    QWORD PTR [rbp-0x8], rdi
        0x405106 <bool+0>         mov    QWORD PTR [rbp-0x10], rsi
        0x40510a <bool+0>         mov    rdx, QWORD PTR [rbp-0x10]
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── arguments (guessed) ────
_ZSteqIcSt11char_traitsIcESaIcEEbRKNSt7__cxx1112basic_stringIT_T0_T1_EEPKS5_ (
   $rdi = 0x007fffffffdc30 → 0x007fffffffdc40 → 0x00002030343031 ("1040 "?),
   $rsi = 0x0000000054b4f0 → "1152 1344 1056 1968 1728 816 1648 784 1584 816 172[...]",
   $rdx = 0x007fffffffdb88 → 0x007fffffffdc21 → 0xc400000000005900
)
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "exatlon_v1", stopped 0x404d37 in main (), reason: BREAKPOINT
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x404d37 → main()
```

6. It seems like `A` is mapped to `1040`, and thus we decided to try every character in `string.printable` to get their mapping.

```
gef➤  r
Starting program: /home/kali/Desktop/exatlon_v1 
[*] Failed to find objfile or not a valid file format: [Errno 2] No such file or directory: 'system-supplied DSO at 0x7ffff7ffd000'

███████╗██╗  ██╗ █████╗ ████████╗██╗      ██████╗ ███╗   ██╗       ██╗   ██╗ ██╗
██╔════╝╚██╗██╔╝██╔══██╗╚══██╔══╝██║     ██╔═══██╗████╗  ██║       ██║   ██║███║
█████╗   ╚███╔╝ ███████║   ██║   ██║     ██║   ██║██╔██╗ ██║       ██║   ██║╚██║
██╔══╝   ██╔██╗ ██╔══██║   ██║   ██║     ██║   ██║██║╚██╗██║       ╚██╗ ██╔╝ ██║
███████╗██╔╝ ██╗██║  ██║   ██║   ███████╗╚██████╔╝██║ ╚████║███████╗╚████╔╝  ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═══╝   ╚═╝


[+] Enter Exatlon Password  : 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

Breakpoint 1, 0x0000000000404d37 in main ()
[ Legend: Modified register | Code | Heap | Stack | String ]
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$rax   : 0x007fffffffdc30  →  0x000000005c3390  →  "768 784 800 816 832 848 864 880 896 912 1552 1568 [...]"
$rbx   : 0x00000000400548  →   add BYTE PTR [rax], al
$rcx   : 0x20363130        
$rdx   : 0x007fffffffdb88  →  0x000000005c31ce  →  0x0000000000000000
$rsp   : 0x007fffffffdc10  →  0x000000005c3170  →  "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN[...]"
$rbp   : 0x007fffffffdc60  →  0x0000000049eb50  →  <__libc_csu_init+0> push r15
$rsi   : 0x0000000054b4f0  →  "1152 1344 1056 1968 1728 816 1648 784 1584 816 172[...]"
$rdi   : 0x007fffffffdc30  →  0x000000005c3390  →  "768 784 800 816 832 848 864 880 896 912 1552 1568 [...]"
$rip   : 0x00000000404d37  →  <main+267> call 0x4050fa <_ZSteqIcSt11char_traitsIcESaIcEEbRKNSt7__cxx1112basic_stringIT_T0_T1_EEPKS5_>
$r8    : 0x007fffffffdbd0  →  0x0000002036313000
$r9    : 0x1b3             
$r10   : 0x007fffffffd834  →  0xadd9b50036313032 ("2016"?)
$r11   : 0x0               
$r12   : 0x0000000049ebe0  →  <__libc_csu_fini+0> push rbp
$r13   : 0x0               
$r14   : 0x000000005a8018  →  0x000000004d6f10  →  <__rawmemchr_avx2+0> mov ecx, edi
$r15   : 0x0               
$eflags: [zero carry parity adjust sign trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x33 $ss: 0x2b $ds: 0x00 $es: 0x00 $fs: 0x00 $gs: 0x00 
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0x007fffffffdc10│+0x0000: 0x000000005c3170  →  "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN[...]"         ← $rsp
0x007fffffffdc18│+0x0008: 0x0000000000005e ("^"?)
0x007fffffffdc20│+0x0010: 0x00000000000078 ("x"?)
0x007fffffffdc28│+0x0018: 0x65646362613938 ("89abcde"?)
0x007fffffffdc30│+0x0020: 0x000000005c3390  →  "768 784 800 816 832 848 864 880 896 912 1552 1568 [...]"         ← $rax, $rdi
0x007fffffffdc38│+0x0028: 0x00000000000001b8
0x007fffffffdc40│+0x0030: 0x00000000000001e0
0x007fffffffdc48│+0x0038: 0x00000020303038 ("800 "?)
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:64 ────
     0x404d29 <main+253>       lea    rax, [rbp-0x30]
     0x404d2d <main+257>       lea    rsi, [rip+0x1467bc]        # 0x54b4f0
     0x404d34 <main+264>       mov    rdi, rax
 →   0x404d37 <main+267>       call   0x4050fa <_ZSteqIcSt11char_traitsIcESaIcEEbRKNSt7__cxx1112basic_stringIT_T0_T1_EEPKS5_>
   ↳    0x4050fa <bool+0>         push   rbp
        0x4050fb <bool+0>         mov    rbp, rsp
        0x4050fe <bool+0>         sub    rsp, 0x10
        0x405102 <bool+0>         mov    QWORD PTR [rbp-0x8], rdi
        0x405106 <bool+0>         mov    QWORD PTR [rbp-0x10], rsi
        0x40510a <bool+0>         mov    rdx, QWORD PTR [rbp-0x10]
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── arguments (guessed) ────
_ZSteqIcSt11char_traitsIcESaIcEEbRKNSt7__cxx1112basic_stringIT_T0_T1_EEPKS5_ (
   $rdi = 0x007fffffffdc30 → 0x000000005c3390 → "768 784 800 816 832 848 864 880 896 912 1552 1568 [...]",
   $rsi = 0x0000000054b4f0 → "1152 1344 1056 1968 1728 816 1648 784 1584 816 172[...]",
   $rdx = 0x007fffffffdb88 → 0x000000005c31ce → 0x0000000000000000
)
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "exatlon_v1", stopped 0x404d37 in main (), reason: BREAKPOINT
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x404d37 → main()
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  x/s 0x000000005c3390
0x5c3390:       "768 784 800 816 832 848 864 880 896 912 1552 1568 1584 1600 1616 1632 1648 1664 1680 1696 1712 1728 1744 1760 1776 1792 1808 1824 1840 1856 1872 1888 1904 1920 1936 1952 1040 1056 1072 1088 1104 1120 1136 1152 1168 1184 1200 1216 1232 1248 1264 1280 1296 1312 1328 1344 1360 1376 1392 1408 1424 1440 528 544 560 576 592 608 624 640 656 672 688 704 720 736 752 928 944 960 976 992 1008 1024 1456 1472 1488 1504 1520 1536 1968 1984 2000 2016 "
```

7. We wrote the Python program to decode the encipher.