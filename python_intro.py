#introdução ao mundo Python
print('--------------------------------')
print('--- Cadastro de funcionarios ---')
print('Seus dados estarão seguros, vamos lá?')
print('--------------------------------')
nome    = input("Escreva seu nome: ")
idade   = input("Sua idade: ")

if idade >= '18':    
     
    end     = input("Seu endereço: ")
    prof    = input("Sua profissão: ")
    
    print("Agradecemos Sr(a): ", nome )
    
    with open('DadosFunc.txt', 'w') as arquivo:
        print("Nome:"+ " " + nome, file=arquivo)
        print("Idade:"+ " " + idade, file=arquivo)
        print("End:"+ " " + end, file=arquivo)
        print("Profissão:"+ " " + prof, file=arquivo)
else:      
    print('Idade minima: 18 anos.')