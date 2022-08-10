def hellow():
    print('hellow')

def fileopen():
    print ('Открываем на чтение файл и по необходимости выводим в другой файл или консоль')
    Fin = open('C:/python/input.txt')
    choose = input('Выводим в файл?')
    if choose == 'да':
        Fout = open('C:/python/output.txt','w')
        for str in Fin:
            Fout.write(str + "\n")
        print('вывели')
    else:
        for str in Fin:
            mass = Fin.read()
            smass = mass.split()
            print(mass, end="")
