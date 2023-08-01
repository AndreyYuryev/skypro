from pin import check_pin


user_input = input("Введите ваш ПИН-код: ")
if check_pin(user_input):
    print("Такой ПИН-код подходит")
else:
    print("Такой ПИН-код НЕ подходит")