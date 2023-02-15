1. We used `strings` to find plaintext in the program. We saw two filenames: `flag` and `flag.enc`
```
$ strings encrypt 
/lib64/ld-linux-x86-64.so.2
libc.so.6
srand
fopen
ftell
time
__stack_chk_fail
fseek
fclose
malloc
fwrite
fread
__cxa_finalize
__libc_start_main
GLIBC_2.4
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u+UH
dH3<%(
[]A\A]A^A_
flag
flag.enc
:*3$"
GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.8061
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
encrypt.c
__FRAME_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
_ITM_deregisterTMCloneTable
fread@@GLIBC_2.2.5
_edata
fclose@@GLIBC_2.2.5
__stack_chk_fail@@GLIBC_2.4
__libc_start_main@@GLIBC_2.2.5
srand@@GLIBC_2.2.5
__data_start
ftell@@GLIBC_2.2.5
__gmon_start__
__dso_handle
_IO_stdin_used
time@@GLIBC_2.2.5
__libc_csu_init
malloc@@GLIBC_2.2.5
fseek@@GLIBC_2.2.5
__bss_start
main
fopen@@GLIBC_2.2.5
fwrite@@GLIBC_2.2.5
__TMC_END__
_ITM_registerTMCloneTable
__cxa_finalize@@GLIBC_2.2.5
.symtab
.strtab
.shstrtab
.interp
.note.gnu.property
.note.gnu.build-id
.note.ABI-tag
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.plt.sec
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.data
.bss
.comment
```

2. We used `strace` to check which system calls are used. It seemed like the program try to read `flag` file but it doesn't exist and thus caused the error.

```
$ strace ./encrypt   
execve("./encrypt", ["./encrypt"], 0x7fffb374c4d0 /* 62 vars */) = 0
brk(NULL)                               = 0x5576bad1e000
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f622dbe3000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
newfstatat(3, "", {st_mode=S_IFREG|0644, st_size=83550, ...}, AT_EMPTY_PATH) = 0
mmap(NULL, 83550, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f622dbce000
close(3)                                = 0
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\300\223\2\0\0\0\0\0"..., 832) = 832
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
pread64(3, "\4\0\0\0\20\0\0\0\5\0\0\0GNU\0\2\200\0\300\4\0\0\0\1\0\0\0\0\0\0\0", 32, 848) = 32
pread64(3, "\4\0\0\0\24\0\0\0\3\0\0\0GNU\0H\267\357\325\313\371\3263}\370\244\215\347\t\321\366"..., 68, 880) = 68
newfstatat(3, "", {st_mode=S_IFREG|0755, st_size=2061320, ...}, AT_EMPTY_PATH) = 0
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
mmap(NULL, 2109328, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f622d800000
mmap(0x7f622d828000, 1507328, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x28000) = 0x7f622d828000
mmap(0x7f622d998000, 360448, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x198000) = 0x7f622d998000
mmap(0x7f622d9f0000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1f0000) = 0x7f622d9f0000
mmap(0x7f622d9f6000, 53136, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f622d9f6000
close(3)                                = 0
mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f622dbcb000
arch_prctl(ARCH_SET_FS, 0x7f622dbcb740) = 0
set_tid_address(0x7f622dbcba10)         = 42718
set_robust_list(0x7f622dbcba20, 24)     = 0
rseq(0x7f622dbcc0e0, 0x20, 0, 0x53053053) = 0
mprotect(0x7f622d9f0000, 16384, PROT_READ) = 0
mprotect(0x5576b8f7a000, 4096, PROT_READ) = 0
mprotect(0x7f622dc18000, 8192, PROT_READ) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
munmap(0x7f622dbce000, 83550)           = 0
getrandom("\x9f\xc9\x83\xda\xea\x3f\x8c\x58", 8, GRND_NONBLOCK) = 8
brk(NULL)                               = 0x5576bad1e000
brk(0x5576bad3f000)                     = 0x5576bad3f000
openat(AT_FDCWD, "flag", O_RDONLY)      = -1 ENOENT (No such file or directory)
--- SIGSEGV {si_signo=SIGSEGV, si_code=SEGV_MAPERR, si_addr=NULL} ---
+++ killed by SIGSEGV +++
zsh: segmentation fault  strace ./encrypt
```

3. We used `objdump` to analyze the machine code.

```
$ objdump -d encrypt -M intel

encrypt:     file format elf64-x86-64


Disassembly of section .init:

0000000000001000 <_init>:
    1000:       f3 0f 1e fa             endbr64
    1004:       48 83 ec 08             sub    rsp,0x8
    1008:       48 8b 05 d9 2f 00 00    mov    rax,QWORD PTR [rip+0x2fd9]        # 3fe8 <__gmon_start__>
    100f:       48 85 c0                test   rax,rax
    1012:       74 02                   je     1016 <_init+0x16>
    1014:       ff d0                   call   rax
    1016:       48 83 c4 08             add    rsp,0x8
    101a:       c3                      ret

Disassembly of section .plt:

0000000000001020 <.plt>:
    1020:       ff 35 4a 2f 00 00       push   QWORD PTR [rip+0x2f4a]        # 3f70 <_GLOBAL_OFFSET_TABLE_+0x8>
    1026:       f2 ff 25 4b 2f 00 00    bnd jmp QWORD PTR [rip+0x2f4b]        # 3f78 <_GLOBAL_OFFSET_TABLE_+0x10>
    102d:       0f 1f 00                nop    DWORD PTR [rax]
    1030:       f3 0f 1e fa             endbr64
    1034:       68 00 00 00 00          push   0x0
    1039:       f2 e9 e1 ff ff ff       bnd jmp 1020 <.plt>
    103f:       90                      nop
    1040:       f3 0f 1e fa             endbr64
    1044:       68 01 00 00 00          push   0x1
    1049:       f2 e9 d1 ff ff ff       bnd jmp 1020 <.plt>
    104f:       90                      nop
    1050:       f3 0f 1e fa             endbr64
    1054:       68 02 00 00 00          push   0x2
    1059:       f2 e9 c1 ff ff ff       bnd jmp 1020 <.plt>
    105f:       90                      nop
    1060:       f3 0f 1e fa             endbr64
    1064:       68 03 00 00 00          push   0x3
    1069:       f2 e9 b1 ff ff ff       bnd jmp 1020 <.plt>
    106f:       90                      nop
    1070:       f3 0f 1e fa             endbr64
    1074:       68 04 00 00 00          push   0x4
    1079:       f2 e9 a1 ff ff ff       bnd jmp 1020 <.plt>
    107f:       90                      nop
    1080:       f3 0f 1e fa             endbr64
    1084:       68 05 00 00 00          push   0x5
    1089:       f2 e9 91 ff ff ff       bnd jmp 1020 <.plt>
    108f:       90                      nop
    1090:       f3 0f 1e fa             endbr64
    1094:       68 06 00 00 00          push   0x6
    1099:       f2 e9 81 ff ff ff       bnd jmp 1020 <.plt>
    109f:       90                      nop
    10a0:       f3 0f 1e fa             endbr64
    10a4:       68 07 00 00 00          push   0x7
    10a9:       f2 e9 71 ff ff ff       bnd jmp 1020 <.plt>
    10af:       90                      nop
    10b0:       f3 0f 1e fa             endbr64
    10b4:       68 08 00 00 00          push   0x8
    10b9:       f2 e9 61 ff ff ff       bnd jmp 1020 <.plt>
    10bf:       90                      nop
    10c0:       f3 0f 1e fa             endbr64
    10c4:       68 09 00 00 00          push   0x9
    10c9:       f2 e9 51 ff ff ff       bnd jmp 1020 <.plt>
    10cf:       90                      nop
    10d0:       f3 0f 1e fa             endbr64
    10d4:       68 0a 00 00 00          push   0xa
    10d9:       f2 e9 41 ff ff ff       bnd jmp 1020 <.plt>
    10df:       90                      nop

Disassembly of section .plt.got:

00000000000010e0 <__cxa_finalize@plt>:
    10e0:       f3 0f 1e fa             endbr64
    10e4:       f2 ff 25 0d 2f 00 00    bnd jmp QWORD PTR [rip+0x2f0d]        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    10eb:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

Disassembly of section .plt.sec:

00000000000010f0 <fread@plt>:
    10f0:       f3 0f 1e fa             endbr64
    10f4:       f2 ff 25 85 2e 00 00    bnd jmp QWORD PTR [rip+0x2e85]        # 3f80 <fread@GLIBC_2.2.5>
    10fb:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001100 <fclose@plt>:
    1100:       f3 0f 1e fa             endbr64
    1104:       f2 ff 25 7d 2e 00 00    bnd jmp QWORD PTR [rip+0x2e7d]        # 3f88 <fclose@GLIBC_2.2.5>
    110b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001110 <__stack_chk_fail@plt>:
    1110:       f3 0f 1e fa             endbr64
    1114:       f2 ff 25 75 2e 00 00    bnd jmp QWORD PTR [rip+0x2e75]        # 3f90 <__stack_chk_fail@GLIBC_2.4>
    111b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001120 <srand@plt>:
    1120:       f3 0f 1e fa             endbr64
    1124:       f2 ff 25 6d 2e 00 00    bnd jmp QWORD PTR [rip+0x2e6d]        # 3f98 <srand@GLIBC_2.2.5>
    112b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001130 <ftell@plt>:
    1130:       f3 0f 1e fa             endbr64
    1134:       f2 ff 25 65 2e 00 00    bnd jmp QWORD PTR [rip+0x2e65]        # 3fa0 <ftell@GLIBC_2.2.5>
    113b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001140 <time@plt>:
    1140:       f3 0f 1e fa             endbr64
    1144:       f2 ff 25 5d 2e 00 00    bnd jmp QWORD PTR [rip+0x2e5d]        # 3fa8 <time@GLIBC_2.2.5>
    114b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001150 <malloc@plt>:
    1150:       f3 0f 1e fa             endbr64
    1154:       f2 ff 25 55 2e 00 00    bnd jmp QWORD PTR [rip+0x2e55]        # 3fb0 <malloc@GLIBC_2.2.5>
    115b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001160 <fseek@plt>:
    1160:       f3 0f 1e fa             endbr64
    1164:       f2 ff 25 4d 2e 00 00    bnd jmp QWORD PTR [rip+0x2e4d]        # 3fb8 <fseek@GLIBC_2.2.5>
    116b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001170 <fopen@plt>:
    1170:       f3 0f 1e fa             endbr64
    1174:       f2 ff 25 45 2e 00 00    bnd jmp QWORD PTR [rip+0x2e45]        # 3fc0 <fopen@GLIBC_2.2.5>
    117b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001180 <fwrite@plt>:
    1180:       f3 0f 1e fa             endbr64
    1184:       f2 ff 25 3d 2e 00 00    bnd jmp QWORD PTR [rip+0x2e3d]        # 3fc8 <fwrite@GLIBC_2.2.5>
    118b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

0000000000001190 <rand@plt>:
    1190:       f3 0f 1e fa             endbr64
    1194:       f2 ff 25 35 2e 00 00    bnd jmp QWORD PTR [rip+0x2e35]        # 3fd0 <rand@GLIBC_2.2.5>
    119b:       0f 1f 44 00 00          nop    DWORD PTR [rax+rax*1+0x0]

Disassembly of section .text:

00000000000011a0 <_start>:
    11a0:       f3 0f 1e fa             endbr64
    11a4:       31 ed                   xor    ebp,ebp
    11a6:       49 89 d1                mov    r9,rdx
    11a9:       5e                      pop    rsi
    11aa:       48 89 e2                mov    rdx,rsp
    11ad:       48 83 e4 f0             and    rsp,0xfffffffffffffff0
    11b1:       50                      push   rax
    11b2:       54                      push   rsp
    11b3:       4c 8d 05 f6 02 00 00    lea    r8,[rip+0x2f6]        # 14b0 <__libc_csu_fini>
    11ba:       48 8d 0d 7f 02 00 00    lea    rcx,[rip+0x27f]        # 1440 <__libc_csu_init>
    11c1:       48 8d 3d c1 00 00 00    lea    rdi,[rip+0xc1]        # 1289 <main>
    11c8:       ff 15 12 2e 00 00       call   QWORD PTR [rip+0x2e12]        # 3fe0 <__libc_start_main@GLIBC_2.2.5>
    11ce:       f4                      hlt
    11cf:       90                      nop

00000000000011d0 <deregister_tm_clones>:
    11d0:       48 8d 3d 39 2e 00 00    lea    rdi,[rip+0x2e39]        # 4010 <__TMC_END__>
    11d7:       48 8d 05 32 2e 00 00    lea    rax,[rip+0x2e32]        # 4010 <__TMC_END__>
    11de:       48 39 f8                cmp    rax,rdi
    11e1:       74 15                   je     11f8 <deregister_tm_clones+0x28>
    11e3:       48 8b 05 ee 2d 00 00    mov    rax,QWORD PTR [rip+0x2dee]        # 3fd8 <_ITM_deregisterTMCloneTable>
    11ea:       48 85 c0                test   rax,rax
    11ed:       74 09                   je     11f8 <deregister_tm_clones+0x28>
    11ef:       ff e0                   jmp    rax
    11f1:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]
    11f8:       c3                      ret
    11f9:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]

0000000000001200 <register_tm_clones>:
    1200:       48 8d 3d 09 2e 00 00    lea    rdi,[rip+0x2e09]        # 4010 <__TMC_END__>
    1207:       48 8d 35 02 2e 00 00    lea    rsi,[rip+0x2e02]        # 4010 <__TMC_END__>
    120e:       48 29 fe                sub    rsi,rdi
    1211:       48 89 f0                mov    rax,rsi
    1214:       48 c1 ee 3f             shr    rsi,0x3f
    1218:       48 c1 f8 03             sar    rax,0x3
    121c:       48 01 c6                add    rsi,rax
    121f:       48 d1 fe                sar    rsi,1
    1222:       74 14                   je     1238 <register_tm_clones+0x38>
    1224:       48 8b 05 c5 2d 00 00    mov    rax,QWORD PTR [rip+0x2dc5]        # 3ff0 <_ITM_registerTMCloneTable>
    122b:       48 85 c0                test   rax,rax
    122e:       74 08                   je     1238 <register_tm_clones+0x38>
    1230:       ff e0                   jmp    rax
    1232:       66 0f 1f 44 00 00       nop    WORD PTR [rax+rax*1+0x0]
    1238:       c3                      ret
    1239:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]

0000000000001240 <__do_global_dtors_aux>:
    1240:       f3 0f 1e fa             endbr64
    1244:       80 3d c5 2d 00 00 00    cmp    BYTE PTR [rip+0x2dc5],0x0        # 4010 <__TMC_END__>
    124b:       75 2b                   jne    1278 <__do_global_dtors_aux+0x38>
    124d:       55                      push   rbp
    124e:       48 83 3d a2 2d 00 00    cmp    QWORD PTR [rip+0x2da2],0x0        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    1255:       00 
    1256:       48 89 e5                mov    rbp,rsp
    1259:       74 0c                   je     1267 <__do_global_dtors_aux+0x27>
    125b:       48 8b 3d a6 2d 00 00    mov    rdi,QWORD PTR [rip+0x2da6]        # 4008 <__dso_handle>
    1262:       e8 79 fe ff ff          call   10e0 <__cxa_finalize@plt>
    1267:       e8 64 ff ff ff          call   11d0 <deregister_tm_clones>
    126c:       c6 05 9d 2d 00 00 01    mov    BYTE PTR [rip+0x2d9d],0x1        # 4010 <__TMC_END__>
    1273:       5d                      pop    rbp
    1274:       c3                      ret
    1275:       0f 1f 00                nop    DWORD PTR [rax]
    1278:       c3                      ret
    1279:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]

0000000000001280 <frame_dummy>:
    1280:       f3 0f 1e fa             endbr64
    1284:       e9 77 ff ff ff          jmp    1200 <register_tm_clones>

0000000000001289 <main>:
    1289:       f3 0f 1e fa             endbr64
    128d:       55                      push   rbp
    128e:       48 89 e5                mov    rbp,rsp
    1291:       48 83 ec 40             sub    rsp,0x40
    1295:       64 48 8b 04 25 28 00    mov    rax,QWORD PTR fs:0x28
    129c:       00 00 
    129e:       48 89 45 f8             mov    QWORD PTR [rbp-0x8],rax
    12a2:       31 c0                   xor    eax,eax
    12a4:       48 8d 35 59 0d 00 00    lea    rsi,[rip+0xd59]        # 2004 <_IO_stdin_used+0x4>
    12ab:       48 8d 3d 55 0d 00 00    lea    rdi,[rip+0xd55]        # 2007 <_IO_stdin_used+0x7>
    12b2:       e8 b9 fe ff ff          call   1170 <fopen@plt>
    12b7:       48 89 45 d8             mov    QWORD PTR [rbp-0x28],rax
    12bb:       48 8b 45 d8             mov    rax,QWORD PTR [rbp-0x28]
    12bf:       ba 02 00 00 00          mov    edx,0x2
    12c4:       be 00 00 00 00          mov    esi,0x0
    12c9:       48 89 c7                mov    rdi,rax
    12cc:       e8 8f fe ff ff          call   1160 <fseek@plt>
    12d1:       48 8b 45 d8             mov    rax,QWORD PTR [rbp-0x28]
    12d5:       48 89 c7                mov    rdi,rax
    12d8:       e8 53 fe ff ff          call   1130 <ftell@plt>
    12dd:       48 89 45 e0             mov    QWORD PTR [rbp-0x20],rax
    12e1:       48 8b 45 d8             mov    rax,QWORD PTR [rbp-0x28]
    12e5:       ba 00 00 00 00          mov    edx,0x0
    12ea:       be 00 00 00 00          mov    esi,0x0
    12ef:       48 89 c7                mov    rdi,rax
    12f2:       e8 69 fe ff ff          call   1160 <fseek@plt>
    12f7:       48 8b 45 e0             mov    rax,QWORD PTR [rbp-0x20]
    12fb:       48 89 c7                mov    rdi,rax
    12fe:       e8 4d fe ff ff          call   1150 <malloc@plt>
    1303:       48 89 45 e8             mov    QWORD PTR [rbp-0x18],rax
    1307:       48 8b 75 e0             mov    rsi,QWORD PTR [rbp-0x20]
    130b:       48 8b 55 d8             mov    rdx,QWORD PTR [rbp-0x28]
    130f:       48 8b 45 e8             mov    rax,QWORD PTR [rbp-0x18]
    1313:       48 89 d1                mov    rcx,rdx
    1316:       ba 01 00 00 00          mov    edx,0x1
    131b:       48 89 c7                mov    rdi,rax
    131e:       e8 cd fd ff ff          call   10f0 <fread@plt>
    1323:       48 8b 45 d8             mov    rax,QWORD PTR [rbp-0x28]
    1327:       48 89 c7                mov    rdi,rax
    132a:       e8 d1 fd ff ff          call   1100 <fclose@plt>
    132f:       bf 00 00 00 00          mov    edi,0x0
    1334:       e8 07 fe ff ff          call   1140 <time@plt>
    1339:       89 45 c8                mov    DWORD PTR [rbp-0x38],eax
    133c:       8b 45 c8                mov    eax,DWORD PTR [rbp-0x38]
    133f:       89 c7                   mov    edi,eax
    1341:       e8 da fd ff ff          call   1120 <srand@plt>
    1346:       48 c7 45 d0 00 00 00    mov    QWORD PTR [rbp-0x30],0x0
    134d:       00 
    134e:       eb 70                   jmp    13c0 <main+0x137>
    1350:       e8 3b fe ff ff          call   1190 <rand@plt>
    1355:       0f b6 c8                movzx  ecx,al
    1358:       48 8b 55 d0             mov    rdx,QWORD PTR [rbp-0x30]
    135c:       48 8b 45 e8             mov    rax,QWORD PTR [rbp-0x18]
    1360:       48 01 d0                add    rax,rdx
    1363:       0f b6 00                movzx  eax,BYTE PTR [rax]
    1366:       89 c2                   mov    edx,eax
    1368:       89 c8                   mov    eax,ecx
    136a:       89 d1                   mov    ecx,edx
    136c:       31 c1                   xor    ecx,eax
    136e:       48 8b 55 d0             mov    rdx,QWORD PTR [rbp-0x30]
    1372:       48 8b 45 e8             mov    rax,QWORD PTR [rbp-0x18]
    1376:       48 01 d0                add    rax,rdx
    1379:       89 ca                   mov    edx,ecx
    137b:       88 10                   mov    BYTE PTR [rax],dl
    137d:       e8 0e fe ff ff          call   1190 <rand@plt>
    1382:       83 e0 07                and    eax,0x7
    1385:       89 c1                   mov    ecx,eax
    1387:       48 8b 55 d0             mov    rdx,QWORD PTR [rbp-0x30]
    138b:       48 8b 45 e8             mov    rax,QWORD PTR [rbp-0x18]
    138f:       48 01 d0                add    rax,rdx
    1392:       0f b6 00                movzx  eax,BYTE PTR [rax]
    1395:       0f b6 c0                movzx  eax,al
    1398:       48 8b 75 d0             mov    rsi,QWORD PTR [rbp-0x30]
    139c:       48 8b 55 e8             mov    rdx,QWORD PTR [rbp-0x18]
    13a0:       48 01 f2                add    rdx,rsi
    13a3:       88 45 c7                mov    BYTE PTR [rbp-0x39],al
    13a6:       89 4d cc                mov    DWORD PTR [rbp-0x34],ecx
    13a9:       0f b6 45 c7             movzx  eax,BYTE PTR [rbp-0x39]
    13ad:       89 c6                   mov    esi,eax
    13af:       8b 45 cc                mov    eax,DWORD PTR [rbp-0x34]
    13b2:       89 c1                   mov    ecx,eax
    13b4:       40 d2 c6                rol    sil,cl
    13b7:       89 f0                   mov    eax,esi
    13b9:       88 02                   mov    BYTE PTR [rdx],al
    13bb:       48 83 45 d0 01          add    QWORD PTR [rbp-0x30],0x1
    13c0:       48 8b 45 d0             mov    rax,QWORD PTR [rbp-0x30]
    13c4:       48 3b 45 e0             cmp    rax,QWORD PTR [rbp-0x20]
    13c8:       7c 86                   jl     1350 <main+0xc7>
    13ca:       48 8d 35 3b 0c 00 00    lea    rsi,[rip+0xc3b]        # 200c <_IO_stdin_used+0xc>
    13d1:       48 8d 3d 37 0c 00 00    lea    rdi,[rip+0xc37]        # 200f <_IO_stdin_used+0xf>
    13d8:       e8 93 fd ff ff          call   1170 <fopen@plt>
    13dd:       48 89 45 f0             mov    QWORD PTR [rbp-0x10],rax
    13e1:       48 8b 55 f0             mov    rdx,QWORD PTR [rbp-0x10]
    13e5:       48 8d 45 c8             lea    rax,[rbp-0x38]
    13e9:       48 89 d1                mov    rcx,rdx
    13ec:       ba 04 00 00 00          mov    edx,0x4
    13f1:       be 01 00 00 00          mov    esi,0x1
    13f6:       48 89 c7                mov    rdi,rax
    13f9:       e8 82 fd ff ff          call   1180 <fwrite@plt>
    13fe:       48 8b 55 e0             mov    rdx,QWORD PTR [rbp-0x20]
    1402:       48 8b 4d f0             mov    rcx,QWORD PTR [rbp-0x10]
    1406:       48 8b 45 e8             mov    rax,QWORD PTR [rbp-0x18]
    140a:       be 01 00 00 00          mov    esi,0x1
    140f:       48 89 c7                mov    rdi,rax
    1412:       e8 69 fd ff ff          call   1180 <fwrite@plt>
    1417:       48 8b 45 f0             mov    rax,QWORD PTR [rbp-0x10]
    141b:       48 89 c7                mov    rdi,rax
    141e:       e8 dd fc ff ff          call   1100 <fclose@plt>
    1423:       b8 00 00 00 00          mov    eax,0x0
    1428:       48 8b 7d f8             mov    rdi,QWORD PTR [rbp-0x8]
    142c:       64 48 33 3c 25 28 00    xor    rdi,QWORD PTR fs:0x28
    1433:       00 00 
    1435:       74 05                   je     143c <main+0x1b3>
    1437:       e8 d4 fc ff ff          call   1110 <__stack_chk_fail@plt>
    143c:       c9                      leave
    143d:       c3                      ret
    143e:       66 90                   xchg   ax,ax

0000000000001440 <__libc_csu_init>:
    1440:       f3 0f 1e fa             endbr64
    1444:       41 57                   push   r15
    1446:       4c 8d 3d 1b 29 00 00    lea    r15,[rip+0x291b]        # 3d68 <__frame_dummy_init_array_entry>
    144d:       41 56                   push   r14
    144f:       49 89 d6                mov    r14,rdx
    1452:       41 55                   push   r13
    1454:       49 89 f5                mov    r13,rsi
    1457:       41 54                   push   r12
    1459:       41 89 fc                mov    r12d,edi
    145c:       55                      push   rbp
    145d:       48 8d 2d 0c 29 00 00    lea    rbp,[rip+0x290c]        # 3d70 <__do_global_dtors_aux_fini_array_entry>
    1464:       53                      push   rbx
    1465:       4c 29 fd                sub    rbp,r15
    1468:       48 83 ec 08             sub    rsp,0x8
    146c:       e8 8f fb ff ff          call   1000 <_init>
    1471:       48 c1 fd 03             sar    rbp,0x3
    1475:       74 1f                   je     1496 <__libc_csu_init+0x56>
    1477:       31 db                   xor    ebx,ebx
    1479:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]
    1480:       4c 89 f2                mov    rdx,r14
    1483:       4c 89 ee                mov    rsi,r13
    1486:       44 89 e7                mov    edi,r12d
    1489:       41 ff 14 df             call   QWORD PTR [r15+rbx*8]
    148d:       48 83 c3 01             add    rbx,0x1
    1491:       48 39 dd                cmp    rbp,rbx
    1494:       75 ea                   jne    1480 <__libc_csu_init+0x40>
    1496:       48 83 c4 08             add    rsp,0x8
    149a:       5b                      pop    rbx
    149b:       5d                      pop    rbp
    149c:       41 5c                   pop    r12
    149e:       41 5d                   pop    r13
    14a0:       41 5e                   pop    r14
    14a2:       41 5f                   pop    r15
    14a4:       c3                      ret
    14a5:       66 66 2e 0f 1f 84 00    data16 cs nop WORD PTR [rax+rax*1+0x0]
    14ac:       00 00 00 00 

00000000000014b0 <__libc_csu_fini>:
    14b0:       f3 0f 1e fa             endbr64
    14b4:       c3                      ret

Disassembly of section .fini:

00000000000014b8 <_fini>:
    14b8:       f3 0f 1e fa             endbr64
    14bc:       48 83 ec 08             sub    rsp,0x8
    14c0:       48 83 c4 08             add    rsp,0x8
    14c4:       c3                      ret
```