def decode():
   
   



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

decode()