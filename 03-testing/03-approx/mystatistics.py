def average(ns):
    if not ns:  # التعامل مع القائمة الفارغة
        return 0
    return sum(ns) / len(ns)