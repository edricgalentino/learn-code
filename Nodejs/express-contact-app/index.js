const express = require("express");
const expressLayouts = require("express-ejs-layouts");
const app = express();
const port = 3000;

// Templating Engine
app.set("view engine", "ejs");
app.use(expressLayouts);

// Build in middleware
app.use(express.static("public"));

app.get("/", (req, res) => {
    // res.json({
    //     message: "Hello World",
    //     status: "success",`
    // });
    // res.sendFile("index.html", { encoding: "utf8", root: __dirname });
    res.render("index", { layout: "layouts/main-layout", title: "Home Page" });
});

app.get("/about", (req, res) => {
    res.render("about", { layout: "layouts/main-layout", title: "About Page" });
});

app.get("/contact", (req, res) => {
    res.render("contact", { layout: "layouts/main-layout", title: "Contact Page" });
});

app.use("/", (req, res) => {
    res.send("404 page");
});

app.listen(3000, () => {
    console.log(`Server is running on port ${port}...`);
});
