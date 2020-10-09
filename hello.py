while True:
    secret = 10
    guess = int(input("Guess the secret number: "))

    if guess > secret:
        print("Too high!")

    if guess < secret:
        print("Too low!")

    if guess == secret:
        print("Correct!")
        exit()
