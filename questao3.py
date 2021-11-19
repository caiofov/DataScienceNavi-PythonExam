
notas = {} #dicionario de notas

for i in range(5): #loop roda 5 vezes
    aluno = "aluno "+str(i+1) #o aluno a qual o loop está referenciando
    
    nota = float(input("Insira a nota do %s: " %aluno)) #recebe o input
    
    notas[aluno] = nota #guarda a nota no dicionario

maxAluno = max(notas, key=notas.get) #acha a chave do dicionario que possui o maior valor

print("A maior nota é do %s e foi %.2f" %(maxAluno, notas[maxAluno]))


