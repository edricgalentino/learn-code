const express = require("express");
const app = express();
const port = 3000;

// Templating Engine
app.set("view engine", "ejs");

app.get("/", (req, res) => {
    // res.json({
    //     message: "Hello World",
    //     status: "success",
    // });
    // res.sendFile("index.html", { encoding: "utf8", root: __dirname });
    res.render("index", { title: "Home Page" });
});

app.get("/about", (req, res) => {
    res.render("about", { title: "About Page" });
});

app.get("/contact", (req, res) => {
    res.render("contact", { title: "Contact Page" });
});

app.use("/", (req, res) => {
    res.send("404 page");
});

app.listen(3000, () => {
    console.log(`Server is running on port ${port}...`);
});
