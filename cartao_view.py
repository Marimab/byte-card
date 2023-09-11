from cartao_service import CartaoService


class CartaoView:



    def cadastrarCartao(self):
        numero = input("Digite o Número do Cartão: ")

        while not numero or not numero.isdigit() or len(numero) != 16:
            numero = input("Digite o Número do Cartão: ")

        validade = input("Digite a Validade do Cartão: ")
        cvv = input("Digite o CVV do Cartão: ")

        limite = float(input("Digite o Limite do Cartão: "))

        while limite < 0.0:
            limite = float(input("Digite o Limite do Cartão (valor positivo): "))

        cliente = input("Digite o Nome do Cliente: ")

        cartao_service = CartaoService()
        try:
            cartao_service.cadastrar(numero, validade, cvv, limite, cliente)
            print(f"Cartão {cliente} cadastrado com sucesso - Número: {numero[-4:]}")
        except ValueError as error:
            print(f"Erro ao cadastrar cartão: {error}")


if __name__ == "__main__":
    cartao_view = CartaoView()
    cartao_view.cadastrarCartao()


