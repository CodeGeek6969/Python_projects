#find prime no between 1 and 100:

num= 100
prime= []             #cretaing an empty list to store prime no

for i in range (1,num+1):         #iterating i till 101
    if i>1:
        for j in range (2,i):  #checking if any other number divides the i if so then its not a prime no and the loop will break
            if i%j == 0:
                break

        else:
            prime.append(i)      #appending it to the list made earlier


print(f"the prime no. till 100 are displayed below: \n {prime}")

#feel free to adjust the range till where you want to display prime numbers!!