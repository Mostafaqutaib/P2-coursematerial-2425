# الاختبارات المعلمة (Parametrized Tests)

في التمرين السابق، طلبنا منك كتابة اختبارات لدالة `overlapping_intervals` كسلسلة من عبارات `assert` في دالة اختبار واحدة:

```python
def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
    # ...
```

ذكرنا سابقاً كيف أن الاختبار يجب ideally أن يفشل لسبب واحد فقط. هنا however، قمنا بحزم عدة عبارات `assert` في اختبار واحد، كل منها يمكن أن يكون سبباً للفشل.

تخيل أن لدينا عشرة مثل هذه العبارات `assert` في اختبار واحد. إذا فشلت أول `assert`، فسوف تطرح استثناء، مما يتسبب في مقاطعة الاختبار وتخطي العبارات `assert` المتبقية. هذا يتخلص من معلومات قيمة محتملة: قد يكون من المثير للاهتمام معرفة ما إذا كانت العمليات الاختيارية الأخرى ستفشل أم ستمر.

يمكننا بسهولة معالجة هذا عن طريق وضع كل `assert` في اختبار خاص به:

```python
def test_overlapping_intervals1():
    assert overlapping_intervals((1, 5), (3, 6))

def test_overlapping_intervals2():
    assert not overlapping_intervals((2, 5), (7, 10))

# ...
```

## تحسين التقارير

يولد `pytest` ملخصاً بعد تشغيل جميع الاختبارات. إنه يمنحك نظرة عامة جميلة عن الاختبارات التي فشلت. دعنا نشغل الاختبارات مع تنفيذ خاطئ لـ `overlapping_intervals`:

[تم حذف التقارير التفصيلية]
```
============================== short test summary info ==============================
FAILED tests.py::test_overlapping_intervals1 - assert False
FAILED tests.py::test_overlapping_intervals2 - assert not True
```

كما ترى، الملخص ليس مفيداً جداً. قد يقترح بعض الأشخاص أن نعطي الاختبارات أسماء أفضل:

```python
def test_overlapping_intervals_1_5_overlaps_with_3_6():
    assert overlapping_intervals((1, 5), (3, 6))

def test_overlapping_intervals_2_5_does_not_overlap_with_7_10():
    assert not overlapping_intervals((2, 5), (7, 10))

# ...
```

بهذه الطريقة، عند تشغيل الاختبارات، تحصل على نظرة عامة أفضل عما فشل:

```
$ pytest
[تم حذف التقارير التفصيلية]
============================== short test summary info ==============================
FAILED tests.py::test_overlapping_intervals_1_5_overlaps_with_3_6 - assert False
FAILED tests.py::test_overlapping_intervals_2_5_does_not_overlap_with_7_10 - assert not True
```

هناك بعض العيوب في هذا النهج though:

- تفرض بايثون (مثل معظم اللغات الأخرى) العديد من القيود على كيفية تسمية دوالنا. على سبيل المثال، سيكون اسم اختبار `test that interval (1, 5) overlaps with interval (3, 6)` أكثر قابلية للقراءة، لكنه غير مسموح بسبب احتوائه على مسافات، أقواس وفواصل.
- نضيف التكرار: كل من الاختبار واسم الاختبار يحتويان على نفس المعلومات حول حدود الفترات.
- يمنعنا من معلمة اختباراتنا (انظر لاحقاً.)

نهج أفضل would be equip الـ `assert` برسالة خطأ:

```python
def test_overlapping_intervals1():
    assert overlapping_intervals((1, 5), (3, 6)), "الفترة (1, 5) تتداخل مع الفترة (3, 6)"

def test_overlapping_intervals2():
    assert not overlapping_intervals((2, 5), (7, 10)), "الفترة (2, 5) لا تتداخل مع الفترة (7, 10)"
```

تشغيل الاختبارات then gives

```
$ pytest
[تم حذف التقارير التفصيلية]
============================== short test summary info ==============================
FAILED tests.py::test_overlapping_intervals1 - AssertionError: الفترة (1, 5) تتداخل مع الفترة (3, 6)
FAILED tests.py::test_overlapping_intervals2 - AssertionError: الفترة (2, 5) لا تتداخل مع الفترة (7, 10)
```

هذا لم يخلصنا من التكرار though. لحسن الحظ، هذا سهل الإصلاح:

```python
def test_overlapping_intervals1():
    interval1 = (1, 5)
    interval2 = (3, 6)
    assert overlapping_intervals(interval1, interval2), f"الفترة {interval1} تتداخل مع الفترة {interval2}"

def test_overlapping_intervals2():
    interval1 = (2, 5)
    interval2 = (7, 10)
    assert not overlapping_intervals(interval1, interval2), f"الفترة {interval1} لا تتداخل مع الفترة {interval2}"
```

## @Parametrize

كتابة الاختبارات certainly seem to involve الكثير من النسخ واللصق: الاختبارات الموضحة أعلاه متطابقة تقريباً. نود جعل الاختبارات more compact. Ideally، نود only have to write down ما هو essential لكل حالة اختبار وليس لدينا أي نوع من boilerplate code.

يسمح لنا Pytest بمعلمة الاختبارات. دعنا نفعل هذا خطوة بخطوة.

أولاً، لاحظ متغيري `interval1` و `interval2` المحليين اللذين أدخلناهما لتجنب التكرار. دعنا نحول these into parameters:

```python
def test_overlapping_intervals1(interval1, interval2):
    assert overlapping_intervals(interval1, interval2), f"الفترة {interval1} تتداخل مع الفترة {interval2}"
```

حسناً، انخفض حجم الاختبار إلى النصف، لكن كيف يعرف الاختبار ما هي القيم التي يجب استخدامها لـ `interval1` و `interval2`؟ يمكننا إعادة تقديم these as follows:

```python
import pytest

@pytest.mark.parametrize('interval1, interval2', [
    ((1, 5), (3, 6)),
])
def test_overlapping_intervals1(interval1, interval2):
    assert overlapping_intervals(interval1, interval2), f"الفترة {interval1} تتداخل مع الفترة {interval2}"
```

يأخذ decorator `parametrize` معاملين:

- الأول هو سلسلة تحتوي على أسماء المعلمات. يجب أن تكون these must be the same as معلمات دالة الاختبار. سيتضح لاحقاً why this is necessary.
- الثاني هو قائمة tuples من القيم ليتم تعيينها إلى المعلمات. في المثال، نخبر Pytest بتعيين `(1, 5)` إلى `interval1` و `(3, 6)` إلى `interval2`.

نحن لسنا مقيدين بـ only one tuple of values:

```python
import pytest

@pytest.mark.parametrize('interval1, interval2', [
    ((1, 5), (3, 6)),
    ((1, 5), (5, 6)),
    ((1, 10), (3, 6)),
    ((6, 8), (3, 6)),
    ((5, 7), (4, 8)),
])
def test_overlapping_intervals1(interval1, interval2):
    assert overlapping_intervals(interval1, interval2), f"الفترة {interval1} تتداخل مع الفترة {interval2}"
```

هذا يولد خمسة اختبارات لك. تشغيل pytest produces

```
$ pytest
[تم حذف التقارير التفصيلية]
============================== short test summary info ==============================
FAILED tests.py::test_overlapping_intervals1[interval10-interval20] - AssertionError: الفترة (1, 5) تتداخل مع الفترة (3, 6)
FAILED tests.py::test_overlapping_intervals1[interval11-interval21] - AssertionError: الفترة (1, 5) تتداخل مع الفترة (5, 6)
FAILED tests.py::test_overlapping_intervals1[interval12-interval22] - AssertionError: الفترة (1, 10) تتداخل مع الفترة (3, 6)
FAILED tests.py::test_overlapping_intervals1[interval13-interval23] - AssertionError: الفترة (6, 8) تتداخل مع الفترة (3, 6)
FAILED tests.py::test_overlapping_intervals1[interval14-interval24] - AssertionError: الفترة (5, 7) تتداخل مع الفترة (4, 8)
```

دعنا يكون لدينا اختباران معلمان: واحد للفترات المتداخلة، وواحد للفترات غير المتداخلة:

```python
import pytest

@pytest.mark.parametrize('interval1, interval2', [
    ((1, 5), (3, 6)),
    ((1, 5), (5, 6)),
    ((1, 10), (3, 6)),
    ((6, 8), (3, 6)),
    ((5, 7), (4, 8)),
])
def test_overlapping_intervals(interval1, interval2):
    assert overlapping_intervals(interval1, interval2), f"الفترة {interval1} تتداخل مع الفترة {interval2}"

@pytest.mark.parametrize('interval1, interval2', [
    ((1, 2), (3, 4)),
    ((1, 5), (5, 1)),
    ((8, 9), (6, 7)),
    ((8, 9), (6, 7)),
])
def test_nonoverlapping_intervals(interval1, interval2):
    assert not overlapping_intervals(interval1, interval2), f"الفترة {interval1} لا تتداخل مع الفترة {interval2}"
```

# التقريب (Approx)

في ملف `mystatistics.py`، اكتب دالة `average(ns)` التي، عند إعطائها قائمة `ns` من الأرقام، تحسب المتوسط. المتوسط يساوي مجموع `ns` مقسوماً على طول `ns`.

في `tests.py`، اكتب اختباراً معلماً بمعلمتين: `ns` و `expected`. تأكد من تضمين الحالة `([0.1, 0.1, 0.1], 0.1)`.

شغل اختباراتك. نتوقع أن تفشل.

## النقاط العائمة (Floating Points)

يمكن أن تكون الأرقام الحقيقية طويلة بشكل لا نهائي: فكر في π، أو حتى مجرد `1/3 = 0.333333...`. لا تستطيع الآلة تحمل تمثيل أرقام طويلة بشكل لا نهائي، لذا تقطعها بعد عدد معين من الأرقام. However، هذا يتسبب في فقدان الدقة.

لنفترض، على سبيل المثال، أن الآلة تعمل بالنظام العشري وأنها يمكنها تخزين 3 أرقام فقط. نتوقع أن `1 / 3 * 3` تساوي 1.

إذا قسمنا 1 على 3، يجب أن نحصل على `0.33333333...` لكن سيتم قطعها بعد 3 أرقام: `0.333`. عندما نضرب هذا في 3، نحصل على `0.999`، which is not equal to 1.

هذه الأنواع من أخطاء التقريب happen all the time. في التطبيقات التي تتضمن العديد من الحسابات العددية (مثل، محركات الفيزياء في الألعاب)، من crucial أن نأخذ هذه الأخطاء في الاعتبار. هناك even a separate field of mathematics that specializes in إيجاد طرق لإبقاء تأثير أخطاء التقريب عند الحد الأدنى.

يعمل الكمبيوتر بالنظام الثنائي. القيم التي تبدو جيدة في النظام العشري (مثل `0.1`) لا يمكن تمثيلها exactly في النظام الثنائي. على سبيل المثال،

```python
>>> sum([0.1] * 10)
0.9999999999999999

>>> sum([0.1] * 10) == 1
False

>>> 1 - sum([0.1] * 10)
1.1102230246251565e-16
```

لذا، إذا أردنا كتابة اختبارات تتضمن أرقام النقاط العائمة،我们必须 take into account أن النتائج قد تكون غير دقيقة قليلاً. لحسن الحظ، هذا easy to solve. إذا توقعنا قيمة متوقعة محددة `expected` ولدينا نتيجة معينة `actual`:

```python
# مزعج: نتوقع نتائج exact
assert expected == actual

# يسمح بهامش خطأ
assert abs(expected - actual) < 0.0001
```

`abs(expected - actual) < 0.0001` تعبر عن أن `expected` و `actual` يجب أن يكونا "متساويين تقريباً": نحن نتسامح مع الاختلافات حتى `0.0001`.

تقدم Pytest دالة مساعدة لتجعل هذا even easier:

```python
from pytest import approx

assert approx(expected) == actual
```

إذا لزم الأمر، يمكنك تحديد tolerance مخصص:

```python
assert approx(expected, abs=0.1) == actual
```

هنا نسمح بهامش خطأ كبير: يمكن أن يختلف `expected` و `actual` حتى `0.1`. This might come in handy للاختبارات، حيث typically not interested في specifying values of up to 7 digits:

```python
# آه، الكثير من الأرقام
assert approx(3.14159265) == pi

# جيد enough لأغراضنا
assert approx(3.14, abs=0.01) == pi
```

الآن، اعتمد على `approx` لجعل اختباراتك تمر. اذهب لدقة `abs=0.01`.