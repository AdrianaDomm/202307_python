class CuentaBancaria:
    cuentas = []
    def __init__(self, tasa_interes=0.05, balance=0):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

        def deposito(self,amount):
            self.balance+= amount
            return self
        
        def retiro(self,amount):
            self.balance-=amount
            return self
        
        def mostrar_info_cuenta(self):
            print("Balance: $", self.balance)
        
        def generar_interes(self):
            if(self.tasa_interes>0):
             self.balance += self.balance * self.tasa_interes
            return self
        
        @classmethod
        def imprimir_instancias(cls):
            for cuenta in cls.cuentas:
                cuenta.mostrar_info_cuenta()

cuenta1 = CuentaBancaria(0.02, 100)
cuenta2 = CuentaBancaria(balance=10)

cuenta1.deposito(800).deposito(150).deposito(100).retiro(150).generar_interes().mostrar_info_cuenta()

cuenta2.deposito(150).deposito(150).retiro(10).retiro(200).retiro(5).retiro(35).generar_interes().mostrar_info_cuenta()

print()
CuentaBancaria.imprimir_instancias()
        