from .Cartao import Cartao


class Cliente:
    def __init__(self, nome: str, id: str, empresa: bool):
        self.nome = nome
        self.id = id
        self.empresa = empresa
        self.cartoes = []
