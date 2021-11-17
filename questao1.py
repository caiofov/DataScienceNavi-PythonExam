count=0 #variável que irá contar os números

for i in range(0,5000001,2): #irá passar apenas pelos números pares
    if (i%49 == 0 and i%37 == 0): #se for divisível por 49 e por 37
        count+=1 #incrementa a variavel

print(count)