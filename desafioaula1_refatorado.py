#Escreva um programa que o usuario inputa seu nome, seu salário e o % do seu bonus e é retornado uma saudação, o valor do bonus
#Salario*bonus + 1000
#Pensar nos erros possíveis e corrigí-los
CONSTANTE_BONUS = 1000
#Input nome
nome = input('Insira seu nome ') #corrigindo caso o nome digitado seja um número/digito

if  nome.isdigit(): #verifica se o input é composto por letras e números
    print('Você digitou seu nome errado')
    exit() #aborta a execução do programa

elif len(nome)==0: #verifica se o input está em branco
    print('Você não digitou seu nome')
    exit() #aborta a execução do programa

elif nome.isspace():
    print('Você digitou só espaço')
    exit()

#input salario
try:
    salario = input('Insira seu salário ')
    salario = float(salario)
except:
    #verificação se o número foi inserido com vírgula
    if ',' in salario or ' ' in salario:
        salario = salario.replace(',', '.').strip() #correção da vírgula para ponto e remoção de espaços em branco
        salario = float(salario)
    elif not salario.isdigit(): #se o input ainda não for um número, entrada inválida
        print('Entrada inválida')
        exit()

#input percentual_bonus
try:
    percentual_bonus = input('Insira o percentual do seu bonus ')
    percentual_bonus = float(percentual_bonus)
except:
    #verificação se o número foi inserido com vírgula
    if ',' in percentual_bonus or ' ' in percentual_bonus:
        percentual_bonus = percentual_bonus.replace(',','.').strip()
        percentual_bonus = float(percentual_bonus)
    elif not salario.isdigit():
        print('Entrada invalida')
        exit()

#calculo do total recebido
calculo = (salario * percentual_bonus)+CONSTANTE_BONUS #substituindo o 1000 hard code por uma variável, melhor a longo prazo
remuneracao_total = salario+calculo

#print
print(f'Olá {nome}, o total de bonus recebido é de {calculo:.2f} e o total recebido no mês é de {remuneracao_total:.2f}')
#o f dentro do print permite printar textos e números/variáveis juntos, do contrário, retornaria um erro. Perceba que a sintaxe muda!!