````md
# 01-oo — أهم ما جاء في المجلد (حسب ملفات الكورس فعليًا)

> هذا الملخص مبني على محتوى مجلد `01-oo` داخل الكورس، مع ذكر **الفكرة التعليمية** و**النقاط اللي يركز عليها الكورس** + لمحة عن الـ assignments بدون حلول.

---

## خريطة المجلد (01-oo)
1. `01-classes-recap`
2. `02-encapsulation-recap` (+ assignment: Queue)
3. `03-properties` (+ assignments متعددة)
4. `04-operator-overloading` (+ Money, CircularBuffer)
5. `05-static-methods` (+ Duration)
6. `06-inheritance` (+ when-to-use, hierarchy, refactoring, assignments)
7. `07-abstract-classes` (+ abstract-methods puzzle, shapes)
8. `08-overriding` (+ shopping-list assignment)
9. `09-super` (+ shape assignment)

---

# 01) Classes recap — (01-classes-recap/01-class-recap.md)

## الفكرة الأساسية في هذا الملف
الكورس يرجّعك لمفاهيم الـ class عبر مثال واحد غني: **BankAccount**. الهدف: تشوف في مثال واحد:
- public vs private
- properties (getter/setter)
- methods عامة مثل deposit/withdraw
- helper method private
- حماية الـ internal state (حتى “التاريخ” يرجّعه copy)

## مثال BankAccount في الكورس (أهم ما فيه)
الكلاس يحتوي:
- `owner` **public attribute**
- `__balance` **private**
- `__transactions` **private**
- property: `balance` (getter + setter)
- methods: `deposit`, `withdraw`
- private helper: `__log_transaction`
- property: `transaction_history` ترجع `copy()` حتى ما تقدر تعدّل الأصل من خارج الكلاس

### الرسائل التعليمية الواضحة في الشرح
- **الـ private مو بس “إخفاء”**: هو طريقة لتجبر نفسك والآخرين يستخدمون واجهة صحيحة.
- `balance` ما ينكتب مباشرة… لازم يمر على setter لأن فيه **قواعد (balance لا يصير سالب)**.
- `deposit/withdraw` هي “العمليات المسموحة” لتغيير الرصيد.
- `transaction_history` ترجع نسخة:
  - لأن لو رجعت الليست الأصلية، أي شخص خارج الكلاس يقدر يضيف “عملية مزيفة” بدون ما تمر على منطق الكلاس.

> مثال موجود في نفس الملف يثبت الفكرة:
> حتى لو تعمل `my_bank_account.transaction_history.append(...)` ما يتغير التاريخ الحقيقي لأنك عدّلت نسخة.

## نقاط امتحانية محتملة (من طبيعة الشرح)
- لماذا `__transactions` private؟
- لماذا `transaction_history` يرجّع `copy()`؟
- الفرق بين method عامة و helper private مثل `__log_transaction`؟
- لماذا `balance` property بدل attribute عادي؟

---

# 02) Encapsulation recap — (02-encapsulation-recap/01-encapsulation.md + conclusions)

## 02.1 معنى Encapsulation حسب الكورس
الملف يعرّفها بصراحة كـ “black box”:
- تخبي التفاصيل الداخلية عشان مستخدم الكلاس ما يحتاج يعرف/يلمس كل شيء.

## 02.2 Public vs Private في OOP (فكرة الكورس)
- **Public**: شيء تريد المستخدم يعرفه ويتعامل معه مباشرة.
- **Private**: شيء لا يحتاجه المستخدم، فتبقيه مخفي لتبسيط “تعليمات الاستخدام”.

## 02.3 كيف في Python؟
الكورس يوضح:
- private في بايثون يكون عبر `__name` (double underscore).
- لكن بايثون “dynamic”، فالتطبيق **بالأغلب convention** (التزام بالمبدأ)، وليس “قفل حديدي” مثل بعض اللغات.

## مثال Wall (داخل الملف)
- `__height` private
- `get_height()` public للقراءة فقط
- محاولة `front_wall.__height = 10` “تسبب error” (الفكرة: لا تفتح الباب للتعديل المباشر)

---

## 02.4 Encapsulation conclusions — (03-encapsulation-conclusions.md)
هذا الملف يربط الفكرة بتمرين Queue ويعطي “منطق لماذا”
### المقارنة اللي يعتمدها الكورس
- `list` = عامة جدًا (تضيف/تحذف في أي مكان وتطلع أي عنصر)
- `Queue` = قائمة “مقيّدة” بقانون:
  - الإضافة فقط في النهاية
  - الإزالة فقط من البداية

### لماذا نغلف (Why encapsulate)؟
الكورس يعطي جواب واضح:
- عشان **تضمن** أن structure ما تُستخدم بطريقة غلط (خصوصًا لما الكود يكبر أو “مستقبلك أنت” ينسى قراراتك القديمة).
- هذا هو جوهر “منع الإساءة” بدل الاعتماد على حسن النية.

### قاعدة مهمة من الملف
> “الـ attribute ممكن يكون public إذا يقبل أي قيمة… لكن أول ما تحتاج تقييد/تحقق → خليه private ووفر وصول غير مباشر (methods/properties).”

---

## Assignment: Queue — (02-encapsulation-recap/assignments/02-queue/assignment.md)
الفكرة: Queue مثل طابور الساندويتش:
- `add(item)` يضيف آخر الطابور
- `next()` يشيل أول واحد
- `is_empty()`

والأهم: داخليًا تستخدم `list` (مثلاً `items`) **لكن لازم تكون private**
- لأن الكورس يعطي مثال “Mallory” اللي تدخل من البداية عبر `insert(0, ...)`
- فالحل المقصود: **إخفاء الليست** حتى ما تنكسر قواعد الطابور.

---

# 03) Properties — (03-properties)

هنا الكورس يبني properties تدريجيًا في 3 ملفات رئيسية:
1) readonly
2) computed attribute
3) setters

---

## 03.1 Readonly properties — (03-properties/01-readonly.md)
### المشكلة اللي يبني عليها الكورس
- عندك `Person(age)` لكن `age` public “غبي”: ممكن يصير سالب بالغلط → مشاكل في النظام.

### الفكرة: Properties = “intelligent attributes”
الكورس يقولها حرفيًا بالمعنى:
- property تقدر تتحكم في **ماذا يحدث عند القراءة والكتابة**.

### Uniform Access Principle (نقطة أساسية جدًا في هذا الملف)
الكورس يوضح: سواء `age` attribute أو property، الاستخدام **نفسه**:
```python
print(person.age)
person.age = 5
````

النتيجة التعليمية:

* تقدر “ترقي” attribute إلى property **بدون ما تغيّر كود العملاء (client code)**.
* وهذا يعتبر قاعدة مهمة: تغييرات محلية بدون “ramifications” عالمية.

### readonly عمليًا

* تخزن القيمة في private: `__age`
* تعمل getter فقط:

```python
@property
def age(self):
    return self.__age
```

* محاولة الكتابة تعطي:
  `AttributeError: can't set attribute`

---

## 03.2 Computed attribute — (03-properties/03-computed-attribute.md)

هنا الكورس يعطيك سبب قوي ليش property مش بس منع كتابة.

### سيناريو الكورس

* لو خزّنت `age` + `birthday` معًا → هذا **redundancy**
* وتقدر تقع في inconsistency.

الكورس يعطي مثال صريح:

> “Say we are in 2023”
> شخص: `age=18` و `birthday=1980` → هذا خطأ منطقي (العمر المفروض 42).

### الفكرة: احذف `__age` وخلي `age` computed

* تخزن فقط `__birthday`
* وعند قراءة `age` تحسبها من تاريخ اليوم:

```python
today = find_out_todays_date()
difference = today - self.__birthday
return difference.years
```

### الرسالة اللي يريدها الكورس

* **لا تخزن شيء يمكن اشتقاقه**.
* properties تسمح تخلي “شكل الاستخدام” كأنه attribute لكن داخليًا حساب.

---

## 03.3 Setters — (03-properties/05-setters.md)

هنا الكورس يعلّم:

* setter = ماذا يحدث عند الكتابة إلى property

### تطبيق على Person.age

* يسمح بالتغيير بشرط `age >= 0`
* وإذا سالب: `raise ValueError('age must be positive')`

### “Fixing the Constructor” (جزء مهم جدًا)

الكورس يكشف ثغرة:

* لو constructor يخزن `self.__age = age` مباشرة → ممكن تنشئ Person بعمر سالب بدون المرور بالتحقق.

الحل اللي يعطيه الكورس لتجنب تكرار المنطق:

* خلي constructor يمر عبر setter:

```python
def __init__(self, age):
    self.age = age  # Calls age's setter
```

### مصطلح الكورس: Gatekeeper

الكورس يقول الفكرة بوضوح:

* اجعل setter هو **البوابة الوحيدة** التي تعرف القواعد وتسمح بالوصول لـ `__age`.
* الجميع (حتى constructor) لازم يمر من نفس البوابة.

---

## Assignments في properties (نظرة على المطلوب)

* **MusicalNote**: properties `name` و `pitch` readonly (لا تسمح بالكتابة).
* **BMICalculator**: property `bmi` computed + `category` computed حسب القيم (underweight/normal/overweight).
* **Time**: hours/minutes/seconds قابلة للقراءة والكتابة لكن محمية بـ properties ضد القيم غير الصحيحة + ملاحظة الكورس: “getter قبل setter”.
* **LengthConverter**: تحويل بين meter/feet/inch باستخدام private واحد `__distance_in_meter`، وكل getter/ setter يعمل conversion.

---

# 04) Operator Overloading — (04-operator-overloading/01-operator-overloading.md)

## الفكرة

الكورس يبدأ بفكرة:

* أنت تتعامل مع أعضاء الكلاس بنقطة `.`
  لكن أحيانًا تحتاج تعامل “لغوي” مثل `+` و `[]` و `len()`.

### مثال Point

* `p + q` يعطي TypeError لأن بايثون لا تعرف كيف تجمع نقطتين.
* الحل: تكتب `__add__`.

الكورس يشرح القاعدة:

> `obj1 + obj2` تتحول داخليًا إلى `obj1.__add__(obj2)`.

### جدول operators اللي ذكره الكورس

* `+` → `__add__`
* `-` → `__sub__`
* `*` → `__mul__`
* `/` → `__truediv__`
* `//` → `__floordiv__`
* `%` → `__mod__`
* `**` → `__pow__`

### قاعدة مهمّة جدًا في الملف

الكورس يحذر:

* دوال operator overloading لازم **ترجع object جديد**
* ولا تعدّل `self` (المثال يعطي “Wrong implementation, never do this!”)

---

## Assignments في operator overloading

### Money

* class فيها `amount` و `currency`
* جمع/طرح مسموح فقط لو العملة نفسها، غير ذلك: `RuntimeError("Mismatched currencies!")`
* ضرب Money * رقم (int/float) مسموح

### CircularBuffer

تمرين يجمع:

* `len(buffer)` عبر `__len__`
* `buffer[index]` عبر `__getitem__`
* وفكرة buffer يحتفظ فقط بآخر N عناصر (إذا زاد → يحذف الأقدم)

---

# 05) Static Methods — (05-static-methods/01-static-methods.md)

## فكرة الكورس

الكورس يوضح:

* عادةً methods تتبع objects (لازم تنشئ object ثم تستعمل method)
* لكن يوجد methods تتبع **class نفسها** عبر `@staticmethod`

مثال Plumbus:

* `fleeb()` static → تناديها: `Plumbus.fleeb()`
* ولا يوجد `self` لأن لا يوجد object.

> ملاحظة صريحة في الكورس: “لا تسميها class method، هذا شيء مختلف”.

## الاستخدام الأساسي اللي يركز عليه الكورس: Factory Functions

مثال `Distance`:

* الهدف: إنشاء object بطريقة توضح “الوحدة” (meters/miles...)
* الكورس يمر بتطوير الفكرة:

  * `Distance(10)` غير واضح (10 ماذا؟)
  * keyword-only args:

    ```python
    def __init__(self, *, size_in_meters):
    ```
  * ثم factory functions:
    `meters(amount)`, `miles(amount)` ...
  * ثم تجميعها داخل class كـ static methods:
    `Distance.miles(5)`

---

## Assignment: Duration

* static factory methods: `from_seconds`, `from_minutes`, `from_hours`
* readonly properties: `seconds`, `minutes`, `hours`
* سبب التسمية `from_unit`: لأنك لا تستطيع امتلاك static method و property بنفس الاسم داخل نفس class.

---

# 06) Inheritance — (06-inheritance)

## 06.1 الأساس (01-inheritance.md)

الكورس يسمي inheritance “Holy-grail” في OOP ويعطي:

* التعريف: child يرث properties/methods من parent
* الهدف: DRY (لا تكرر نفسك)
* syntax:

```python
class Cow(Animal):
    ...
```

* ويذكر استخدام `super()` للوصول لـ constructor الأب.

## 06.2 متى تستخدم inheritance؟ (03-when-to-use.md)

قاعدة الكورس الذهبية:

> استخدم inheritance فقط إذا كل child هو فعلاً نوع من parent.

ويكتبها بجملة:
`ALL CATS ARE ANIMALS BUT NOT ALL ANIMALS ARE CATS`

يعني: إذا العلاقة “is-a” غير صحيحة → inheritance غالبًا غلط.

## 06.3 Hierarchy (04-inheritance-hierarchy.md)

* ممكن شجرة عميقة (Cat ← Animal ← LivingThing)
* لكن تحذير: لا تورّث إذا كنت “تحتاج بعض” من الأب وتكره بعضه.
  هذا مؤشر أن inheritance اختيار غير صحيح.

## 06.4 Refactoring (06-refactoring.md) — من أقوى ملفات المجلد

الملف يبدأ بتكرار في functions ثم يوسع الفكرة لتكرار في classes (chess).

### مثال الشطرنج في الملف

* `Pawn` و `King` متشابهين جدًا:

  * position, color, validation, move...
  * الاختلاف الحقيقي فقط في `is_legal_move`

### المطلوب التعليمي

* استخرج المشترك في class جديد `ChessPiece`
* اجعل `Pawn(ChessPiece)` و `King(ChessPiece)`
* واترك لكل واحد فقط `is_legal_move` الخاصة به.

### الرسالة الأهم

* refactoring = تغييرات بنيوية بدون تغيير سلوك.
* اختبارات (tests) هي “pins” للسلوك: تعمل refactor صغير → تشغّل tests → تتأكد ما كسرت شيء.
* الكورس يحذر من “technical debt” لو تترك الكود شغال لكن سيئ البنية.

---

## Assignments في inheritance

* **Human / Archer**: Archer يرث Human، constructor يستدعي parent constructor ثم يضيف `__num_arrows`.
* **Crossbowman**: يرث Archer، يضيف `triple_shot()` + `use_arrows()` داخل Archer مع استثناء “not enough arrows”.
* **Chess**: هذا مرتبط مباشرة بملف refactoring (اقرأه قبل الحل).

---

# 07) Abstract Classes — (07-abstract-classes)

## 07.1 Abstract Methods (01-abstract-methods.md)

الكورس يرجع لمثال الشطرنج:

* `ChessPiece.move()` يعتمد على `is_legal_move()`
* لكن `is_legal_move` موجودة فقط في الأبناء.
* إذا أنشأت `ChessPiece` مباشرة → “غير منطقي” + ممكن `AttributeError`.

الحل:

* تجعل ChessPiece abstract:

```python
from abc import ABC, abstractmethod

class ChessPiece(ABC):
    @abstractmethod
    def is_legal_move(self, new_position):
        ...
```

> نقطة دقيقة ذكرها الكورس:
> الثلاث نقاط `...` ليست “اختصار” في الشرح، بل هي كود فعلي (literal ellipsis).

والنتيجة:

* محاولة إنشاء `ChessPiece` تعطي TypeError: لا يمكنك instantiate كلاس abstract فيه abstract method.

## 07.2 Abstract Properties (03-abstract-properties.md)

الكورس يوضح شكل abstract property:

```python
@property
@abstractmethod
def my_property(self):
    ...

@my_property.setter
@abstractmethod
def my_property(self, value):
    ...
```

ويذكر أن `@abstractproperty` deprecated.

---

## Assignments في abstract classes

* **abstract-methods puzzle**:

  * الكورس يعطي “قواعد” كأنها خوارزمية:

    * D = methods الموجودة (defined + inherited)
    * C = methods التي يناديها الكلاس على `self`
    * إذا C فيها شيء غير موجود في D → عندك “holes” → لازم abstract method + class becomes abstract.
* **shapes**:

  * اعمل parent `Shape` فيها “contract” (أعضاء abstract مشتركة) لـ Rectangle و Circle.
  * حتى لو ما فيه كود مشترك، الهدف ضمان أن كل shape يطبق نفس الواجهة.

---

# 08) Overriding — (08-overriding/01-overriding.md)

الكورس يشرح overriding ببساطة:

* إذا child عرّف method بنفس اسم الأب → هذا override.
* عند الاستدعاء على object من child → نسخة child “تفوز”.

مثال:

* Parent.method() → "Parent.method"
* Child.method() → "Child.method"

ملاحظة: الكورس يقول “overriding (not overwriting)”.

## Assignment: Shopping List

* تعريف `Item(name, price)`
* `Item.can_be_sold_to(customer)` كبداية يرجع True
* `AgeRestrictedItem(Item)` override `can_be_sold_to` (>= 18)
* `CountryRestrictedItem(Item)` ممنوع لـ Arstotzka
  (وهذا يجهزك مباشرة لملف 09-super اللي يناقش تعميم القيم بدل hardcode)

---

# 09) super — (09-super/01-super.md)

هذا الملف يعلمك “ليش super عمليًا” عبر مشكلة واقعية:

## مشكلة hardcoding

* AgeRestrictedItem hardcoded 18
* CountryRestrictedItem hardcoded Arstotzka
  → الكورس يقول: الأفضل تعميمها بباراميترات.

## المشكلة اللي تظهر عند تغيير **init**

عندما تكتب `__init__(minimum_age)` في child:

* أنت عملت override لـ `Item.__init__`
* فصارت attributes `name` و `price` غير موجودة → AttributeError عند الوصول لها.

## الحل الذي يركز عليه الكورس

* استقبل name, price, minimum_age في child constructor
* واستدعِ parent constructor عبر:

```python
super().__init__(name, price)
self.minimum_age = minimum_age
```

## الفكرة التعليمية

`super()` = الوصول للنسخة “القديمة/الأصلية” من method (مثل `__init__`) لكي:

* لا تكرر كود الأب
* وتبقي initialization متناسق

---

## Assignment: Shape (في 09-super/assignments/02-shape)

* موجود Shape abstract properties perimeter/area (حسب starter code)
* اكتب:

  * Rectangle (length/width readonly)
  * Square يرث Rectangle (side فقط + property Side ترجع نفس length/width)
  * Ellipse (major/minor readonly) + perimeter يرفع `NotImplementedError`
  * Circle يرث Ellipse (radius فقط + property radius)

الكورس يعطي جدول Formulae للتذكير (محيط/مساحة).

---

# “قواعد ذهبية” تجمع روح 01-oo (كما يظهر من الملفات)

1. **اخفِ الداخل** إذا عندك قواعد تريد فرضها (Encapsulation).
2. **لا تخزن شيء يمكن اشتقاقه** (Computed attribute لتجنب redundancy).
3. **اجعل بوابة واحدة للقواعد** (Setter Gatekeeper + constructor يمر عبره).
4. **Operator overloading يرجع object جديد** ولا يفسد self.
5. **Static methods = functions تنتمي للكلاس** وغالبًا factory واضحة.
6. **Inheritance فقط لعلاقة is-a الصحيحة** (Cats/Animals).
7. **Refactoring = بنية أفضل + نفس السلوك**، والـ tests حزام الأمان.
8. **Abstract class = عقد/قالب** يمنع instantiation غير المنطقي ويجبر الأبناء يكملوا “holes”.
9. **super() لتجنب تكرار كود الأب** خصوصًا مع overriding لـ `__init__`.

---

## سؤال واحد حتى أضبط لك المراجعة للامتحان بشكل أدق:

أي جزء في 01-oo أكثر شيء يضيعك: **properties** ولا **inheritance/abstract** ولا **operator overloading**؟

```
```
