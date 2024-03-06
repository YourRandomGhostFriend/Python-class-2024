def main():
    hour = 23
    minute = 59
    print("Enter hours first, and then minutes ")
    hours = read(0, hour)
    minutes = read(0, minute)
    print (f'You entered {hours} hours and {minutes} minutes')
    

def read(low, high):
    value = int(input(f'Enter a value between {low} and {high} '))
    while value < low or value > high:
        print("error - enter a correct value")
        value = int(input("Enter a value "))
    return value

main()
