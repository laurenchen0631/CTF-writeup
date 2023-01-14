1. The challenge gave us the source code of the website, but it didn't include the flag file.

2. The flag was read in the `src/config/config.js`, and it will be encrypted by `POST /ingredients` according `src/routes.js`.

3. After googling the zip and its exploitation, we found out there exists a known plaintext attack. There are also tools to do this, [bkcrack](https://github.com/kimci86/bkcrack) and [pkcrack](https://github.com/keyunluo/pkcrack).

4. We followed the [tutorial](https://github.com/kimci86/bkcrack/blob/master/example/tutorial.md) of bkcrack to get the flag.
    - We need to use `echo -n` to create the plaintext file since some editors would add `newline` byte to the file.

```
$ ./bkcrack -L ~/Desktop/ingredients.zip                                                                                                                                              130 ⨯
bkcrack 1.5.0 - 2023-01-13
Archive: /home/parallels/Desktop/ingredients.zip
Index Encryption Compression CRC32    Uncompressed  Packed size Name
----- ---------- ----------- -------- ------------ ------------ ----------------
    0 ZipCrypto  Store       49ba4df2           43           55 tmp/af5bc730b9d810986e4674b83e8e237b/ingredients.txt

$ echo -n "Secret: HTB{" > plain.txt

$ ./bkcrack -c tmp/af5bc730b9d810986e4674b83e8e237b/ingredients.txt -C ~/Desktop/ingredients.zip -p plain.txt                                                                           1 ⨯
bkcrack 1.5.0 - 2023-01-13
[11:41:28] Z reduction using 5 bytes of known plaintext
100.0 % (5 / 5)
[11:41:28] Attack on 1058289 Z values at index 6
Keys: 5af3b754 0b6da23c f78b44bc                                       
1.1 % (11782 / 1058289) 
[11:41:45] Keys
5af3b754 0b6da23c f78b44bc


$ ./bkcrack -c tmp/af5bc730b9d810986e4674b83e8e237b/ingredients.txt -C ~/Desktop/ingredients.zip -k 5af3b754 0b6da23c f78b44bc -d out
bkcrack 1.5.0 - 2023-01-13
[11:42:40] Writing deciphered data /home/parallels/out.zip (maybe compressed)
Wrote deciphered data.

$ cat ~/Desktop/out.zip 
Secret: HTB{...}`
```