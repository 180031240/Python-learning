class Sound:
    def noise(self,song):
        song.language()

class PopMusic:
    def language(self):
        print("I am sining a pop song")
class Veena:
    def language(self):
        print("I am playing veena")

song = Sound()
classical = Veena()

song.noise(classical)