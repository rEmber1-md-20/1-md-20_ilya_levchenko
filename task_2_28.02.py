c = ''
while True:
    b = input("Какое слово?: ")
    if b == "stop":
        break
    c += b + " "
print(c)