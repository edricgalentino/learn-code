// Function main untuk mencari nilai s dengan membaca baris ke...

function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}
// function vAndCons untuk mengurutkan s dari huruf auieo lalu dilanjutkan dengan sisa huruf konsonannya dengan menggunakan properti INCLUDES()
function vowelsAndConsonants(s) {
    const vowels = 'aeiou';
    var consonants = '';
    for (var i = 0; i < s.length; i++) {
        if (vowels.includes(s[i])) {
            console.log(s[i]);  
        }
        else {
            consonants += s[i] + '\n';  
        }
    }
    console.log(consonants.trim());
}