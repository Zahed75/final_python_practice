#add 2 values

def two_values(first,second):
    return first+second

num1=2
num2=2
sum= two_values(num1,num2)
print("The values of",sum)

#Grade Show in Function

marks=int(input("Please Enter your mark:"))

def grade_show(mark):
    print("Your Grade is:",mark)

if marks>=80:
    grade_show("A+")

elif marks<80 and marks>=70:
    grade_show("A")
elif marks>=33:
    grade_show("You are pass")

else:
    grade_show("You got A Dabba")

print("Finished")
