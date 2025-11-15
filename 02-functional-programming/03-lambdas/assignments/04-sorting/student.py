def sort_by_age(people):
    new_lijst = sorted(people, key=lambda p: p.age)
    return new_lijst

def sort_by_decreasing_age(people):
    new_lijst = sorted(people, key=lambda p: p.age, reverse=True)
    return new_lijst

def sort_by_name(people):
    new_lijst = sorted(people, key=lambda p: p.name)
    return new_lijst

def sort_by_name_then_age(people):
    new_lijst = sorted(people, key=lambda p: (p.name, p.age))
    return new_lijst

def sort_by_name_then_decreasing_age(people):
    new_lijst = sorted(people, key=lambda p: (p.name, -p.age))
    return new_lijst