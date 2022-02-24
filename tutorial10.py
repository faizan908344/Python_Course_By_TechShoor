num1 = float(input("Enter the first number: "));
num2 = float(input("Enter the second number: "));
operator = input("Choose your operator through which the operation you want to perform \n \t+ \t- \t* \t/ \t% \n Your Operator: ");
if operator == '+':
    {
        print("The Sum Of num1 and num2 is: ", num1+num2)
    }
elif operator == '-':
    {
        print("The Subtraction Of num1 and num2 is: ", num1-num2)
    }
elif operator == '*':
    {
        print("The Multiplication Of num1 and num2 is: ", num1*num2)
    }
elif operator == '/':
    {
        print("The Divison Of num1 and num2 is: ", num1/num2)
    }
elif operator == '%':
    {
        print("The Reminder Of num1 and num2 is: ", num1%num2)
    }
else:
    {
        print("Idiot!!!!!!!!!!! The Enter Number is Invalid")
    }