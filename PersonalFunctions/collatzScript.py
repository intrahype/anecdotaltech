#work in progress from Automate the Boring Stuff Chapter 3

#a small script to run the collatz sequence for fun

print("Enter number")

number = input()

def collatz():
    print(number)
    if number % 2 == 0:
        number = number / 2
        return number
    if number == 1:
        sys.exit()
    else:
        number = 3 * number + 1
    
