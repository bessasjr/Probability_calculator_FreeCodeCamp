import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **colors):
        self.cores = colors
        self.cor = []
        self.valor = []
        self.count = 0
        self.contents = ''
        self.cont = []

        for chave in self.cores.keys():
            self.cor.append(f'{chave}')
            self.valor.append(f'{self.cores[chave]}')

        for n in range(len(self.cor)):
            c = f'{self.cor[n]} ' * int(self.valor[n])
            self.cont.append(c.split())
            self.count += int(self.valor[n])

        for p in range(len(self.cont)):
            for y in range(len(self.cont[p])):
                self.contents += self.cont[p][y] + ','
        self.contents = self.contents[:-1].split(',')

    def draw(self, balls_drawn):
        self.cor_order = sorted(self.cor)
        self.conteudo = sorted(self.contents)
        self.lista = []
        self.sorteados = []

        if len(self.conteudo) >= balls_drawn:
            self.sorteio = random.choices(self.conteudo, k=balls_drawn)
            self.sorteados += sorted(self.sorteio)
            self.lista.append(sorted(self.sorteio))
            for i in self.conteudo:
                self.conteudo.remove(i)
        if len(self.conteudo) < balls_drawn:
            self.conteudo += self.sorteados
            self.conteudo = sorted(self.conteudo)
                    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    dicionario = {}

    count = 0
    count1 = 0
    contagem = 0
    prob = 0

    for p in expected_balls:
        #print(p)
        if p == '':
            expected_balls[p] = 1
        print(expected_balls.values())

    while contagem < num_experiments:
        drawn = hat.draw(num_balls_drawn)
        for n in hat.lista:
            for s in hat.cor_order:
                count = n.count(s)
                if s in expected_balls:
                    dicionario[s] = count
                    if dicionario[s] == 0:
                        dicionario.pop(s)

            count1 += 1

            #print(f'{count1:4}: {n} / {dicionario}')

            if expected_balls == dicionario:
                prob += 1

        contagem += 1

    #print(prob)

    probability = prob / num_experiments

    return probability


hat = Hat(red=5, blue=2)
probability = experiment(hat=hat, expected_balls={"blue", "red"}, num_balls_drawn=2, num_experiments=10)
#print("Probability:", probability)