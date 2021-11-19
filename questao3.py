
notas = {}

for i in range(5):
    aluno = "aluno "+str(i+1)
    
    nota = float(input("Insira a nota do %s: " %aluno))
    
    notas[aluno] = nota

alunoMaior = max(notas, key=notas.get)
print("A maior nota é do %s e foi %.2f" %(alunoMaior, notas[alunoMaior]))


