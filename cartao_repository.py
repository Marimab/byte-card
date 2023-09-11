def save(cartao):
    with open("cartao.txt", "a") as arquivo:
        arquivo.write(f"Número do cartao: {cartao.numero}\nValidade: {cartao.validade}\nCVV: {cartao.cvv}\nLimite do cartao: R${cartao.limite}\nNome do cliente: {cartao.cliente}\n\n")