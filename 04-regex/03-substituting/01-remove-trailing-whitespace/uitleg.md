تمام 👍
هذا تمرين **substitution كلاسيكي** في الكورس، ومقصوده يعلّمك شيئين مهمّين:

1. كيف نستخدم `re.sub`
2. كيف نتعامل مع **نهاية السطر** و **multiline mode**

خلّيني أفهّمك المطلوب خطوة خطوة، وبعدين أعطيك الحل النهائي بنفس ستايل Programmeren 2.

---

## 🎯 المطلوب باختصار

نكتب دالة:

```python
remove_trailing_whitespace(string)
```

* تشيل **المسافات (whitespace)** الموجودة **في نهاية كل سطر**
* بدون ما تأثر على المسافات داخل السطر
* وتشتغل على نص متعدد الأسطر

مثال:

### قبل:

```text
hello␣␣
world␣
test
```

### بعد:

```text
hello
world
test
```

(␣ = space)

---

## 🧠 كيف نفكّر بالـ regex؟

### 1️⃣ ما هو “trailing whitespace”؟

هو:

* مسافات (spaces أو tabs)
* **قبل نهاية السطر مباشرة**

---

### 2️⃣ كيف نعبّر عن “نهاية السطر” في regex؟

الرمز:

```
$
```

لكن ⚠️
بدون شيء إضافي، `$` يعني **نهاية النص كله**.

👉 عشان `$` يشتغل على **نهاية كل سطر**، لازم نفعل:

```python
re.MULTILINE
```

---

### 3️⃣ كيف نطابق المسافات؟

نقدر نستخدم:

* `\s` → أي whitespace
  أو (الأكثر شيوعًا في الكورس):
* `[ \t]` → space أو tab فقط

ونسمح بواحد أو أكثر:

```
[ \t]+
```

---

### 4️⃣ نركّب الـ regex كامل

```
[ \t]+$
```

يعني:

> واحد أو أكثر من spaces أو tabs
> **مباشرة قبل نهاية السطر**

---

## 🔁 استخدام `re.sub`

بما إننا نبي **نشيل** المسافات:

* replacement = `''` (string فارغ)

---

## ✅ الحل النهائي بأسلوب الكورس

```python
import re

def remove_trailing_whitespace(string: str) -> str:
    """Remove trailing whitespace at the end of each line."""
    return re.sub(r'[ \t]+$', '', string, flags=re.MULTILINE)
```

---

## ✔ مثال عملي

```python
text = "hello   \nworld\t\t\ntest\n"
print(remove_trailing_whitespace(text))
```

### الناتج:

```text
hello
world
test
```

---

## 🧠 نقاط مهمّة للاختبار

* `re.sub` → للاستبدال
* `''` → حذف
* `$` → نهاية السطر
* `re.MULTILINE` → خلي `$` يشتغل على **كل سطر**
* ما استخدمنا `^` لأننا نهتم بالنهاية فقط

---

لو تحبين، نقدر نكمّل بالتمرين اللي بعده (غالبًا يكون عن **إزالة التعليقات** أو **normalizing whitespace**) 👌
