from itertools import pairwise

def total_distance(path, distance):
    total = 0  # 🔢 نبدأ من الصفر
    
    # 🔄 pairwise ينشئ أزواج: (0,5), (5,3), (3,4)
    for city1, city2 in pairwise(path):
        # ➕ نجمع المسافة بين كل مدينتين متتاليتين
        total += distance(city1, city2)
    
    return total  # 📊 نرجع المجموع