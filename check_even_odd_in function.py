def check_even_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False


starting = 0
while starting < 100:
    if check_even_odd(starting):
        print("Starting number:", even)
    else:
        print("Odd")
    starting = starting + 1

print("Finished")
