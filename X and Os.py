a = 0
Grid = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
while a < 9:
    Xx = int(input('Enter the row for the X '))
    Xy = int(input('Enter the column for the X '))
    while Grid[(Xx-1)*3 + Xy - 1] == 'O':
        print('There is something there')
        Xx = int(input('Enter the row for the X '))
        Xy = int(input('Enter the column for the X '))
    Grid[(Xx-1)*3 + Xy - 1] = 'X'
    print(Grid[0],'|',Grid[1],'|',Grid[2])
    print('= = = = =')
    print(Grid[3],'|',Grid[4],'|',Grid[5])
    print('= = = = =')
    print(Grid[6],'|',Grid[7],'|',Grid[8])
    if Grid[0] == Grid[1] == Grid[2] == ('O' or 'X') or Grid[3] == Grid[4] == Grid[5] == ('O' or 'X') or Grid[6] == Grid[7] == Grid[8] == ('O' or 'X') or Grid[0] == Grid[3] == Grid[6] == ('O' or 'X') or Grid[1] == Grid[4] == Grid[7] == ('O' or 'X') or Grid[2] == Grid[5] == Grid[8] == ('O' or 'X') or Grid[0] == Grid[4] == Grid[8] == ('O' or 'X') or Grid[2] == Grid[4] == Grid[6] == ('O' or 'X'):
        input('Game over. Would you like to play again? ')
        if ans.lower == 'yes':
            a = 0
            Grid = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        else:
            a = 9
            break
    Ox = int(input('Enter the row for the O '))
    Oy = int(input('Enter the column for the O '))
    while Grid[(Ox-1)*3 + Oy - 1] == 'X':
        print('There is something there')
        Ox = int(input('Enter the row for the O '))
        Oy = int(input('Enter the column for the O '))
    Grid[(Ox-1)*3 + Oy - 1] = 'O'
    print(Grid[0],'|',Grid[1],'|',Grid[2])
    print('= = = = =')
    print(Grid[3],'|',Grid[4],'|',Grid[5])
    print('= = = = =')
    print(Grid[6],'|',Grid[7],'|',Grid[8])
    if Grid[0] == Grid[1] == Grid[2] == ('O' or 'X') or Grid[3] == Grid[4] == Grid[5] == ('O' or 'X') or Grid[6] == Grid[7] == Grid[8] == ('O' or 'X') or Grid[0] == Grid[3] == Grid[6] == ('O' or 'X') or Grid[1] == Grid[4] == Grid[7] == ('O' or 'X') or Grid[2] == Grid[5] == Grid[8] == ('O' or 'X') or Grid[0] == Grid[4] == Grid[8] == ('O' or 'X') or Grid[2] == Grid[4] == Grid[6] == ('O' or 'X'):
        input('Game over. Would you like to play again? ')
        if ans.lower == 'yes':
            a = 0
        else:
            a = 9
    elif a == 8:
        ans = input('Draw. Would you like to play again? ')
        if ans.lower == 'yes':
            a = 0
            Grid = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        else:
            a = 9
print('Thank you for playing')