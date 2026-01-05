تمام 👍 هذا تمرين **Queue** كلاسيكي في الكورس، ونقدر نشرحه + نترجمه لكود عملي بنفس الأسلوب اللي شفتَه في **Encapsulation**.

خلّينا نمشي بالترتيب 👇

---

## 🧠 أولًا: ما هي Queue؟

الـ **Queue** تعتمد مبدأ:

> **FIFO** = First In, First Out
> (أول واحد يدخل → أول واحد يطلع)

زي طابور السندويشات بالضبط:

* `add` → إضافة في **آخر** الطابور
* `next` → إزالة من **أول** الطابور

---

## 🔒 ثانيًا: شرط مهم (Encapsulation)

الكورس شدّد على نقطة مهمة جدًا:

> القائمة الداخلية **يجب أن تكون مخفية**

ليش؟
عشان ما يصير هذا:

```python
queue.items.insert(0, "Mallory")  # ❌ قطع الدور
```

إذًا:

* نستخدم **خاصية private**
* يعني نسمّيها `__items`

---

## ✅ الحل الكامل (بنفس أسلوب الكورس)

```python
class Queue:
    def __init__(self):
        # قائمة داخلية خاصة (private)
        self.__items = []

    def add(self, item):
        # نضيف في آخر القائمة
        self.__items.append(item)

    def next(self):
        # نزيل ونرجع أول عنصر
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        return self.__items.pop(0)

    def is_empty(self):
        return len(self.__items) == 0
```

---

## 🧩 شرح كل جزء ببساطة

### 1️⃣ `__init__`

```python
self.__items = []
```

* هذه هي **القائمة الحقيقية**
* مخفية (`__items`) → المستخدم لا يلمسها

---

### 2️⃣ `add(self, item)`

```python
self.__items.append(item)
```

* `append` = إضافة في **آخر** القائمة
* هذا يطابق: *الدخول لنهاية الطابور*

---

### 3️⃣ `next(self)`

```python
return self.__items.pop(0)
```

* `pop(0)` = حذف وإرجاع أول عنصر
* هذا يطابق: *خدمة أول شخص في الطابور*

ولو الطابور فاضي؟

```python
raise RuntimeError("Queue is empty")
```

→ سلوك واضح وآمن

---

### 4️⃣ `is_empty(self)`

```python
return len(self.__items) == 0
```

* ترجع `True` إذا الطابور فاضي
* ترجع `False` إذا فيه ناس

---

## 🧪 مثال استخدام (زي اللي في السؤال)

```python
queue = Queue()

queue.add('Alice')
queue.add('Bob')
queue.add('Charlie')

print(queue.next())  # Alice
print(queue.next())  # Bob
print(queue.next())  # Charlie
```

---

## 🔐 ماذا لو حاول أحد الغش؟

```python
queue.__items.insert(0, "Mallory")  # ❌ AttributeError
```

ليش؟

* لأن `__items` **خاص**
* هذا بالضبط معنى Encapsulation 💪

---

## 🧠 الخلاصة (احفظها):

* Queue = FIFO
* `add` → append
* `next` → pop(0)
* البيانات الداخلية **Private**
* المستخدم يتعامل فقط مع الواجهة (methods)

---

### سؤال صغير للتأكد 👇

ليش استخدمنا `__items` وليس `items`؟
(جواب سطر واحد يكفي)
