def main():
    input1 = int(input("Enter number\n1: Encrypt\n2: Decrypt\n3: Brute Force\n> "))
    alpha = []
    for i in range(26):
        alpha.append(chr(97+i))
    if input1 == 1:
        a,b,pt = int(input("Enter A and B Keys, and plaintext\n> ")), int(input("> ")), input("> ")
        if check_input(a,b,pt):
            cipher = encrypt(a,b,pt,alpha)
            print(cipher)
        else:
            print("Invalid Input")
        main()
    elif input1 == 2:
        a,b,ct = int(input("Enter A and B Keys, and ciphertext\n> ")), int(input("> ")), input("> ")
        if check_input(a,b,ct):
            plaintext = decrypt(a,b,ct,alpha)
            print(plaintext)
        else:
            print("Invalid Input")
            main()
    elif input1 == 3:
        ct = input("Enter ciphertext to use brute force\n ")
        bruteforce(ct,alpha)
        main()
    else:
        print("Invalid Input")
        main()
    main()

def bruteforce(ct,alpha):
    pn = ["1","3","5","7","9","11","15","17","19","21","23","25"]
    x = 0
    ui = ""
    while ui == "" and x <= 8:
        for i in range(25):
            print("Testing keys: A: ", pn[x], "B: ", i)
            test = decrypt(int(pn[x]),i,ct,alpha)
            print(test)
            ui = input("[ENTER] to try next key >")
            if ui != "":
                break
        x += 1

def check_input(a,b,ct):
    pn = ["1","3","5","7","9","11","15","17","19","21","23","25"]
    if(str(a) in pn) and (b >= 0 and b <= 25) and (ct.isalpha() == True):
        return True
    else:
        return False

def encrypt(a,b,pt,alpha):
    temp = []
    ts = ""
    for i in range(len(pt)):
        if pt[i] != " ":
            temp.append(alpha[(a * (ord(pt[i])-97) + b) % 26])
        else:
            temp.append(" ")
    ts = "".join(temp)
    return ts

def decrypt(a,b,ct,alpha):
    temp = []
    ts = ""
    mi = 0
    x = 1
    while mi != 1:
        mi = a * x % 26
        x+=1
    print("The multiplicative inverse is: ", x-1)
    for i in range(len(ct)):
        if ct[i] != " ":
            temp.append(alpha[(x-1) * ((ord(ct[i])-97) - b) % 26])
        else:
            temp.append(" ")
    ts = "".join(temp)
    return ts

main()
    

                        
