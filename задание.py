from abc import ABC
from abc import abstractmethod
class Bib(ABC): 
    @abstractmethod
    def entrance(self):
        pass
    @abstractmethod
    def search(self):
        pass
    @abstractmethod
    def exit(self):
        pass
class Biblioteka1(Bib): 
    def entrance(self):
        print('Зашли в библиотеку Ломоносова')
    def search(self):
        print('Выбираем книгу')
    def exit(self):
        print('Выходим из библиотеке')
class Biblioteka2(Bib): 
    def entrance(self):
        print('Приехали в библиотеку на Гагарина')
    def search(self):
        print('Выбираем книгу')
    def exit(self):
        print('Выходим из библиотеке')
class Human:
    def actions(self, hum):
        hum.entrance()
        hum.search()
        hum.exit()

bib1 = Biblioteka1()
bib2 = Biblioteka2()
h = Human()
h.actions(bib1)

