// NPM Modules
// Contact App

const { makeQuestion, saveContact } = require("./contact");

const getContacts = async () => {
    const name = await makeQuestion("Write your name : ");
    const email = await makeQuestion("Write your email : ");
    const phoneNumber = await makeQuestion("Write your phone number : ");

    saveContact(name, email, phoneNumber);
};

getContacts();
