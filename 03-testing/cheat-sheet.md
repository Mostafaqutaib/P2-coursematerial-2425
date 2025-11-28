
# 🧪✨ **Python Testing Cheat-Sheet (Programmeren 2 Style)**

## 🔵 1) **البدء مع pytest**

يشغّل كل ملفات الاختبارات:

```bash
pytest
```

يختبر ملف واحد:

```bash
pytest tests.py
```

إظهار معلومات أكثر (مفيد جدًا):

```bash
pytest -v
```

---

# 🟣 2) **هيكلة مشاريع التستينغ في الكورس**

الكورس دائمًا يتبع هذا الباترن:

```
project/
    assignments/
        exercise.py   ← هنا كودك
        tests.py      ← هنا الاختبارات
```

✔️ ممنوع تعدّل `tests.py`
✔️ شغّله وتأكد إن كل شيء "أخضر" 🙂

---

# 🟢 3) **كتابة Tests باستخدام assert**

## ✔️ الأساس:

```python
def test_add():
    assert add(2, 3) == 5
```

### أهم قواعد الـ assert:

* يقارن قيم
* لو كان False → يفشل الاختبار
* لو True → الاختبار يمر بنجاح

---

# 🟠 4) **اختبار Exceptions**

الكورس يستخدم:

```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
```

---

# 🟡 5) **اختبار قيم كثيرة (Parameterized tests)**

الكورس يستخدمها كثيرًا خصوصًا مع ال functions الصغيرة.

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 5, 5),
    (-1, 2, 1)
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

---

# 🟤 6) **اختبار أن الفنكشن لا تغيّر القيمة الأصلية**

الكورس دايمًا يهتم بـ “pure functions”
مثال:

```python
def test_pure():
    data = [1, 2, 3]
    result = double(data)
    assert data == [1, 2, 3]   # لم تتغير
    assert result == [2, 4, 6]
```

---

# 🔴 7) **Fixtures (المذكورة في الكورس)**

تعطيك بيانات جاهزة قبل كل اختبار.

```python
@pytest.fixture
def numbers():
    return [1, 2, 3]

def test_sum(numbers):
    assert sum(numbers) == 6
```

---

# 🔵 8) **اختبار الـ Iterators و Generators**

الكورس يعمل هذا كثيرًا:

```python
def test_generator():
    gen = counter(1, 4)
    assert next(gen) == 1
    assert next(gen) == 2
    assert next(gen) == 3
```

أو:

```python
assert list(counter(1, 4)) == [1, 2, 3]
```

---

# 🟣 9) **اختبار itertools pipelines**

```python
from itertools import chain, filterfalse

def test_pipeline():
    nums = chain([1,2], [3,4])
    evens = filterfalse(lambda x: x % 2, nums)
    assert list(evens) == [2,4]
```

---

# 🟢 10) **اختبار الدوال التي تعيد None**

القيمة الوحيدة اللي تختبرها هي side-effects:

```python
def test_print(capsys):
    greet("Ali")
    captured = capsys.readouterr()
    assert captured.out == "Hello Ali\n"
```

---

# 🟡 11) **اختبار Classes في الكورس**

```python
def test_person():
    p = Person("Ali", 20)
    assert p.age == 20
    assert p.name == "Ali"
```

---

# 🧩 12) **Testing Tips (مطابقة للكورس)**

| الشيء              | ليش مهم؟                         |
| ------------------ | -------------------------------- |
| اختبر حالة عادية   | expected main behavior           |
| اختبر edge cases   | قيم empty, صفر، أعداد سالبة      |
| اختبر exceptions   | validate correctness             |
| اختبر الـ types    | الكورس يستخدم type-checking كثير |
| اختبر immutability | عشان functional programming      |

---

# 🧨 13) **كيف تعرف إن كل شيء ناجح؟**

يشغّل:

```bash
pytest -v
```

تشوف:

* ✔️ أخضر → كل شيء تمام
* ❌ أحمر → اقرأ الرسالة، راح تقول لك وين الغلط بالضبط

---
