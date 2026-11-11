from abc import ABC , abstractmethod
class Animal(ABC):
    def move(self):
        pass
class human(Animal):
        def move(self):
            print("I can walk on two.legs")
class snake(Animal):
        def move(self):
            print("I can crawl")
class dog(Animal):
        def move(self):
             print("I can bark")
class Lion(Animal):
      def move(self):
          print("I can roar")
R = human()
R.move()

K = snake()
K.move()

X = dog()
X.move()

L = Lion()
L.move()

