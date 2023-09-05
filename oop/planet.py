from human import Human
from robot import Robot

class Planet:

    def __init__(self, n="Planet"):
        self.name = n
        self.inhabitants = []

    def __str__(self):
        x=[]
        y=[]
        for dude in self.inhabitants:
            if isinstance(dude, Human):
                x.append(dude)
            elif isinstance(dude, Robot):
                y.append(dude)
        return f"{self.name} contains: \nHumans: {x}\nRobots: {y}\n\n"

    def __repr__(self):
        return f"Planet(name={self.name}, inhabitants={self.inhabitants})"

    def add(self, inh):
        self.inhabitants.append(inh)

    def remove(self, inh):
        if inh in self.inhabitants:
            self.inhabitants.remove(inh)


if __name__ == "__main__":
    h1 = Human("Bob", 23)
    h2 = Human("Betty", 28)
    r1 = Robot("Wall-E", 2)
    r2 = Robot("RoboCop", 34)
    mars = Planet("Mars")
    print(mars)
    mars.add_inhabitant(r1)
    mars.add_inhabitant(r2)
    mars.add_inhabitant(h1)
    print(mars)
    mars.add_inhabitant(h2)
    print(mars)
    mars.add_inhabitant(h2)
    print(mars)
    mars.remove_inhabitant(h1)
    mars.remove_inhabitant(r2)
    print(repr(mars))