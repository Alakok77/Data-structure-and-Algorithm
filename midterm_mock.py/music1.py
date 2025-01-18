"""music class"""
class Song():
    def __init__(self, name, genre, time):
        self.name = name
        self.genre = genre
        self.durations = (time//60) + (time%60/100)

    def show_info(self):
        """show info"""
        return f"{self.name} <|> {self.genre} <|> {self.durations:.2f}"

Rickroll = Song(input(), input(), int(input()))
print(Rickroll.show_info())
