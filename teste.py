import random

class Hat:
    def __init__(self):
        self.contents = ['blue', 'blue', 'blue', 'blue', 'red', 'red', 'green', 'green', 'green', 'green', 'green', 'green']
        self.cor = ['blue', 'green', 'red',]

    # metodo draw
    def draw(self):
        self.conteudo = sorted(self.contents)
        lista = []
        self.drawn = 4
        self.sorteados = []
        testes = 1000
        dicionario = {}

        while len(lista) < testes:
            count = 0
            if len(self.conteudo) >= self.drawn:
                self.sorteio = random.choices(self.conteudo, k=self.drawn)
                self.sorteados += sorted(self.sorteio)
                lista.append(sorted(self.sorteio))
                #print(self.sorteio)

                for i in self.conteudo:
                    self.conteudo.remove(i)
                    if len(self.conteudo) < self.drawn:
                        self.conteudo += self.sorteados
                        self.conteudo = sorted(self.conteudo)


        expected_balls={'blue': 2,'red': 1}    
        barra = '/'
        cont1 = 0
        cont2 = 0
        for n in lista:
            for s in sorted(self.cor):
                count = n.count(s)
                dicionario[s] = count
                if dicionario[s] == 0:
                    dicionario.pop(s)

                if len(dicionario.keys()) > len(expected_balls.keys()):

                    if s not in expected_balls:
                        dicionario.pop(s)               

            cont1 += 1


            print(f'{cont1:4}: {n} / {dicionario}')


            if expected_balls == dicionario:
                cont2 += 1
                #print(f'{cont1:4}: {n} / {dicionario}')
                
        print(f'{cont2} / {testes}')
        print(cont2/testes)


# ATÉ AQUI TÁ OK, A LISTA FUNCIONOU DIREITINHO
        
#            cont = 0
#            for d in lista:
#    
#                for s in sorted(self.cor):
#                    count = d.count(s)
#                    if count != 0:
#                        dicionario[s] = count
#                        cont +=1
#                print(cont, dicionario)
                #if len(testando_dicio) < testes:
                #    testando_dicio.append(dicionario)
                        



#            expected_balls={'blue': 2,'red': 1}
#            count_1 = 0
#            if dicionario == expected_balls:
                #print(dicionario)
#                count_1 + 1
        #print(count)

        #print(dicionario)
        #print(lista)
        #print()
        #print(dicionario)
        #print(testando_dicio)


        



hat = Hat()

#print(hat.draw())
hat.draw()

#print(len(hat.contents))