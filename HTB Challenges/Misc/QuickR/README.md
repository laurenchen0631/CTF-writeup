1. The challenge gave us a host, and then we connected it via `nc 138.68.176.115 31190`. The server responded with a QR code and asked us to answer it in 3 seconds.

2. We wrote a Python script to read the QRCode.

3. We cannot find any library to decode QRCode from text stream; thus, I screenshot the terminal directly. We needed to make sure that the terminal was big enough to contain the whole code image`.
4. We used [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar/issues/131) to do the decoding. On our macOS, it needed [additional step](https://github.com/NaturalHistoryMuseum/pyzbar/issues/131) to run.
5. The png compression took too much time and hence I used `bmp` format.
6. The decoded text contains the expression that cannot be evaluated by python, such as `x` and `=`. Therefore, we replaced those symbols.