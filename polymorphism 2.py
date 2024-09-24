class Colour:
    def code(self,crayon):
        crayon.draw()

class PinkCrayon:
    def draw(self):
        print("I am drawing with pink crayon")

class RedCrayon:
    def draw(self):
        print("I am drawing with red crayon")

crayon1 = Colour()
crayon = PinkCrayon()

crayon1.code(crayon)

crayon1.code(PinkCrayon())

crayon2 = Colour()
crayon2.code(RedCrayon())