
import random as rn


def coding():
    print("Making Code: ")
    a = input("Enter the string: ")
    b = a.split()

    random = ['vfu','eto','eyr','xcv','org']
    F = rn.choice(random)
    L = rn.choice(random)
    d = []
    str = ''
    for i in b:
        if len(i) <= 3:

            c = i[::-1]

        else:

            a = i[0]
            b = i[1:]
            c = b + a
            c = F + c + L
        d.append(c)

    for i in d:
        str += i + ' '

    print("The code is Ready :")
    print(str)
coding()