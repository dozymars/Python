secret_number = 9
guess_number = int(input("guess a number: "))

while guess_number != secret_number:
    print("Try Again")
    Try = int(input("guess another number: "))
    if Try == int(9):
        print("got it")


     
