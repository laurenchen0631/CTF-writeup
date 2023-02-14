1. We checked any interesting string existing in the binary file.

```
$ strings behindthescenes
/lib64/ld-linux-x86-64.so.2
libc.so.6
strncmp
puts
__stack_chk_fail
printf
strlen
sigemptyset
memset
sigaction
__cxa_finalize
__libc_start_main
GLIBC_2.4
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u+UH
[]A\A]A^A_
./challenge <password>
> HTB{%s}
:*3$"
GCC: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0
```

2. We called `ltrace` to look for any specific library calls.

```
$ ltrace ./behindthescenes
--- SIGILL (Illegal instruction) ---
--- SIGILL (Illegal instruction) ---
./challenge <password>
--- SIGILL (Illegal instruction) ---
+++ exited (status 1) +++

$ ltrace ./behindthescenes password
--- SIGILL (Illegal instruction) ---
--- SIGILL (Illegal instruction) ---
--- SIGILL (Illegal instruction) ---
+++ exited (status 0) +++
```

3. We used `objdump` to check the machine code and its data section.

```
$ objdump -s behindthescenes       

behindthescenes:     file format elf64-x86-64

Contents of section .interp:
 0318 2f6c6962 36342f6c 642d6c69 6e75782d  /lib64/ld-linux-
 0328 7838362d 36342e73 6f2e3200           x86-64.so.2.    
Contents of section .note.gnu.property:
 0338 04000000 10000000 05000000 474e5500  ............GNU.
 0348 020000c0 04000000 03000000 00000000  ................
Contents of section .note.gnu.build-id:
 0358 04000000 14000000 03000000 474e5500  ............GNU.
 0368 e60ae4c8 86619b86 9178148a fd12d0a5  .....a...x......
 0378 428bfe18                             B...            
Contents of section .note.ABI-tag:
 037c 04000000 10000000 01000000 474e5500  ............GNU.
 038c 00000000 03000000 02000000 00000000  ................
Contents of section .gnu.hash:
 03a0 02000000 0d000000 01000000 06000000  ................
 03b0 00008100 00000000 0d000000 00000000  ................
 03c0 d165ce6d                             .e.m            
Contents of section .dynsym:
 03c8 00000000 00000000 00000000 00000000  ................
 03d8 00000000 00000000 0b000000 12000000  ................
 03e8 00000000 00000000 00000000 00000000  ................
 03f8 8b000000 20000000 00000000 00000000  .... ...........
 0408 00000000 00000000 13000000 12000000  ................
 0418 00000000 00000000 00000000 00000000  ................
 0428 4a000000 12000000 00000000 00000000  J...............
 0438 00000000 00000000 30000000 12000000  ........0.......
 0448 00000000 00000000 00000000 00000000  ................
 0458 18000000 12000000 00000000 00000000  ................
 0468 00000000 00000000 29000000 12000000  ........).......
 0478 00000000 00000000 00000000 00000000  ................
 0488 43000000 12000000 00000000 00000000  C...............
 0498 00000000 00000000 63000000 12000000  ........c.......
 04a8 00000000 00000000 00000000 00000000  ................
 04b8 37000000 12000000 00000000 00000000  7...............
 04c8 00000000 00000000 a7000000 20000000  ............ ...
 04d8 00000000 00000000 00000000 00000000  ................
 04e8 b6000000 20000000 00000000 00000000  .... ...........
 04f8 00000000 00000000 54000000 22000000  ........T..."...
 0508 00000000 00000000 00000000 00000000  ................
Contents of section .dynstr:
 0518 006c6962 632e736f 2e360073 74726e63  .libc.so.6.strnc
 0528 6d700070 75747300 5f5f7374 61636b5f  mp.puts.__stack_
 0538 63686b5f 6661696c 00707269 6e746600  chk_fail.printf.
 0548 7374726c 656e0073 6967656d 70747973  strlen.sigemptys
 0558 6574006d 656d7365 74007369 67616374  et.memset.sigact
 0568 696f6e00 5f5f6378 615f6669 6e616c69  ion.__cxa_finali
 0578 7a65005f 5f6c6962 635f7374 6172745f  ze.__libc_start_
 0588 6d61696e 00474c49 42435f32 2e340047  main.GLIBC_2.4.G
 0598 4c494243 5f322e32 2e35005f 49544d5f  LIBC_2.2.5._ITM_
 05a8 64657265 67697374 6572544d 436c6f6e  deregisterTMClon
 05b8 65546162 6c65005f 5f676d6f 6e5f7374  eTable.__gmon_st
 05c8 6172745f 5f005f49 544d5f72 65676973  art__._ITM_regis
 05d8 74657254 4d436c6f 6e655461 626c6500  terTMCloneTable.
Contents of section .gnu.version:
 05e8 00000200 00000200 02000200 03000200  ................
 05f8 02000200 02000000 00000200           ............    
Contents of section .gnu.version_r:
 0608 01000200 01000000 10000000 00000000  ................
 0618 1469690d 00000300 75000000 10000000  .ii.....u.......
 0628 751a6909 00000200 7f000000 00000000  u.i.............
Contents of section .rela.dyn:
 0638 803d0000 00000000 08000000 00000000  .=..............
 0648 20120000 00000000 883d0000 00000000   ........=......
 0658 08000000 00000000 e0110000 00000000  ................
 0668 08400000 00000000 08000000 00000000  .@..............
 0678 08400000 00000000 d83f0000 00000000  .@.......?......
 0688 06000000 02000000 00000000 00000000  ................
 0698 e03f0000 00000000 06000000 09000000  .?..............
 06a8 00000000 00000000 e83f0000 00000000  .........?......
 06b8 06000000 0b000000 00000000 00000000  ................
 06c8 f03f0000 00000000 06000000 0c000000  .?..............
 06d8 00000000 00000000 f83f0000 00000000  .........?......
 06e8 06000000 0d000000 00000000 00000000  ................
Contents of section .rela.plt:
 06f8 983f0000 00000000 07000000 01000000  .?..............
 0708 00000000 00000000 a03f0000 00000000  .........?......
 0718 07000000 03000000 00000000 00000000  ................
 0728 a83f0000 00000000 07000000 04000000  .?..............
 0738 00000000 00000000 b03f0000 00000000  .........?......
 0748 07000000 05000000 00000000 00000000  ................
 0758 b83f0000 00000000 07000000 06000000  .?..............
 0768 00000000 00000000 c03f0000 00000000  .........?......
 0778 07000000 07000000 00000000 00000000  ................
 0788 c83f0000 00000000 07000000 08000000  .?..............
 0798 00000000 00000000 d03f0000 00000000  .........?......
 07a8 07000000 0a000000 00000000 00000000  ................
Contents of section .init:
 1000 f30f1efa 4883ec08 488b05d9 2f000048  ....H...H.../..H
 1010 85c07402 ffd04883 c408c3             ..t...H....     
Contents of section .plt:
 1020 ff35622f 0000f2ff 25632f00 000f1f00  .5b/....%c/.....
 1030 f30f1efa 68000000 00f2e9e1 ffffff90  ....h...........
 1040 f30f1efa 68010000 00f2e9d1 ffffff90  ....h...........
 1050 f30f1efa 68020000 00f2e9c1 ffffff90  ....h...........
 1060 f30f1efa 68030000 00f2e9b1 ffffff90  ....h...........
 1070 f30f1efa 68040000 00f2e9a1 ffffff90  ....h...........
 1080 f30f1efa 68050000 00f2e991 ffffff90  ....h...........
 1090 f30f1efa 68060000 00f2e981 ffffff90  ....h...........
 10a0 f30f1efa 68070000 00f2e971 ffffff90  ....h......q....
Contents of section .plt.got:
 10b0 f30f1efa f2ff253d 2f00000f 1f440000  ......%=/....D..
Contents of section .plt.sec:
 10c0 f30f1efa f2ff25cd 2e00000f 1f440000  ......%......D..
 10d0 f30f1efa f2ff25c5 2e00000f 1f440000  ......%......D..
 10e0 f30f1efa f2ff25bd 2e00000f 1f440000  ......%......D..
 10f0 f30f1efa f2ff25b5 2e00000f 1f440000  ......%......D..
 1100 f30f1efa f2ff25ad 2e00000f 1f440000  ......%......D..
 1110 f30f1efa f2ff25a5 2e00000f 1f440000  ......%......D..
 1120 f30f1efa f2ff259d 2e00000f 1f440000  ......%......D..
 1130 f30f1efa f2ff2595 2e00000f 1f440000  ......%......D..
Contents of section .text:
 1140 f30f1efa 31ed4989 d15e4889 e24883e4  ....1.I..^H..H..
 1150 f050544c 8d056603 0000488d 0def0200  .PTL..f...H.....
 1160 00488d3d f9000000 ff15722e 0000f490  .H.=......r.....
 1170 488d3d99 2e000048 8d05922e 00004839  H.=....H......H9
 1180 f8741548 8b054e2e 00004885 c07409ff  .t.H..N...H..t..
 1190 e00f1f80 00000000 c30f1f80 00000000  ................
 11a0 488d3d69 2e000048 8d35622e 00004829  H.=i...H.5b...H)
 11b0 fe4889f0 48c1ee3f 48c1f803 4801c648  .H..H..?H...H..H
 11c0 d1fe7414 488b0525 2e000048 85c07408  ..t.H..%...H..t.
 11d0 ffe0660f 1f440000 c30f1f80 00000000  ..f..D..........
 11e0 f30f1efa 803d252e 00000075 2b554883  .....=%....u+UH.
 11f0 3d022e00 00004889 e5740c48 8b3d062e  =.....H..t.H.=..
 1200 0000e8a9 feffffe8 64ffffff c605fd2d  ........d......-
 1210 0000015d c30f1f00 c30f1f80 00000000  ...]............
 1220 f30f1efa e977ffff fff30f1e fa554889  .....w.......UH.
 1230 e5897dec 488975e0 488955d8 488b45d8  ..}.H.u.H.U.H.E.
 1240 488945f8 488b45f8 488b80a8 00000048  H.E.H.E.H......H
 1250 8d500248 8b45f848 8990a800 0000905d  .P.H.E.H.......]
 1260 c3f30f1e fa554889 e54881ec b0000000  .....UH..H......
 1270 89bd5cff ffff4889 b550ffff ff64488b  ..\...H..P...dH.
 1280 04252800 00004889 45f831c0 488d8560  .%(...H.E.1.H..`
 1290 ffffffba 98000000 be000000 004889c7  .............H..
 12a0 e87bfeff ff488d85 60ffffff 4883c008  .{...H..`...H...
 12b0 4889c7e8 78feffff 488d056a ffffff48  H...x...H..j...H
 12c0 898560ff ffffc745 e8040000 00488d85  ..`....E.....H..
 12d0 60ffffff ba000000 004889c6 bf040000  `........H......
 12e0 00e8fafd ffff0f0b 83bd5cff ffff0274  ..........\....t
 12f0 1a0f0b48 8d3d0a0d 0000e8d1 fdffff0f  ...H.=..........
 1300 0bb80100 0000e92e 0100000f 0b488b85  .............H..
 1310 50ffffff 4883c008 488b0048 89c7e8cd  P...H...H..H....
 1320 fdffff48 83f80c0f 85050100 000f0b48  ...H...........H
 1330 8b8550ff ffff4883 c008488b 00ba0300  ..P...H...H.....
 1340 0000488d 35d20c00 004889c7 e86ffdff  ..H.5....H...o..
 1350 ff85c00f 85d00000 000f0b48 8b8550ff  ...........H..P.
 1360 ffff4883 c008488b 004883c0 03ba0300  ..H...H..H......
 1370 0000488d 35a60c00 004889c7 e83ffdff  ..H.5....H...?..
 1380 ff85c00f 85970000 000f0b48 8b8550ff  ...........H..P.
 1390 ffff4883 c008488b 004883c0 06ba0300  ..H...H..H......
 13a0 0000488d 357a0c00 004889c7 e80ffdff  ..H.5z...H......
 13b0 ff85c075 620f0b48 8b8550ff ffff4883  ...ub..H..P...H.
 13c0 c008488b 004883c0 09ba0300 0000488d  ..H..H........H.
 13d0 35520c00 004889c7 e8e3fcff ff85c075  5R...H.........u
 13e0 2d0f0b48 8b8550ff ffff4883 c008488b  -..H..P...H...H.
 13f0 004889c6 488d3d30 0c0000b8 00000000  .H..H.=0........
 1400 e80bfdff ff0f0bb8 00000000 eb2b0f0b  .............+..
 1410 b8000000 00eb220f 0bb80000 0000eb19  ......".........
 1420 0f0bb800 000000eb 100f0bb8 00000000  ................
 1430 eb070f0b b8000000 00488b4d f8644833  .........H.M.dH3
 1440 0c252800 00007405 e8b3fcff ffc9c390  .%(...t.........
 1450 f30f1efa 41574c8d 3d232900 00415649  ....AWL.=#)..AVI
 1460 89d64155 4989f541 544189fc 55488d2d  ..AUI..ATA..UH.-
 1470 14290000 534c29fd 4883ec08 e87ffbff  .)..SL).H.......
 1480 ff48c1fd 03741f31 db0f1f80 00000000  .H...t.1........
 1490 4c89f24c 89ee4489 e741ff14 df4883c3  L..L..D..A...H..
 14a0 014839dd 75ea4883 c4085b5d 415c415d  .H9.u.H...[]A\A]
 14b0 415e415f c366662e 0f1f8400 00000000  A^A_.ff.........
 14c0 f30f1efa c3                          .....           
Contents of section .fini:
 14c8 f30f1efa 4883ec08 4883c408 c3        ....H...H....   
Contents of section .rodata:
 2000 01000200 2e2f6368 616c6c65 6e676520  ...../challenge 
 2010 3c706173 73776f72 643e0049 747a005f  <password>.Itz._
 2020 306e004c 795f0055 4432003e 20485442  0n.Ly_.UD2.> HTB
 2030 7b25737d 0a00                        {%s}..          
Contents of section .eh_frame_hdr:
 2038 011b033b 4c000000 08000000 e8efffff  ...;L...........
 2048 80000000 78f0ffff a8000000 88f0ffff  ....x...........
 2058 c0000000 08f1ffff 68000000 f1f1ffff  ........h.......
 2068 d8000000 29f2ffff f8000000 18f4ffff  ....)...........
 2078 18010000 88f4ffff 60010000           ........`...    
Contents of section .eh_frame:
 2088 14000000 00000000 017a5200 01781001  .........zR..x..
 2098 1b0c0708 90010000 14000000 1c000000  ................
 20a8 98f0ffff 2f000000 00440710 00000000  ..../....D......
 20b8 24000000 34000000 60efffff 90000000  $...4...`.......
 20c8 000e1046 0e184a0f 0b770880 003f1a3a  ...F..J..w...?.:
 20d8 2a332422 00000000 14000000 5c000000  *3$"........\...
 20e8 c8efffff 10000000 00000000 00000000  ................
 20f8 14000000 74000000 c0efffff 80000000  ....t...........
 2108 00000000 00000000 1c000000 8c000000  ................
 2118 11f1ffff 38000000 00450e10 8602430d  ....8....E....C.
 2128 066f0c07 08000000 1c000000 ac000000  .o..............
 2138 29f1ffff ee010000 00450e10 8602430d  )........E....C.
 2148 0603e501 0c070800 44000000 cc000000  ........D.......
 2158 f8f2ffff 65000000 00460e10 8f02490e  ....e....F....I.
 2168 188e0345 0e208d04 450e288c 05440e30  ...E. ..E.(..D.0
 2178 8606480e 38830747 0e406e0e 38410e30  ..H.8..G.@n.8A.0
 2188 410e2842 0e20420e 18420e10 420e0800  A.(B. B..B..B...
 2198 10000000 14010000 20f3ffff 05000000  ........ .......
 21a8 00000000 00000000                    ........        
Contents of section .init_array:
 3d80 20120000 00000000                     .......        
Contents of section .fini_array:
 3d88 e0110000 00000000                    ........        
Contents of section .dynamic:
 3d90 01000000 00000000 01000000 00000000  ................
 3da0 0c000000 00000000 00100000 00000000  ................
 3db0 0d000000 00000000 c8140000 00000000  ................
 3dc0 19000000 00000000 803d0000 00000000  .........=......
 3dd0 1b000000 00000000 08000000 00000000  ................
 3de0 1a000000 00000000 883d0000 00000000  .........=......
 3df0 1c000000 00000000 08000000 00000000  ................
 3e00 f5feff6f 00000000 a0030000 00000000  ...o............
 3e10 05000000 00000000 18050000 00000000  ................
 3e20 06000000 00000000 c8030000 00000000  ................
 3e30 0a000000 00000000 d0000000 00000000  ................
 3e40 0b000000 00000000 18000000 00000000  ................
 3e50 15000000 00000000 00000000 00000000  ................
 3e60 03000000 00000000 803f0000 00000000  .........?......
 3e70 02000000 00000000 c0000000 00000000  ................
 3e80 14000000 00000000 07000000 00000000  ................
 3e90 17000000 00000000 f8060000 00000000  ................
 3ea0 07000000 00000000 38060000 00000000  ........8.......
 3eb0 08000000 00000000 c0000000 00000000  ................
 3ec0 09000000 00000000 18000000 00000000  ................
 3ed0 1e000000 00000000 08000000 00000000  ................
 3ee0 fbffff6f 00000000 01000008 00000000  ...o............
 3ef0 feffff6f 00000000 08060000 00000000  ...o............
 3f00 ffffff6f 00000000 01000000 00000000  ...o............
 3f10 f0ffff6f 00000000 e8050000 00000000  ...o............
 3f20 f9ffff6f 00000000 03000000 00000000  ...o............
 3f30 00000000 00000000 00000000 00000000  ................
 3f40 00000000 00000000 00000000 00000000  ................
 3f50 00000000 00000000 00000000 00000000  ................
 3f60 00000000 00000000 00000000 00000000  ................
 3f70 00000000 00000000 00000000 00000000  ................
Contents of section .got:
 3f80 903d0000 00000000 00000000 00000000  .=..............
 3f90 00000000 00000000 30100000 00000000  ........0.......
 3fa0 40100000 00000000 50100000 00000000  @.......P.......
 3fb0 60100000 00000000 70100000 00000000  `.......p.......
 3fc0 80100000 00000000 90100000 00000000  ................
 3fd0 a0100000 00000000 00000000 00000000  ................
 3fe0 00000000 00000000 00000000 00000000  ................
 3ff0 00000000 00000000 00000000 00000000  ................
Contents of section .data:
 4000 00000000 00000000 08400000 00000000  .........@......
Contents of section .comment:
 0000 4743433a 20285562 756e7475 20392e33  GCC: (Ubuntu 9.3
 0010 2e302d31 37756275 6e747531 7e32302e  .0-17ubuntu1~20.
 0020 30342920 392e332e 3000               04) 9.3.0.
```

```
$ objdump -d behindthescenes       

behindthescenes:     file format elf64-x86-64


Disassembly of section .init:

0000000000001000 <_init>:
    1000:       f3 0f 1e fa             endbr64
    1004:       48 83 ec 08             sub    $0x8,%rsp
    1008:       48 8b 05 d9 2f 00 00    mov    0x2fd9(%rip),%rax        # 3fe8 <__gmon_start__>
    100f:       48 85 c0                test   %rax,%rax
    1012:       74 02                   je     1016 <_init+0x16>
    1014:       ff d0                   call   *%rax
    1016:       48 83 c4 08             add    $0x8,%rsp
    101a:       c3                      ret

Disassembly of section .plt:

0000000000001020 <.plt>:
    1020:       ff 35 62 2f 00 00       push   0x2f62(%rip)        # 3f88 <_GLOBAL_OFFSET_TABLE_+0x8>
    1026:       f2 ff 25 63 2f 00 00    bnd jmp *0x2f63(%rip)        # 3f90 <_GLOBAL_OFFSET_TABLE_+0x10>
    102d:       0f 1f 00                nopl   (%rax)
    1030:       f3 0f 1e fa             endbr64
    1034:       68 00 00 00 00          push   $0x0
    1039:       f2 e9 e1 ff ff ff       bnd jmp 1020 <.plt>
    103f:       90                      nop
    1040:       f3 0f 1e fa             endbr64
    1044:       68 01 00 00 00          push   $0x1
    1049:       f2 e9 d1 ff ff ff       bnd jmp 1020 <.plt>
    104f:       90                      nop
    1050:       f3 0f 1e fa             endbr64
    1054:       68 02 00 00 00          push   $0x2
    1059:       f2 e9 c1 ff ff ff       bnd jmp 1020 <.plt>
    105f:       90                      nop
    1060:       f3 0f 1e fa             endbr64
    1064:       68 03 00 00 00          push   $0x3
    1069:       f2 e9 b1 ff ff ff       bnd jmp 1020 <.plt>
    106f:       90                      nop
    1070:       f3 0f 1e fa             endbr64
    1074:       68 04 00 00 00          push   $0x4
    1079:       f2 e9 a1 ff ff ff       bnd jmp 1020 <.plt>
    107f:       90                      nop
    1080:       f3 0f 1e fa             endbr64
    1084:       68 05 00 00 00          push   $0x5
    1089:       f2 e9 91 ff ff ff       bnd jmp 1020 <.plt>
    108f:       90                      nop
    1090:       f3 0f 1e fa             endbr64
    1094:       68 06 00 00 00          push   $0x6
    1099:       f2 e9 81 ff ff ff       bnd jmp 1020 <.plt>
    109f:       90                      nop
    10a0:       f3 0f 1e fa             endbr64
    10a4:       68 07 00 00 00          push   $0x7
    10a9:       f2 e9 71 ff ff ff       bnd jmp 1020 <.plt>
    10af:       90                      nop

Disassembly of section .plt.got:

00000000000010b0 <__cxa_finalize@plt>:
    10b0:       f3 0f 1e fa             endbr64
    10b4:       f2 ff 25 3d 2f 00 00    bnd jmp *0x2f3d(%rip)        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    10bb:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

Disassembly of section .plt.sec:

00000000000010c0 <strncmp@plt>:
    10c0:       f3 0f 1e fa             endbr64
    10c4:       f2 ff 25 cd 2e 00 00    bnd jmp *0x2ecd(%rip)        # 3f98 <strncmp@GLIBC_2.2.5>
    10cb:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

00000000000010d0 <puts@plt>:
    10d0:       f3 0f 1e fa             endbr64
    10d4:       f2 ff 25 c5 2e 00 00    bnd jmp *0x2ec5(%rip)        # 3fa0 <puts@GLIBC_2.2.5>
    10db:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

00000000000010e0 <sigaction@plt>:
    10e0:       f3 0f 1e fa             endbr64
    10e4:       f2 ff 25 bd 2e 00 00    bnd jmp *0x2ebd(%rip)        # 3fa8 <sigaction@GLIBC_2.2.5>
    10eb:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

00000000000010f0 <strlen@plt>:
    10f0:       f3 0f 1e fa             endbr64
    10f4:       f2 ff 25 b5 2e 00 00    bnd jmp *0x2eb5(%rip)        # 3fb0 <strlen@GLIBC_2.2.5>
    10fb:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

0000000000001100 <__stack_chk_fail@plt>:
    1100:       f3 0f 1e fa             endbr64
    1104:       f2 ff 25 ad 2e 00 00    bnd jmp *0x2ead(%rip)        # 3fb8 <__stack_chk_fail@GLIBC_2.4>
    110b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

0000000000001110 <printf@plt>:
    1110:       f3 0f 1e fa             endbr64
    1114:       f2 ff 25 a5 2e 00 00    bnd jmp *0x2ea5(%rip)        # 3fc0 <printf@GLIBC_2.2.5>
    111b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

0000000000001120 <memset@plt>:
    1120:       f3 0f 1e fa             endbr64
    1124:       f2 ff 25 9d 2e 00 00    bnd jmp *0x2e9d(%rip)        # 3fc8 <memset@GLIBC_2.2.5>
    112b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

0000000000001130 <sigemptyset@plt>:
    1130:       f3 0f 1e fa             endbr64
    1134:       f2 ff 25 95 2e 00 00    bnd jmp *0x2e95(%rip)        # 3fd0 <sigemptyset@GLIBC_2.2.5>
    113b:       0f 1f 44 00 00          nopl   0x0(%rax,%rax,1)

Disassembly of section .text:

0000000000001140 <_start>:
    1140:       f3 0f 1e fa             endbr64
    1144:       31 ed                   xor    %ebp,%ebp
    1146:       49 89 d1                mov    %rdx,%r9
    1149:       5e                      pop    %rsi
    114a:       48 89 e2                mov    %rsp,%rdx
    114d:       48 83 e4 f0             and    $0xfffffffffffffff0,%rsp
    1151:       50                      push   %rax
    1152:       54                      push   %rsp
    1153:       4c 8d 05 66 03 00 00    lea    0x366(%rip),%r8        # 14c0 <__libc_csu_fini>
    115a:       48 8d 0d ef 02 00 00    lea    0x2ef(%rip),%rcx        # 1450 <__libc_csu_init>
    1161:       48 8d 3d f9 00 00 00    lea    0xf9(%rip),%rdi        # 1261 <main>
    1168:       ff 15 72 2e 00 00       call   *0x2e72(%rip)        # 3fe0 <__libc_start_main@GLIBC_2.2.5>
    116e:       f4                      hlt
    116f:       90                      nop

0000000000001170 <deregister_tm_clones>:
    1170:       48 8d 3d 99 2e 00 00    lea    0x2e99(%rip),%rdi        # 4010 <__TMC_END__>
    1177:       48 8d 05 92 2e 00 00    lea    0x2e92(%rip),%rax        # 4010 <__TMC_END__>
    117e:       48 39 f8                cmp    %rdi,%rax
    1181:       74 15                   je     1198 <deregister_tm_clones+0x28>
    1183:       48 8b 05 4e 2e 00 00    mov    0x2e4e(%rip),%rax        # 3fd8 <_ITM_deregisterTMCloneTable>
    118a:       48 85 c0                test   %rax,%rax
    118d:       74 09                   je     1198 <deregister_tm_clones+0x28>
    118f:       ff e0                   jmp    *%rax
    1191:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)
    1198:       c3                      ret
    1199:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)

00000000000011a0 <register_tm_clones>:
    11a0:       48 8d 3d 69 2e 00 00    lea    0x2e69(%rip),%rdi        # 4010 <__TMC_END__>
    11a7:       48 8d 35 62 2e 00 00    lea    0x2e62(%rip),%rsi        # 4010 <__TMC_END__>
    11ae:       48 29 fe                sub    %rdi,%rsi
    11b1:       48 89 f0                mov    %rsi,%rax
    11b4:       48 c1 ee 3f             shr    $0x3f,%rsi
    11b8:       48 c1 f8 03             sar    $0x3,%rax
    11bc:       48 01 c6                add    %rax,%rsi
    11bf:       48 d1 fe                sar    %rsi
    11c2:       74 14                   je     11d8 <register_tm_clones+0x38>
    11c4:       48 8b 05 25 2e 00 00    mov    0x2e25(%rip),%rax        # 3ff0 <_ITM_registerTMCloneTable>
    11cb:       48 85 c0                test   %rax,%rax
    11ce:       74 08                   je     11d8 <register_tm_clones+0x38>
    11d0:       ff e0                   jmp    *%rax
    11d2:       66 0f 1f 44 00 00       nopw   0x0(%rax,%rax,1)
    11d8:       c3                      ret
    11d9:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)

00000000000011e0 <__do_global_dtors_aux>:
    11e0:       f3 0f 1e fa             endbr64
    11e4:       80 3d 25 2e 00 00 00    cmpb   $0x0,0x2e25(%rip)        # 4010 <__TMC_END__>
    11eb:       75 2b                   jne    1218 <__do_global_dtors_aux+0x38>
    11ed:       55                      push   %rbp
    11ee:       48 83 3d 02 2e 00 00    cmpq   $0x0,0x2e02(%rip)        # 3ff8 <__cxa_finalize@GLIBC_2.2.5>
    11f5:       00 
    11f6:       48 89 e5                mov    %rsp,%rbp
    11f9:       74 0c                   je     1207 <__do_global_dtors_aux+0x27>
    11fb:       48 8b 3d 06 2e 00 00    mov    0x2e06(%rip),%rdi        # 4008 <__dso_handle>
    1202:       e8 a9 fe ff ff          call   10b0 <__cxa_finalize@plt>
    1207:       e8 64 ff ff ff          call   1170 <deregister_tm_clones>
    120c:       c6 05 fd 2d 00 00 01    movb   $0x1,0x2dfd(%rip)        # 4010 <__TMC_END__>
    1213:       5d                      pop    %rbp
    1214:       c3                      ret
    1215:       0f 1f 00                nopl   (%rax)
    1218:       c3                      ret
    1219:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)

0000000000001220 <frame_dummy>:
    1220:       f3 0f 1e fa             endbr64
    1224:       e9 77 ff ff ff          jmp    11a0 <register_tm_clones>

0000000000001229 <segill_sigaction>:
    1229:       f3 0f 1e fa             endbr64
    122d:       55                      push   %rbp
    122e:       48 89 e5                mov    %rsp,%rbp
    1231:       89 7d ec                mov    %edi,-0x14(%rbp)
    1234:       48 89 75 e0             mov    %rsi,-0x20(%rbp)
    1238:       48 89 55 d8             mov    %rdx,-0x28(%rbp)
    123c:       48 8b 45 d8             mov    -0x28(%rbp),%rax
    1240:       48 89 45 f8             mov    %rax,-0x8(%rbp)
    1244:       48 8b 45 f8             mov    -0x8(%rbp),%rax
    1248:       48 8b 80 a8 00 00 00    mov    0xa8(%rax),%rax
    124f:       48 8d 50 02             lea    0x2(%rax),%rdx
    1253:       48 8b 45 f8             mov    -0x8(%rbp),%rax
    1257:       48 89 90 a8 00 00 00    mov    %rdx,0xa8(%rax)
    125e:       90                      nop
    125f:       5d                      pop    %rbp
    1260:       c3                      ret

0000000000001261 <main>:
    1261:       f3 0f 1e fa             endbr64
    1265:       55                      push   %rbp
    1266:       48 89 e5                mov    %rsp,%rbp
    1269:       48 81 ec b0 00 00 00    sub    $0xb0,%rsp
    1270:       89 bd 5c ff ff ff       mov    %edi,-0xa4(%rbp)
    1276:       48 89 b5 50 ff ff ff    mov    %rsi,-0xb0(%rbp)
    127d:       64 48 8b 04 25 28 00    mov    %fs:0x28,%rax
    1284:       00 00 
    1286:       48 89 45 f8             mov    %rax,-0x8(%rbp)
    128a:       31 c0                   xor    %eax,%eax
    128c:       48 8d 85 60 ff ff ff    lea    -0xa0(%rbp),%rax
    1293:       ba 98 00 00 00          mov    $0x98,%edx
    1298:       be 00 00 00 00          mov    $0x0,%esi
    129d:       48 89 c7                mov    %rax,%rdi
    12a0:       e8 7b fe ff ff          call   1120 <memset@plt>
    12a5:       48 8d 85 60 ff ff ff    lea    -0xa0(%rbp),%rax
    12ac:       48 83 c0 08             add    $0x8,%rax
    12b0:       48 89 c7                mov    %rax,%rdi
    12b3:       e8 78 fe ff ff          call   1130 <sigemptyset@plt>
    12b8:       48 8d 05 6a ff ff ff    lea    -0x96(%rip),%rax        # 1229 <segill_sigaction>
    12bf:       48 89 85 60 ff ff ff    mov    %rax,-0xa0(%rbp)
    12c6:       c7 45 e8 04 00 00 00    movl   $0x4,-0x18(%rbp)
    12cd:       48 8d 85 60 ff ff ff    lea    -0xa0(%rbp),%rax
    12d4:       ba 00 00 00 00          mov    $0x0,%edx
    12d9:       48 89 c6                mov    %rax,%rsi
    12dc:       bf 04 00 00 00          mov    $0x4,%edi
    12e1:       e8 fa fd ff ff          call   10e0 <sigaction@plt>
    12e6:       0f 0b                   ud2
    12e8:       83 bd 5c ff ff ff 02    cmpl   $0x2,-0xa4(%rbp)
    12ef:       74 1a                   je     130b <main+0xaa>
    12f1:       0f 0b                   ud2
    12f3:       48 8d 3d 0a 0d 00 00    lea    0xd0a(%rip),%rdi        # 2004 <_IO_stdin_used+0x4>
    12fa:       e8 d1 fd ff ff          call   10d0 <puts@plt>
    12ff:       0f 0b                   ud2
    1301:       b8 01 00 00 00          mov    $0x1,%eax
    1306:       e9 2e 01 00 00          jmp    1439 <main+0x1d8>
    130b:       0f 0b                   ud2
    130d:       48 8b 85 50 ff ff ff    mov    -0xb0(%rbp),%rax
    1314:       48 83 c0 08             add    $0x8,%rax
    1318:       48 8b 00                mov    (%rax),%rax
    131b:       48 89 c7                mov    %rax,%rdi
    131e:       e8 cd fd ff ff          call   10f0 <strlen@plt>
    1323:       48 83 f8 0c             cmp    $0xc,%rax
    1327:       0f 85 05 01 00 00       jne    1432 <main+0x1d1>
    132d:       0f 0b                   ud2
    132f:       48 8b 85 50 ff ff ff    mov    -0xb0(%rbp),%rax
    1336:       48 83 c0 08             add    $0x8,%rax
    133a:       48 8b 00                mov    (%rax),%rax
    133d:       ba 03 00 00 00          mov    $0x3,%edx
    1342:       48 8d 35 d2 0c 00 00    lea    0xcd2(%rip),%rsi        # 201b <_IO_stdin_used+0x1b>
    1349:       48 89 c7                mov    %rax,%rdi
    134c:       e8 6f fd ff ff          call   10c0 <strncmp@plt>
    1351:       85 c0                   test   %eax,%eax
    1353:       0f 85 d0 00 00 00       jne    1429 <main+0x1c8>
    1359:       0f 0b                   ud2
    135b:       48 8b 85 50 ff ff ff    mov    -0xb0(%rbp),%rax
    1362:       48 83 c0 08             add    $0x8,%rax
    1366:       48 8b 00                mov    (%rax),%rax
    1369:       48 83 c0 03             add    $0x3,%rax
    136d:       ba 03 00 00 00          mov    $0x3,%edx
    1372:       48 8d 35 a6 0c 00 00    lea    0xca6(%rip),%rsi        # 201f <_IO_stdin_used+0x1f>
    1379:       48 89 c7                mov    %rax,%rdi
    137c:       e8 3f fd ff ff          call   10c0 <strncmp@plt>
    1381:       85 c0                   test   %eax,%eax
    1383:       0f 85 97 00 00 00       jne    1420 <main+0x1bf>
    1389:       0f 0b                   ud2
    138b:       48 8b 85 50 ff ff ff    mov    -0xb0(%rbp),%rax
    1392:       48 83 c0 08             add    $0x8,%rax
    1396:       48 8b 00                mov    (%rax),%rax
    1399:       48 83 c0 06             add    $0x6,%rax
    139d:       ba 03 00 00 00          mov    $0x3,%edx
    13a2:       48 8d 35 7a 0c 00 00    lea    0xc7a(%rip),%rsi        # 2023 <_IO_stdin_used+0x23>
    13a9:       48 89 c7                mov    %rax,%rdi
    13ac:       e8 0f fd ff ff          call   10c0 <strncmp@plt>
    13b1:       85 c0                   test   %eax,%eax
    13b3:       75 62                   jne    1417 <main+0x1b6>
    13b5:       0f 0b                   ud2
    13b7:       48 8b 85 50 ff ff ff    mov    -0xb0(%rbp),%rax
    13be:       48 83 c0 08             add    $0x8,%rax
    13c2:       48 8b 00                mov    (%rax),%rax
    13c5:       48 83 c0 09             add    $0x9,%rax
    13c9:       ba 03 00 00 00          mov    $0x3,%edx
    13ce:       48 8d 35 52 0c 00 00    lea    0xc52(%rip),%rsi        # 2027 <_IO_stdin_used+0x27>
    13d5:       48 89 c7                mov    %rax,%rdi
    13d8:       e8 e3 fc ff ff          call   10c0 <strncmp@plt>
    13dd:       85 c0                   test   %eax,%eax
    13df:       75 2d                   jne    140e <main+0x1ad>
    13e1:       0f 0b                   ud2
    13e3:       48 8b 85 50 ff ff ff    mov    -0xb0(%rbp),%rax
    13ea:       48 83 c0 08             add    $0x8,%rax
    13ee:       48 8b 00                mov    (%rax),%rax
    13f1:       48 89 c6                mov    %rax,%rsi
    13f4:       48 8d 3d 30 0c 00 00    lea    0xc30(%rip),%rdi        # 202b <_IO_stdin_used+0x2b>
    13fb:       b8 00 00 00 00          mov    $0x0,%eax
    1400:       e8 0b fd ff ff          call   1110 <printf@plt>
    1405:       0f 0b                   ud2
    1407:       b8 00 00 00 00          mov    $0x0,%eax
    140c:       eb 2b                   jmp    1439 <main+0x1d8>
    140e:       0f 0b                   ud2
    1410:       b8 00 00 00 00          mov    $0x0,%eax
    1415:       eb 22                   jmp    1439 <main+0x1d8>
    1417:       0f 0b                   ud2
    1419:       b8 00 00 00 00          mov    $0x0,%eax
    141e:       eb 19                   jmp    1439 <main+0x1d8>
    1420:       0f 0b                   ud2
    1422:       b8 00 00 00 00          mov    $0x0,%eax
    1427:       eb 10                   jmp    1439 <main+0x1d8>
    1429:       0f 0b                   ud2
    142b:       b8 00 00 00 00          mov    $0x0,%eax
    1430:       eb 07                   jmp    1439 <main+0x1d8>
    1432:       0f 0b                   ud2
    1434:       b8 00 00 00 00          mov    $0x0,%eax
    1439:       48 8b 4d f8             mov    -0x8(%rbp),%rcx
    143d:       64 48 33 0c 25 28 00    xor    %fs:0x28,%rcx
    1444:       00 00 
    1446:       74 05                   je     144d <main+0x1ec>
    1448:       e8 b3 fc ff ff          call   1100 <__stack_chk_fail@plt>
    144d:       c9                      leave
    144e:       c3                      ret
    144f:       90                      nop

0000000000001450 <__libc_csu_init>:
    1450:       f3 0f 1e fa             endbr64
    1454:       41 57                   push   %r15
    1456:       4c 8d 3d 23 29 00 00    lea    0x2923(%rip),%r15        # 3d80 <__frame_dummy_init_array_entry>
    145d:       41 56                   push   %r14
    145f:       49 89 d6                mov    %rdx,%r14
    1462:       41 55                   push   %r13
    1464:       49 89 f5                mov    %rsi,%r13
    1467:       41 54                   push   %r12
    1469:       41 89 fc                mov    %edi,%r12d
    146c:       55                      push   %rbp
    146d:       48 8d 2d 14 29 00 00    lea    0x2914(%rip),%rbp        # 3d88 <__do_global_dtors_aux_fini_array_entry>
    1474:       53                      push   %rbx
    1475:       4c 29 fd                sub    %r15,%rbp
    1478:       48 83 ec 08             sub    $0x8,%rsp
    147c:       e8 7f fb ff ff          call   1000 <_init>
    1481:       48 c1 fd 03             sar    $0x3,%rbp
    1485:       74 1f                   je     14a6 <__libc_csu_init+0x56>
    1487:       31 db                   xor    %ebx,%ebx
    1489:       0f 1f 80 00 00 00 00    nopl   0x0(%rax)
    1490:       4c 89 f2                mov    %r14,%rdx
    1493:       4c 89 ee                mov    %r13,%rsi
    1496:       44 89 e7                mov    %r12d,%edi
    1499:       41 ff 14 df             call   *(%r15,%rbx,8)
    149d:       48 83 c3 01             add    $0x1,%rbx
    14a1:       48 39 dd                cmp    %rbx,%rbp
    14a4:       75 ea                   jne    1490 <__libc_csu_init+0x40>
    14a6:       48 83 c4 08             add    $0x8,%rsp
    14aa:       5b                      pop    %rbx
    14ab:       5d                      pop    %rbp
    14ac:       41 5c                   pop    %r12
    14ae:       41 5d                   pop    %r13
    14b0:       41 5e                   pop    %r14
    14b2:       41 5f                   pop    %r15
    14b4:       c3                      ret
    14b5:       66 66 2e 0f 1f 84 00    data16 cs nopw 0x0(%rax,%rax,1)
    14bc:       00 00 00 00 

00000000000014c0 <__libc_csu_fini>:
    14c0:       f3 0f 1e fa             endbr64
    14c4:       c3                      ret

Disassembly of section .fini:

00000000000014c8 <_fini>:
    14c8:       f3 0f 1e fa             endbr64
    14cc:       48 83 ec 08             sub    $0x8,%rsp
    14d0:       48 83 c4 08             add    $0x8,%rsp
    14d4:       c3                      ret

```

4. In the data section, we found a interesting string `Itz._0n.Ly_.UD2` (`.` is `00` in hex representation). Thus, we combined these words into `Itz_0nLy_UD2` and try it as our password.

> `strings` didn't find those words because its search min length is `4`. We can change it into `strings -n3 ./behindthescenes` to find those words.