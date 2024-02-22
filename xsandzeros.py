doska = [[' ' for _ in range(3)] for _ in range(3)]
def print_doska(doska):
    for row in doska:
        print(' | '.join(row))
        print('---------')

current_player = '1'
while True:
    print_doska(doska)
    row = int(input(f'Игрок {current_player}, введите номер строки (0, 1 или 2): '))
    col = int(input(f'Игрок {current_player}, введите номер столбца (0, 1 или 2): '))
    if doska[row][col] == ' ':
        doska[row][col] = current_player

        if current_player == '1':
            current_player = '2'
        else:
            current_player = '1'
    else:
        print('Клетка уже занята, выберите другую!')
