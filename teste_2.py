import random

class Hat:
    contents = []

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            for i in range(value):
                Hat.contents.append(key)
                
        
    def draw(self,number):
        self.number = number
        #print(self.number)
        removed_balls = []
        if self.number < len(Hat.contents):
            while self.number > 0:
                random_number = random.randrange(len(Hat.contents))
                removed_balls.append(Hat.contents[random_number])
                self.number -= 1
            return removed_balls

        else:
            return 0
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
#    pass
    result = hat.draw(num_balls_drawn)
    successful = 0
    good = []
    total = num_experiments
    count = len(hat.contents)
    for key, value in expected_balls.items():
        for i in range(value):
            good.append(key)
    while num_experiments > 0:
        count = len(hat.contents)
        while count > 0:
            result = hat.draw(num_balls_drawn)
            if result == good:
                successful += 1
                count = 0
                num_experiments -= 1
            else:
                count = 0
                num_experiments -= 1
                print(result)
                #print(expected_balls)
    if successful > 0:
        resultado = (successful / total * 100)
        resultado = round(resultado, 2)
    else:
        resultado = 0
    print(successful, "/", total)
    print(str(resultado) + "%")
   

hat = Hat(blue=3,red=2,green=6)
#print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))

probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)