#this is a simpe dice simmulator game where user can roll the dice and get the output of the dice

import random
print('--WELCOME TO THE DICE SIMULATOR--')

outputs=[1,2,3,4,5,6]
while True:
    print('Press (1) to roll the dice and (2) to exit')
    
    user_input=float(input('Enter your choice:'))
    if user_input == 1:
        
        print("Rolling the dice...no. is : ", random.sample(outputs,1))
        
    
    elif user_input == 2:
        print('thanks for palying!!')
        break

            




    


    




