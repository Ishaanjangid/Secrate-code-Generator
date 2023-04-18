


import random as rn

intro = "'Welcome to the Secret Code Generator'"
print(intro.center(50))
das = '______________________________________'
print(das.center(50))


print()
print("For making Secret Code: Type '1'")
print("For Decoding Secrate Code: Type '2'")
print()
X = int(input("Enter: "))

if X == 1:
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
elif X == 2:
  print("Decoding Code: ")
  a = input("Enter the Message: ")
  b = a.split()

  H = []
  Decode = ''

  for i in b:
    if len(i) <= 3:
      c = i[::-1]

    else:
      G = i[3:]
      d = G[0:len(G)-3]
      e = d[-1]
      f = d[:-1]

      c= e + f
    H.append(c)
  for i in H:
    Decode += i + ' '

  print("The code is Decode")
  print(Decode)
else:
  print("Exit")
  