
def allf():
    numberfuc = input("какое задание?")
    match numberfuc:
        case "1": f1()
        case "2": f2()
        case "3": f3()
        case "4": f4()
def f1():
    a = [12,34,2,5677,45]
    n = int(input("Введите число: "))
    if n in a:
        print("Вы угадали!!!")
    else:
        print("Поробуйте еще раз!")



def f2():
    a = [12,45,"bkmz","bkmz",12,345]
    p = []
    for i in a:
        if a.count(i) > 1:
            p.append(i)
    p = set(p)
    print(p)



def f3():
    dn = ("pn","vt","sr","cht","pt","sub","vs")
    n = int(input("Сколько дней недели вы хотите?: "))
    vahod = dn[-n:]
    works = dn[:-n]
    print("Выходные: ",vahod,"Рабочие дни: ",works)



def f4():
    g1 = ["Иванов","Левченко","Матвеев","Решетников","Близгарёв","Казадерова","Федеров","Кучев","Семенов"]
    g2 = ["Соколенко", "Казарян", "Белкина", "Гагельганс", "Токарева", "Идрисова", "Попов", "Богданчук", "Малкиель"]
    Comand = tuple(g1[:5] + g2[:5])
    print('группа 1: ', g1)
    print('группа 2: ', g2)
    print('футбольная команда: ', Comand)
    print(len(Comand))
    Comand = sorted(Comand)
    print(Comand)
    ivanov = Comand.count('Иванов')
    print('в команде с фамилией "Иванов" ', ivanov, ' человек(a)')

allf()



