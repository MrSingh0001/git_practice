
    details = login()
    dice = roll()
    return


def login ():
    while True:
        name = input('enter your name>>')
        if name == 'name':
            password = input('enter your password>>')
            
            if password == 'password':
                print (' access granted')
                break
            else:
                print('access denied. please try again')
                break
                return()
        
def roll():
    minimum = 1
    maximum = 6
    throw = 'yes'
    answer = 'no'

    import time # so i can store a value 
    import random # so i can get a number between 1 and 6

    throw = input('should i roll the dice')
    while throw == 'yes':

        dice1= (random.randint(minimum,maximum))
        print(dice1)
        time.sleep(1)

        dice2 = (random.randint(minimum,maximum))
        print(dice2)
        time.sleep(1)
        
        break
    
    total1 = dice1 + dice2
    score = (total1)
    if total1%2==1:
        score = total1 +5
    if total1%2==0:
        score = total1 +10

    throw == ("Your total score is", score)
    print(score)
    return()
    
main()
