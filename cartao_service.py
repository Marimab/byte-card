from cartao_dto import Cartao
from datetime import date
from cartao_repository import save

class CartaoService:
    def cadastrar(self, numero_cartao, nome_cliente, limite, validade, cvv):
        self.numero_cartao = numero_cartao
        self.nome_cliente = nome_cliente
        self.limite= limite
        self.validade = validade
        self.cvv = cvv

        if len(numero_cartao) != 16:
            raise ValueError("O número do cartão deve ter 16 dígitos.")

        if limite <= '0':
            raise ValueError("O limite do cartão não pode ser negativo.")

        numero_ultimos_digitos = numero_cartao[-4:]
        #print(f"Cartão cadastrado com sucesso - Número: {numero_ultimos_digitos}")
        

