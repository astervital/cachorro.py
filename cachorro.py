class Cachorro:
    def __init__(self, nome, idade, raca, comida):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.comida = comida
        self.acordado = False
        self.feliz = False
        self.energia = 100




    def comer(self):
        if self.acordado:
            self.comida -= 1
            print(f"{self.nome} comeu")
        else:
            print(f"{self.nome} está dormindo e não pode comer")


    def latir(self):
        print(f"{self.nome} está latindo: AU AU!!")
    

    def brincar(self):
        if self.acordado:
            if self.energia >=20:
                self.energia -= 20
                self.feliz = True
                print(f"{self.nome} está brincando e está feliz")
            else:
                print(f"{self.nome} está cansado e não consegue brincar")
        else:
            print(f"{self.nome} está dormindo e não pode brincar")
        

    def acordar(self):
        self.acordado = True
        print(f"{self.nome} está acordado")
    

    def dormir(self):
        self.energia = 100
        self.acordado = False
        print(f"{self.nome} está dormindo tranquilo(a)")


    

