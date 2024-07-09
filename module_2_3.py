print('Задача "Нули ничто, отрицание недопустимо!"')
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
current_item = 0
while current_item <= len(my_list):
    if my_list[current_item] > 0:
        print(my_list[current_item])
    current_item = current_item + 1
    if my_list[current_item] < 0:
        break
    if my_list[current_item] == 0:
        break