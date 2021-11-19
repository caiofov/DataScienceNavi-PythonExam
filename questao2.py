from math import factorial, log

vetor = []

for i in range(10): #vetor de 10 posiçoes (0 a 9)
    if(i%2 == 0): #se for par
        vetor.append(pow(3,i)+7*factorial(i)) 

    else: #se for impar
        vetor.append(2+4*log(i))


print("Maior elemento: %.2f \nMédia: %.2f" %(max(vetor), (sum(vetor)/len(vetor)) ))