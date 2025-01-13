#this is a quiz game and you will get the points as you enter the right answer

print('--WELCOME TO THE QUIZ GAME--')
player = input('enter the player name: ')
print (f'welcome!! {player}')
choice=input('enter do you want to continue (y/n): ')
point=0
if choice=='y':
    ques1 = input('what is the capital of India?: ')
    if ques1 == 'Delhi' or 'delhi':
        print('correct')
        point+=1
    else:
        print('wrong')

    ques2 = input('who is the CEO of nvedia?: ')
    if ques2 == 'Jensen huang' or 'jensen huang':
        print('correct')
        point+=1
    else:
        print('wrong')
    
    ques3 = input('what does ML stands for ?: ')
    if ques3 == 'Machine Learning' or 'machine learning':
        print('correct')
        point+=1
    else:
        print('wrong')

    ques4 = input('Are strings mutable in python [yes/no]?: ').lower()
    if ques4 == 'no':
        print('Correct')
        point+=1
    else:
        print('Wrong')

        print(f'your points are:{point} well done!')

elif choice == 'n':
    print('SEE YOU AGIN!')

else:
    print('choose appropriate option')