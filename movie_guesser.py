import random
movies = []

for i in range(3):
    movies.append(input("Enter movie name:\n"))

pholder = input("Enter your place holder:\n")

tit = movies[random.randint(0,3)]


def obfuscate_title(tit, pholder):
    n = int(0.8*len(tit))
    for j in range(n):
        k = random.randint(0,len(tit)-1)
        tit=tit.replace(tit[k],pholder)
    return tit

match = obfuscate_title(tit,pholder)
print("Mystery word is",match)

user_guess = input("Guess The Name!\n")
if user_guess.lower() == tit.lower():
    print("correct")
else:
    print("You're Wrong!")
