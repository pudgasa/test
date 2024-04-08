def cal(express):
    list_express = express.split()
    if len(list_express) == 3:
        a = int(list_express[0])
        b = int(list_express[2])
        operation = list_express[1]

        if a > 10 or a < 1 or b > 10 or b < 1:
            raise Exception('Формат математической операции не удовлетворяет заданию')
        if operation not in list_operation:
            raise Exception('Формат математической операции не удовлетворяет заданию')
    else:
        raise Exception('Формат математической операции не удовлетворяет заданию')

    result = str(round(eval(express)))
    return result


list_operation = ['+', '-', '*', '/']

while True:
    express = input('Введите выражение: ')

    print(cal(express))
