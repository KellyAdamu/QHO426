import random #Takind definitions from a package "random" into my scope

secret_n = random. randint(1,20)
print("Welcome to my Guess Game! I am thinking of a number betwenn 1 and 20")

for attempts in range(1,6):
    print(f"Attempt nr {attempts}")
    guess = int(input("Take a guess"))
    if guess == secret_n:
        print("Congrats! You have guessed correctly!")
        break
    elif guess > secret_n:
        print("Too high!")
    else:
        print("Too low!")
if guess != secret_n:
    print(f"Game Over! My number was {secret_n}")
