punkty = int(input("Podaj punkty: "))

if punkty > 100:
    print("za dużo punktów")
elif punkty >= 90:
    print("Ocena: 5")
elif punkty >= 80:
    print("Ocena: 4")
elif punkty >= 70:
    print("Ocena: 3")
elif punkty >= 60:
    print("Ocena: 2")
elif punkty >= 0:
    print("Ocena: 1")
else:
    print("za mało punktów")
