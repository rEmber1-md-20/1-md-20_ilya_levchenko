def allf():
    numberfuc = input("какое задание?")
    match numberfuc:
        case "1": f1()
        case "2": f2()
        case "3": f3()

def f1():
    a = int(input("Введите число: "))
    if a % 5 == 0:
        print("Число делеться на 5 :)")
    else:
        print("Число не делетсья на 5 :(")

def f2():
    try:
        a = int(input("Введите число: "))
        d = 300 / a
        print(d)
    except ValueError:
        print("Ошибка, число не полное!")
    except ZeroDivisionError:
        print("На ноль делить нельзяя!!!")

def f3():
    date = input("Введите дату: ")
    d, m, y = map(int, date.split("."))
    umn = d * m
    last_number = y % 100
    if umn == last_number:
        return print("Магическая дата")
    else:
        return print("Немагическая дата")

allf()







