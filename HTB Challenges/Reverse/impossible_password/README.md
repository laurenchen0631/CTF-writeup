1. We ran `impossible_password.bin` and it asked for an input.

2. We used `strings impossible_password.bin`  and we found `SuperSeKretKey` in it. However, the program then asked for the second input.

3. We used `ltrace impossible_password.bin`. It seems that the second string is a random 21 characters string, but it is only generated after the second input is asked.

```
$ ltrace ./impossible_password.bin
__libc_start_main(0x40085d, 1, 0x7ffde28f84e8, 0x4009e0 <unfinished ...>
printf("* ")                                                                                      = 2
__isoc99_scanf(0x400a82, 0x7ffde28f83b0, 0, 0* SuperSeKretKey      
)                                                    = 1
printf("[%s]\n", "SuperSeKretKey"[SuperSeKretKey]
)                                                                = 17
strcmp("SuperSeKretKey", "SuperSeKretKey")                                                        = 0
printf("** ")                                                                                     = 3
__isoc99_scanf(0x400a82, 0x7ffde28f83b0, 0, 0** SuperSeKretKey
)                                                    = 1
time(0)                                                                                           = 1676481448
srand(0xd0033031, 10, 0xce858920, 0)                                                              = 1
malloc(21)                                                                                        = 0x10e2ac0
rand(0x10e2ac0, 21, 0, 33)                                                                        = 0x5fc9e551
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2ac0, 94)                                               = 0x7f54a408
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2ac1, 94)                                               = 0x69947eac
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2ac2, 94)                                               = 0x65a5b3e2
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2ac3, 94)                                               = 0x23defd63
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2ac4, 94)                                               = 0x4cf9e58b
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2ac5, 94)                                               = 0x355bba42
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2ac6, 94)                                               = 0x164db64a
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2ac7, 94)                                               = 0x4fe345e
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2ac8, 94)                                               = 0x6de87ac8
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2ac9, 94)                                               = 0x4285b903
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2aca, 94)                                               = 0x2651468b
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2acb, 94)                                               = 0x30a2ae13
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2acc, 94)                                               = 0x7622add3
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2acd, 94)                                               = 0x2dee43e2
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2ace, 94)                                               = 0x36a8fb5e
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2acf, 94)                                               = 0x7a9797c
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2ad0, 94)                                               = 0x41b4faaa
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2ad1, 94)                                               = 0x39f09aa1
rand(0x7fcf2ddf4840, 0x7ffde28f8314, 0x10e2ad2, 94)                                               = 0x2f7d4b73
strcmp("SuperSeKretKey", "$QU]@Jm_A-fJ,HGuCQ<H")                                                  = 47
```

4. We used `objdump -M intel -d ` to check the machine code. There are two `strcmp` in the code and the second strcmp's address is `0x400961`

```
Disassembly of section .text:

00000000004006a0 <.text>:
  4006a0:       31 ed                   xor    ebp,ebp
  4006a2:       49 89 d1                mov    r9,rdx
  4006a5:       5e                      pop    rsi
  4006a6:       48 89 e2                mov    rdx,rsp
  4006a9:       48 83 e4 f0             and    rsp,0xfffffffffffffff0
  4006ad:       50                      push   rax
  4006ae:       54                      push   rsp
  4006af:       49 c7 c0 50 0a 40 00    mov    r8,0x400a50
  4006b6:       48 c7 c1 e0 09 40 00    mov    rcx,0x4009e0
  4006bd:       48 c7 c7 5d 08 40 00    mov    rdi,0x40085d
  4006c4:       e8 47 ff ff ff          call   400610 <__libc_start_main@plt>
  4006c9:       f4                      hlt
  4006ca:       66 0f 1f 44 00 00       nop    WORD PTR [rax+rax*1+0x0]
  4006d0:       b8 7f 10 60 00          mov    eax,0x60107f
  4006d5:       55                      push   rbp
  4006d6:       48 2d 78 10 60 00       sub    rax,0x601078
  4006dc:       48 83 f8 0e             cmp    rax,0xe
  4006e0:       48 89 e5                mov    rbp,rsp
  4006e3:       77 02                   ja     4006e7 <rand@plt+0x57>
  4006e5:       5d                      pop    rbp
  4006e6:       c3                      ret
  4006e7:       b8 00 00 00 00          mov    eax,0x0
  4006ec:       48 85 c0                test   rax,rax
  4006ef:       74 f4                   je     4006e5 <rand@plt+0x55>
  4006f1:       5d                      pop    rbp
  4006f2:       bf 78 10 60 00          mov    edi,0x601078
  4006f7:       ff e0                   jmp    rax
  4006f9:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]
  400700:       b8 78 10 60 00          mov    eax,0x601078
  400705:       55                      push   rbp
  400706:       48 2d 78 10 60 00       sub    rax,0x601078
  40070c:       48 c1 f8 03             sar    rax,0x3
  400710:       48 89 e5                mov    rbp,rsp
  400713:       48 89 c2                mov    rdx,rax
  400716:       48 c1 ea 3f             shr    rdx,0x3f
  40071a:       48 01 d0                add    rax,rdx
  40071d:       48 d1 f8                sar    rax,1
  400720:       75 02                   jne    400724 <rand@plt+0x94>
  400722:       5d                      pop    rbp
  400723:       c3                      ret
  400724:       ba 00 00 00 00          mov    edx,0x0
  400729:       48 85 d2                test   rdx,rdx
  40072c:       74 f4                   je     400722 <rand@plt+0x92>
  40072e:       5d                      pop    rbp
  40072f:       48 89 c6                mov    rsi,rax
  400732:       bf 78 10 60 00          mov    edi,0x601078
  400737:       ff e2                   jmp    rdx
  400739:       0f 1f 80 00 00 00 00    nop    DWORD PTR [rax+0x0]
  400740:       80 3d 31 09 20 00 00    cmp    BYTE PTR [rip+0x200931],0x0        # 601078 <rand@plt+0x2009e8>
  400747:       75 11                   jne    40075a <rand@plt+0xca>
  400749:       55                      push   rbp
  40074a:       48 89 e5                mov    rbp,rsp
  40074d:       e8 7e ff ff ff          call   4006d0 <rand@plt+0x40>
  400752:       5d                      pop    rbp
  400753:       c6 05 1e 09 20 00 01    mov    BYTE PTR [rip+0x20091e],0x1        # 601078 <rand@plt+0x2009e8>
  40075a:       f3 c3                   repz ret
  40075c:       0f 1f 40 00             nop    DWORD PTR [rax+0x0]
  400760:       48 83 3d b8 06 20 00    cmp    QWORD PTR [rip+0x2006b8],0x0        # 600e20 <rand@plt+0x200790>
  400767:       00 
  400768:       74 1e                   je     400788 <rand@plt+0xf8>
  40076a:       b8 00 00 00 00          mov    eax,0x0
  40076f:       48 85 c0                test   rax,rax
  400772:       74 14                   je     400788 <rand@plt+0xf8>
  400774:       55                      push   rbp
  400775:       bf 20 0e 60 00          mov    edi,0x600e20
  40077a:       48 89 e5                mov    rbp,rsp
  40077d:       ff d0                   call   rax
  40077f:       5d                      pop    rbp
  400780:       e9 7b ff ff ff          jmp    400700 <rand@plt+0x70>
  400785:       0f 1f 00                nop    DWORD PTR [rax]
  400788:       e9 73 ff ff ff          jmp    400700 <rand@plt+0x70>
  40078d:       55                      push   rbp
  40078e:       48 89 e5                mov    rbp,rsp
  400791:       48 83 ec 30             sub    rsp,0x30
  400795:       89 7d dc                mov    DWORD PTR [rbp-0x24],edi
  400798:       48 c7 45 f0 00 00 00    mov    QWORD PTR [rbp-0x10],0x0
  40079f:       00 
  4007a0:       c7 45 ec 7e 00 00 00    mov    DWORD PTR [rbp-0x14],0x7e
  4007a7:       c7 45 e8 21 00 00 00    mov    DWORD PTR [rbp-0x18],0x21
  4007ae:       bf 00 00 00 00          mov    edi,0x0
  4007b3:       e8 98 fe ff ff          call   400650 <time@plt>
  4007b8:       89 c2                   mov    edx,eax
  4007ba:       8b 45 dc                mov    eax,DWORD PTR [rbp-0x24]
  4007bd:       0f af d0                imul   edx,eax
  4007c0:       8b 05 ae 08 20 00       mov    eax,DWORD PTR [rip+0x2008ae]        # 601074 <rand@plt+0x2009e4>
  4007c6:       83 c0 01                add    eax,0x1
  4007c9:       89 05 a5 08 20 00       mov    DWORD PTR [rip+0x2008a5],eax        # 601074 <rand@plt+0x2009e4>
  4007cf:       8b 05 9f 08 20 00       mov    eax,DWORD PTR [rip+0x20089f]        # 601074 <rand@plt+0x2009e4>
  4007d5:       01 d0                   add    eax,edx
  4007d7:       89 c7                   mov    edi,eax
  4007d9:       e8 42 fe ff ff          call   400620 <srand@plt>
  4007de:       8b 45 dc                mov    eax,DWORD PTR [rbp-0x24]
  4007e1:       83 c0 01                add    eax,0x1
  4007e4:       48 98                   cdqe
  4007e6:       48 89 c7                mov    rdi,rax
  4007e9:       e8 72 fe ff ff          call   400660 <malloc@plt>
  4007ee:       48 89 45 f0             mov    QWORD PTR [rbp-0x10],rax
  4007f2:       48 83 7d f0 00          cmp    QWORD PTR [rbp-0x10],0x0
  4007f7:       74 58                   je     400851 <rand@plt+0x1c1>
  4007f9:       c7 45 fc 00 00 00 00    mov    DWORD PTR [rbp-0x4],0x0
  400800:       eb 31                   jmp    400833 <rand@plt+0x1a3>
  400802:       e8 89 fe ff ff          call   400690 <rand@plt>
  400807:       8b 55 ec                mov    edx,DWORD PTR [rbp-0x14]
  40080a:       83 c2 01                add    edx,0x1
  40080d:       89 d1                   mov    ecx,edx
  40080f:       2b 4d e8                sub    ecx,DWORD PTR [rbp-0x18]
  400812:       99                      cdq
  400813:       f7 f9                   idiv   ecx
  400815:       8b 45 e8                mov    eax,DWORD PTR [rbp-0x18]
  400818:       01 d0                   add    eax,edx
  40081a:       89 45 e4                mov    DWORD PTR [rbp-0x1c],eax
  40081d:       8b 45 fc                mov    eax,DWORD PTR [rbp-0x4]
  400820:       48 63 d0                movsxd rdx,eax
  400823:       48 8b 45 f0             mov    rax,QWORD PTR [rbp-0x10]
  400827:       48 01 c2                add    rdx,rax
  40082a:       8b 45 e4                mov    eax,DWORD PTR [rbp-0x1c]
  40082d:       88 02                   mov    BYTE PTR [rdx],al
  40082f:       83 45 fc 01             add    DWORD PTR [rbp-0x4],0x1
  400833:       8b 45 fc                mov    eax,DWORD PTR [rbp-0x4]
  400836:       3b 45 dc                cmp    eax,DWORD PTR [rbp-0x24]
  400839:       7c c7                   jl     400802 <rand@plt+0x172>
  40083b:       8b 45 dc                mov    eax,DWORD PTR [rbp-0x24]
  40083e:       48 63 d0                movsxd rdx,eax
  400841:       48 8b 45 f0             mov    rax,QWORD PTR [rbp-0x10]
  400845:       48 01 d0                add    rax,rdx
  400848:       c6 00 00                mov    BYTE PTR [rax],0x0
  40084b:       48 8b 45 f0             mov    rax,QWORD PTR [rbp-0x10]
  40084f:       eb 0a                   jmp    40085b <rand@plt+0x1cb>
  400851:       bf 01 00 00 00          mov    edi,0x1
  400856:       e8 25 fe ff ff          call   400680 <exit@plt>
  40085b:       c9                      leave
  40085c:       c3                      ret
  40085d:       55                      push   rbp
  40085e:       48 89 e5                mov    rbp,rsp
  400861:       48 83 ec 50             sub    rsp,0x50
  400865:       89 7d bc                mov    DWORD PTR [rbp-0x44],edi
  400868:       48 89 75 b0             mov    QWORD PTR [rbp-0x50],rsi
  40086c:       48 c7 45 f8 70 0a 40    mov    QWORD PTR [rbp-0x8],0x400a70
  400873:       00 
  400874:       c6 45 c0 41             mov    BYTE PTR [rbp-0x40],0x41
  400878:       c6 45 c1 5d             mov    BYTE PTR [rbp-0x3f],0x5d
  40087c:       c6 45 c2 4b             mov    BYTE PTR [rbp-0x3e],0x4b
  400880:       c6 45 c3 72             mov    BYTE PTR [rbp-0x3d],0x72
  400884:       c6 45 c4 3d             mov    BYTE PTR [rbp-0x3c],0x3d
  400888:       c6 45 c5 39             mov    BYTE PTR [rbp-0x3b],0x39
  40088c:       c6 45 c6 6b             mov    BYTE PTR [rbp-0x3a],0x6b
  400890:       c6 45 c7 30             mov    BYTE PTR [rbp-0x39],0x30
  400894:       c6 45 c8 3d             mov    BYTE PTR [rbp-0x38],0x3d
  400898:       c6 45 c9 30             mov    BYTE PTR [rbp-0x37],0x30
  40089c:       c6 45 ca 6f             mov    BYTE PTR [rbp-0x36],0x6f
  4008a0:       c6 45 cb 30             mov    BYTE PTR [rbp-0x35],0x30
  4008a4:       c6 45 cc 3b             mov    BYTE PTR [rbp-0x34],0x3b
  4008a8:       c6 45 cd 6b             mov    BYTE PTR [rbp-0x33],0x6b
  4008ac:       c6 45 ce 31             mov    BYTE PTR [rbp-0x32],0x31
  4008b0:       c6 45 cf 3f             mov    BYTE PTR [rbp-0x31],0x3f
  4008b4:       c6 45 d0 6b             mov    BYTE PTR [rbp-0x30],0x6b
  4008b8:       c6 45 d1 38             mov    BYTE PTR [rbp-0x2f],0x38
  4008bc:       c6 45 d2 31             mov    BYTE PTR [rbp-0x2e],0x31
  4008c0:       c6 45 d3 74             mov    BYTE PTR [rbp-0x2d],0x74
  4008c4:       bf 7f 0a 40 00          mov    edi,0x400a7f
  4008c9:       b8 00 00 00 00          mov    eax,0x0
  4008ce:       e8 2d fd ff ff          call   400600 <printf@plt>
  4008d3:       48 8d 45 e0             lea    rax,[rbp-0x20]
  4008d7:       48 89 c6                mov    rsi,rax
  4008da:       bf 82 0a 40 00          mov    edi,0x400a82
  4008df:       b8 00 00 00 00          mov    eax,0x0
  4008e4:       e8 87 fd ff ff          call   400670 <__isoc99_scanf@plt>
  4008e9:       48 8d 45 e0             lea    rax,[rbp-0x20]
  4008ed:       48 89 c6                mov    rsi,rax
  4008f0:       bf 87 0a 40 00          mov    edi,0x400a87
  4008f5:       b8 00 00 00 00          mov    eax,0x0
  4008fa:       e8 01 fd ff ff          call   400600 <printf@plt>
  4008ff:       48 8b 55 f8             mov    rdx,QWORD PTR [rbp-0x8]
  400903:       48 8d 45 e0             lea    rax,[rbp-0x20]
  400907:       48 89 d6                mov    rsi,rdx
  40090a:       48 89 c7                mov    rdi,rax
  40090d:       e8 1e fd ff ff          call   400630 <strcmp@plt>
  400912:       89 45 f4                mov    DWORD PTR [rbp-0xc],eax
  400915:       83 7d f4 00             cmp    DWORD PTR [rbp-0xc],0x0
  400919:       74 0a                   je     400925 <rand@plt+0x295>
  40091b:       bf 01 00 00 00          mov    edi,0x1
  400920:       e8 5b fd ff ff          call   400680 <exit@plt>
  400925:       bf 8d 0a 40 00          mov    edi,0x400a8d
  40092a:       b8 00 00 00 00          mov    eax,0x0
  40092f:       e8 cc fc ff ff          call   400600 <printf@plt>
  400934:       48 8d 45 e0             lea    rax,[rbp-0x20]
  400938:       48 89 c6                mov    rsi,rax
  40093b:       bf 82 0a 40 00          mov    edi,0x400a82
  400940:       b8 00 00 00 00          mov    eax,0x0
  400945:       e8 26 fd ff ff          call   400670 <__isoc99_scanf@plt>
  40094a:       bf 14 00 00 00          mov    edi,0x14
  40094f:       e8 39 fe ff ff          call   40078d <rand@plt+0xfd>
  400954:       48 89 c2                mov    rdx,rax
  400957:       48 8d 45 e0             lea    rax,[rbp-0x20]
  40095b:       48 89 d6                mov    rsi,rdx
  40095e:       48 89 c7                mov    rdi,rax
  400961:       e8 ca fc ff ff          call   400630 <strcmp@plt>
  400966:       85 c0                   test   eax,eax
  400968:       75 0c                   jne    400976 <rand@plt+0x2e6>
  40096a:       48 8d 45 c0             lea    rax,[rbp-0x40]
  40096e:       48 89 c7                mov    rdi,rax
  400971:       e8 02 00 00 00          call   400978 <rand@plt+0x2e8>
  400976:       c9                      leave
  400977:       c3                      ret
  400978:       55                      push   rbp
  400979:       48 89 e5                mov    rbp,rsp
  40097c:       48 83 ec 20             sub    rsp,0x20
  400980:       48 89 7d e8             mov    QWORD PTR [rbp-0x18],rdi
  400984:       48 8b 45 e8             mov    rax,QWORD PTR [rbp-0x18]
  400988:       48 89 45 f8             mov    QWORD PTR [rbp-0x8],rax
  40098c:       c6 45 f3 09             mov    BYTE PTR [rbp-0xd],0x9
  400990:       c7 45 f4 00 00 00 00    mov    DWORD PTR [rbp-0xc],0x0
  400997:       eb 19                   jmp    4009b2 <rand@plt+0x322>
  400999:       48 8b 45 f8             mov    rax,QWORD PTR [rbp-0x8]
  40099d:       0f b6 00                movzx  eax,BYTE PTR [rax]
  4009a0:       32 45 f3                xor    al,BYTE PTR [rbp-0xd]
  4009a3:       0f be c0                movsx  eax,al
  4009a6:       89 c7                   mov    edi,eax
  4009a8:       e8 43 fc ff ff          call   4005f0 <putchar@plt>
  4009ad:       48 83 45 f8 01          add    QWORD PTR [rbp-0x8],0x1
  4009b2:       48 8b 45 f8             mov    rax,QWORD PTR [rbp-0x8]
  4009b6:       0f b6 00                movzx  eax,BYTE PTR [rax]
  4009b9:       3a 45 f3                cmp    al,BYTE PTR [rbp-0xd]
  4009bc:       74 0e                   je     4009cc <rand@plt+0x33c>
  4009be:       8b 45 f4                mov    eax,DWORD PTR [rbp-0xc]
  4009c1:       8d 50 01                lea    edx,[rax+0x1]
  4009c4:       89 55 f4                mov    DWORD PTR [rbp-0xc],edx
  4009c7:       83 f8 13                cmp    eax,0x13
  4009ca:       7e cd                   jle    400999 <rand@plt+0x309>
  4009cc:       bf 0a 00 00 00          mov    edi,0xa
  4009d1:       e8 1a fc ff ff          call   4005f0 <putchar@plt>
  4009d6:       c9                      leave
  4009d7:       c3                      ret
  4009d8:       0f 1f 84 00 00 00 00    nop    DWORD PTR [rax+rax*1+0x0]
  4009df:       00 
  4009e0:       41 57                   push   r15
  4009e2:       41 89 ff                mov    r15d,edi
  4009e5:       41 56                   push   r14
  4009e7:       49 89 f6                mov    r14,rsi
  4009ea:       41 55                   push   r13
  4009ec:       49 89 d5                mov    r13,rdx
  4009ef:       41 54                   push   r12
  4009f1:       4c 8d 25 18 04 20 00    lea    r12,[rip+0x200418]        # 600e10 <rand@plt+0x200780>
  4009f8:       55                      push   rbp
  4009f9:       48 8d 2d 18 04 20 00    lea    rbp,[rip+0x200418]        # 600e18 <rand@plt+0x200788>
  400a00:       53                      push   rbx
  400a01:       4c 29 e5                sub    rbp,r12
  400a04:       31 db                   xor    ebx,ebx
  400a06:       48 c1 fd 03             sar    rbp,0x3
  400a0a:       48 83 ec 08             sub    rsp,0x8
  400a0e:       e8 ad fb ff ff          call   4005c0 <putchar@plt-0x30>
  400a13:       48 85 ed                test   rbp,rbp
  400a16:       74 1e                   je     400a36 <rand@plt+0x3a6>
  400a18:       0f 1f 84 00 00 00 00    nop    DWORD PTR [rax+rax*1+0x0]
  400a1f:       00 
  400a20:       4c 89 ea                mov    rdx,r13
  400a23:       4c 89 f6                mov    rsi,r14
  400a26:       44 89 ff                mov    edi,r15d
  400a29:       41 ff 14 dc             call   QWORD PTR [r12+rbx*8]
  400a2d:       48 83 c3 01             add    rbx,0x1
  400a31:       48 39 eb                cmp    rbx,rbp
  400a34:       75 ea                   jne    400a20 <rand@plt+0x390>
  400a36:       48 83 c4 08             add    rsp,0x8
  400a3a:       5b                      pop    rbx
  400a3b:       5d                      pop    rbp
  400a3c:       41 5c                   pop    r12
  400a3e:       41 5d                   pop    r13
  400a40:       41 5e                   pop    r14
  400a42:       41 5f                   pop    r15
  400a44:       c3                      ret
  400a45:       90                      nop
  400a46:       66 2e 0f 1f 84 00 00    cs nop WORD PTR [rax+rax*1+0x0]
  400a4d:       00 00 00 
  400a50:       f3 c3                   repz ret
  400a52:       66 90                   xchg   ax,ax

```

5. We ran `gdb` and set a breakpoint on the `0x400961` since the program doesn't contain any debug symbol.

```
$ gdb impossible_password.bin
GNU gdb (Debian 12.1-3) 12.1

GEF for linux ready, type `gef' to start, `gef config' to configure
90 commands loaded and 5 functions added for GDB 12.1 in 0.02ms using Python engine 3.10
Reading symbols from impossible_password.bin...
(No debugging symbols found in impossible_password.bin)
gef➤  disas 0x400961, +16
Dump of assembler code from 0x400961 to 0x400971:
   0x0000000000400961:  call   0x400630 <strcmp@plt>
   0x0000000000400966:  test   eax,eax
   0x0000000000400968:  jne    0x400976
   0x000000000040096a:  lea    rax,[rbp-0x40]
   0x000000000040096e:  mov    rdi,rax
End of assembler dump.

gef➤  b *0x400961
Breakpoint 1 at 0x400961
```

6. Now we can run the program on gdb and set our second input string in the runtime.

```
gef➤  r
Starting program: /home/kali/Desktop/impossible_password.bin 
[*] Failed to find objfile or not a valid file format: [Errno 2] No such file or directory: 'system-supplied DSO at 0x7ffff7fc6000'
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
* SuperSeKretKey
[SuperSeKretKey]
** secondinput

Breakpoint 1, 0x0000000000400961 in ?? ()
[ Legend: Modified register | Code | Heap | Stack | String ]
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$rax   : 0x007fffffffdc20  →  "secondinput"
$rbx   : 0x0               
$rcx   : 0x5e              
$rdx   : 0x00000000602ac0  →  "fyZ(b<o5x{DkJa$9[5Z/"
$rsp   : 0x007fffffffdbf0  →  0x007fffffffdd58  →  0x007fffffffe0ed  →  "/home/kali/Desktop/impossible_password.bin"
$rbp   : 0x007fffffffdc40  →  0x0000000000000001
$rsi   : 0x00000000602ac0  →  "fyZ(b<o5x{DkJa$9[5Z/"
$rdi   : 0x007fffffffdc20  →  "secondinput"
$rip   : 0x00000000400961  →   call 0x400630 <strcmp@plt>
$r8    : 0x007ffff7df4240  →  0xec1bf962203d3100
$r9    : 0x007ffff7df4260  →  0x0000000000000008
$r10   : 0x007ffff7c090e0  →  0x000e0012000027bc
$r11   : 0x007ffff7c41040  →  <rand+0> sub rsp, 0x8
$r12   : 0x007fffffffdd58  →  0x007fffffffe0ed  →  "/home/kali/Desktop/impossible_password.bin"
$r13   : 0x0000000040085d  →   push rbp
$r14   : 0x0               
$r15   : 0x007ffff7ffd020  →  0x007ffff7ffe2c0  →  0x0000000000000000
$eflags: [zero carry PARITY adjust sign trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x33 $ss: 0x2b $ds: 0x00 $es: 0x00 $fs: 0x00 $gs: 0x00 
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0x007fffffffdbf0│+0x0000: 0x007fffffffdd58  →  0x007fffffffe0ed  →  "/home/kali/Desktop/impossible_password.bin"         ← $rsp
0x007fffffffdbf8│+0x0008: 0x0000000100000000
0x007fffffffdc00│+0x0010: "A]Kr=9k0=0o0;k1?k81t"
0x007fffffffdc08│+0x0018: "=0o0;k1?k81t"
0x007fffffffdc10│+0x0020: 0x0000007431386b ("k81t"?)
0x007fffffffdc18│+0x0028: 0x0000000000000000
0x007fffffffdc20│+0x0030: "secondinput"  ← $rax, $rdi
0x007fffffffdc28│+0x0038: 0x00796500747570 ("put"?)
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:64 ────
     0x400957                  lea    rax, [rbp-0x20]
     0x40095b                  mov    rsi, rdx
     0x40095e                  mov    rdi, rax
●→   0x400961                  call   0x400630 <strcmp@plt>
   ↳    0x400630 <strcmp@plt+0>   jmp    QWORD PTR [rip+0x200a02]        # 0x601038 <strcmp@got.plt>
        0x400636 <strcmp@plt+6>   push   0x4
        0x40063b <strcmp@plt+11>  jmp    0x4005e0
        0x400640 <__gmon_start__@plt+0> jmp    QWORD PTR [rip+0x2009fa]        # 0x601040 <__gmon_start__@got.plt>
        0x400646 <__gmon_start__@plt+6> push   0x5
        0x40064b <__gmon_start__@plt+11> jmp    0x4005e0
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── arguments (guessed) ────
strcmp@plt (
   $rdi = 0x007fffffffdc20 → "secondinput",
   $rsi = 0x00000000602ac0 → "fyZ(b<o5x{DkJa$9[5Z/",
   $rdx = 0x00000000602ac0 → "fyZ(b<o5x{DkJa$9[5Z/"
)
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "impossible_pass", stopped 0x400961 in ?? (), reason: BREAKPOINT
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x400961 → call 0x400630 <strcmp@plt>
[#1] 0x7ffff7c2920a → __libc_start_call_main(main=0x40085d, argc=0x1, argv=0x7fffffffdd58)
[#2] 0x7ffff7c292bc → __libc_start_main_impl(main=0x40085d, argc=0x1, argv=0x7fffffffdd58, init=<optimized out>, fini=<optimized out>, rtld_fini=<optimized out>, stack_end=0x7fffffffdd48)
[#3] 0x4006c9 → hlt 
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  x/s $rsi
0x602ac0:       "fyZ(b<o5x{DkJa$9[5Z/"
gef➤  x/s $rdi
0x7fffffffdc20: "secondinput"
gef➤  set $rdi="fyZ(b<o5x{DkJa$9[5Z/"
gef➤  x/s $rdi
0x602ae0:       "fyZ(b<o5x{DkJa$9[5Z/"
gef➤  c
Continuing.
HTB{...}
```