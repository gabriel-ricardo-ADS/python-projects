# input das notas das matérias 
notaPython = float(input('Nota de Python: '))
notaJava = float(input('Nota de Java: '))
notaFront = float(input('Nota de Front End: '))
notaEng = float(input('Nota de Engenharia de Software: '))
notaData = float(input('Nota de Database: '))
notaIA = float(input('Nota de IA: '))

notas_Aluno = {    # Dicionario de nome das matérias e notas
    'Python': notaPython, 
    'Java': notaJava, 
    'Front End': notaFront, 
    'Eng Soft': notaEng, 
    'Database': notaData,
    'IA': notaIA,
}
    

# calculo da média
media_notas = sum(notas_Aluno.values()) / len(notas_Aluno)

print(f"\nMedia do Aluno: {media_notas:.2f}") # Adicionado :.2f para mostrar 2 casas decimais

input('\naperte ENTER para sair')