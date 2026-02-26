import random
car_list = ["ferrari", "bugatti", "lamborghini", "mclaren", "pagani", "porsche", "koenigsegg", "fiat", "toyota", "chevrolet", "lexus", "lotus", "maserati", "nissan", "astonmartin"]
random.shuffle(car_list)
rounds = 15
right = 0
right = 0

print("super car game")
for number in range(rounds):
    print("round:", number + 1)
    print("write this car brand:", car_list[number])
    user = input("type here:")
    if user == car_list[number]:
        print("correct")
        right += 1
    else:
        print("incorrect")
        wrong += 1
        