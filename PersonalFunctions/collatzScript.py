#work in progress from Automate the Boring Stuff Chapter 3

#a small script to run the collatz sequence for fun

def collatz(value):
    """
    Function to print the collatz sequence from an user inputted number
    param: int(intput())
    return: return printed list of numbers from input to 1
    """
    steps = 0   #intialize steps variable at 0 to count number of mutations
    print(value)    #print initial value
    while value != 1:   #while loop to look for condition of value == 1
        if (value % 2) == 0:    #check value and mutate as appropriate
            value = value / 2
            steps += 1
            print(value)    #print mutated value
        else:
            value = (value * 3) + 1
            steps +=1
            print(value)    #print mutated value
    return steps    #return number of mutations before value == 1