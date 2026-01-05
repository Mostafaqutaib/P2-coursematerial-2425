تمام، خلّيني أشرح لك **هذا الجزء كامل (Datetime + apply)** خطوة خطوة، وبأسلوب الكورس نفسه، بدون قفزات 👌
اعتبره **تفكيك + فهم عميق** لما كتبته.

---

# 🕒 Datetime في Pandas

## 1️⃣ قراءة الملف ولماذا التاريخ مشكلة؟

```python
df = pd.read_csv("Google_Stock_Price.csv")
df.head(10)
```

Pandas قرأت الملف، لكن:

```python
df.info()
```

تلاحظ:

* أعمدة أرقام → `float` / `int`
* عمود التاريخ → `object`

❗ `object` يعني **نص (string)**
والمشكلة؟
👉 لا تقدر:

* تطرح تاريخين
* ترتّب حسب التاريخ صح
* تستخرج اليوم / الشهر / السنة

---

## 2️⃣ التأكد أن التاريخ String

```python
type(df["date"][0])
```

النتيجة:

```text
<class 'str'>
```

يعني فعلًا التاريخ نص.

---

## 3️⃣ تحويل التاريخ إلى Datetime

```python
df["date"] = pd.to_datetime(df["date"])
df.info()
```

الآن:

```text
datetime64[ns]
```

✔️ هذا هو النوع الصح في Pandas
يسمح بكل عمليات الوقت.

---

## 4️⃣ التعامل مع تاريخ واحد

```python
date = pd.to_datetime("01-05-2025")
```

Pandas **تفترض**:

* month-day-year (أمريكي 😅)

لذلك:

```python
print(date.day)    # 5
print(date.month)  # 1
```

❌ غلط بالنسبة لنا

---

## 5️⃣ حل المشكلة: format

```python
date = pd.to_datetime("01-05-2025", format="%d-%m-%Y")
```

الرموز المهمة:

* `%d` → day
* `%m` → month
* `%Y` → year (4 أرقام)
* `%y` → year (رقمين)

النتيجة الآن ✔️:

```python
date.day      # 1
date.month    # 5
date.year     # 2025
```

---

## 6️⃣ فرق بين تاريخين (Timedelta)

```python
date2 = pd.to_datetime("10-05-2025", dayfirst=True)
time_passed = date2 - date
```

النتيجة:

```text
9 days
```

وهذا كائن اسمه **Timedelta**

تقدر تسأل عنه:

```python
time_passed.days        # عدد الأيام
time_passed.components  # تفاصيل
time_passed.components.minutes
```

📌 مهم جدًا في:

* تحليل الزمن
* Stock data
* Logs

---

## 7️⃣ إنشاء تاريخ من أعمدة متعددة

عندك:

```python
data = {
    "day": ["01", "02", "03"],
    "month": ["01","01","01"],
    "year": ["2020", "2020","2020"]
}
```

Pandas ذكية 😎:

```python
date_df["date"] = pd.to_datetime(date_df)
```

تدمج day + month + year تلقائيًا.

---

# 🔁 apply() في Pandas (جزء مهم جدًا 🔥)

## 8️⃣ ما هي apply()؟

```python
df.apply(function, axis= ?)
```

* `axis=1` → تطبّق الدالة على **كل صف**
* `axis=0` → تطبّق الدالة على **كل عمود**

---

## 9️⃣ مثال الأسهم (Stock labels)

الدالة:

```python
def func(row):
    if row["open"] > row["close"]:
        if row["open"] == row["high"]:
            return "drop"
        else:
            return "downwards"
    elif row["open"] < row["close"]:
        if row["close"] ==  row["high"]:
            return "rise"
        else:
            return "upwards"
    else:
        return "steady"
```

تُطبّق على **كل صف**:

```python
df["label"] = df.apply(func, axis=1)
```

📌 هنا:

* `row` = صف كامل
* `row["open"]` = قيمة عمود open في هذا الصف

---

## 10️⃣ apply مع دالة بسيطة (sqrt)

```python
def sqrt(x):
    return x**(1/2)

sq.apply(sqrt)
```

* Pandas تطبّق الدالة على **كل عنصر**
* لأن `axis=0` افتراضيًا

---

## 11️⃣ apply مع sum

```python
sq.apply(sum, axis=1)
```

✔️ تجمع كل صف

```python
sq.apply(sum, axis=0)
```

✔️ تجمع كل عمود

---

# 🧠 خلاصة ذهنية (مهم تحفظها)

### Datetime

* لا تترك التاريخ `string`
* استخدم `pd.to_datetime`
* استخدم `format` لما يكون التاريخ غير أمريكي
* فرق تاريخين = `Timedelta`

### apply

* `axis=1` → صف
* `axis=0` → عمود
* قوية جدًا لكن **أبطأ من العمليات المباشرة**

---

إذا حاب:

* أربط **Datetime + Visualization**
* أشرح **متى لا تستخدم apply**
* أو أحوّل هذا المثال إلى **تمرين امتحاني**

احكي 👍
