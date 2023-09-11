def save(compra):
    with open("compras.txt", "a") as arquivo:
        arquivo.write(f"Número: {compra.cartao}\nValor: R${compra._valor}\nCategoria: {compra._categoria}\nEstabelecimento: {compra._estabelecimento}\n\n")