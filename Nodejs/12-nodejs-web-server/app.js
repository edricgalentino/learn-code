const http = require("http");
const port = 3000;

http.createServer((req, res) => {
    res.writeHead(200, {
        "Content-Type": "text/html",
    });
    const url = req.url;
    if (url === "/about") {
        res.write("About Page");
    } else if (url === "/contact") {
        res.write("Contact Page");
    } else {
        res.write("Home Page");
    }
    res.end();
}).listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});
