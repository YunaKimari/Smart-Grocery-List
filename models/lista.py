from datetime import datetime

class ListaDeCompras:
    def __init__(self, titulo, local=None):
        self.titulo = titulo
        self.data_criacao = datetime.now().strftime("%d/%m/%Y")
        self.local = local
        self.itens = []
        
    def mostrar_detalhes(self):
        print(f"\n📋 Lista: {self.titulo}")
        print(f"📅 Data: {self.data_criacao}")
        print(f"🏬 Local: {self.local if self.local else '(não informado)'}")
            
    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"\n✅ Item '{item.nome}' adicionado com sucesso!")
        
    def mostrar_total(self):
        total = sum(item.calcular_total() for item in self.itens if item.valor_unitario)
        print(f"\n💰 Valor total da compra (itens com preço): R$ {total:.2f}")