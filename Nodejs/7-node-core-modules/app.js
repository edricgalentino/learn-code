// Core Modules
const fs = require("fs");
const rl = require("readline");

const readline = rl.createInterface({
    input: process.stdin,
    output: process.stdout,
});

readline.question("Masukkan nama anda :  ", (nama) => {
    readline.question("Masukkan nomor HP anda :  ", (telp) => {
        obj.contacts.push({
            name: nama,
            nomor: telp,
        });
        fs.readFile("data/contacts.json", "utf8", (err, data) => {
            if (err) throw err;
            console.log(err);
            object = JSON.parse(data); //now it an object
            object.contacts.push({ name: nama, nomor: telp }); //add some data
            fs.writeFile("data/contacts.json", JSON.stringify(object), (err) => {
                if (err) throw err;
                console.log("File saved!");
            }); // write it back
        });
        readline.close();
    });
});

// const util = require("util");
// const question = util.promisify(rl.question).bind(rl);

// async function questionExample() {
//     try {
//         const nama = await question("Masukkan nama anda : ");
//         // const hp = await question("Masukkan nomor HP anda : ");
//         console.log(`Hello ${nama}, dengan nomor HP `);
//     } catch (err) {
//         console.error("Question rejected", err);
//     }
// }
// questionExample();
