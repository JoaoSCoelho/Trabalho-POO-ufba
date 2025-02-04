from Transacao import Transacao
import datetime


class Cartao:
    def __init__(self,
                 numero: int,
                 titular: str,
                 taxa_de_cashback: float = 0,
                 eh_especial: bool = False,
                 eh_corporativo: bool = False,
                 limite: float = 0,
                 ):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = 0
        if (eh_especial):
            self.__limite = limite
        else:
            self.__limite = 1440
        if (eh_especial):
            self.__taxa_de_cashback = taxa_de_cashback
        else:
            self.__taxa_de_cashback = 0
        self.__eh_especial = eh_especial
        self.__eh_corporativo = eh_corporativo
        self.__transacao_atual = None
        self.__historico_transacoes: list[Transacao] = []

    def comprar(self, valor: float):
        if (self.limite - self.saldo < valor):
            print('Limite excedido!')
            return False
        if (self.transacao_atual is not None):
            print('Existe uma transação em andamento!')
            return False

        if (self.eh_especial):
            print('Compra feita com cashback')
            valor = valor * (1 - self.taxa_de_cashback)

        transacao = Transacao(valor, 'Compra', 'compra', datetime.date.today())

        self.saldo += valor
        self.transacao_atual = transacao
        return True

    def concluir_transacao(self):
        self.historico_transacoes.append(self.transacao_atual)
        self.transacao_atual = None

    def adicionar_transacao(self, valor, descricao, tipo):
        transacao = Transacao(valor, descricao, tipo, datetime.date.today())
        self.historico_transacoes.append(transacao)

    def consultar_historico(self):
        historico = ''
        for transacao in self.historico_transacoes:
            historico += f'{transacao}\n'
        return historico

    def consultar_por_tipo(self, tipo):
        for transacao in self.historico_transacoes:
            if (transacao.tipo == tipo):
                return transacao
        return None

    def consultar_por_data(self, data):
        for transacao in self.historico_transacoes:
            if (transacao.data == data):
                return transacao
        return None

    def __str__(self):
        print(
            f'Numero: {self.numero}\nLimite: {self.limite}\nSaldo: {self.saldo}')
        if (self.eh_especial):
            print(f'É especial! Taxa de cashback: {self.taxa_de_cashback}')
        elif (self.eh_corporativo):
            print('É corporativo!')
        else:
            print('É comum!')

    @property
    def titular(self):
        return self.__titular

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def taxa_de_cashback(self):
        return self.__taxa_de_cashback

    @property
    def eh_especial(self):
        return self.__eh_especial

    @property
    def eh_corporativo(self):
        return self.__eh_corporativo

    @property
    def transacao_atual(self):
        return self.__transacao_atual

    @property
    def historico_transacoes(self):
        return self.__historico_transacoes

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @taxa_de_cashback.setter
    def taxa_de_cashback(self, taxa_de_cashback):
        self.__taxa_de_cashback = taxa_de_cashback

    @eh_especial.setter
    def eh_especial(self, eh_especial):
        self.__eh_especial = eh_especial

    @eh_corporativo.setter
    def eh_corporativo(self, eh_corporativo):
        self.__eh_corporativo = eh_corporativo

    @transacao_atual.setter
    def transacao_atual(self, transacao_atual):
        self.__transacao_atual = transacao_atual

    @historico_transacoes.setter
    def historico_transacoes(self, historico_transacoes):
        self.__historico_transacoes = historico_transacoes


if (__name__ == '__main__'):
    cartao = Cartao(1234, 0.1, True, False, 5000)
    cartao.comprar(100)
    cartao.concluir_transacao()
    cartao.comprar(100)
    cartao.concluir_transacao()
    cartao.comprar(100)
    print(cartao.consultar_historico())
