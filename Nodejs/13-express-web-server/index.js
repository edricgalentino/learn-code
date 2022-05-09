const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
    res.send("Hello Express!");
});

app.get("/about", (req, res) => {
    res.send("About page");
});

app.get("/contact", (req, res) => {
    res.send("Contact page");
});

app.use("/", (req, res) => {
    res.send("404 page");
});

app.listen(3000, () => {
    console.log(`Server is running on port ${port}...`);
});
