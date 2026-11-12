produtos = []


opcao = 0

while opcao != 9:
    print("1 - Adicionar um produto")
    print("2 - Listar produtos")
    print("3 - Consultar produto")
    print("4 - Remover produto")
    print("5 - Atualizar a quantidade")
    print("6 - Atualizar o preço")
    print("7 - Valor total do estoque")
    print('8 - Produto com maior quantidade')
    print('9 - Sair')
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o valor do produto: "))
        while preco < 0:
            print("Preço inválido. O preço não pode ser negativo.")
            preco = float(input("Digite o valor do produto: "))
        quantidade = int(input("Quantas unidades existem? "))
        while quantidade < 0:
            print("Quantidade inválida. A quantidade não pode ser negativa.")
            quantidade = int(input("Quantas unidades existem? "))
        produto = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }
        produtos.append(produto)

    elif opcao == 2:
        for produto in produtos:
            print(f'Produto: {produto["nome"]} \nPreço: R${produto["preco"]:.2f} \nQuantidade: {produto["quantidade"]}')
            print('-----------------------------')
        
    elif opcao == 3:
        nome_busca = input("Digite o produto que deseja consultar: ").lower()
        encontrado = False
        for produto in produtos:
            if produto["nome"].lower() == nome_busca:
                encontrado = True
                print(f'Produto: {produto["nome"]} \nPreço: R${produto["preco"]:.2f} \nQuantidade: {produto["quantidade"]}')
                print('-----------------------------')
        if encontrado == False:
            print("Produto não encontrado.")

    elif opcao == 4:
        nome_remover = input("Digite o nome do produto que deseja remover: ").lower()
        encontrado = False
        for produto in produtos:
            if produto["nome"].lower() == nome_remover:
                encontrado = True
                produtos.remove(produto)
                print("produto removido com sucesso.")
                break
                
        if encontrado == False:
            print("Produto não encontrado.")

    elif opcao == 5:
        nome_busca = input("Qual produto deseja atualizar a quantidade? ").lower()
        encontrado = False
        for produto in produtos:
            if produto["nome"].lower() == nome_busca:
                encontrado = True
                nova_quantidade = int(input("Digite a nova quantidade: "))
                while nova_quantidade < 0:
                    print("Quantidade inválida. A quantidade não pode ser negativa.")
                    nova_quantidade = int(input("Digite a nova quantidade: ")) 
                produto["quantidade"] = nova_quantidade
                print("Quantidade atualizada com sucesso.")
                break
        if encontrado == False:
            print("Produto não encontrado.")         

    elif opcao == 6:
        nome_busca = input("Qual produto deseja atualizar o preço? ").lower()
        encontrado = False
        for produto in produtos:
            if produto["nome"].lower() == nome_busca:
                encontrado = True
                novo_preco = float(input("Digite o novo preço: "))
                while novo_preco < 0:
                    print("Preço inválido. O preço não pode ser negativo.")
                    novo_preco = float(input("Digite o novo preço: "))
                produto["preco"] = novo_preco
                print("Preço atualizado com sucesso.")
                break
        if encontrado == False:
            print('Produto não encontrado. ')

    elif opcao == 7:
        total_estoque = 0
        for produto in produtos:
            total_estoque += produto["preco"] * produto["quantidade"]

        print(f'O valor total do estoque é: R${total_estoque:.2f}')

    elif opcao == 8:
        maior_quantidade = 0
        nome_maior = ''
        if len(produtos) == 0:
            print("Não existem produtos cadastrados ainda.")
        else:

            for produto in produtos:
                if produto["quantidade"] > maior_quantidade:
                    maior_quantidade = produto["quantidade"]
                    nome_maior = produto["nome"]

            print(f"O produto com maior quantidade é: {nome_maior}")
            print(f'Quantidade: {maior_quantidade}')

    elif opcao == 9:
        print('Encerrando o sistema...')

    else:
        print("Opção inválida. Digite novamente.")


