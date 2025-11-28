

# 🌀 **itertools – Cheat Sheet مختصر وواضح**

## 🚀 الاستيراد الأساسي

```python
from itertools import *
```

---

# 🔵 **1) Iterators لا نهائية Infinite Iterators**

### ✔️ `count(start=0, step=1)`

يعد بدون توقف.

```python
for n in count(10, 2):
    print(n)   # 10 12 14 ...
```

### ✔️ `cycle(iterable)`

يعيد العناصر بشكل دائري.

```python
cycle("AB")  # A B A B A B...
```

### ✔️ `repeat(value, times=None)`

يرجع قيمة متكرّرة.

```python
repeat("Hi", 3)  # Hi Hi Hi
```

---

# 🟣 **2) Iterators للتجميع / الدمج Combining Iterables**

### ✔️ `chain(iter1, iter2, ...)`

دمج عدة iterables.

```python
list(chain([1,2], [3,4]))  # [1,2,3,4]
```

### ✔️ `chain.from_iterable(list_of_iters)`

مثل chain لكن يأخذ iterable واحد يحتوي iterables داخله.

### ✔️ `product(iter1, iter2, ...)`

المنتج الديكارتي (كل التركيبات الممكنة).

```python
list(product([1,2], ['A','B']))
# [(1,'A'), (1,'B'), (2,'A'), (2,'B')]
```

### ✔️ `permutations(iterable, r=None)`

كل الترتيبات—الترتيب مهم.

```python
permutations("ABC", 2)
```

### ✔️ `combinations(iterable, r)`

اختيارات بدون تكرار—ترتيب غير مهم.

```python
combinations([1,2,3], 2)
```

### ✔️ `combinations_with_replacement(iterable, r)`

مثل combinations لكن يسمح بالتكرار.

---

# 🟢 **3) Iterators للفلترة Filtering**

### ✔️ `filterfalse(predicate, iterable)`

عكس filter → يرجع العناصر اللي الشرط عليها False.

```python
filterfalse(lambda x: x%2==0, [1,2,3,4])
# [1,3]
```

### ✔️ `takewhile(predicate, iterable)`

خذ عناصر *طالما الشرط True*.

```python
takewhile(lambda x: x < 5, [1,2,3,6,1])
# [1,2,3]
```

### ✔️ `dropwhile(predicate, iterable)`

تجاهل العناصر التي الشرط عليها True حتى أول False.

```python
dropwhile(lambda x: x < 5, [1,2,3,6,1])
# [6,1]
```

### ✔️ `islice(iterable, start, stop, step)`

Slice لكن للـ iterables.

```python
islice(range(10), 2, 8, 2)
# [2,4,6]
```

---

# 🟠 **4) Iterators للتجميع / التجميع Grouping**

### ✔️ `groupby(iterable, key=None)`

يجمع عناصر حسب key.
⚠️ **لازم يكون iterable sorted حسب نفس المفتاح.**

```python
items = [('A',1), ('A',2), ('B',3)]
for k, g in groupby(items, lambda x: x[0]):
    print(k, list(g))
```

---

# 🟡 **5) Iterators للتراكم / المعالجة الإضافية**

### ✔️ `accumulate(iterable, func=operator.add)`

تراكم القيم.

```python
list(accumulate([1,2,3,4]))
# [1, 3, 6, 10]
```

مع دوال أخرى:

```python
import operator
accumulate([1,2,3,4], operator.mul)
# [1, 2, 6, 24]
```

---

# 🔥 **6) Useful patterns (مهمّة للتمارين!)**

### ▪️ دمج + فلترة:

```python
evens = filterfalse(lambda x: x % 2, chain([1,2], [3,4]))
```

### ▪️ combinations لحل مسائل اختيار:

```python
list(combinations(range(5), 3))
```

### ▪️ permutations لحل الترتيب:

```python
list(permutations("ABC"))
```

### ▪️ takewhile لإيقاف generator:

```python
list(takewhile(lambda x: x < 10, count()))
```

### ▪️ islice لقطع sequences:

```python
list(islice(count(0), 5))
# [0,1,2,3,4]
```

---

# 🎯 **تلخيص التلخيص**

| الفئة          | الدوال                                             |
| -------------- | -------------------------------------------------- |
| 🔵 لا نهائية   | `count`, `cycle`, `repeat`                         |
| 🟣 دمج وعمليات | `chain`, `product`, `permutations`, `combinations` |
| 🟢 فلترة       | `filterfalse`, `takewhile`, `dropwhile`, `islice`  |
| 🟠 تجميع       | `groupby`                                          |
| 🟡 تراكم       | `accumulate`                                       |

