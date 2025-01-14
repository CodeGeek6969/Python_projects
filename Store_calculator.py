# This program will calculate the sum until Enter is pressed
Final_amount = 0
    
while True:
    amount = input('Enter amount (or press "q" to stop ): ')
    if amount !='q':
        Final_amount += int(amount)
        print(f"Current sum is: {Final_amount}")

        
    else:
        print("thanks for using our store calculator...!")
        break   
    
    
    
    


