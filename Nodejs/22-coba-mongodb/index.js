const { MongoClient } = require("mongodb");

const uri = "mongodb://127.0.0.1:27017";
const dbName = "linktree-mern-project";

const client = new MongoClient(uri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

client.connect((err) => {
    if (err) {
        return "Terdapat error";
    }
    console.log("Berhasil terkoneksi dengan MongoDB");

    const db = client.db(dbName);
    const collection = db.collection("users-data");

    // get all data
    collection.find({}).toArray((err, result) => {
        if (err) {
            return "Terdapat error";
        }
        console.log(result);
    });
});
