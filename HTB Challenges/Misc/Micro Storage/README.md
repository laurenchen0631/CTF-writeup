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

