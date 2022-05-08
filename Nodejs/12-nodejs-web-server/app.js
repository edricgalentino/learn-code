const http = require("http");
const fs = require("fs");
const port = 3000;

const writePages = (path, res) => {
    fs.readFile(path, (err, data) => {
        if (err) {
            res.writeHead(404);
            res.write("404 Not Found");
        } else {
            res.write(data, "utf8");
        }
    });
};

const server = http.createServer((req, res) => {
    const url = req.url;
    res.writeHead(200, {
        "Content-Type": "text/html",
    });
    if (url === "/about") {
        writePages("./pages/about.html", res);
        res.end();
    } else if (url === "/contact") {
        writePages("./pages/contact.html", res);
        res.end();
    } else {
        writePages("./index.html", res);
        res.end();
    }
});

server.listen(port, () => {
    console.log(`Server is listening on port ${port}...`);
});
