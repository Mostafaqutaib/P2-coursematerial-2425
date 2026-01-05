تمام 👍 خلّينا نأخذ **properties** و **computed attributes** و **setters** من الصفر، وبأسلوب كورس **Programmeren 2**، مع أمثلة واضحة وربط مباشر بـ **Encapsulation**.

سأقسم الشرح إلى أقسام، وكل قسم يبني على اللي قبله.

---

# 1️⃣ المشكلة الأساسية: لماذا نحتاج Properties؟

خلّينا نبدأ بكلاس بسيط جدًا:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

الاستخدام:

```python
p = Person("Ali", 20)
print(p.age)     # 20
p.age = -5       # 😨 مسموح!
```

❌ المشكلة:

* المستخدم قدر يضع عمر غير منطقي (`-5`)
* الكلاس فقد السيطرة على بياناته

هنا **Encapsulation** انكسرت.

---

# 2️⃣ الحل القديم (قبل properties): getters و setters

نخلي المتغير **private** ونضيف دوال:

```python
class Person:
    def __init__(self, name, age):
        self.__age = age
        self.name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.__age = age
```

الاستخدام:

```python
p = Person("Ali", 20)
p.set_age(25)
print(p.get_age())
```

✅ آمن
❌ لكنه **غير مريح** في الاستخدام

بايثون عندها حل أجمل 👇

---

# 3️⃣ ما هي Properties؟

**Property** تسمح لك:

* بالوصول للخاصية **وكأنها متغير**
* لكن خلف الكواليس يتم استدعاء دالة

يعني:

```python
p.age
```

تبدو كمتغير
لكنها في الحقيقة **دالة**

---

# 4️⃣ Property (getter) – خطوة بخطوة

```python
class Person:
    def __init__(self, name, age):
        self.__age = age
        self.name = name

    @property
    def age(self):
        return self.__age
```

الاستخدام:

```python
p = Person("Ali", 20)
print(p.age)   # 20
```

ماذا حدث؟

* `age` **ليست متغيرًا**
* لكنها تُستعمل كمتغير
* بايثون تنفذ الدالة `age(self)`

✔️ هذا يحافظ على Encapsulation
✔️ ويجعل الكود نظيفًا

---

# 5️⃣ Setter – التحكم عند التعديل

الآن نريد السماح بالتعديل **لكن بشروط**.

نضيف setter:

```python
class Person:
    def __init__(self, name, age):
        self.__age = age
        self.name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self.__age = value
```

الاستخدام:

```python
p = Person("Ali", 20)
p.age = 30      # ✅
p.age = -5      # ❌ ValueError
```

لاحظ:

* ما كتبنا `set_age`
* لكن التحكم موجود
* المستخدم لا يشعر بالتعقيد

---

# 6️⃣ ماذا لو لم نكتب setter؟

```python
class Wall:
    def __init__(self, height):
        self.__height = height

    @property
    def height(self):
        return self.__height
```

الاستخدام:

```python
w = Wall(10)
print(w.height)   # ✅
w.height = 20     # ❌ AttributeError
```

✔️ هذا يسمى **read-only property**
ممتاز لحماية القيم

---

# 7️⃣ Computed Attribute (خاصية محسوبة)

أحيانًا لا نملك قيمة مخزنة، بل **نحسبها**.

مثال:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
```

الاستخدام:

```python
r = Rectangle(4, 5)
print(r.area)   # 20
```

ملاحظات مهمة:

* `area` **غير موجودة في **init****
* لا نخزنها
* تُحسب كل مرة
* لكنها تُستعمل كأنها متغير

✨ هذا هو **Computed Attribute**

---

# 8️⃣ لماذا لا نخزن القيمة المحسوبة؟

لو خزّناها:

```python
self.area = self.width * self.height
```

مشكلة:

```python
r.width = 10
print(r.area)   # ❌ قيمة خاطئة
```

لكن مع property:

* دائمًا صحيحة
* لا نحتاج تحديث يدوي

---

# 9️⃣ مثال من الكورس (Money)

```python
class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    @property
    def amount(self):
        return self.__amount

    @property
    def currency(self):
        return self.__currency
```

هنا:

* `amount` و `currency` **public interface**
* القيم الحقيقية مخفية
* لا تعديل مباشر
* Encapsulation ✔️

---

# 🔟 ربط المفاهيم مع بعض

| المفهوم            | ماذا يفعل              |
| ------------------ | ---------------------- |
| Private attribute  | يخفي البيانات          |
| Property (getter)  | قراءة آمنة             |
| Setter             | تعديل مع شروط          |
| Computed attribute | قيمة محسوبة بدون تخزين |

---

# 🧠 القاعدة الذهبية (مهمة جدًا للكورس)

> ❝ إذا احتجت قراءة قيمة → property
> إذا احتجت تحكم عند التعديل → setter
> إذا كانت القيمة ناتجة عن حساب → computed attribute ❞

---

## سؤال أخير للتأكد من الفهم 👇

لماذا نفضل `@property` بدل كتابة `get_x()` في بايثون؟
(فكر من ناحية **واجهة الاستخدام** وليس التنفيذ)
