1. Given an `apk` file, we first needed a way to analyze. According to [Android APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer), "APKs are files that follow the ZIP file format". Thus we can decompress the file directly.

2. Inside the directory, we found out that the app seems to be made of React Native. Thus we follow [HackTricks](https://book.hacktricks.xyz/mobile-pentesting/android-app-pentesting/react-native-application) to analyze the app core.

3. After analyzing the file from the start, we noticed that the topmost part is just React Native Core javascript. Thus we can browse the file from the bottom.

```javascript
__d(function(g, r, i, a, m, e, d) {
    Object.defineProperty(e, "__esModule", {
        value: !0
    }),
    e.myConfig = void 0;
    var t = {
        importantData: "baNaNa".toLowerCase(),
        apiUrl: 'https://www.hackthebox.eu/',
        debug: 'SFRCezIzbTQxbl9jNDFtXzRuZF9kMG43XzB2MzIyMzRjN30='
    };
    e.myConfig = t
}, 400, []);
```

4. `debug` property looks like base64 encoding. Once it was decoded, we got our flag!