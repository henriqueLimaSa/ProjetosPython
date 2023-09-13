from contas import Conta
from clientes import Cliente

cliente1 = Cliente(123, "Joao", "Rua 1")
cliente2 = Cliente(345, "Maria", "Rua 2")
conta1 = Conta([cliente1, cliente2], 1, 0)
#conta1.gerarsaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.gerarsaldo()
