class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.value == other.value and self.suit == other.suit
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.value, self.suit))
def genres(movies):
    return {genre for movie in movies for genre in movie.genres}

def actors(movies):
    return {actor for movie in movies for actor in movie.actors}
def repeat_consecutive(xs, n):
    return [x for x in xs for _ in range(n)]