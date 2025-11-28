# استخدام itertools لحل التمارين

سأستخدم دوال module `itertools` لحل التمارين المطلوبة:

## 1. استخدام `pairwise` - أول تمرين

```python
from itertools import pairwise

def example_pairwise():
    return list(pairwise(range(5)))

print(example_pairwise())  # [(0, 1), (1, 2), (2, 3), (3, 4)]
```

## الآن دعني أقدم أهم دوال itertools مع أمثلة:

### **1. `count()` - عداد لا نهائي**
```python
from itertools import count

def infinite_counter():
    counter = count(start=1, step=2)  # 1, 3, 5, 7, ...
    return list(next(counter) for _ in range(5))

print("count:", infinite_counter())  # [1, 3, 5, 7, 9]
```

### **2. `cycle()` - تكرار لا نهائي**
```python
from itertools import cycle

def infinite_cycle():
    cycler = cycle('ABC')
    return list(next(cycler) for _ in range(6))

print("cycle:", infinite_cycle())  # ['A', 'B', 'C', 'A', 'B', 'C']
```

### **3. `repeat()` - تكرار قيمة**
```python
from itertools import repeat

def repeat_value():
    repeater = repeat(5, times=4)  # repeat 5 four times
    return list(repeater)

print("repeat:", repeat_value())  # [5, 5, 5, 5]
```

### **4. `chain()` - ربط iterables**
```python
from itertools import chain

def chain_example():
    result = chain('ABC', 'DEF', [1, 2, 3])
    return list(result)

print("chain:", chain_example())  # ['A', 'B', 'C', 'D', 'E', 'F', 1, 2, 3]
```

### **5. `compress()` - تصفية بقالب**
```python
from itertools import compress

def compress_example():
    data = 'ABCDEF'
    selectors = [1, 0, 1, 0, 1, 1]  # 1 = نأخذ, 0 = نتجاهل
    return list(compress(data, selectors))

print("compress:", compress_example())  # ['A', 'C', 'E', 'F']
```

### **6. `dropwhile()` و `takewhile()`**
```python
from itertools import dropwhile, takewhile

def drop_take_example():
    numbers = [1, 4, 6, 4, 1]
    
    # نتجاهل حتى يصبح الشرط False
    dropped = list(dropwhile(lambda x: x < 5, numbers))
    
    # نأخذ حتى يصبح الشرط False  
    taken = list(takewhile(lambda x: x < 5, numbers))
    
    return dropped, taken

print("dropwhile/takewhile:", drop_take_example())  
# ([6, 4, 1], [1, 4])
```

### **7. `groupby()` - تجميع حسب مفتاح**
```python
from itertools import groupby

def groupby_example():
    data = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
    # نجمع حسب طول الكلمة
    grouped = {key: list(group) for key, group in groupby(data, key=len)}
    return grouped

print("groupby:", groupby_example())
# {5: ['apple'], 6: ['banana', 'cherry'], 4: ['date'], 10: ['elderberry']}
```

### **8. `permutations()` و `combinations()`**
```python
from itertools import permutations, combinations

def permutations_combinations():
    data = [1, 2, 3]
    
    # جميع التباديل (الترتيب مهم)
    perms = list(permutations(data, 2))
    
    # جميع التوافيق (الترتيب غير مهم)
    combs = list(combinations(data, 2))
    
    return perms, combs

perms, combs = permutations_combinations()
print("permutations:", perms)  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print("combinations:", combs)  # [(1, 2), (1, 3), (2, 3)]
```

### **9. `product()` - جداء ديكارتي**
```python
from itertools import product

def product_example():
    # جداء ديكارتي بين قائمتين
    result = product('AB', [1, 2])
    return list(result)

print("product:", product_example())  # [('A', 1), ('A', 2), ('B', 1), ('B', 2)]
```

### **10. `islice()` - تقطيع iterator**
```python
from itertools import islice

def islice_example():
    numbers = count()  # iterator لا نهائي
    return list(islice(numbers, 5, 10))  # من الفهرس 5 إلى 10

print("islice:", islice_example())  # [5, 6, 7, 8, 9]
```

## أمثلة عملية باستخدام itertools:

### **مثال 1: معالجة بيانات طلاب**
```python
from itertools import groupby

students = [
    {'name': 'Ahmed', 'grade': 'A'},
    {'name': 'Mohamed', 'grade': 'B'},
    {'name': 'Fatima', 'grade': 'A'},
    {'name': 'Sara', 'grade': 'C'},
    {'name': 'Ali', 'grade': 'B'}
]

# تجميع الطلاب حسب الدرجة
students.sort(key=lambda x: x['grade'])
grouped = {grade: list(group) for grade, group in groupby(students, key=lambda x: x['grade'])}

print("مجموعات الطلاب:")
for grade, group in grouped.items():
    names = [s['name'] for s in group]
    print(f"الدرجة {grade}: {', '.join(names)}")
```

### **مثال 2: توليد جميع الاحتمالات**
```python
from itertools import product

def generate_passwords(chars, length):
    """توليد جميع كلمات المرور الممكنة"""
    return [''.join(combo) for combo in product(chars, repeat=length)]

passwords = generate_passwords('ABC', 2)
print("كلمات المرور:", passwords)  # ['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']
```

### **مثال 3: تحليل تسلسل**
```python
from itertools import pairwise, takewhile

def analyze_sequence(sequence):
    """تحليل تسلسل الأرقام"""
    # الفروق بين العناصر المتتالية
    differences = [b - a for a, b in pairwise(sequence)]
    
    # نأخذ الأرقام حتى يصبح الفرق سالب
    increasing = list(takewhile(lambda x: x >= 0, differences))
    
    return differences, increasing

seq = [1, 3, 5, 4, 2, 6]
diffs, inc = analyze_sequence(seq)
print("الفروق:", diffs)        # [2, 2, -1, -2, 4]
print("التزايد المستمر:", inc) # [2, 2]
```

## الخلاصة:

- **`itertools`** ⇢ مكتبة قوية للتعامل مع iterators
- **الكفاءة** ⇢ تعمل مع البيانات الكبيرة بدون تخزينها كلها
- **المرونة** ⇢ دوال للجمع، التصفية، التكرار، والتوليد
- **الاستخدام** ⇢ مثالية لمعالجة البيانات، توليد الاحتمالات، والتحليل

الآن يمكنك استخدام `itertools` لحل التمارين المعقدة بكفاءة! 🚀622995term
# استخدام itertools لحل التمارين

سأستخدم دوال module `itertools` لحل التمارين المطلوبة:

## 1. استخدام `pairwise` - أول تمرين

```python
from itertools import pairwise

def example_pairwise():
    return list(pairwise(range(5)))

print(example_pairwise())  # [(0, 1), (1, 2), (2, 3), (3, 4)]
```

## الآن دعني أقدم أهم دوال itertools مع أمثلة:

### **1. `count()` - عداد لا نهائي**
```python
from itertools import count

def infinite_counter():
    counter = count(start=1, step=2)  # 1, 3, 5, 7, ...
    return list(next(counter) for _ in range(5))

print("count:", infinite_counter())  # [1, 3, 5, 7, 9]
```

### **2. `cycle()` - تكرار لا نهائي**
```python
from itertools import cycle

def infinite_cycle():
    cycler = cycle('ABC')
    return list(next(cycler) for _ in range(6))

print("cycle:", infinite_cycle())  # ['A', 'B', 'C', 'A', 'B', 'C']
```

### **3. `repeat()` - تكرار قيمة**
```python
from itertools import repeat

def repeat_value():
    repeater = repeat(5, times=4)  # repeat 5 four times
    return list(repeater)

print("repeat:", repeat_value())  # [5, 5, 5, 5]
```

### **4. `chain()` - ربط iterables**
```python
from itertools import chain

def chain_example():
    result = chain('ABC', 'DEF', [1, 2, 3])
    return list(result)

print("chain:", chain_example())  # ['A', 'B', 'C', 'D', 'E', 'F', 1, 2, 3]
```

### **5. `compress()` - تصفية بقالب**
```python
from itertools import compress

def compress_example():
    data = 'ABCDEF'
    selectors = [1, 0, 1, 0, 1, 1]  # 1 = نأخذ, 0 = نتجاهل
    return list(compress(data, selectors))

print("compress:", compress_example())  # ['A', 'C', 'E', 'F']
```

### **6. `dropwhile()` و `takewhile()`**
```python
from itertools import dropwhile, takewhile

def drop_take_example():
    numbers = [1, 4, 6, 4, 1]
    
    # نتجاهل حتى يصبح الشرط False
    dropped = list(dropwhile(lambda x: x < 5, numbers))
    
    # نأخذ حتى يصبح الشرط False  
    taken = list(takewhile(lambda x: x < 5, numbers))
    
    return dropped, taken

print("dropwhile/takewhile:", drop_take_example())  
# ([6, 4, 1], [1, 4])
```

### **7. `groupby()` - تجميع حسب مفتاح**
```python
from itertools import groupby

def groupby_example():
    data = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
    # نجمع حسب طول الكلمة
    grouped = {key: list(group) for key, group in groupby(data, key=len)}
    return grouped

print("groupby:", groupby_example())
# {5: ['apple'], 6: ['banana', 'cherry'], 4: ['date'], 10: ['elderberry']}
```

### **8. `permutations()` و `combinations()`**
```python
from itertools import permutations, combinations

def permutations_combinations():
    data = [1, 2, 3]
    
    # جميع التباديل (الترتيب مهم)
    perms = list(permutations(data, 2))
    
    # جميع التوافيق (الترتيب غير مهم)
    combs = list(combinations(data, 2))
    
    return perms, combs

perms, combs = permutations_combinations()
print("permutations:", perms)  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print("combinations:", combs)  # [(1, 2), (1, 3), (2, 3)]
```

### **9. `product()` - جداء ديكارتي**
```python
from itertools import product

def product_example():
    # جداء ديكارتي بين قائمتين
    result = product('AB', [1, 2])
    return list(result)

print("product:", product_example())  # [('A', 1), ('A', 2), ('B', 1), ('B', 2)]
```

### **10. `islice()` - تقطيع iterator**
```python
from itertools import islice

def islice_example():
    numbers = count()  # iterator لا نهائي
    return list(islice(numbers, 5, 10))  # من الفهرس 5 إلى 10

print("islice:", islice_example())  # [5, 6, 7, 8, 9]
```

## أمثلة عملية باستخدام itertools:

### **مثال 1: معالجة بيانات طلاب**
```python
from itertools import groupby

students = [
    {'name': 'Ahmed', 'grade': 'A'},
    {'name': 'Mohamed', 'grade': 'B'},
    {'name': 'Fatima', 'grade': 'A'},
    {'name': 'Sara', 'grade': 'C'},
    {'name': 'Ali', 'grade': 'B'}
]

# تجميع الطلاب حسب الدرجة
students.sort(key=lambda x: x['grade'])
grouped = {grade: list(group) for grade, group in groupby(students, key=lambda x: x['grade'])}

print("مجموعات الطلاب:")
for grade, group in grouped.items():
    names = [s['name'] for s in group]
    print(f"الدرجة {grade}: {', '.join(names)}")
```

### **مثال 2: توليد جميع الاحتمالات**
```python
from itertools import product

def generate_passwords(chars, length):
    """توليد جميع كلمات المرور الممكنة"""
    return [''.join(combo) for combo in product(chars, repeat=length)]

passwords = generate_passwords('ABC', 2)
print("كلمات المرور:", passwords)  # ['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']
```

### **مثال 3: تحليل تسلسل**
```python
from itertools import pairwise, takewhile

def analyze_sequence(sequence):
    """تحليل تسلسل الأرقام"""
    # الفروق بين العناصر المتتالية
    differences = [b - a for a, b in pairwise(sequence)]
    
    # نأخذ الأرقام حتى يصبح الفرق سالب
    increasing = list(takewhile(lambda x: x >= 0, differences))
    
    return differences, increasing

seq = [1, 3, 5, 4, 2, 6]
diffs, inc = analyze_sequence(seq)
print("الفروق:", diffs)        # [2, 2, -1, -2, 4]
print("التزايد المستمر:", inc) # [2, 2]
```

## الخلاصة:

- **`itertools`** ⇢ مكتبة قوية للتعامل مع iterators
- **الكفاءة** ⇢ تعمل مع البيانات الكبيرة بدون تخزينها كلها
- **المرونة** ⇢ دوال للجمع، التصفية، التكرار، والتوليد
- **الاستخدام** ⇢ مثالية لمعالجة البيانات، توليد الاحتمالات، والتحليل

الآن يمكنك استخدام `itertools` لحل التمارين المعقدة بكفاءة! 🚀
# استخدام itertools لحل التمارين

سأستخدم دوال module `itertools` لحل التمارين المطلوبة:

## 1. استخدام `pairwise` - أول تمرين

```python
from itertools import pairwise

def example_pairwise():
    return list(pairwise(range(5)))

print(example_pairwise())  # [(0, 1), (1, 2), (2, 3), (3, 4)]
```

## الآن دعني أقدم أهم دوال itertools مع أمثلة:

### **1. `count()` - عداد لا نهائي**
```python
from itertools import count

def infinite_counter():
    counter = count(start=1, step=2)  # 1, 3, 5, 7, ...
    return list(next(counter) for _ in range(5))

print("count:", infinite_counter())  # [1, 3, 5, 7, 9]
```

### **2. `cycle()` - تكرار لا نهائي**
```python
from itertools import cycle

def infinite_cycle():
    cycler = cycle('ABC')
    return list(next(cycler) for _ in range(6))

print("cycle:", infinite_cycle())  # ['A', 'B', 'C', 'A', 'B', 'C']
```

### **3. `repeat()` - تكرار قيمة**
```python
from itertools import repeat

def repeat_value():
    repeater = repeat(5, times=4)  # repeat 5 four times
    return list(repeater)

print("repeat:", repeat_value())  # [5, 5, 5, 5]
```

### **4. `chain()` - ربط iterables**
```python
from itertools import chain

def chain_example():
    result = chain('ABC', 'DEF', [1, 2, 3])
    return list(result)

print("chain:", chain_example())  # ['A', 'B', 'C', 'D', 'E', 'F', 1, 2, 3]
```

### **5. `compress()` - تصفية بقالب**
```python
from itertools import compress

def compress_example():
    data = 'ABCDEF'
    selectors = [1, 0, 1, 0, 1, 1]  # 1 = نأخذ, 0 = نتجاهل
    return list(compress(data, selectors))

print("compress:", compress_example())  # ['A', 'C', 'E', 'F']
```

### **6. `dropwhile()` و `takewhile()`**
```python
from itertools import dropwhile, takewhile

def drop_take_example():
    numbers = [1, 4, 6, 4, 1]
    
    # نتجاهل حتى يصبح الشرط False
    dropped = list(dropwhile(lambda x: x < 5, numbers))
    
    # نأخذ حتى يصبح الشرط False  
    taken = list(takewhile(lambda x: x < 5, numbers))
    
    return dropped, taken

print("dropwhile/takewhile:", drop_take_example())  
# ([6, 4, 1], [1, 4])
```

### **7. `groupby()` - تجميع حسب مفتاح**
```python
from itertools import groupby

def groupby_example():
    data = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
    # نجمع حسب طول الكلمة
    grouped = {key: list(group) for key, group in groupby(data, key=len)}
    return grouped

print("groupby:", groupby_example())
# {5: ['apple'], 6: ['banana', 'cherry'], 4: ['date'], 10: ['elderberry']}
```

### **8. `permutations()` و `combinations()`**
```python
from itertools import permutations, combinations

def permutations_combinations():
    data = [1, 2, 3]
    
    # جميع التباديل (الترتيب مهم)
    perms = list(permutations(data, 2))
    
    # جميع التوافيق (الترتيب غير مهم)
    combs = list(combinations(data, 2))
    
    return perms, combs

perms, combs = permutations_combinations()
print("permutations:", perms)  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print("combinations:", combs)  # [(1, 2), (1, 3), (2, 3)]
```

### **9. `product()` - جداء ديكارتي**
```python
from itertools import product

def product_example():
    # جداء ديكارتي بين قائمتين
    result = product('AB', [1, 2])
    return list(result)

print("product:", product_example())  # [('A', 1), ('A', 2), ('B', 1), ('B', 2)]
```

### **10. `islice()` - تقطيع iterator**
```python
from itertools import islice

def islice_example():
    numbers = count()  # iterator لا نهائي
    return list(islice(numbers, 5, 10))  # من الفهرس 5 إلى 10

print("islice:", islice_example())  # [5, 6, 7, 8, 9]
```

## أمثلة عملية باستخدام itertools:

### **مثال 1: معالجة بيانات طلاب**
```python
from itertools import groupby

students = [
    {'name': 'Ahmed', 'grade': 'A'},
    {'name': 'Mohamed', 'grade': 'B'},
    {'name': 'Fatima', 'grade': 'A'},
    {'name': 'Sara', 'grade': 'C'},
    {'name': 'Ali', 'grade': 'B'}
]

# تجميع الطلاب حسب الدرجة
students.sort(key=lambda x: x['grade'])
grouped = {grade: list(group) for grade, group in groupby(students, key=lambda x: x['grade'])}

print("مجموعات الطلاب:")
for grade, group in grouped.items():
    names = [s['name'] for s in group]
    print(f"الدرجة {grade}: {', '.join(names)}")
```

### **مثال 2: توليد جميع الاحتمالات**
```python
from itertools import product

def generate_passwords(chars, length):
    """توليد جميع كلمات المرور الممكنة"""
    return [''.join(combo) for combo in product(chars, repeat=length)]

passwords = generate_passwords('ABC', 2)
print("كلمات المرور:", passwords)  # ['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']
```

### **مثال 3: تحليل تسلسل**
```python
from itertools import pairwise, takewhile

def analyze_sequence(sequence):
    """تحليل تسلسل الأرقام"""
    # الفروق بين العناصر المتتالية
    differences = [b - a for a, b in pairwise(sequence)]
    
    # نأخذ الأرقام حتى يصبح الفرق سالب
    increasing = list(takewhile(lambda x: x >= 0, differences))
    
    return differences, increasing

seq = [1, 3, 5, 4, 2, 6]
diffs, inc = analyze_sequence(seq)
print("الفروق:", diffs)        # [2, 2, -1, -2, 4]
print("التزايد المستمر:", inc) # [2, 2]
```

## الخلاصة:

- **`itertools`** ⇢ مكتبة قوية للتعامل مع iterators
- **الكفاءة** ⇢ تعمل مع البيانات الكبيرة بدون تخزينها كلها
- **المرونة** ⇢ دوال للجمع، التصفية، التكرار، والتوليد
- **الاستخدام** ⇢ مثالية لمعالجة البيانات، توليد الاحتمالات، والتحليل

الآن يمكنك استخدام `itertools` لحل التمارين المعقدة بكفاءة! 🚀
# استخدام itertools لحل التمارين

سأستخدم دوال module `itertools` لحل التمارين المطلوبة:

## 1. استخدام `pairwise` - أول تمرين

```python
from itertools import pairwise

def example_pairwise():
    return list(pairwise(range(5)))

print(example_pairwise())  # [(0, 1), (1, 2), (2, 3), (3, 4)]
```

## الآن دعني أقدم أهم دوال itertools مع أمثلة:

### **1. `count()` - عداد لا نهائي**
```python
from itertools import count

def infinite_counter():
    counter = count(start=1, step=2)  # 1, 3, 5, 7, ...
    return list(next(counter) for _ in range(5))

print("count:", infinite_counter())  # [1, 3, 5, 7, 9]
```

### **2. `cycle()` - تكرار لا نهائي**
```python
from itertools import cycle

def infinite_cycle():
    cycler = cycle('ABC')
    return list(next(cycler) for _ in range(6))

print("cycle:", infinite_cycle())  # ['A', 'B', 'C', 'A', 'B', 'C']
```

### **3. `repeat()` - تكرار قيمة**
```python
from itertools import repeat

def repeat_value():
    repeater = repeat(5, times=4)  # repeat 5 four times
    return list(repeater)

print("repeat:", repeat_value())  # [5, 5, 5, 5]
```

### **4. `chain()` - ربط iterables**
```python
from itertools import chain

def chain_example():
    result = chain('ABC', 'DEF', [1, 2, 3])
    return list(result)

print("chain:", chain_example())  # ['A', 'B', 'C', 'D', 'E', 'F', 1, 2, 3]
```

### **5. `compress()` - تصفية بقالب**
```python
from itertools import compress

def compress_example():
    data = 'ABCDEF'
    selectors = [1, 0, 1, 0, 1, 1]  # 1 = نأخذ, 0 = نتجاهل
    return list(compress(data, selectors))

print("compress:", compress_example())  # ['A', 'C', 'E', 'F']
```

### **6. `dropwhile()` و `takewhile()`**
```python
from itertools import dropwhile, takewhile

def drop_take_example():
    numbers = [1, 4, 6, 4, 1]
    
    # نتجاهل حتى يصبح الشرط False
    dropped = list(dropwhile(lambda x: x < 5, numbers))
    
    # نأخذ حتى يصبح الشرط False  
    taken = list(takewhile(lambda x: x < 5, numbers))
    
    return dropped, taken

print("dropwhile/takewhile:", drop_take_example())  
# ([6, 4, 1], [1, 4])
```

### **7. `groupby()` - تجميع حسب مفتاح**
```python
from itertools import groupby

def groupby_example():
    data = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
    # نجمع حسب طول الكلمة
    grouped = {key: list(group) for key, group in groupby(data, key=len)}
    return grouped

print("groupby:", groupby_example())
# {5: ['apple'], 6: ['banana', 'cherry'], 4: ['date'], 10: ['elderberry']}
```

### **8. `permutations()` و `combinations()`**
```python
from itertools import permutations, combinations

def permutations_combinations():
    data = [1, 2, 3]
    
    # جميع التباديل (الترتيب مهم)
    perms = list(permutations(data, 2))
    
    # جميع التوافيق (الترتيب غير مهم)
    combs = list(combinations(data, 2))
    
    return perms, combs

perms, combs = permutations_combinations()
print("permutations:", perms)  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print("combinations:", combs)  # [(1, 2), (1, 3), (2, 3)]
```

### **9. `product()` - جداء ديكارتي**
```python
from itertools import product

def product_example():
    # جداء ديكارتي بين قائمتين
    result = product('AB', [1, 2])
    return list(result)

print("product:", product_example())  # [('A', 1), ('A', 2), ('B', 1), ('B', 2)]
```

### **10. `islice()` - تقطيع iterator**
```python
from itertools import islice

def islice_example():
    numbers = count()  # iterator لا نهائي
    return list(islice(numbers, 5, 10))  # من الفهرس 5 إلى 10

print("islice:", islice_example())  # [5, 6, 7, 8, 9]
```

## أمثلة عملية باستخدام itertools:

### **مثال 1: معالجة بيانات طلاب**
```python
from itertools import groupby

students = [
    {'name': 'Ahmed', 'grade': 'A'},
    {'name': 'Mohamed', 'grade': 'B'},
    {'name': 'Fatima', 'grade': 'A'},
    {'name': 'Sara', 'grade': 'C'},
    {'name': 'Ali', 'grade': 'B'}
]

# تجميع الطلاب حسب الدرجة
students.sort(key=lambda x: x['grade'])
grouped = {grade: list(group) for grade, group in groupby(students, key=lambda x: x['grade'])}

print("مجموعات الطلاب:")
for grade, group in grouped.items():
    names = [s['name'] for s in group]
    print(f"الدرجة {grade}: {', '.join(names)}")
```

### **مثال 2: توليد جميع الاحتمالات**
```python
from itertools import product

def generate_passwords(chars, length):
    """توليد جميع كلمات المرور الممكنة"""
    return [''.join(combo) for combo in product(chars, repeat=length)]

passwords = generate_passwords('ABC', 2)
print("كلمات المرور:", passwords)  # ['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']
```

### **مثال 3: تحليل تسلسل**
```python
from itertools import pairwise, takewhile

def analyze_sequence(sequence):
    """تحليل تسلسل الأرقام"""
    # الفروق بين العناصر المتتالية
    differences = [b - a for a, b in pairwise(sequence)]
    
    # نأخذ الأرقام حتى يصبح الفرق سالب
    increasing = list(takewhile(lambda x: x >= 0, differences))
    
    return differences, increasing

seq = [1, 3, 5, 4, 2, 6]
diffs, inc = analyze_sequence(seq)
print("الفروق:", diffs)        # [2, 2, -1, -2, 4]
print("التزايد المستمر:", inc) # [2, 2]
```

## الخلاصة:

- **`itertools`** ⇢ مكتبة قوية للتعامل مع iterators
- **الكفاءة** ⇢ تعمل مع البيانات الكبيرة بدون تخزينها كلها
- **المرونة** ⇢ دوال للجمع، التصفية، التكرار، والتوليد
- **الاستخدام** ⇢ مثالية لمعالجة البيانات، توليد الاحتمالات، والتحليل

الآن يمكنك استخدام `itertools` لحل التمارين المعقدة بكفاءة! 🚀