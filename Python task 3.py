from random import randint
import string
print('')
print(''' NUMBER GUESSING GAME!!!''')
print('')

E = ''
M = ''
H = ''

start = True
while start:
    try:
        difficulty = str(input('Select Difficulty[E for Easy, M for Medium, H for hard]: ')).upper()
        start = False
        try:
            if difficulty == 'E':
                secret_num = randint(1,10) 
                print('You have 6 trials')
                for num_guesses in range(6):
                    guess = eval(input('pick guess[1-10]? '))
                    while guess != secret_num:
                        while guess <1 or guess > 10:
                            print('input valid figure, choose from 1-10')
                            guess = eval(input('pick guess[1-10]? '))
                        if guess > secret_num:
                            print ('That was wrong, hint: lesser than previous guess! You have',5-num_guesses,'chance(s) left')
                        if guess < secret_num:
                            print ('That was wrong, hint: greater than previous! You have',5-num_guesses,'chance(s) left')
                        break
                                                    
                    else:                        
                         print('You got it right')
                         break
                else:
                    print ('Gameover!!!')
                    print('The right answer was', secret_num)
                    print ('')
                    start = False
        except ValueError:
            print('Invalid data, play again')
            
             
        try:
            if difficulty == 'M':
                secret_num = randint(1,20)                
                print('You have 4 trials')
                for num_guesses in range(4):
                    guess = eval(input('pick guess[1-20]? '))
                    while guess != secret_num:
                        while guess <1 or guess > 20:
                            print('input valid figure choose from 1-20')
                            guess = eval(input('pick guess[1-20]? '))
                        if guess > secret_num:
                            print ('That was wrong, hint: lesser than previous guess! You have',3-num_guesses,'chance(s) left')
                        if guess < secret_num:
                            print ('That was wrong, hint: greater than previous guess! You have',3-num_guesses,'chance(s) left')
                        break
                                                    
                    else:                        
                         print('You got it right')
                         break
                else:
                    print ('Gameover!!!')
                    print('The right answer was', secret_num)
                    print ('')
                    start = False
        except ValueError:
            print('Invalid data, play again')
            
               
        try:
            if difficulty == 'H':
                secret_num = randint(1,50)                
                print('You have 3 trials')
                for num_guesses in range(3):
                    guess = eval(input('pick guess[1-50]? '))
                    while guess != secret_num:
                        while guess <1 or guess > 50:
                            print('input valid figure choose from 1-50')
                            guess = eval(input('pick guess[1-50]? '))
                        if guess > secret_num:
                            print ('That was wrong, hint: lesser than previous guess! You have',2-num_guesses,'chance(s) left')
                        if guess < secret_num:
                            print ('That was wrong, hint: greater than previous guess! You have',2-num_guesses,'chance(s) left')
                        break
                                                    
                    else:                        
                         print('You got it right')
                         break
                else:
                    print ('Gameover!!!')
                    print('The right answer was', secret_num)
                    print ('')
                    start = False
        except ValueError:
            print('Invalid data, play again')   
                
                
                                                        
    except NameError:
        print('Input valid data, play again')
        
               
    continuation = str(input('Do you want to continue game [yes/no]? ')).upper()
    print('')
    print('')
    if continuation == 'YES':
        start = True
    else:
        start = False
        print('')
    