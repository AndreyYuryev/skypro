from validators.validate_card import validate_card
from validators.validate_pin import validate_pin

print('Введите ваш номер карты')
card_number = input()
print("Введите ваш ПИН-код")
card_pin = input()

if validate_card(card_number):
    print("Номер карты допустимый")
else:
    print("Номер карты недопустимый")

if validate_pin(card_pin):
    print("ПИН-код допустимый")
else:
    print("ПИН-код недопустимый")
