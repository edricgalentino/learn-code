const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
    // res.json({
    //     message: "Hello World",
    //     status: "success",
    // });
    res.sendFile("index.html", { encoding: "utf8", root: __dirname });
});

app.get("/about", (req, res) => {
    res.sendFile("about.html", { encoding: "utf8", root: __dirname });
});

app.get("/contact", (req, res) => {
    res.sendFile("contact.html", { encoding: "utf8", root: __dirname });
});

app.use("/", (req, res) => {
    res.send("404 page");
});

app.listen(3000, () => {
    console.log(`Server is running on port ${port}...`);
});
