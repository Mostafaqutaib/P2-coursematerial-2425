تمام — خلّينا نكمّل التمرين **Counting birds** من مكانك بالضبط، وبنفس أسلوب الكورس (Pandas + Matplotlib)، مع كود “جاهز نسخ/لصق” + شرح ليه كل سطر موجود.

> ملاحظة صغيرة: عندك جزء الحمام (Pigeons) والجزء العصافير (Sparrows) مكتوبين، لكن **مش مطابقين للمواصفات**:

* رسم الحمام لازم `figsize=(10,6)` + خط أزرق كامل + `linewidth=2` + `markersize=8` + legend
* رسم العصافير لازم `linestyle=':'` + لون أخضر + marker `>` + حواف marker حمراء بعرض 1 **وكمان لازم يظهر معاه رسم الحمام بنفس الشكل في نفس الرسم**.

أنا تحت بديك حل مرتب لكل جزء: Part 1 → Part 4.

---

## ✅ تجهيز البيانات (هذا عندك صح)

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {
    'year': ['2020', '2021', '2022', '2023', '2024'],
    'Pigeons': [33, 52, 26, 40, 38],
    'Sparrows': [54, 48, 66, 59, 61],
    'others': [104, 98, 88, 92, 101]
}

df = pd.DataFrame(data)
df = df.set_index('year')
df.index.name = None
df
```

---

# ✅ Counting birds — Part 1

## 1) Plotting the pigeon count (مطابق للمواصفات 100%)

المطلوب:

* Line graph
* `figsize=(10,6)`
* full blue line + circle marker
* `linewidth=2`, `markersize=8`
* labels + legend + title + grid

```python
plt.figure(figsize=(10, 6))

plt.plot(
    df.index, df['Pigeons'],
    linestyle='-',
    color='blue',
    marker='o',
    linewidth=2,
    markersize=8,
    label='Pigeons'
)

plt.title('Pigeons counted per year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.grid(True)
plt.legend()
plt.show()
```

ليش استخدمنا `plt.plot` بدل `df['Pigeons'].plot`؟
لأنه أسهل وأوضح بالتحكم بالمواصفات الدقيقة (line/marker/legend…).

---

## 2) Plotting the sparrow count + ensure pigeon plot is incorporated

المطلوب:

* Line graph
* sparrows dotted `':'`
* color Green
* marker triangle right `>`
* marker edge red width 1
* **لازم يظهر رسم الحمام في نفس الشكل**

يعني: نفتح figure جديدة، ونرسم **Pigeons** ثم **Sparrows** على نفس الـ axes.

```python
plt.figure(figsize=(10, 6))

# 1) Pigeons (نفس مواصفات الجزء السابق)
plt.plot(
    df.index, df['Pigeons'],
    linestyle='-',
    color='blue',
    marker='o',
    linewidth=2,
    markersize=8,
    label='Pigeons'
)

# 2) Sparrows (حسب المواصفات)
plt.plot(
    df.index, df['Sparrows'],
    linestyle=':',              # dotted
    color='green',
    marker='>',                 # triangle right
    linewidth=2,
    markersize=8,
    markeredgecolor='red',      # red edge
    markeredgewidth=1,          # edge width 1
    label='Sparrows'
)

plt.title('Pigeons and Sparrows counted per year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.grid(True)
plt.legend()
plt.show()
```

> غلط شائع: استخدام `marker='.'` (نقطة) — هذا لا يحقق شرط “مثلث لليمين”.

---

## 3) Plotting the other birds (Add a line for others)

المطلوب: تضيف خط ثالث “others” بأي style تختاره، لكن الأفضل نخليه واضح.

```python
plt.figure(figsize=(10, 6))

# Pigeons
plt.plot(
    df.index, df['Pigeons'],
    linestyle='-',
    color='blue',
    marker='o',
    linewidth=2,
    markersize=8,
    label='Pigeons'
)

# Sparrows
plt.plot(
    df.index, df['Sparrows'],
    linestyle=':',
    color='green',
    marker='>',
    linewidth=2,
    markersize=8,
    markeredgecolor='red',
    markeredgewidth=1,
    label='Sparrows'
)

# Others (ستايل من اختيارنا)
plt.plot(
    df.index, df['others'],
    linestyle='--',
    color='orange',
    marker='s',
    linewidth=2,
    markersize=7,
    label='Others'
)

plt.title('Bird counts per year (by species)')
plt.xlabel('Year')
plt.ylabel('Count')
plt.grid(True)
plt.legend()
plt.show()
```

---

# ✅ Counting birds — Part 2

## 4) Add total column (إضافة مجموع الطيور لكل سنة)

المطلوب: تضيف عمود في DataFrame اسمه total.

أفضل طريقة: نجمع أعمدة الأنواع فقط:

```python
df['total'] = df[['Pigeons', 'Sparrows', 'others']].sum(axis=1)
df
```

---

## 5) Add barplot (total) on top of the existing plots

المطلوب:

* بار بلوت للـ total **فوق نفس الرسم** اللي فيه خطوط الأنواع
* Bar width = 0.4
* Bar color = purple
* labels + legend

هنا مهم نستخدم **محور x رقمي** عشان البارات تنضبط (لأن index عندك Strings).

```python
x = np.arange(len(df.index))  # [0,1,2,3,4]

plt.figure(figsize=(10, 6))

# Bars for total (خليها شفافة شوي عشان ما تغطي الخطوط)
plt.bar(
    x, df['total'],
    width=0.4,
    color='purple',
    alpha=0.25,
    label='Total'
)

# Lines for each species
plt.plot(x, df['Pigeons'], linestyle='-', color='blue', marker='o',
         linewidth=2, markersize=8, label='Pigeons')

plt.plot(x, df['Sparrows'], linestyle=':', color='green', marker='>',
         linewidth=2, markersize=8, markeredgecolor='red', markeredgewidth=1,
         label='Sparrows')

plt.plot(x, df['others'], linestyle='--', color='orange', marker='s',
         linewidth=2, markersize=7, label='Others')

# X ticks لازم ترجعها لسنوات
plt.xticks(x, df.index)

plt.title('Bird counts per year (species + total)')
plt.xlabel('Year')
plt.ylabel('Count')
plt.grid(True)
plt.legend()
plt.show()
```

ليش عملنا `alpha=0.25`؟
عشان البار البنفسجي ما يغطّي خطوط الأنواع وتضل الرسمة مقروءة.

---

# ✅ Counting birds — Part 3

## 6) Bar chart (total) + Stacked bar chart (species)

المطلوب:

* عرض البيانات باستخدام:

  * **stacked bar** (Pigeons/Sparrows/others) على **اليسار**
  * **bar chart للـ total** على **اليمين**
* “Make it informative (and pretty)”

إذن نستخدم subplots (1 صف، 2 أعمدة):

```python
fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

# Left: stacked bar for species
df[['Pigeons', 'Sparrows', 'others']].plot(
    kind='bar',
    stacked=True,
    ax=ax_left
)
ax_left.set_title('Stacked counts by species')
ax_left.set_xlabel('Year')
ax_left.set_ylabel('Count')
ax_left.grid(True, axis='y')

# Right: bar chart for total (purple)
ax_right.bar(df.index, df['total'], color='purple', width=0.6)
ax_right.set_title('Total birds per year')
ax_right.set_xlabel('Year')
ax_right.grid(True, axis='y')

# تحسين شكل x labels
ax_left.tick_params(axis='x', rotation=0)
ax_right.tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.show()
```

> لاحظ: المطلوب “total على اليمين” — وهذا اللي عملناه بالـ `ax_right`.

---

# ✅ Counting birds — Part 4

## 7) Grouped bar chart

المطلوب:

* grouped bar chart
* **Pigeons + Sparrows على يسار الـ x-tick**
* **others + total على يمين الـ x-tick**
* bars لا تتداخل

هذا يعني: لكل سنة (x-tick)، عندك 4 بارات موزعين:

* يسار: Pigeons, Sparrows
* يمين: others, total

نستخدم عرض صغير (width) ونزحزح كل بار بمقدار:

```python
x = np.arange(len(df.index))
width = 0.18  # عرض صغير عشان 4 بارات ما يتداخلوا

plt.figure(figsize=(10, 6))

# Left of tick: pigeons & sparrows
plt.bar(x - 1.5*width, df['Pigeons'], width, label='Pigeons')
plt.bar(x - 0.5*width, df['Sparrows'], width, label='Sparrows')

# Right of tick: others & total
plt.bar(x + 0.5*width, df['others'], width, label='Others')
plt.bar(x + 1.5*width, df['total'], width, label='Total')

plt.xticks(x, df.index)
plt.title('Bird counts per year (Grouped bar chart)')
plt.xlabel('Year')
plt.ylabel('Count')
plt.grid(True, axis='y')
plt.legend()
plt.show()
```

كيف تأكدنا أنها “left vs right”؟

* أي شيء سالب من `x` (مثل `x - 1.5*width`) يطلع **يسار** الـ tick
* وأي شيء موجب من `x` (مثل `x + 1.5*width`) يطلع **يمين** الـ tick

---

## ✅ تلخيص سريع لما صار

* Part 1: رسمنا خطوط للأنواع مع styling المطلوب + دمج pigeon مع sparrow
* Part 2: أضفنا `total` ورسمناه كـ bar فوق نفس خطوط الأنواع
* Part 3: سوينا شكلين جنب بعض: stacked يسار + total يمين
* Part 4: grouped bar chart مع توزيع يسار/يمين بدون تداخل

إذا بدك، ابعتلي **سكرينشوت للـ output المطلوب** أو المثال اللي حاطينه بالتمرين (إن وجد) وأنا أخلي شكل الرسوم مطابق تمامًا (مثل حجم الخطوط، ترتيب legend، أو ألوان معيّنة).
