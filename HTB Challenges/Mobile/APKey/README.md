1. We open an android emulator with sdk version lower than `30`. Then, we pull the APK file into the emulator and open the app. The app contains a username field and a password field. However, it shows us "Wrong Credential" after a few testing.

2. Thus, we decided to reverse engineer the APK file. To do that, we follow the [article](https://www.hebunilhanli.com/wonderland/mobile-security/decompile-modify-smali-recompile-and-sign-apk/)

3. We used `jadx-gui` to get the program's Java (obfuscated) source code. In `AndroidManifest.xml`, we got the entry of the app is `com.example.apkey.MainActivity`.


```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" android:versionCode="1" android:versionName="1.0" android:compileSdkVersion="30" android:compileSdkVersionCodename="11" package="com.example.apkey" platformBuildVersionCode="30" platformBuildVersionName="11">
    <uses-sdk android:minSdkVersion="16" android:targetSdkVersion="30"/>
    <application android:theme="@style/Theme.APKey" android:label="@string/app_name" android:icon="@mipmap/ic_launcher" android:allowBackup="true" android:supportsRtl="true" android:roundIcon="@mipmap/ic_launcher_round" android:appComponentFactory="androidx.core.app.CoreComponentFactory">
        <activity android:name="com.example.apkey.MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
    </application>
</manifest>
```

```java
package com.example.apkey;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import c.b.a.b;
import c.b.a.g;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/* loaded from: classes.dex */
public class MainActivity extends Activity {

    /* renamed from: b  reason: collision with root package name */
    public Button f927b;

    /* renamed from: c  reason: collision with root package name */
    public EditText f928c;
    public EditText d;
    public b e = new b();
    public g f = new g();

    /* loaded from: classes.dex */
    public class a implements View.OnClickListener {
        public a() {
        }

        @Override // android.view.View.OnClickListener
        public void onClick(View view) {
            Toast makeText;
            String str;
            try {
                if (MainActivity.this.f928c.getText().toString().equals("admin")) {
                    MainActivity mainActivity = MainActivity.this;
                    b bVar = mainActivity.e;
                    String obj = mainActivity.d.getText().toString();
                    try {
                        MessageDigest messageDigest = MessageDigest.getInstance("MD5");
                        messageDigest.update(obj.getBytes());
                        byte[] digest = messageDigest.digest();
                        StringBuffer stringBuffer = new StringBuffer();
                        for (byte b2 : digest) {
                            stringBuffer.append(Integer.toHexString(b2 & 255));
                        }
                        str = stringBuffer.toString();
                    } catch (NoSuchAlgorithmException e) {
                        e.printStackTrace();
                        str = "";
                    }
                    if (str.equals("a2a3d412e92d896134d9c9126d756f")) {
                        Context applicationContext = MainActivity.this.getApplicationContext();
                        MainActivity mainActivity2 = MainActivity.this;
                        b bVar2 = mainActivity2.e;
                        g gVar = mainActivity2.f;
                        makeText = Toast.makeText(applicationContext, b.a(g.a()), 1);
                        makeText.show();
                    }
                }
                makeText = Toast.makeText(MainActivity.this.getApplicationContext(), "Wrong Credentials!", 0);
                makeText.show();
            } catch (Exception e2) {
                e2.printStackTrace();
            }
        }
    }

    @Override // android.app.Activity
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView(R.layout.activity_main);
        this.f927b = (Button) findViewById(R.id.button);
        this.f928c = (EditText) findViewById(R.id.editTextTextPersonName);
        this.d = (EditText) findViewById(R.id.editTextTextPassword);
        this.f927b.setOnClickListener(new a());
    }
}
```

4. After analyzing the program, we got the username as `admin` and the password's hash is `a2a3d412e92d896134d9c9126d756f`. However, the `str` is too short to be an MD5 value. In addition, `b.a(g.a())` could be our flag, but, if we just copy the source code, the packages include the `Android` library, and thus we cannot directly run it as java program. We need to modify the code and rebuild a new APK.

5. To modify the program, we needed to use [apktool](https://ibotpeaches.github.io/Apktool/) to decompile into `smali` format. 

> Note: there is a bug in `apktool`. Thus, we need to provide `-r -f` when decompiling; otherwise, the program cannot be built as APK later.

```
$ sudo apktool d -r -f APKey.apk

I: Using Apktool 2.7.0 on APKey.apk
I: Copying raw resources...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
                             
```

```smali
$ cat "APKe/smali/com/example/apkey/MainActivity\$a.smali"
.class public Lcom/example/apkey/MainActivity$a;
.super Ljava/lang/Object;
.source ""

# interfaces
.implements Landroid/view/View$OnClickListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingMethod;
    value = Lcom/example/apkey/MainActivity;->onCreate(Landroid/os/Bundle;)V
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x1
    name = null
.end annotation


# instance fields
.field public final synthetic b:Lcom/example/apkey/MainActivity;


# direct methods
.method public constructor <init>(Lcom/example/apkey/MainActivity;)V
    .locals 0

    iput-object p1, p0, Lcom/example/apkey/MainActivity$a;->b:Lcom/example/apkey/MainActivity;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 4

    :try_start_0
    iget-object p1, p0, Lcom/example/apkey/MainActivity$a;->b:Lcom/example/apkey/MainActivity;

    iget-object p1, p1, Lcom/example/apkey/MainActivity;->c:Landroid/widget/EditText;

    invoke-virtual {p1}, Landroid/widget/EditText;->getText()Landroid/text/Editable;

    move-result-object p1

    invoke-virtual {p1}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object p1

    const-string v0, "admin"

    invoke-virtual {p1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result p1

    const/4 v0, 0x0

    if-eqz p1, :cond_1

    iget-object p1, p0, Lcom/example/apkey/MainActivity$a;->b:Lcom/example/apkey/MainActivity;

    iget-object v1, p1, Lcom/example/apkey/MainActivity;->e:Lc/b/a/b;

    iget-object p1, p1, Lcom/example/apkey/MainActivity;->d:Landroid/widget/EditText;

    invoke-virtual {p1}, Landroid/widget/EditText;->getText()Landroid/text/Editable;

    move-result-object p1

    invoke-virtual {p1}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object p1
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_1

    :try_start_1
    const-string v1, "MD5"

    .line 1
    invoke-static {v1}, Ljava/security/MessageDigest;->getInstance(Ljava/lang/String;)Ljava/security/MessageDigest;

    move-result-object v1

    invoke-virtual {p1}, Ljava/lang/String;->getBytes()[B

    move-result-object p1

    invoke-virtual {v1, p1}, Ljava/security/MessageDigest;->update([B)V

    invoke-virtual {v1}, Ljava/security/MessageDigest;->digest()[B

    move-result-object p1

    new-instance v1, Ljava/lang/StringBuffer;

    invoke-direct {v1}, Ljava/lang/StringBuffer;-><init>()V

    const/4 v2, 0x0

    :goto_0
    array-length v3, p1

    if-ge v2, v3, :cond_0

    aget-byte v3, p1, v2

    and-int/lit16 v3, v3, 0xff

    invoke-static {v3}, Ljava/lang/Integer;->toHexString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v1, v3}, Ljava/lang/StringBuffer;->append(Ljava/lang/String;)Ljava/lang/StringBuffer;

    add-int/lit8 v2, v2, 0x1

    goto :goto_0

    :cond_0
    invoke-virtual {v1}, Ljava/lang/StringBuffer;->toString()Ljava/lang/String;

    move-result-object p1
    :try_end_1
    .catch Ljava/security/NoSuchAlgorithmException; {:try_start_1 .. :try_end_1} :catch_0
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_1

    goto :goto_1

    :catch_0
    move-exception p1

    :try_start_2
    invoke-virtual {p1}, Ljava/security/NoSuchAlgorithmException;->printStackTrace()V

    const-string p1, ""

    :goto_1
    const-string v1, "21232f297a57a5a743894a0e4a801fc3"

    .line 2
    invoke-virtual {p1, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result p1

    if-eqz p1, :cond_1

    iget-object p1, p0, Lcom/example/apkey/MainActivity$a;->b:Lcom/example/apkey/MainActivity;

    invoke-virtual {p1}, Landroid/app/Activity;->getApplicationContext()Landroid/content/Context;

    move-result-object p1

    iget-object v0, p0, Lcom/example/apkey/MainActivity$a;->b:Lcom/example/apkey/MainActivity;

    iget-object v1, v0, Lcom/example/apkey/MainActivity;->e:Lc/b/a/b;

    iget-object v0, v0, Lcom/example/apkey/MainActivity;->f:Lc/b/a/g;

    invoke-static {}, Lc/b/a/g;->a()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Lc/b/a/b;->a(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    const/4 v1, 0x1

    invoke-static {p1, v0, v1}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object p1

    :goto_2
    invoke-virtual {p1}, Landroid/widget/Toast;->show()V

    goto :goto_3

    :cond_1
    iget-object p1, p0, Lcom/example/apkey/MainActivity$a;->b:Lcom/example/apkey/MainActivity;

    invoke-virtual {p1}, Landroid/app/Activity;->getApplicationContext()Landroid/content/Context;

    move-result-object p1

    const-string v1, "Wrong Credentials!"

    invoke-static {p1, v1, v0}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object p1
    :try_end_2
    .catch Ljava/lang/Exception; {:try_start_2 .. :try_end_2} :catch_1

    goto :goto_2

    :catch_1
    move-exception p1

    invoke-virtual {p1}, Ljava/lang/Exception;->printStackTrace()V

    :goto_3
    return-void
.end method

```

6. Even though we don't understand the `smali`, we still can look for the program we need to modify.
    - `const-string v1, "21232f297a57a5a743894a0e4a801fc3"` is the hash value.
    - `if-eqz p1, :cond_1` may jump the `cond_1`
    - After `:cond_1`, `const-string v1, "Wrong Credentials!"` exists.


7. After googling `if-eqz`, we know that `:cond_1` is executed if `p1` is `0`. Therefore, we can modify the `p1` as `1` by adding `const/4 p1, 0x1` above `if-eqz p1, :cond_1`.

8. Run `sudo apktool b -d -f -out out.apk APKey` to build the APK from smali.

9. To install the apk, we need to sign the apk file first. To make it simple, we used [uber-apk-signer](https://github.com/patrickfav/uber-apk-signer). After downloading it, run `java -jar uber-apk-signer-1.2.1.jar --apks out.apk --skipZipAlig`.

10. Delete the old app from the emulator and install the new apk file. Fill `admin` in the username field and random characters in the password field. The flag will show.