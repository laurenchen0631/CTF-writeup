1. The challenge gave us a password-protected zip file and an image.

2. After zooming in the image, we found out there are dots and lines on it. In the other words, it is a morse code image.

3. After checking the zip file, there are files called `flag_998.zip` and another `pwd.png` in it.

4. We guessed the flag is compressed as zip file `1000` times from `flag_999.zip` to `flag_0.zip`. Thus, we wrote a Python script to do the uncompression and morse code translation based on the [morse-ocr](https://github.com/eauxfolles/morse-ocr) source code.