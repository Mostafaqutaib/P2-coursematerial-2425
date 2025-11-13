def count(collection, condition):
    count = 0
    for i in collection:
        if condition(i):
            count += 1
    return count


def indices_of(collection, condition):
    result = []
    for index, element in enumerate(collection):
        if condition(element):
            result.append(index)
    return result


def count_older_than(people, min_age):
    def older_than(person):
        return person.age > min_age
    return count(people, older_than)


def indices_of_cards_with_suit(cards, suit):
    def has_suit(card):
        return card.suit == suit
    return indices_of(cards, has_suit)

