import json
import os
import re
from datetime import datetime
from models.lista import ListaDeCompras
from models.item import Item
from config import PASTA_LISTAS

def buscar_listas_por_titulo():
    if not os.path.exists(PASTA_LISTAS):
        print("📁 Nenhuma lista salva encontrada.")
        return[]
    
    arquivos = sorted(
        [f for f in os.listdir(PASTA_LISTAS) if f.endswith(".json")],
        key=lambda x: os.path.getmtime(os.path.join(PASTA_LISTAS, x)),
        reverse=True
    )
    
    if not arquivos:
        print("📁 Nenhuma lista salva encontrada.")
        return[]
    
    termo = input("Digite uma palavra-chave para buscar no título: ").strip().lower()
    resultados = []
    
    for f in arquivos:
        nome_formatado = f.replace("_", " ").replace(".json", "").lower()
        if termo in nome_formatado:
            resultados.append(f)
            
    if not resultados:
        print("Nenhuma lista encontrada com esse termo.")
    else:
        print("\nResultados encontrados:")
        for i, nome in enumerate(resultados, 1):
            caminho = os.path.join(PASTA_LISTAS, nome)
            modificado_em = datetime.fromtimestamp(os.path.getmtime(caminho)).strftime("%d/%m/%Y %H:%M")
            with open(caminho, "r", encoding="utf-8") as f:
                dados = json.load(f)
                qtd_itens = len(dados.get("itens", []))
            print(f"{i}. {nome} | 🕒 {modificado_em} | 📦 {qtd_itens} item(ns)")
            
    return resultados

def salvar_lista(lista):
    if not os.path.exists(PASTA_LISTAS):
        os.makedirs(PASTA_LISTAS)
        
    nome_arquivo = f"{lista.titulo} - {lista.data_criacao}.json"
    nome_arquivo = re.sub(r'[\\/*?:"<>|]', "", nome_arquivo).replace(" ", "_")
    caminho = os.path.join(PASTA_LISTAS, nome_arquivo)
    dados = {
        "titulo": lista.titulo,
        "data_criacao": lista.data_criacao,
        "local": lista.local,
        "itens": [
            {
                "nome": item.nome,
                "quantidade": item.quantidade,
                "unidade": item.unidade,
                "valor_unitario": item.valor_unitario,
                "anotacao": item.anotacao
            } for item in lista.itens
        ]
    }
    
    if os.path.exists(caminho):
        resposta = input(f"⚠️ O arquivo '{nome_arquivo}' já existe. Deseja sobrescrevê-lo? (s/n): ").strip().lower()
        if resposta != 's':
            print("❌ Salvamento cancelado.")
            return
    
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print(f"\n💾 Lista salva como '{nome_arquivo}' na pasta '{PASTA_LISTAS}'.")
    
def carregar_lista():
    if not os.path.exists(PASTA_LISTAS):
        print("📁 Nenhuma lista salva encontrada.")
        return None

    arquivos = sorted(
        [f for f in os.listdir(PASTA_LISTAS) if f.endswith(".json")],
        key=lambda x: os.path.getmtime(os.path.join(PASTA_LISTAS, x)),
        reverse=True
    )

    if not arquivos:
        print("📁 Nenhuma lista salva encontrada.")
        return None
    
    usar_busca = input("Deseja buscar uma lista por título? (s/n): ").strip().lower()
    if usar_busca == 's':
        arquivos = buscar_listas_por_titulo()
        if not arquivos:
            return None
        
    print("\n📂 Listas disponíveis:")
    for i, nome_arquivo in enumerate(arquivos):
        caminho = os.path.join(PASTA_LISTAS, nome_arquivo)
        modificado_em = datetime.fromtimestamp(os.path.getmtime(caminho)).strftime("%d/%m/%Y %H:%M")
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                dados = json.load(f)
                qtd_itens = len(dados.get("itens", []))
        except:
            qtd_itens = "?"
        print(f"{i + 1}. {nome_arquivo} | 🕒 Modificado em: {modificado_em} | 📦 {qtd_itens} item(ns)")
    
    escolha = input("Digite o número da lista que deseja carregar: ").strip()
    if not escolha.isdigit() or not (1 <= int(escolha) <= len(arquivos)):
        print("❌ Escolha inválida.")
        return None
    
    caminho = os.path.join(PASTA_LISTAS, arquivos[int(escolha) - 1])
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)
        
    lista = ListaDeCompras(dados["titulo"], dados["local"])
    lista.data_criacao = dados["data_criacao"]
    
    for i in dados["itens"]:
        item_obj = Item(
            nome=i["nome"],
            quantidade=i["quantidade"],
            unidade=i["unidade"],
            valor_unitario=i.get("valor_unitario"),
            anotacao=i.get("anotacao")
        )
        lista.itens.append(item_obj)
        
    print(f"\n✅ Lista '{lista.titulo}' carregada com sucesso!\n")
    return lista