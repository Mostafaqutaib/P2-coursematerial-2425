

## 1. إيش يعني *comprehension* أصلاً؟

بدون comprehensions، غالبًا تكتب كود بالطريقة هذي:

```python
result = []
for x in xs:
    result.append(f(x))
```

نفس الفكرة بالـ **list comprehension**:

```python
result = [f(x) for x in xs]
```

الشكل العام:

```python
[new_element   for element in input_collection   if condition(element)]
```

وبالمثل في:

* **set comprehension**: نستخدم `{}` بدل `[]`
* **dict comprehension**: نستخدم `{key_expr: value_expr for ...}`

---

## 2. ملف `01-mapping.md` — *Mapping + List Comprehensions*

الفكرة هنا: **تحويل قائمة لقائمة ثانية** نفس الطول، لكن كل عنصر فيها متغيّر بعملية معيّنة (تربيع، تحويل إلى string، أخذ خاصية من object…).

مثال الكورس:

```python
def squares(ns):
    result = []
    for n in ns:
        result.append(n**2)
    return result
```

هذي اسمها **mapping**:
ناخذ `ns` ونرجّع **قائمة جديدة**، كل عنصر فيها هو `n**2`.

بنفس الفكرة بالـ **list comprehension**:

```python
def squares(ns):
    return [n**2 for n in ns]
```

الشكل العام اللي في الملف:

```python
new_list = [map(element) for element in input_list]
```

* `map(element)` → التعبير اللي يحوّل العنصر
* `input_list` → القائمة اللي نلف عليها

الملف بعدين يربط هذا مع فكرة الـ **higher-order functions** زي `map()` (الـ built-in) لكن الأساس هنا:

> لو عندك for-loop بسيط بس يـ *حوّل* العناصر → غالبًا تقدر تكتبه كـ list comprehension أوضح وأقصر وأسرع شوية (وفي `benchmark.py` في نفس الفولدر يورّيك الفرق في الزمن).

---

## 3. ملف `03-filtering.md` — *Filtering*

هنا نضيف فكرة ثانية: بدل ما *نحوّل كل عنصر*، أحيانًا نبي **نختار بعض العناصر فقط**.

مثال الكورس:

```python
def select_adults(people):
    result = []
    for person in people:
        if person.age >= 18:
            result.append(person)
    return result
```

هذي اسمها **filtering**: نحتفظ بالعناصر اللي تحقق شرط (predicate).

الشكل العام بالـ for-loop:

```python
result = []
for element in input:
    if condition(element):
        result.append(element)        # أو map(element) لو تبي كمان تحويل
```

وبالـ list comprehension:

```python
result = [element for element in input if condition(element)]
# أو:
result = [map(element) for element in input if condition(element)]
```

فالصيغة العامة اللي في الملف:

```python
result = [map(element) for element in input if condition(element)]
```

> الفرق عن mapping بس: أضفنا جزء `if condition(element)` في النهاية.

---

## 4. ملف `05-set-comprehensions.md` — *Set Comprehension*

نفس فكرة list comprehension، لكن بدل `[]` نستخدم `{}` و النتيجة **set**:

```python
def squares(ns):
    return {n**2 for n in ns}
```

الملف يورّيك الفرق:

```python
[n**2 for n in range(-10, 10)]
# ترجع list فيها تكرار للقيم

{n**2 for n in range(-10, 10)}
# ترجع set بدون عناصر مكرّرة، والترتيب مش محفوظ
```

نقاط مهمّة من الملف:

* الـ **set**:

  * ما يسمح بالتكرار
  * ما يضمن ترتيب العناصر
* لما تستخدم `{... for ... in ...}` → انت تقول: *“أبغى مجموعة من القيم الفريدة اللي ناتجة من هالعملية”*

مثال عملي:

```python
unique_genres = {genre
                 for movie in movies
                 for genre in movie.genres}
```

---

## 5. ملف `07-dictionary-comprehension.md` — *Dictionary Comprehension*

نفس الفكرة لكن نصنع **قاموس** بدل list/set.

الصيغة الأساسية:

```python
{key_expr: value_expr   for element in collection}
```

مثال الكورس (students by id):

```python
students_by_id = {student.id: student for student in students}
```

هنا:

* `student.id` → المفتاح في الدكشنري
* `student` → القيمة
* `students` → الـ collection اللي نلف عليها

ممكن نضيف شرط:

```python
long_movies_by_title = {
    movie.title: movie
    for movie in movies
    if movie.runtime > 120
}
```

لاحظ الفرق عن set comprehension:

```python
{expr for ...}                 # set
{key_expr: value_expr for ...} # dict
```

---

## 6. ملف `09-flatten.md` — *Nested Loops + Flattening*

هنا الموضوع يصير مستوى أعلى شوية:

الفكرة: عندك **قائمة من القوائم** (nested list)، وودّك تعمل لها **flatten** (تصير قائمة واحدة).

### أ) nested for-loop عادي

مثال بسيط:

```python
argument = [[1, 2, 3], [4, 5], [6]]
result = []
for lst in argument:
    for element in lst:
        result.append(element)
# result = [1, 2, 3, 4, 5, 6]
```

### ب) نفس الشي بالـ list comprehension

```python
result = [element
          for lst in argument
          for element in lst]
```

الترتيب مهم:
هو فعليًا يعادل:

```python
for lst in argument:
    for element in lst:
        ...
```

### ج) إضافة شروط

الكورس يعطي مثال مبالغ فيه بشروط كثيرة:

```python
result = []
for lst in argument:
    if len(lst) > 3:
        for element in lst:
            if element > 6:
                if element < 10:
                    result.append(element)
```

بالـ comprehension:

```python
result = [
    element
    for lst in argument
    if len(lst) > 3
    for element in lst
    if element > 6
    if element < 10
]
```

> نفس المنطق، لكن مضغوط في سطر/سطرين. لازم تنتبه للترتيب عشان ما يصير الكود معقّد زيادة.

---

## 7. ملف `11-builtin-functions.md` — *دوال بايثون المدمجة اللي نستخدمها مع comprehensions*

هذا الملف يذكّرك ببعض الـ built-in functions اللي غالبًا نستخدمها مع comprehensions.

المذكورة:

### `len`

```python
len(xs)   # عدد العناصر
```

مع comprehension:

```python
number_of_long_movies = len([m for m in movies if m.runtime > 120])
```

---

### `min` و `max`

أصغر / أكبر عنصر:

```python
shortest_runtime = min([m.runtime for m in movies])
longest_runtime = max([m.runtime for m in movies])
```

---

### `sum`

جمع العناصر:

```python
total_runtime = sum([m.runtime for m in movies])
average_runtime = total_runtime / len(movies)
```

---

### `all` و `any`

* `all(iterable)` → True لو **كل** العناصر truthy
* `any(iterable)` → True لو **واحد على الأقل** truthy

مع comprehensions:

```python
all_old = all([m.year < 2000 for m in movies])      # هل كل الأفلام قديمة؟
has_long_movie = any([m.runtime > 180 for m in movies])
```

---

### `zip`

يجمع قائمتين لقائمة من tuples:

```python
xs = ['a', 'b', 'c']
ys = [1, 2, 3]

list(zip(xs, ys))
# [('a', 1), ('b', 2), ('c', 3)]
```

مع comprehension:

```python
pairs = [(x, y) for x, y in zip(xs, ys)]
```

---

### `enumerate`

يعطيك `(index, element)`:

```python
xs = ['a', 'b', 'c']
list(enumerate(xs))
# [(0, 'a'), (1, 'b'), (2, 'c')]
```

مع comprehension:

```python
indexed = [(i, x) for i, x in enumerate(xs)]
```

---

## 8. ملفات الـ assignments داخل `assignments/`

داخل نفس الفولدر `04-comprehensions/assignments` عندك تمارين تطبّق كل اللي فوق:

* `02-mapping/assignment.md`
  تكتب دوال تشتغل على قائمة `Movie` وتستخرج منها معلومات (عناوين، سنوات، runtimes...) باستخدام **mapping** ويفضّل بـ list comprehensions.

* `04-filtering/assignment.md`
  دوال ترجع subset من الأفلام بناءً على شروط (سنة معيّنة، مدة معيّنة، نوع معيّن…) باستخدام **filtering**:
  `[movie for movie in movies if condition(movie)]`.

* `06-set-comprehension/assignment.md`
  تمارين على **set comprehensions** → مثلاً مجموعة الأنواع (genres) بدون تكرار، مجموعة المخرجين، إلخ.

* `08-dictionary-comprehension/assignment.md`
  تبني **dictionaries** من قائمة الأفلام، مثل:

  * `id -> movie`
  * `title -> runtime`
    باستخدام `{key_expr: value_expr for movie in movies}`.

* `10-flatten/assignment.md`
  تمارين على **flatten** للقوائم المتداخلة، غالبًا باستخدام:

  ```python
  [x for sub in outer for x in sub]
  ```

  ومع شوية شروط إضافية.

* `12-builtin-functions/assignment.md`
  تستخدم `len`, `min`, `max`, `sum`, `all`, `any`, `zip`, `enumerate` مع comprehensions لحل أسئلة مثل:

  * أطول فيلم
  * متوسط مدة الأفلام
  * هل كل الأفلام بعد سنة معيّنة
  * إلخ…

* `13-group-movies-by-year/assignment.md`
  المطلوب دالة:

  ```python
  def group_movies_by_year(movies):
      ...
  ```

  ترجع dict بالشكل:

  ```python
  {
      1944: [title1, title2],
      1995: [title3],
      2018: [title4, title5, title6]
  }
  ```

  فكرة الحل اللي تعتمد على comprehensions ممكن تكون (مجرد فكرة):

  ```python
  years = {movie.year for movie in movies}
  return {
      year: [m.title for m in movies if m.year == year]
      for year in years
  }
  ```

