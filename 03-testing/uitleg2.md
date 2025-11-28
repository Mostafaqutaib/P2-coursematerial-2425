

# 🎯 **أول شيء: وش يعني Testing في P2؟**

في الكورس، كل تمرين يكون معه ملف اسمه:

```
tests.py
```

هذا الملف هو **الحَكَم**.
يحدّد:

* اسم الـ functions اللي لازم تكتبها
* البارامترات اللي تستقبلها
* القيم اللي لازم ترجعها
* السلوك اللي لازم يصير

انت **ما تعدّل على tests**.
انت تكتب كودك بحيث **ينجح** في الاختبارات.

---

# 🧪 **كيف يفكر الـ Test؟ (المفهوم اللي لازم تفهمه)**

الـ test يعمل حاجة وحدة:

> **يشغّل الـ function اللي انت كتبتها… ويقارن النتيجة بشيء محدد.**

مثال بسيط من نفس أسلوب الكورس:

```python
def test_double():
    assert double(3) == 6
```

معنى هذا:

1. لازم تسوي function اسمها `double`
2. تستقبل رقم واحد
3. ترجع ضعف الرقم (3 → 6)

الحل يكون:

```python
def double(x):
    return x * 2
```

انتهى.

---

# 🚀 **أهم فكرة لازم تفهمها**

## الـ tests هي وثيقة المواصفات (specs)

بمعنى:
بدل ما الدكتور يشرح لك verbally…
الـ **tests** هي اللي تقول لك:

* وش نسوي
* وش نرجّع
* متى نرمي error
* وش شكل المخرجات

**إذا فهمت الـ tests… فهمت التمرين كامل.**

---

# 📌 طيب… كيف أقرأ test؟ (الخلاصة اللي تخليك تفهم كل شيء)

لنفترض هذا test (أسلوب الكورس):

```python
def test_clean_name():
    assert clean_name("  ali ") == "Ali"
```

أقرأه هكذا:

1. اسم ال function: **clean_name**
2. تستقبل: **string**
3. المطلوب:

   * تشيل المسافات
   * تخلي أول حرف capital
4. ترجع: `"Ali"`

فتكتب:

```python
def clean_name(name):
    name = name.strip()
    return name.capitalize()
```

—

# 🧪 **وش يعني assert؟**

هذا قلب الاختبار:

```python
assert something == expected
```

معناه:

> لو `something` ما يساوي `expected` → FAIL

---

# 🔥 مثال ثاني واضح مرّة

test:

```python
def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([]) == 0
```

إيش نفهم؟

* function اسمها sum_list
* تاخذ list
* ترجع مجموع العناصر
* لو اللست فاضية → ترجع 0

الحل:

```python
def sum_list(numbers):
    return sum(numbers)
```

تم.

---

# 🔥 مثال مهم زي اللي في الكورس (return types)

test:

```python
def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4]) == [2, 4]
```

إيش نفهم؟

* function ترجع **list**
* ما تغير ترتيب العناصر
* ما ترجع tuple أو set
* لازم تبقى list

الحل:

```python
def get_even_numbers(lst):
    return [n for n in lst if n % 2 == 0]
```

---

# ❗ أهم 3 مهارات لفهم الـ Testing في الكورس

## 1) **اقرأ test line-by-line**

كل سطر يقول لك شيء.

## 2) **انتبه للـ types**

إذا الاختبار يتوقع list لازم ترجع list.
إذا dict لازم dict.
إذا string لازم string.

## 3) **لا تكتب شيء ما طلبه الاختبار**

لا تضيف print
لا تضيف input
لا تغيّر behavior
اتبع الاختبار بالحرف.
