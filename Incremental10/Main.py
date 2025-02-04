from Cliente import Cliente
from Cartao import Cartao
from Transacao import Transacao

client1 = Cliente('Cliente 1', '123456789', False)

client1.criar_cartao(123456789, 0.1, False, False)
client1.retornar_dados(123456789)
client1.comprar(123456789, 100)

client1.relatorio_fatura(123456789)
