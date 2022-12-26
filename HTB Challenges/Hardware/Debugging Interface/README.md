1. After we got the file `debugging_interface_signal.sal`, we check its content and found out it is an zip file.

```
$ file debugging_interface_signal.sal
debugging_interface_signal.zip: Zip archive data, at least v2.0 to extract, compression method=deflate
```

2. Extract the files from it, and then we check the files in it.

```
$ cat digital-0.bin 
<SALEAE>d�AK��^xffffff�?:�����@���3����@��3�L����@���Lf����@��f�����@��������@���������@���������@���������@���������@����▒����@���▒2����@��2�K����@���Ke����@��e�~����@���~�����@���������@���������@���������@���������@��������@���1����@��1�J����@���Jd����@��d�}����@���}�����@���������Lc�~L@YL@YL@LALALAL@LALAYYLAL@LAL@YYLALALAL@LALAeDeDLAL@LALALAL@eEL@LALALA@�    LAYLAL@LA~HLAL@LALAYeDYL@LAeDLALAeDL@LBL@LAYLALAYLALAYYL@eEL@LAL@LAYLAL@YL@LAeDLAL@eEL@LALALAYrLALA@�        LAYLAYYYYL@LAYLAYeEL@LALArL@YL@LBL@LAL@YL@YLALAYLAL@eEYLA@�     LAYLALALAL@LAYYL@LALAYeCYLALAL@LAeDYYLAL@YeDYL@LAL@eEL@YYLALALAL@LAYYL@LBL@eDLAYYLAeDLAL@YYLAeDLAL@YYLALALAYeDYLALAYYYYLAeCLBL@YYLAL@LAeDYYLAYLAeDYL@LALALAL@LALAYYLBreEYLAeDLAL@YYLAL@eEL@YYLAreDYLALAYeCYLALAL@LAYeEYLAL@YYYYLALAYeDYL@LAYLBYYYLAL@eEL@YYLAL@LALALAYYL@LAL@LArYL@LAYYLAYYLBL@LAL@LAYYLALA~GYYLAreDYLALALArYL@LALALAL@LALAYYLAL@YYYYLAL@YeDYL@LALAYeDYL@LAreDYLAL@YYYYLAeDLAL@YYLAYLAYYYLALAeDLAYYLBL@LAYeEYLAL@LALALAYYL@LAL@LAeDYYLAYYL@YYLAeDLALAYYLAL@YYYF2�0
>3����g�+▒▒�������ROLAeDLAYYL@LAYLAeDYL@LAYLAeDYL@LBL@LArYLALAL@LAYeEYLAL@LAYeEYLAeDLAL@YYLALALArYL@LB~GYYLAL@LALALAYYL@LAL@eEL@YYLAYYYYL@LALAYYYYLAL@LAL@LBYYLALAL@LArYL@LAeDLAL@YYLALAYYYYLBL@LAL@YrLAYLAL@LArLAL@YLAYLALAL@LALALAL@YYLAL@LALAYYLAL@LALALAL@eEeCLALALAL@LALAeDLALAL@LA@�   LAYLALALA~GLAL@LBL@YeDYLALAeDLAL@eEL@LAL@LAYLAL@YL@LAYYLAeDL@LALALAYLAL@YLALAeDLAL@eDLALAL@LAYrL@LA@�   LAYLAYYYYLALAYLAYeDLALAL@rLAYL@LAL@LBL@YL@YL@LAYLALAeDYLB@�  LAYLA~GYYLA~GYYLALAYYYYLAYLAeCYLALAL@LAYeEYLAeDLAL@YYLAL@YYYYLAeDLALAYYLAL@LArYLALAeDLAL@YYLAL@LBL@LAL@YYLAYYYYL@LB~GYYLAL@LALALAYYL@LAL@LALALAYYL@LALAYeDYL@LAeDLAYYLALAYLAYYYLAeDLAYYL@LAL@YYYYLALALAL@LALAYYLBYLAeDYLALAL@YeDYL@LAL@YeDYL@LALAeDL@YYLAreDYLAL@LAeDYYLAYLAYYYLAL@LBYeDYLALALArYL@LALALArYLALAL@YYYYLAL@LALALAYYL@LAeDLAYYL@LALAYeCYL@LBL@YYYYLAYYL@YYLAL@YYYYLAYYYYL@LAreEYLA~GYYLAYLAYYYLALALArYL@LALALAL@LAYYLALAL@LAL@LBL@YYLAL@LArYL@LAYLAeDYL@LAeDLAYYL@LBeCLAYYLALAL@LAeDYYLAYYL@YYLALALAeCYYLALAYeCYLALAeCLBL@YYLAYYYYL@LAeDLAL@YYLAYLAYYYLBL@LAeDYYLAL@YeDYL@LAL@LArYL@LAeDLALAYYLALALAYeEYLAL@LArYLALAL@eEL@YYLAJn
E��n��d��
```

3. After googling `SALEAE`, we knew it was a logic analyzer and thus we should download its [software](https://www.saleae.com/downloads/) to do the analysis.

4. Load the `sal` file, and then change the tab of the rightmost panel to `Analyzers`.

5. We need to find the signal's bitrate first. To do that, we zoomed in Channel 0 where wave existed. Most of signal's intervals are `32.02` or `32.04` µs. Thus, its bitrate is $10^6 / 32.02 \approx 31230$ Bits/s

6. Then we chose `Async Serial` and set its bitrate as `31230`.

7. We checked `Terminal` to check whether we got the correct decoding.