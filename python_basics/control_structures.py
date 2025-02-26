# 1
def is_even(num):
    if (num % 2 == 0):
        print("number is even")
    else:
         print("number is odd")
        

while True:
    try:
        number = int(input("Enter your number : "))
        is_even(number)
        break

    except ValueError:
        print("invalid input")

# 2
for i in range(1,51):
    print(i)

# 3
x=10
while x <= 10:
    print(x)
    x-=1

    if x == 0:
        break
