height = int(input("What is you height in cm? "))

if height < 120:
    print("Sorry, you are not tall enough to ride. ")
else:
    age = int(input("What is your age? "))
    if age < 12:
        print("Your child ticket is $5")
    else:
        print("Your adult ticket is $10")