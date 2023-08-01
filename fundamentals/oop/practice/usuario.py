class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

def hacer_deposito(self,amount):
    self.balance_cuenta+=amount

def hacer_retiro(self,amount):
    self.balance_cuenta-=amount

def mostrar_balance_usuario(self):
    print(self.name+", Balance:"+str(self.balance_cuenta))

def transferir_dinero(self,other_user, amount):
    self.balance_cuenta-=amount
    other_user.balance_cuenta+=amount

    pinky = Usuario("Pinky","pinkyraw@gmail.com")
    darky = Usuario("Darky","darkywao@gmail.com")
    stormy = Usuario("Stormy","tolmywao@gmail.com")

    pinky.hacer_deposito(5000)
    pinky.hacer_deposito(2000)
    pinky.hacer_deposito(5000)
    pinky.hacer_retiro(1500)
    pinky.mostrar_balance_usuario()

    darky.hacer_deposito(5000)
    darky.hacer_deposito(2000)
    darky.hacer_retiro(3500)
    darky.hacer_retiro(2200)
    darky.mostrar_balance_usuario()

    stormy.hacer_deposito(12000)
    stormy.hacer_retiro(2500)
    stormy.hacer_retiro(2000)
    stormy.hacer_retiro(2500)
    stormy.mostrar_balance_usuario()

    pinky.transferir_dinero(stormy, 2500)
    pinky.mostrar_balance_usuario()
    stormy.mostrar_balance_usuario()
