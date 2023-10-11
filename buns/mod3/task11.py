s1 = input()
s2 = input()
s3 = input()

if s1.count('X') == 3 or s2.count('X') == 3 or s3.count('X') == 3:
    print('X')
if s1.count('O') == 3 or s2.count('O') == 3 or s3.count('O') == 3:
    print('O')
    
field = [list(s1), list(s2), list(s3)]

if field[0][0] == field[1][0] and field[1][0] == field[2][0]:
    print('X' if field[0][0] == 'X' else 'O')
    
elif field[0][1] == field[1][1] and field[1][1] == field[2][1]:
    print('X' if field[0][1] == 'X' else 'O')

elif field[0][2] == field[1][2] and field[1][2] == field[2][2]:
    print('X' if field[0][2] == 'X' else 'O')

elif field[0][0] == field[1][1] and field[1][1] == field[2][2]:
    print('X' if field[0][0] == 'X' else 'O')

elif field[0][2] == field[1][1] and field[1][1] == field[2][0]:
    print('X' if field[0][2] == 'X' else 'O')

else: print('Ничья')
