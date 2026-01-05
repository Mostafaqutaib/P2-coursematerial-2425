أكيد 👍 خلّينا نشرح **مكتبة Pandas** بأسلوب بسيط وعملي، وبما يتماشى مع أسلوب كورس **Programmeren 2** اللي تشتغل عليه.

![Image](https://media.geeksforgeeks.org/wp-content/uploads/finallpandas.png)

![Image](https://storage.googleapis.com/lds-media/images/series-and-dataframe.width-1200.png)

![Image](https://jalammar.github.io/images/pandas-intro/0%20excel-to-pandas.png)

![Image](https://www.datacourses.com/wp-content/uploads/2019/08/Screen-Shot-2019-08-21-at-3.54.29-PM-1024x448.png)

---

## 📦 ما هي Pandas؟

**Pandas** هي مكتبة في **Python** تُستخدم للتعامل مع **البيانات** بسهولة:

* تنظيم البيانات (جداول)
* قراءة ملفات (CSV, Excel)
* تحليل البيانات
* تنظيف البيانات

تخيلها مثل **Excel** لكن داخل Python 💡

---

## 🧱 أهم شيئين في Pandas

### 1️⃣ Series

* تمثل **عمود واحد**
* تشبه list لكن أقوى

```python
import pandas as pd

ages = pd.Series([20, 21, 22])
print(ages)
```

🔹 تستخدم لما يكون عندك بيانات بسيطة بخط واحد.

---

### 2️⃣ DataFrame (الأهم 🔥)

* جدول كامل (صفوف + أعمدة)
* أكثر شي بتستخدمه في الكورس

```python
import pandas as pd

data = {
    'Name': ['Ali', 'Sara', 'Omar'],
    'Age': [20, 21, 22],
    'Grade': [85, 90, 78]
}

df = pd.DataFrame(data)
print(df)
```

📌 هذا يشبه جدول Excel:

* Name → عمود
* Ali → صف

---

## 📂 قراءة البيانات من ملف

غالبًا البيانات تكون في ملف:

```python
df = pd.read_csv('data.csv')
```

أول 5 صفوف:

```python
df.head()
```

آخر 5 صفوف:

```python
df.tail()
```

---

## 🔍 استكشاف البيانات

مهم جدًا قبل التحليل:

```python
df.shape      # عدد الصفوف والأعمدة
df.columns    # أسماء الأعمدة
df.info()     # معلومات عامة
df.describe() # إحصائيات (متوسط، أكبر، أصغر...)
```

---

## 🎯 اختيار بيانات معيّنة

### عمود واحد:

```python
df['Age']
```

### أكثر من عمود:

```python
df[['Name', 'Grade']]
```

### صفوف بشرط:

```python
df[df['Age'] > 20]
```

---

## ✏️ تعديل البيانات

### إضافة عمود:

```python
df['Passed'] = df['Grade'] >= 60
```

### تعديل قيمة:

```python
df.loc[0, 'Age'] = 25
```

---

## 🧹 تنظيف البيانات (شي مهم جدًا)

### حذف القيم الفارغة:

```python
df.dropna()
```

### استبدال القيم الفارغة:

```python
df.fillna(0)
```

---

## 🤝 ليش Pandas مهمة لك؟

بما إنك:

* تدرس برمجة
* اشتغلت على DataFrames بالكورس
* ممكن تفكر تستثمر معرفتك

👉 Pandas تُستخدم في:

* Data Analysis
* AI & Machine Learning
* Business Intelligence
* Automation
* مشاريع حقيقية 💼

---

إذا تحب:

* أشرح Pandas **بأمثلة من تمارين الكورس**
* أو أربطها بـ **NumPy**
* أو أشرح لك **خطأ معيّن صار معك**

قولّي وناخذها خطوة خطوة 👌
