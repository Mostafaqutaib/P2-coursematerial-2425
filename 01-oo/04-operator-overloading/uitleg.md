تمام 👍 خلّينا نشرح **Operator Overloading** بهدوء وبعمق، وبأسلوب الكورس، ونربطه بكل اللي أخذته قبل:
**Encapsulation – Properties – OOP – Python behavior**.

---

# 🔹 ما هو Operator Overloading؟

**Operator Overloading** يعني:

> إعطاء معنى جديد للـ operators (`+ - * / ...`) عندما نستخدمها مع كائنات (objects) من كلاس نحن كتبناه.

باختصار:

* `+` لا يعني دائمًا “جمع أرقام”
* المعنى يعتمد على **نوع الكائن**

---

## 🔹 لماذا نحتاجه؟

انظر لهذا المثال:

```python
5 + 3             # أرقام
"a" + "b"         # Strings
[1, 2] + [3, 4]   # Lists
```

نفس الرمز `+`
لكن:

* مع الأرقام → جمع
* مع النصوص → دمج
* مع القوائم → دمج

إذًا:
👉 **المعامل نفسه، لكن السلوك مختلف حسب النوع**

---

## 🔹 المشكلة مع الكلاسات الخاصة بنا

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
q = Point(3, 4)

p + q
```

❌ النتيجة:

```text
TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
```

ليش؟

* Python **لا يعرف** ماذا يعني جمع نقطتين
* لازم أنت تشرح له

---

# 🔹 الحل الأول (الطريقة العادية – بدون operator)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)
```

الاستخدام:

```python
p.add(q)
```

✅ يعمل
❌ لكنه **غير طبيعي** للمستخدم

---

# 🔹 الحل الصحيح: Operator Overloading

نستخدم **dunder method** اسمه `__add__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )
```

الآن:

```python
p + q
```

🎉 تعمل!

---

## 🔹 ماذا يحدث خلف الكواليس؟

عندما تكتب:

```python
p + q
```

Python **تترجمها تلقائيًا** إلى:

```python
p.__add__(q)
```

يعني:

* لا يوجد سحر
* مجرد استدعاء دالة باسم خاص

---

# 🔹 لماذا اسمها dunder methods؟

لأنها محاطة بشرطتين سفليتين:

```text
__add__
__sub__
__mul__
```

اسمها الكامل:

> **Double UNDERscore** → dunder

---

# 🔹 أشهر operators و dunder methods

| Operator | Method         |
| -------- | -------------- |
| `+`      | `__add__`      |
| `-`      | `__sub__`      |
| `*`      | `__mul__`      |
| `/`      | `__truediv__`  |
| `//`     | `__floordiv__` |
| `%`      | `__mod__`      |
| `**`     | `__pow__`      |

---

# 🔹 قاعدة مهمة جدًا (يمتحن عليها 💥)

> ❗ **Operator overloading يجب أن يكون غير مدمّر (non-mutating)**

يعني:

* لا تعدّل `self`
* دائمًا **ارجع object جديد**

---

## ✅ التنفيذ الصحيح

```python
def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)
```

---

## ❌ التنفيذ الخاطئ (ممنوع في الكورس)

```python
def __add__(self, other):
    self.x += other.x
    self.y += other.y
```

ليش هذا غلط؟

* `p + q` **يغيّر p**
* هذا سلوك غير متوقع
* يخالف قواعد OOP
* يكسر Encapsulation

---

# 🔹 مثال ربط مع Money (اللي طبقته)

```python
def __add__(self, other):
    if self.__currency != other.currency:
        raise RuntimeError("Mismatched currencies!")
    return Money(self.__amount + other.amount, self.__currency)
```

لاحظ:

* ✔️ تحقق من المنطق
* ✔️ لم نعدّل `self`
* ✔️ أرجعنا كائن جديد
* ✔️ سلوك طبيعي ومتوقع

---

# 🔹 Operator Overloading ≠ Syntax Sugar فقط

هو:

* تحسين واجهة الاستخدام (API)
* جعل الكلاس **يتصرف مثل الأنواع المدمجة**
* زيادة قابلية القراءة

بدل:

```python
money1.add(money2)
```

نكتب:

```python
money1 + money2
```

👈 أوضح + أنظف + أسهل

---

# 🔹 ربط سريع مع Encapsulation

* `__add__` جزء من **واجهة الكلاس**
* لا تكشف تفاصيل داخلية
* المستخدم لا يعرف كيف تم الجمع
* فقط يعرف **كيف يستخدمه**

---

# 🧠 الخلاصة الذهبية

> ❝ Operator overloading يسمح لك بجعل كائناتك تتصرف مثل الأنواع الأصلية في Python،
> بشرط أن يكون السلوك منطقيًا، غير مدمّر، وواضحًا ❞

---

## سؤال مهم (تفكير امتحان 🎓):

لماذا يعتبر تعديل `self` داخل `__add__` خطأ تصميميًا، حتى لو “اشتغل” الكود؟
(فكّر من ناحية **توقعات المستخدم**)
