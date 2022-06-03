const { MongoClient } = require("mongodb");

const url = "mongodb://127.0.0.1:27017";
const dbName = "coba-mongodb";

const client = new MongoClient(uri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

client.connect((err) => {
    if (err) {
        return "Terdapat error";
    }
    console.log("Berhasil terkoneksi dengan MongoDB");
});
