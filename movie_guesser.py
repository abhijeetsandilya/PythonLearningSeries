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

# import random
#
# movies = []
#
# for i in range(3):
#     movies.append(input("Enter movie name:\n"))
#
# pholder = input("Enter your placeholder:\n")
#
# tit = movies[random.randint(0, 2)]
#
#
# def obfuscate_title(title, pholder):
#     title_list = list(title)
#     n = int(0.7 * len(title))
#
#     positions = random.sample(range(len(title)), n)
#
#     for pos in positions:
#         title_list[pos] = pholder
#
#     return "".join(title_list)
#
#
# new_tit = obfuscate_title(tit, pholder)
#
# print("Mystery word is:", new_tit)
#
# user_guess = input("Guess The Name!\n")
# if user_guess == tit:
#     print("Correct!")
# else:
#     print("You're Wrong! The correct movie was:", tit)