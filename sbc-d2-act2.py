from random import randint

type1 = "Hayang"
type2 = "Kulob"
c2 = randint(1, 2)
c3 = randint(1, 2)

p1 = input("Enter your Choice 'Hayang' or 'Kulob': ")


if p1 == "Hayang":
    p1 = "Hayang"
    print("RPlayer 1: Hayang")
else:
    p1 = "Kulob"
    print("RPlayer 1: Kulob")

if (c2 == 1):
    c2 = "Hayang"
    print("CPlayer2: Hayang")
else:
    c2 = "Kulob"
    print("CPlayer2: Kulob")


if (c3 == 1):
    c3 = "Hayang"
    print("CPlayer3: Hayang")
else:
    c3 = "Kulob"
    print("CPlayer3: Kulob")


if (p1 == "Hayang" and c2 == "Kulob" and c3 == "Kulob") or (p1 == "Kulob" and c2 == "Hayang" and c3 == "Hayang"):
    print("RPlayer 1 Win")

elif (p1 == "Kulob" and c2 == "Hayang" and c3 == "Kulob") or (p1 == "Hayang" and c2 == "Kulob" and c3 == "Hayang"):
    print("CPlayer 2 Win")

elif (p1 == "Kulob" and c2 == "Kulob" and c3 == "Hayang") or (p1 == "Hayang" and c2 == "Hayang" and c3 == "Kulob"):
    print("CPlayer 3 Win")

else:
    print("No Wins >>> Try again <<<")