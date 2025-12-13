تمام 👍
هذا تمرين **sub مع replacement كدالة**، وهو بالضبط الامتداد الطبيعي للتمارين الثلاثة اللي قبلها. خلّينا نمشي **بنفس المنطق اللي شرحه الكورس حرفيًا**.

---

## 🎯 المطلوب

نكتب دالة:

```python
hide_email_addresses(string)
```

* تبحث عن **كل الإيميلات** داخل النص
* وتستبدل كل إيميل بـ:

  ```
  ***
  ```

  لكن **بعدد نجوم يساوي عدد حروف الإيميل نفسه**

مثال:

```text
"Contact me at test@mail.com"
```

الإيميل:

```
test@mail.com   (13 حرف)
```

الناتج:

```text
"Contact me at *************"
```

---

## 🧠 كيف نفكّر (حسب الكورس)

### 1️⃣ نستخدم `re.sub`

لكن بدل ما نمرّر string كـ replacement، نمرّر **دالة**.

### 2️⃣ الـ replacement function:

* تستقبل `match`
* `match.group()` يعطيك **الإيميل كامل**
* نحتاج نرجع:

  ```python
  '*' * len(match.group())
  ```

---

## 🧩 نحتاج regex للإيميل

نستخدم نفس النمط البسيط اللي استعملناه في تمارين scraping:

```regex
[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z0-9]+
```

(وهذا تمام لستايل الكورس)

---

## ✅ الحل النهائي بأسلوب Programmeren 2

```python
import re

def hide_email_addresses(string: str) -> str:
    """Replace all email addresses by asterisks of equal length."""
    
    def replace(match):
        email = match.group()
        return '*' * len(email)
    
    pattern = r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z0-9]+'
    return re.sub(pattern, replace, string)
```

---

## ✔ أمثلة

```python
hide_email_addresses("Mail me at test@mail.com")
# 'Mail me at *************'

hide_email_addresses("Emails: a@b.com and long.email123@test-site.org")
# 'Emails: ****** and ****************************'
```

---

## 🧠 خلاصة مهمّة (تلخيص الفصل كامل)

| الهدف               | الطريقة                             |
| ------------------- | ----------------------------------- |
| استبدال ثابت        | `re.sub(pattern, 'text', string)`   |
| استبدال ذكي         | `re.sub(pattern, function, string)` |
| الوصول للنص المطابق | `match.group()`                     |
| طول النص            | `len(match.group())`                |

هذا التمرين **يجمع كل اللي تعلمتيه**:

* regex
* capturing (ولو بدون groups هنا)
* `sub`
* replacement function

لو حابة نجرّبه مع **groups** أو نخليه **case-insensitive** أو نناقش حدود هذا regex، أنا جاهز 👌🔥
