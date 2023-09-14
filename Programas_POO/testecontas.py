from contas import Conta
from clientes import Cliente

cliente1 = Cliente("123", "Joao", "Rua X")
cliente2 = Cliente("456", "Maria", "Rua W")
conta1 = Conta([cliente1, cliente2], 1, 2000)
conta1.depositar(1000)
conta1.sacar(1500)
conta1.extrato.extrato(conta1.numero)
Extrato: 1
