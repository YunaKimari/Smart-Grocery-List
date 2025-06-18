# === Constants and globals ===
from models.item import Item
from models.lista import ListaDeCompras, datetime
from services.historico import(
    json,
    os,
    carregar_historico,
    salvar_historico,
    atualizar_historico,
    sugerir_valor_item,
    mostrar_menor_preco
    
)
from services.arquivo import re, salvar_lista, carregar_lista  
from config import PASTA_LISTAS
from config import CAMINHO_HISTORICO
from controllers.lista_controllers import (
    input_float,
    criar_lista,
    remover_itens,
    duplicar_lista
)
from controllers.lista_criacao import atualizar_valores_itens        
                                                   
# === Main menu ===    
def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Criar nova lista")
        print("2 - Carregar lista existente")
        print("3 - Duplicar lista existente")
        print("4 - Editar lista existente")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            criar_lista()
        elif opcao == '2':
            lista = carregar_lista()
            if lista:
                print("\n📄 Lista carregada:")
                for item in lista.itens:
                    item.mostrar()
                lista.mostrar_total()
        elif opcao == '3':
            duplicar_lista()
        elif opcao == '4':
            lista = carregar_lista()
            if lista:
                editar_lista(lista)
        elif opcao == '5':
            print("👋 Até a próxima!")
            break
        else:
            print("❌ Opção inválida.")
            
def editar_lista(lista):
    while True:
        print("\nO que você deseja fazer com esta lista?")
        print("1 - Adicionar item(s)")
        print("2 - Remover item(s)")
        print("3 - Atualizar valor de item(s)")
        print("4 - Ver lista atual")
        print("5 - Salvar e sair")
        print("6 - Cancelar edição")
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '1':
            while True:
                nome = input("\nNome do item: ").strip()
                mostrar_menor_preco(nome)
                quantidade = input_float("Quantidade: ")
                unidade = input("Unidade (ex.: kg, g, un): ").strip()
                entrada_valor = input("Valor unitário (ou deixe em branco): R$ ").strip()
                if entrada_valor:
                    try:
                        valor = float(entrada_valor)
                    except ValueError:
                        print("❌ Valor inválido. O item será adicionado sem valor.")
                        valor = None
                else:
                    valor = None
                anotacao = input("Anotação (opcional): ").strip()
                item_obj = Item(nome, quantidade, unidade, valor, anotacao if anotacao else None)
                lista.adicionar_item(item_obj)
                atualizar_historico(item_obj, lista.data_criacao, lista.local)
                if input("Adicionar outro item? (s/n): ").strip().lower() != 's':
                    break
                
        elif escolha == '2':
            remover_itens(lista)
            
        elif escolha == '3':
            atualizar_valores_itens(lista)
            
        elif escolha == '4':
            print("\n📄 Lista atual:")
            for item in lista.itens:
                item.mostrar()
            lista.mostrar_total()
            
        elif escolha == '5':
            salvar_lista(lista)
            print("✅ Alterações salvas com sucesso!")
            break
        
        elif escolha == '6':
            print("❌ Edição cancelada. Nenhuma alteração foi salva.")
            break
        
        else:
            print("❌ Opção inválida.")
                        
def main():
    carregar_historico()
    menu_principal()

# === Entry point ===            
if __name__ == "__main__":
    main()