from compra_dto import Compra
from datetime import date
from compra_repository import save

def cadastrar(numero_cartao, valor_compra, categoria, estabelecimento_compra):
    if valor_compra < 0:
        raise ValueError("O valor da compra não pode ser negativo.")

    categorias = {
        1: "saúde",
        2: "alimentação",
        3: "educação",
        4: "lazer"
    }

    categoria_str = categorias[categoria]
    compra = Compra(valor_compra, date.today(), estabelecimento_compra, categoria_str, numero_cartao)
    save(compra)




