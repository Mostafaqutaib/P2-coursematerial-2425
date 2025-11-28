**itertools** من أحلى أجزاء الكورس لأنها تعطيك أدوات جبّارة للتعامل مع أي iterable…
وهي جزء رسمي من البايثون (module built-in)، والكورس يستخدمها بكثرة.

خلّيني أشرح لك **itertools** كما هي موجودة في مجلد الـ `.md` الخاص بها في الكورس، وبنفس أسلوب الكتابة الموجود هناك + زيادة تبسيط.

---

# 🔵 ما هو **itertools**؟

مكتبة جاهزة في بايثون تحتوي "أدوات" تساعدك تعمل عمليات قوية على الـ iterables، خصوصًا في **functional programming**، مثل:

* التكرار اللانهائي
* التجميع
* التوليف والتبديل
* الفلترة
* الدمج
* إنشاء sequences بدون تخزينها في الذاكرة
  ✨ وبشكل عام: شغل functional عالي المستوى.

الكورس يقسم itertools عادةً إلى مجموعات:

---

# #️⃣ **1. iterators that produce infinite sequences**

⏳ هذول يعطوك *تسلسلات لا نهائية*، ولا يحسبون شيء إلا عند الحاجة (lazy evaluation).

## ✔️ `itertools.count(start=0, step=1)`

يعدّ لك أرقام بدون توقف:

```python
from itertools import count

for n in count(5, 2):
    print(n)
    if n > 15:
        break
```

يعطي:

```
5, 7, 9, 11, 13, 15
```

---

## ✔️ `itertools.cycle(iterable)`

يكرّر العناصر بشكل دائري:

```python
from itertools import cycle

for i, c in zip(range(10), cycle("AB")):
    print(c)
```

الناتج:

```
A B A B A B A B A B
```

---

## ✔️ `itertools.repeat(value, times=None)`

يرجع قيمة مكرّرة:

```python
from itertools import repeat

for item in repeat("Hi", 3):
    print(item)
```

```
Hi
Hi
Hi
```

---

# #️⃣ **2. Iterators for combining / chaining**

## ✔️ `itertools.chain(a, b, c...)`

يربط أكثر من iterable وكأنها قائمة واحدة.

```python
from itertools import chain

result = chain([1, 2], (3, 4), "56")
print(list(result))
```

ناتج:

```
[1, 2, 3, 4, '5', '6']
```

---

## ✔️ `itertools.product(iter1, iter2)`

منتج ديكارتي (جميع التركيبات الممكنة).

```python
from itertools import product

print(list(product([1, 2], ['A', 'B'])))
```

```
[(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
```

---

## ✔️ `itertools.combinations(iterable, r)`

يطلع جميع *الاختيارات بدون تكرار*—ترتيب غير مهم.

```python
from itertools import combinations

print(list(combinations([1, 2, 3], 2)))
```

```
[(1, 2), (1, 3), (2, 3)]
```

---

## ✔️ `itertools.permutations(iterable, r)`

جميع الترتيبات الممكنة—الترتيب مهم.

```python
from itertools import permutations

print(list(permutations("ABC", 2)))
```

```
[('A', 'B'), ('A', 'C'), ('B', 'A'), ...]
```

---

# #️⃣ **3. Iterators for filtering**

## ✔️ `itertools.filterfalse(predicate, iterable)`

عكس filter → يرجع *العناصر التي الشرط عليها False*

```python
from itertools import filterfalse

nums = [1, 2, 3, 4, 5]

print(list(filterfalse(lambda x: x % 2 == 0, nums)))
```

```
[1, 3, 5]
```

---

## ✔️ `itertools.takewhile(predicate, iterable)`

ياخذ عناصر *طالما الشرط True*.

```python
from itertools import takewhile

print(list(takewhile(lambda x: x < 5, [1, 2, 3, 7, 2])))
```

```
[1, 2, 3]
```

---

## ✔️ `itertools.dropwhile(predicate, iterable)`

العكس → يتجاهل العناصر اللي الشرط عليها True بالبداية.

```python
from itertools import dropwhile

print(list(dropwhile(lambda x: x < 5, [1, 2, 3, 7, 2])))
```

```
[7, 2]
```

---

# #️⃣ **4. Grouping helpers**

## ✔️ `itertools.groupby(iterable, key=None)`

يجمع عناصر حسب مفتاح معين.

لكن ملاحظة في الكورس:
**لازم يكون iterable مفرز sorted** عشان التجميع صح.

```python
from itertools import groupby

items = [('A', 1), ('A', 2), ('B', 5), ('B', 7)]

for key, group in groupby(items, lambda x: x[0]):
    print(key, list(group))
```

الناتج:

```
A [(1), (2)]
B [(5), (7)]
```

---

# #️⃣ **5. Useful tools**

## ✔️ `itertools.accumulate(iterable)`

تراكم القيم (جمع تدريجي):

```python
from itertools import accumulate

print(list(accumulate([1, 2, 3, 4])))
```

```
[1, 3, 6, 10]
```

ممكن تستخدم دالة ثانية:

```python
import operator
accumulate([1,2,3,4], operator.mul)
```

---

# #️⃣ **6. itertools + functional programming**

الكورس يركز على إنها:

* ما تخزّن البيانات → memory efficient
* كلها iterators (lazy evaluation)
* ممتازة مع map/filter
* ممتازة مع chaining pipelines

زي مثال الكورس:

```python
from itertools import chain, filterfalse

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

result = chain(nums1, nums2)
evens = filterfalse(lambda x: x % 2, result)

print(list(evens))
```

```
[2, 4, 6]
```
