import copy
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
        #self.content = self.content.split(',')


    def draw(self, balls_drawn):
        self.cor_order = sorted(self.cor)
        self.lista = []

        if balls_drawn >= len(self.contents):
            self.lista = self.contents.copy()
            self.contents.clear()
            return self.lista

        for n in range(balls_drawn):
            h = len(self.contents) - 1
            p = random.randint(0, h)
            self.lista.append(self.contents[p])
            self.contents.pop(p)
        return self.lista


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    dicionario = {}
    count = 0
    count1 = 0
    prob = 0

    for h in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        
        for p in expected_balls:
            if expected_balls[p] > drawn.count(p):
                prob -= 1
                break
        prob += 1

    probability = prob / num_experiments

    return probability
