import datetime


class Transacao:
    def __init__(self, valor: float, descricao: str, tipo: str, data: datetime.date):
        self.__valor = valor
        self.__descricao = descricao
        self.__tipo = tipo
        self.__data = data

    def __str__(self):
        return f'Valor: {self.valor}, Descricao: {self.descricao}, Tipo: {self.tipo}, Data: {self.data}'

    @property
    def valor(self):
        return self.__valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def tipo(self):
        return self.__tipo

    @property
    def data(self):
        return self.__data

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @data.setter
    def data(self, data):
        self.__data = data
