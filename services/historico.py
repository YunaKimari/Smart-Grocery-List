import json
import os
from config import CAMINHO_HISTORICO

historico_de_precos = {}

def carregar_historico():
    global historico_de_precos
    if os.path.exists(CAMINHO_HISTORICO):
        with open(CAMINHO_HISTORICO, "r", encoding="utf-8") as f:
            historico_de_precos = json.load(f)
            
def salvar_historico():
    with open(CAMINHO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(historico_de_precos, f, ensure_ascii=False, indent=4)
        
def atualizar_historico(item, data, local):
    if item.valor_unitario is None:
        return
       
    entrada = {
        "data": data,
        "local": local,
        "unidade": item.unidade,
        "valor_unitario": item.valor_unitario,
        "quantidade": item.quantidade,
        "valor_total": item.calcular_total()
    }
        
    nome = item.nome.lower()
    historico_de_precos.setdefault(nome, []).append(entrada)
    salvar_historico()
    
def sugerir_valor_item(nome_item):
    nome = nome_item.lower()
    
    if nome not in historico_de_precos or not historico_de_precos[nome]:
        return None
    
    valores = [e['valor_unitario'] for e in historico_de_precos[nome]]
    return round(sum(valores) / len(valores), 2)

def mostrar_menor_preco(nome_item):
    nome = nome_item.lower()
    
    if nome not in historico_de_precos or not historico_de_precos[nome]:
        return   
    
    menor = min(historico_de_precos[nome], key=lambda x: x['valor_unitario'])
    print(f"💵 Menor valor já pago por '{nome_item}': R$ {menor['valor_unitario']:.2f} no local '{menor['local']}' em 📅 {menor['data']}")