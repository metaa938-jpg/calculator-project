
num1 = float (input("enter your first num :"))
operation =input("enter your operation: ")
num2 = float(input("enter your second num :"))

if operation == "+":
     print ( num1 + num2)
elif operation == "-":
        print(num1 - num2)
elif operation == "*":
            print(num1 * num2)
elif operation == "/":
                print(num1 / num2)
elif operation == "%":
                    print(num1 % num2)
elif operation == "**":
                        print(num1 ** num2)
else :
    print ("wrong operation")