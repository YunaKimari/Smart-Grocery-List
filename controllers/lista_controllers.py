from models.lista import ListaDeCompras
from models.item import Item
from services.historico import (
    atualizar_historico,
    sugerir_valor_item,
    mostrar_menor_preco
)
from services.arquivo import (
    salvar_lista,
    carregar_lista,
    buscar_listas_por_titulo
)
from controllers.lista_criacao import adicionar_itens_a_lista, atualizar_valores_itens

def input_float(mensagem):
    while True:
        entrada = input(mensagem).strip()
        try:
            return float(entrada)
        except ValueError:
            print("❌ Valor inválido. Digite um número válido, como 1, 2.5, 10...")   

def criar_lista():
    titulo = input("Título da nova lista: ").strip()
    while not titulo:
        print("❌ O título da lista é obrigatório.")
        titulo = input("Título da nova lista: ").strip()

    local = input("Local da compra (opcional): ").strip()
    lista = ListaDeCompras(titulo, local if local else None)
    lista.mostrar_detalhes()

    adicionar_itens_a_lista(lista)
    salvar_lista(lista)

def duplicar_lista():
    lista_original = carregar_lista()
    
    if not lista_original:
        return
    
    novo_titulo = input("\nDigite o novo título para a lista duplicada: ").strip()
    novo_local = input("Digite o local da nova compra (opcional): ").strip()
    nova_lista = ListaDeCompras(novo_titulo, novo_local if novo_local else None)
    
    for item in lista_original.itens:
        item_copiado = Item(
            nome=item.nome,
            quantidade=item.quantidade,
            unidade=item.unidade,
            valor_unitario=item.valor_unitario,
            anotacao=item.anotacao
        )
        nova_lista.adicionar_item(item_copiado)
    
    print("\n📄 Lista copiada:")
    
    for item in nova_lista.itens:
        item.mostrar()
    nova_lista.mostrar_total()
    
    if input("\nDeseja remover algum item antes de salvar? (s/n): ").strip().lower() == 's':
        remover_itens(nova_lista)
        
    if input("Deseja adicionar novos itens à lista? (s/n): ").lower().strip() == 's':
        adicionar_itens_a_lista(nova_lista)
        
    if input("Deseja atualizar valores de algum item? (s/n): ").lower().strip() == 's':
        atualizar_valores_itens(nova_lista)
        
    salvar_lista(nova_lista)
    
def remover_itens(lista):
    while True:
        if not lista.itens:
            print("❌ A lista está vazia. Nenhum item para remover.")
            break       
        print("\n📄 Itens na lista:")
        for i, item in enumerate(lista.itens, 1):
            print(f"{i}. {item.nome} - {item.quantidade} {item.unidade}")           
        escolha = input("\nDigite o número do item que deseja remover (ou 's' para sair): ").strip().lower()
        if escolha == 's':
            break
        elif escolha.isdigit() and 1 <= int(escolha) <= len(lista.itens):
            removido = lista.itens.pop(int(escolha) - 1)
            print(f"✅ Item '{removido.nome}' removido com sucesso!")
        else:
            print("❌ Entrada inválida.")