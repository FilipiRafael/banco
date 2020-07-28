from clientes import Cliente
from contas import Conta
from bancos import Banco

joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria Silva", "555-4434")
josé = Cliente("José Vargas", "9721-3040")

contaJ = Conta([josé], 10)
contaJM = Conta([maria, joão], 100)

tatu = Banco("Tatú")
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
tatu.lista_contas()

