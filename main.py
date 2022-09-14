import random

def spsci(comp,mine):
    if (comp==mine):
        return None
    if(comp=='stone'and mine=="paper"):
        '''wining possibilities'''
        return True
    elif(comp=="paper" and mine=="scissors"):
        return True
    elif(comp=="scissors" and mine=="stone"):
        return True
    else:
        return False

choice = ('stone','paper','scissors')

comp = random.randint(0,2) 
'''computer will chose randomly'''
comp = choice[comp] # i'm just converting the numbers with stone,paper and scissors

mine = input('Choose either stone,paper or scissors :')

win = spsci(comp,mine)

print(f"You chose {mine} and the computer chose {comp}")

if win==None: 
    '''function call'''
    print('Match Drawn ')
elif win:
    
    print("You won")
else:
    
    print("You lose")