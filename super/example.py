class Equus:
    def __init__(self, is_male):
        pass
    def run(self):
        print(f'I run at speed {self.speed}')
        print(f'I\'m {self.gender}')
    
    def roar(self):
        print('Equus roars')

class Horse(Equus):
    def __init__(self, is_male):
        print('Horse init')
        self.speed = 30
        self.gender = 'male' if is_male else 'female'
        self.is_horse = True
    def roar(self):
        print('Horse: Hee haw~')
        super().roar()
        #This line lead to donkey due to C3linearization, probably
        #try to commentize super().roar() here
        print("horse roared!")

class Donkey(Equus):
    def __init__(self, is_female):
        print('Donkey init')
        self.speed = 20
        self.gender = 'female' if is_female else 'male'
        self.is_donkey = True
    def roar(self):
        print('Donkey: Hee haw hee hee haw~')
        super().roar()
        #This line lead to Equus due to C3linearization, probably
        #try to commentize super().roar() here
        print("donkey roared?")

class Mule(Horse, Donkey):
    def __init__(self, is_male):
        print('Mule init')
        super().__init__(is_male)
    
    def roar(self):
        print('Mule: Muuuuleee~~~')
        super().roar()
        print("superagain\n")
        super().roar()
        print("mule roared")

mule = Mule(is_male=True)
print(" ")
mule.roar()