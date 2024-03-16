fun main() {
	val name: String = "Edric G"
	val age: Int = 20
	sayHi(name)
	birthdayGreetings(name, age)

	val bornDateYear: Int = 2003
	val todaysAge = getAge(bornDateYear)
	sayHi(name)
	birthdayGreetings(name, todaysAge)

	showTutorial()

	val fullName: String = concatString("Edric", "Dela Cruz")
	println(fullName)

	val firstNumber: Int = 5
	val secondNumber: Int = 3
	val sum: Int = addNumbers(firstNumber, secondNumber)
	println("The sum of $firstNumber and $secondNumber is $sum.")
}

fun sayHi(name: String = "World") {
	println("Hello, $name!")
}

fun birthdayGreetings(name: String, age: Int): Unit {
	println("Happy Birthday, $name! You are now $age years old!")
}

fun getAge(bornDateYear: Int): Int {
	val currentYear: Int = Year.now().value
	val age: Int = currentYear - bornDateYear
	println("You are $age years old.")
	return age
}

// ---

fun showTutorial() {
	println("Use the val keyword when the value doesn't change.")
	println("Use the var keyword when the value can change.")
	println("When you define a function, you define the parameters that can be passed to it.")
	println("When you call a function, you pass arguments for the parameters.")
}

fun concatString(name: String, lastName: String): String {
	return "$name $lastName"
}

fun addNumbers(a: Int, b: Int): Int {
	return a + b
}

fun isEven(number: Int): Boolean {
	return number % 2 == 0
}