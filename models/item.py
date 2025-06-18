class Item:
    def __init__(self, nome, quantidade, unidade, valor_unitario=None, anotacao=None):
        self.nome = nome
        self.quantidade = quantidade
        self.unidade = unidade
        self.valor_unitario = valor_unitario
        self.anotacao = anotacao
        
    def calcular_total(self):
        return self.quantidade * self.valor_unitario if self.valor_unitario else 0
    
    def mostrar(self):
        print(f"\n📌 {self.nome} - {self.quantidade} {self.unidade}(s)")
        print(f"💵 Valor unitário: R$ {self.valor_unitario:.2f}" if self.valor_unitario else "💵 Valor unitário: (a definir)")
        print(f"💰 Total: R$ {self.calcular_total():.2f}" if self.valor_unitario else "💰 Total: (indisponível)")
        if self.anotacao:
            print(f"📝 Anotação: {self.anotacao}")