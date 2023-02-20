1. We executed the `Bypass.exe` on Windows machine, and it asked us a username and password.

```
PS C:\Users\User\Desktop> .\Bypass.exe
Enter a username:
Enter a password:
Wrong username and/or password
```

2. Since it is an 32-bit `exe` program, we would used 32-bit `dnSpy` to analyze the program. 

```C#
using System;

// Token: 0x02000002 RID: 2
public class 0
{
	// Token: 0x06000002 RID: 2 RVA: 0x00002058 File Offset: 0x00000258
	public static void 0()
	{
		bool flag = global::0.1();
		bool flag2 = flag;
		if (flag2)
		{
			global::0.2();
		}
		else
		{
			Console.WriteLine(5.0);
			global::0.0();
		}
	}

	// Token: 0x06000003 RID: 3 RVA: 0x00002090 File Offset: 0x00000290
	public static bool 1()
	{
		Console.Write(5.1);
		string text = Console.ReadLine();
		Console.Write(5.2);
		string text2 = Console.ReadLine();
		return false;
	}

	// Token: 0x06000004 RID: 4 RVA: 0x000020C8 File Offset: 0x000002C8
	public static void 2()
	{
		string <<EMPTY_NAME>> = 5.3;
		Console.Write(5.4);
		string b = Console.ReadLine();
		bool flag = <<EMPTY_NAME>> == b;
		if (flag)
		{
			Console.Write(5.5 + global::0.2 + 5.6);
		}
		else
		{
			Console.WriteLine(5.7);
			global::0.2();
		}
	}

	// Token: 0x04000001 RID: 1
	public static string 0;

	// Token: 0x04000002 RID: 2
	public static string 1;

	// Token: 0x04000003 RID: 3
	public static string 2 = 5.8;
}

```

3. We analyzed the program, and we found that
   1. `global::0.1()` is the function that asked username and password.
   2. `global::0.1()` always returns `false`.
   3. If `0.1()` returns `true`, `global::0.2()` would be executed then.
   4. `global::0.2()` ask for another input.

4. We would use debugger in dnSpy and added breakpoints on `bool flag = global::0.1();` and `string <<EMPTY_NAME>> = 5.3;`.

5. Run the debugger and then we can change the value of `flag` from `false` to `true`, and check the value of `5.3` and used it as our final input.