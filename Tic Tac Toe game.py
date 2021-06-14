line = '---|---|---'
line_1 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
line_2 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
line_3 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
positions = {'t1':1,'t2':5,'t3':9,'m1':1,'m2':5,'m3':9,'b1':1,'b2':5,'b3':9}
players = ['X','O']
game_over = False

def intro():
    print(' T1 | T2 | T3 ')
    print('----|----|----')
    print(' M1 | M2 | M3 ')
    print('----|----|----')
    print(' B1 | B2 | B3 ')
    
    print('\nRules:')
    
    print('Player 1 is represented with "X" and PLayer 2 will be represented with an "O"')
    print('Player 1 will first enter their input for the position of "X"')
    print('To choose the position, please enter the keywords referring to the diagram above. e.g.(to select top left, enter T1)')

def user_input():
    
    # player1 = True, player2 = False
    players_turn = True
    position_remainder = ['t1','t2','t3','m1','m2','m3','b1','b2','b3','FIN']
    player_1 = 'nothing'
    numbers = [1,2,3,4,5]
    
    if game_over is True:
        print('Game Over')

    while game_over is False:
        
        while players_turn is True:
            while player_1 not in position_remainder:
                player_1 = input('Player 1, Please choose a position : ').lower()

            if player_1 in position_remainder:
                players_turn = False
                game_dis1(player_1)
                position_remainder.remove(str(player_1))
                who_wins()
            
        if game_over is True:
            break


        elif position_remainder == ['FIN']:
            print('Draw, Game Over')
            break
            
            
        while players_turn is False:
            player_2 = input('Player 2, Please choose a position : ').lower()

            while player_2 not in position_remainder:
                player_2 = input('Player 2, Please choose a position : ').lower()

            if player_2 in position_remainder:
                players_turn = True
                game_dis2(player_2)
                position_remainder.remove(str(player_2))
                who_wins()

line = '---|---|---'
def game_dis1(chosen_spot):
    
    if chosen_spot[0] == 't':
        line_1[positions[chosen_spot]] = 'X'
        print(''.join(map(str,line_1)))
        print(line)
        print(''.join(map(str,line_2)))
        print(line)
        print(''.join(map(str,line_3)))
        
    elif chosen_spot[0] == 'm':
        line_2[positions[chosen_spot]] = 'X'
        print(''.join(map(str,line_1)))
        print(line)
        print(''.join(map(str,line_2)))
        print(line)
        print(''.join(map(str,line_3)))
        
    elif chosen_spot[0] == 'b':
        line_3[positions[chosen_spot]] = 'X'
        print(''.join(map(str,line_1)))
        print(line)
        print(''.join(map(str,line_2)))
        print(line)
        print(''.join(map(str,line_3)))
        

line2 = '---|---|---'
def game_dis2(chosen_spot2):
    if chosen_spot2[0] == 't':
        line_1[positions[chosen_spot2]] = 'O'
        print(''.join(map(str,line_1)))
        print(line2)
        print(''.join(map(str,line_2)))
        print(line2)
        print(''.join(map(str,line_3)))
        
    elif chosen_spot2[0] == 'm':
        line_2[positions[chosen_spot2]] = 'O'
        print(''.join(map(str,line_1)))
        print(line2)
        print(''.join(map(str,line_2)))
        print(line2)
        print(''.join(map(str,line_3)))
        
    elif chosen_spot2[0] == 'b':
        line_3[positions[chosen_spot2]] = 'O'
        print(''.join(map(str,line_1)))
        print(line2)
        print(''.join(map(str,line_2)))
        print(line2)
        print(''.join(map(str,line_3)))

def who_wins():
    
    global game_over
    for s in players:
        if line_1[1] == s and line_1[5] == s and line_1[9] == s:
            if s == 'X': 
                print('Player 1 wins, Game Over')
                game_over = True
                break
            
            else: 
                print('Player 2 wins, Game Over')
                game_over = True
                break
                
        if line_2[1] == s and line_2[5] == s and line_2[9] == s:
            if s == 'X': 
                print('Player 1 wins, Game Over')
                game_over = True
                break

            else: 
                print('Player 2 wins, Game Over')
                game_over = True
                break
                
        if line_3[1] == s and line_3[5] == s and line_3[9] == s:
            if s == 'X': 
                print('Player 1 wins, Game Over')
                game_over = True
                break
            
            else: 
                print('Player 2 wins, Game Over')
                game_over = True
                break
                
        if line_1[1] == s and line_2[1] == s and line_3[1] == s:
            if s == 'X': 
                print('Player 1 wins, Game Over')
                game_over = True
                break
            
            else: 
                print('Player 2 wins, Game Over')
                game_over = True
                break
                
        if line_1[5] == s and line_2[5] == s and line_3[5] == s:
            if s == 'X': 
                print('Player 1 wins, Game Over')
                game_over = True
                break

            else: 
                print('Player 2 wins, Game Over')
                game_over = True
                break
                
        if line_1[9] == s and line_2[9] == s and line_3[9] == s:
            if s == 'X': 
                print('Player 1 wins, Game Over')
                game_over = True
                break
                
            else: 
                print('Player 2 wins,  Game Over')
                game_over = True
                break
                
        if line_1[1] == s and line_2[5] == s and line_3[9] == s:
            if s == 'X': 
                print('Player 1 wins, Game Over')
                game_over = True
                break
            else: 
                print('Player 2 wins, Game Over')
                game_over = True
                break
                
        elif line_1[9] == s and line_2[5] == s and line_3[1] == s:
            if s == 'X': 
                print('Player 1 wins, Game Over')
                game_over = True
                break
            else: 
                print('Player 2 wins, Game Over')
                game_over = True
                break

        
        else: pass


def The_game():
    intro()
    user_input()

The_game()
