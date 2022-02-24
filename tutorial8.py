#(1) IF STATEMENT
print("=================================================================================")
print("IF CONDITION/STATEMENT")
print("=================================================================================")
number1 = 254
number2 = 354
number3 = 454
print("FIRST NUMBER IS: ", number1)
print("SECOND NUMBER IS: ", number2)
print("THIRD NUMBER IS: ", number3)
if number1 < number2 and number2 > number3:
    print("THE VALUE OF FIRST NUMBER WHICH IS", number1 , "IS LESSER THEN", number2, "AND THE VALUE OF THIRD NUMBER WHICH IS",number3 ," IS ALSO LESSER THEN", number2)
else:
    print("THE VALUE OF FIRST NUMBER WHICH IS", number1 , "IS MAYBE GREATER THEN", number2, "AND THE VALUE OF THIRD NUMBER WHICH IS",number3 ," IS ALSO GREATER MAYBE LESSER THEN", number2)
print("=================================================================================")

#(2) IF-ELSE STATEMENT
print("=================================================================================")
print("IF-ELSE CONDITION/STATEMENT")
print("=================================================================================")
number1 = 325
number2 = 425
sum = number1 + number2
print("FIRST NUMBER IS: ", number1)
print("SECOND NUMBER IS: ", number2)
print("THE ADDITION OF", number1, "AND", number2, ":", sum)
if sum > 1000 :
    print("THE ADDITION OF", number1, "AND", number2, "IS GREATER NUMBER THEN EVEN 1000")
else:
    print("THE ADDITION OF", number1, "AND", number2, "IS LESSER NUMBER THEN 1000")
print("=================================================================================")

#(3) ELSE-IF STATEMENT
print("=================================================================================")
print("ELSE-IF CONDITION/STATEMENT")
print("=================================================================================")
number1 = 325
number2 = 425
sum = number1 + number2
multiply = number1 * number2
print("FIRST NUMBER IS: ", number1)
print("SECOND NUMBER IS: ", number2)
print("THE ADDITION OF", number1, "AND", number2, ":", sum)
print("THE MULTIPLICATION OF", number1, "AND", number2, ":", multiply)
if multiply > 10000 :
    print("THE MULTIPLICATION OF", number1, "AND", number2, "IS GREATER NUMBER THEN EVEN 10000")
elif multiply < 10000 :
    print("THE MULTIPLICATION OF", number1, "AND", number2, "IS LESSER NUMBER THEN 10000")
else:
    print("THERE IS NOTHING TO SAY ABOUT IT")
print("=================================================================================")

print("ENTER YOUR NAME: ")
emp_name = input()
print("THE EMPLOYEE NAME IS: ", emp_name)
if emp_name == "MUHAMMAD FAIZAN":
    print("MISTER", emp_name, "YOU MAY GO NOW TO GIVE THE INTERVIEW FOR THIS JOB")
else:
    print("SORRY! THE PERSON NAMED MUHAMMAD FAIZAN IS ALLOWED TO GIVE THE INTERVIEW FOR THIS JOB YOU MAY TRY NEXT YEAR")

