from compra_service import cadastrar


class CompraView:

    def cadastrarCompra(self):        
        numero_cartao = input("Digite o Número do Cartão: ")

        while not numero_cartao or not numero_cartao.isdigit() or len(numero_cartao) != 16:
            numero_cartao = input("Digite o Número do Cartão: ")

        valor_compra = float(input("Digite o valor da compra: "))

        print("Digite 1 - Para saúde\n2- Para alimentação\n3- para educação\n4- para lazer\n")
        categoria = int(input())

        while categoria not in (1, 2, 3, 4):
            print("Opção inválida. Digite novamente: ")
            categoria = int(input())
        estabelecimento = input("Digite o estabelecimento da compra: ")

        cadastrar(numero_cartao, valor_compra, categoria, estabelecimento)
        print("Compra cadastrada com sucesso! (Últimos 4 dígitos do cartão: {})".format(numero_cartao[-4:]))

if __name__ == "__main__":
    compra = CompraView()
    compra.cadastrarCompra()