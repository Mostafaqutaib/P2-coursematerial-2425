
def partition(lst, condition):
    first_list = []
    second_list = []
    for i in lst :
        if condition(i):
            first_list.append(i)
        else:
            second_list.append(i)

    return (first_list, second_list)

def children_and_adults(people):
    return partition(people, lambda p: p.age <18)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice", 12)
bob = Person("Bob", 22)
carol = Person("Carol", 16)

children, adults = children_and_adults([alice, bob, carol])

print([p.name for p in children])  # ['Alice', 'Carol']
print([p.name for p in adults])    # ['Bob']
