ممتاز 👌
خلّينا نفسّر **الـ Static Methods** خطوة بخطوة، وبأسلوب الكورس بالضبط.

---

## 🧱 أولًا: الفكرة العامة

في العادة لما نكتب دوال داخل كلاس، يكون عندها `self`.
يعني لازم نُنشئ **object** (كائن) أول، بعدين نستدعي الدالة منه.

مثلاً:

```python
class Plumbus:
    def schleem(self):
        print("schleem called!")

p = Plumbus()
p.schleem()
```

هنا لازم نكتب `p = Plumbus()` قبل ما نستدعي `schleem()`.

لكن أحيانًا نحتاج **دالة داخل الكلاس** لا تستخدم `self`،
يعني لا تحتاج كائن أصلاً — هي منطق يخص الكلاس نفسه، مش الكائنات منه.

---

## ⚙️ ثانيًا: نستخدم @staticmethod

نكتبها هكذا:

```python
class Plumbus:
    @staticmethod
    def fleeb():
        print("fleeb called!")
```

لاحظ:

* ما في `self` في الدالة.
* نقدر نستدعيها بدون إنشاء object.

مثلاً:

```python
Plumbus.fleeb()   # ✅ ناديناها مباشرة من الكلاس
```

---

## 💡 الفكرة: “دالة تخص الكلاس، مش الكائن”

يعني:

* ما تعتمد على أي خصائص داخل object.
* بس مفيدة منطقيًا أن تنتمي إلى الكلاس.

---

## 🏭 ثالثًا: استخدامها كـ **Factory Functions**

الكورس يعطي مثال `Distance`:

```python
class Distance:
    def __init__(self, *, size_in_meters):
        self.size_in_meters = size_in_meters

    @staticmethod
    def meters(amount):
        return Distance(size_in_meters=amount)

    @staticmethod
    def millimeters(amount):
        return Distance(size_in_meters=amount / 1000)

    @staticmethod
    def miles(amount):
        return Distance(size_in_meters=amount * 1609.34)
```

الآن يمكنك تكتب:

```python
d1 = Distance.meters(10)        # 10 متر
d2 = Distance.miles(3)          # 3 أميال
```

يعني كل واحدة من هذه الدوال **تصنع object جاهز** من نفس الكلاس،
لكن بطريقة أكثر وضوحًا — بدل ما تكتب أرقام وتحسبها بنفسك.

---

## 📊 ملخّص الفروق

| نوع الدالة           | تحتاج `self`؟ | تُستدعى من؟         | الغرض                  |
| -------------------- | ------------- | ------------------- | ---------------------- |
| **عادية (instance)** | نعم           | من object           | تتعامل مع خصائص الكائن |
| **Static method**    | لا            | من الكلاس مباشرة    | منطق عام أو factory    |
| **Class method**     | تستخدم `cls`  | من الكلاس أو الكائن | تتعامل مع الكلاس نفسه  |

---

سؤال صغير للتأكد من الفهم 👇
لماذا لا نستخدم `self` داخل `@staticmethod`؟ ما الذي يعنيه غيابها؟
