def first_letter(word):
    return word[0]
def word_length(word):
    return len(word)
def age(person):
    return person.age

def group_by(xs, key_function):
    resultaat = {}
    for i in xs:
        key = key_function(i)
        if key not in resultaat:
            resultaat[key] = []
        resultaat[key].append(i)
    return resultaat
words = ["apple", "pear", "peach", "plum", "banana"]
print(group_by(words, first_letter))
print(group_by(words, word_length))
group_by([
    Person(name='John', age=14),
    Person(name='Marc', age=17),
    Person(name='Sophie', age=15),
    Person(name='Chris', age=17),
    Person(name='Morgan', age=15),
], age)