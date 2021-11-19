count=0 #variável que irá contar os números

for i in range(0,5000001,2): #irá passar apenas pelos números pares -> uma forma de diminuir o custo do algoritmo
    
    if (i%49 == 0 and i%37 == 0): #se for divisível por 49 e por 37
        count+=1 #incrementa a variavel

print("A quantidade de números entre 1 e 5000000 que seguem os requisitos é", count)