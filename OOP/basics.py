class animal:
    def __init__(self,name=None,habitat=None):
        self.name = name
        self.habitat = habitat

    def printAnimal(self):
        print(self.name)

def main():
    bear = animal("bear","land")
    fish = animal("fish","ocean" )
    bird = animal("bird", "air")
    bear.printAnimal()


if __name__ == '__main__':
    main()
