binurl = "/";
const blobToBase64 = (t) => {
  let e = new FileReader();
  return (
    e.readAsDataURL(t),
    new Promise((t) => {
      e.onloadend = () => {
        t(e.result);
      };
    })
  );
};
async function randtext() {
  let t = "";
  for (let e = 0; e < 2e4; e++)
    t += (Math.random() + 1).toString(36).substring(2);
  return t;
}
async function start() {
  var t = window.location.hash.substr(1);
  (extraText = await randtext()),
    await (zipWriter = new zip.ZipWriter(
      new zip.BlobWriter("application/zip"),
      { password: "testlactf123" }
    )).add("key.txt", new zip.TextReader(t)),
    await zipWriter.add("secret.txt", new zip.TextReader(extraText));
  let e = await zipWriter.close();
  fetch(binurl, {
    method: "POST",
    headers: new Headers({
      "content-type": "text/plain",
      "actual-content-length": 1e4,
    }),
    body: e,
  });
  let a = document.getElementById("1");
  a.remove();
}
const script = document.createElement("script");
(script.type = "text/javascript"),
  (script.src = "https://static.lac.tf/zip.min.js"),
  (script.onload = start),
  document.head.appendChild(script);
