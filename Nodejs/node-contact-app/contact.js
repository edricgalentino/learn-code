const fs = require("fs");
const rl = require("readline");

const readline = rl.createInterface({
    input: process.stdin,
    output: process.stdout,
});

if (!fs.existsSync("./data")) {
    fs.mkdirSync("./data");
}

if (!fs.existsSync("./data/contacts.json")) {
    fs.writeFileSync(
        "data/contacts.json",
        `{
        "contacts": []
    }`,
        "utf8"
    );
}

const makeQuestion = (q) => {
    return new Promise((resolve, reject) => {
        readline.question(q, (ans) => {
            resolve(ans);
        });
    });
};

const saveContact = (name, email, phoneNumber) => {
    fs.readFile("data/contacts.json", "utf8", (err, data) => {
        if (err) throw err;
        object = JSON.parse(data);
        object.contacts.push({ name, email, phoneNumber });
        fs.writeFile("data/contacts.json", JSON.stringify(object), (err) => {
            if (err) throw err;
            console.log("File saved!");
        });
    });
    readline.close();
};

module.exports = { makeQuestion, saveContact };
