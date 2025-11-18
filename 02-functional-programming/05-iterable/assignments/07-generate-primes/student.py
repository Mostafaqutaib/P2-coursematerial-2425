def is_prime(n):
    if n < 2:        # ❌ الأقل من 2 ليس أولي
        return False
    if n == 2:       # ✅ 2 أولي
        return True  
    if n % 2 == 0:   # ❌ الأعداد الزوجية (عدا 2) ليست أولية
        return False
    
    # 🔍 نتحقق من القسمة على 3, 5, 7, ... حتى الجذر التربيعي
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True      # ✅ لم نجد قواسم، العدد أولي

def primes():
    yield 2          # ⏸️ نرجع 2 أولاً
    n = 3            # 🔢 نبدأ من 3
    while True:      # ♾️ حلقة لا نهائية
        if is_prime(n):  # ✅ إذا كان أولي
            yield n      # ⏸️ نرجع العدد
        n += 2           # ⏭️ ننتقل للعدد الفردي التالي