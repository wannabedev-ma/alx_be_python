num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("hoose the operation (+, -, *, /):")
match operation:
	case "/" if num2 == 0 :
                print("Cannot divide by zero")
	case "+":
		print("The result is " + num1 + num2)
	case "*":
                print("The result is " + num1 * num2)
	case "/":
                print("The result is " + num1 / num2)
	case "-":
                print("The result is " + num1 - num2)
