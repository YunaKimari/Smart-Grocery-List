from models.item import Item
from services.historico import atualizar_historico, mostrar_menor_preco, sugerir_valor_item

def adicionar_itens_a_lista(lista):
    while True:
        nome = input("\nNome do item: ").strip()
        mostrar_menor_preco(nome)

        try:
            quantidade = float(input("Quantidade: ").strip())
        except ValueError:
            print("❌ Quantidade inválida. Tente novamente.")
            continue

        unidade = input("Unidade (ex.: kg, g, un): ").strip()

        valor_sugerido = sugerir_valor_item(nome)
        if valor_sugerido:
            print(f"\n💵 Valor sugerido: R$ {valor_sugerido:.2f}")
            usar = input("Deseja usar esse valor? (s/n): ").strip().lower()
            if usar == 's':
                valor = valor_sugerido
            else:
                try:
                    valor = float(input("Digite o valor unitário: R$ ").strip())
                except ValueError:
                    print("❌ Valor inválido. O item será adicionado sem valor.")
                    valor = None
        else:
            try:
                valor = float(input("Digite o valor unitário: R$ ").strip())
            except ValueError:
                print("❌ Valor inválido. O item será adicionado sem valor.")
                valor = None

        anotacao = input("Anotação (opcional): ").strip()
        item = Item(nome, quantidade, unidade, valor, anotacao if anotacao else None)

        lista.adicionar_item(item)
        atualizar_historico(item, lista.data_criacao, lista.local)

        continuar = input("Adicionar outro item? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("\n📄 Itens na lista:")
    for item in lista.itens:
        item.mostrar()

    lista.mostrar_total()

    if input("\nDeseja atualizar o valor de algum item? (s/n): ").strip().lower() == 's':
        atualizar_valores_itens(lista)

    print("\n📄 Lista final:")
    for item in lista.itens:
        item.mostrar()

    lista.mostrar_total()
    
def atualizar_valores_itens(lista):
    while True:
        print("\n📋 Itens na lista:")
        for i, item in enumerate(lista.itens):
            print(f"{i + 1}. {item.nome} - Valor atual: {f'R$ {item.valor_unitario:.2f}' if item.valor_unitario else '(não definido)'}")        
        escolha = input("\nDigite o número do item para atualizar o valor ou 's' para sair: ").strip().lower()
        
        if escolha == 's':
            break 
        
        if escolha.isdigit() and 1 <= int(escolha) <= len(lista.itens):
            index = int(escolha) - 1
            try:
                novo_valor = float(input(f"Novo valor unitário para '{lista.itens[index].nome}': R$ "))
                lista.itens[index].valor_unitario = novo_valor
                atualizar_historico(lista.itens[index], lista.data_criacao, lista.local)
                print(f"✅ Valor atualizado!")
            except ValueError:
                print("❌ Valor inválido. Digite um número.")
        else:
            print("❌ Entrada inválida.")