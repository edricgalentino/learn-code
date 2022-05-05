// membuat deret fibonacci
// ex: 2,3,5,8,13,21,34,55,89
function fibonacci(e) {
    if (e>100) {
        return
    }
    
    return e + fibonacci(e+e)
}