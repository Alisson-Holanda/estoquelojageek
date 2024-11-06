#Estoque loja GEEK NERD
os import
os.system

estoque = []

while True:
    menu = input('''
Escolha uma opção:
(1) Cadastrar
(2) Consultar
(3) Alterar
(4) Relatório 
(5) Deletar Item
(6) Sair
==>  ''')

if menu == '1':
    prod = input('Digite o nome do produto: ')
    cod = input('Código do Produto: ')
    marca = input('Marca do produto: ')
    cat = input('Categoria: ')
    desc = input('Insira a descrição: ')
    estoque.append([prod, cod, marca, cat , desc])
    print('Produto adicionado ao estoque!', cod, prod, marca, cat , desc)
    input('Deseja voltar ao menu? Digite Sim ou Não: ')
    #esta mostrando o numero 1 ao terminal, corrigir
    if 'Sim':
        #aqui tb n funcionou
        print(menu)
    elif 'Não':
        exit
elif menu == '2':
    print(estoque)
    
elif menu == '3':
    input('Digite o item a ser alterado: ')
    estoque.append([cod, prod, val, marca , cat, desc])
    
elif menu == '4':
    print(estoque)
    
elif menu == '5':
    estoque.remove
    
elif menu == '6':
    print('Encerrando o programa.')

else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
    