def directors(movies):
    return {m.director for m in movies}
def common_elements(xs, ys):
    return {x for x in xs if x in ys}