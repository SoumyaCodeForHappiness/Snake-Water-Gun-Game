# Snake Water Gun
# N.B - 
# S --> Snake
# w --> Water
# g --> Gun
import random
def game(comp, you):
    # If two values are equal, declare a tie
    if you == comp:
        return None
    # check for all possibilities when computer chose Snake
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    # check for all possibilities when computer chose Water
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True 
    # check for all possibilities when computer chose Gun
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True   
print("Computer's Turn: Snake(s) water(w) or gun(g) ?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
else:
    comp = 'g'
you = input("Your Turn: Snake(s) water(w) or gun(g) ?")
a = game(comp, you)

if a == None:
    print('The ganme is a tie!')
elif a:
    print('You Win!')
else:
    print('You Lose!')
