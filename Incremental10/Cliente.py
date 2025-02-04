from Cartao import Cartao
from time import sleep


class Cliente:
    def __init__(self, nome: str, identificao: str, empresa: bool):
        self.__nome = nome
        self.__cartoes = []
        if (empresa):
            self.__cnpj = identificao
        else:
            self.__cpf = identificao

    def criar_cartao(self, numero: int, taxa_de_cashback: float, eh_especial: bool, eh_corporativo: bool, limite: float = 0, cartao: Cartao = None):
        if (cartao is not None):
            self.cartoes.append(cartao)
            return
        self.cartoes.append(
            Cartao(numero, taxa_de_cashback, eh_especial, eh_corporativo, limite))

    def retornar_dados(self, numero_cartao):
        for cartao in self.cartoes:
            if (cartao.numero == numero_cartao):
                print(f'Saldo: {cartao.saldo}')
                print(f'Limite: {cartao.limite}')

    def relatorio_fatura(self, numero_cartao):
        for cartao in self.cartoes:
            if (cartao.numero == numero_cartao):
                print(cartao.consultar_historico())

    def comprar(self, numero_cartao, valor: float):
        for cartao in self.cartoes:
            if (cartao.numero == numero_cartao):
                compra_feita = cartao.comprar(valor)
                if (compra_feita):
                    sleep(0.5)
                    cartao.concluir_transacao()
                return compra_feita

    @property
    def cartoes(self):
        return self.__cartoes

    @property
    def nome(self):
        return self.__nome

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def cpf(self):
        return self.__cpf

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cartoes.setter
    def cartoes(self, cartoes):
        self.__cartoes = cartoes

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj


if __name__ == '__main__':
    cliente = Cliente('Cliente 1', '123456789', False)
    cliente.criar_cartao(123456789, 0.1, False, False)
    cliente.retornar_dados(123456789)
    cliente.comprar(123456789, 100)

    cliente.relatorio_fatura(123456789)
