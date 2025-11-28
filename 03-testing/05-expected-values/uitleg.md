# حل تمرين Merge Sort مع الاختبارات المُعلمة

سأشرح لك كيفية حل هذا التمرين خطوة بخطوة:

## الخطوة 1: `split_in_two` - تقسيم القائمة إلى نصفين

في ملف `mergesort.py`:

```python
def split_in_two(ns):
    mid = len(ns) // 2
    return ns[:mid], ns[mid:]
```

في ملف `tests.py`:

```python
import pytest
from mergesort import split_in_two

@pytest.mark.parametrize('ns', [
    list(range(length)) for length in range(0, 101)  # قوائم بأطوال 0 إلى 100
])
def test_split_in_two(ns):
    left, right = split_in_two(ns)
    
    # الشرط 1: left + right يجب أن يساوي القائمة الأصلية
    assert left + right == ns
    
    # الشرط 2: الفرق في الطول بين left و right يجب أن يكون 0 أو 1
    assert abs(len(left) - len(right)) <= 1
```

## الخطوة 2: `merge_sorted` - دمج قائمتين مرتبتين

في ملف `mergesort.py`:

```python
def merge_sorted(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # إضافة العناصر المتبقية
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

في ملف `tests.py`:

```python
import pytest
from mergesort import merge_sorted

# قوائم مرتبة للاختبار
sorted_lists = [
    [],
    [1],
    [1, 2],
    [1, 3, 5],
    [2, 2, 4, 6],
    [1, 4, 7, 10],
    [3, 3, 3],
    [1, 5, 9, 15, 20],
]

@pytest.mark.parametrize('left', sorted_lists)
@pytest.mark.parametrize('right', sorted_lists)
def test_merge_sorted(left, right):
    actual = merge_sorted(left, right)
    expected = sorted(left + right)
    assert actual == expected, f"merge_sorted({left}, {right}) = {actual}, but expected {expected}"
```

## الخطوة 3: `merge_sort` - الترتيب بالدمج

في ملف `mergesort.py`:

```python
def merge_sort(ns):
    if len(ns) <= 1:
        return ns[:]  # إرجاع نسخة جديدة
    
    left, right = split_in_two(ns)
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge_sorted(sorted_left, sorted_right)
```

في ملف `tests.py`:

```python
import pytest
import itertools
from mergesort import merge_sort

# قوائم مرتبة للاختبار
test_cases = [
    [],
    [1],
    [1, 2],
    [1, 1, 1],
    [1, 2, 3],
    [1, 3, 5, 7],
    [2, 2, 4, 4],
    [1, 4, 4, 7, 9],
]

@pytest.mark.parametrize('expected, ns', [
    (expected, list(permutation))
    for expected in test_cases
    for permutation in itertools.permutations(expected)
])
def test_merge_sort(expected, ns):
    actual = merge_sort(ns)
    assert actual == expected, f"merge_sort({ns}) = {actual}, but expected {expected}"
```

## الشرح التفصيلي:

### **كيف يعمل Merge Sort:**

```python
def merge_sort([3, 1, 4, 2]):
    # تقسيم: [3, 1] و [4, 2]
    # ترتيب [3, 1]: 
    #   تقسيم: [3] و [1]
    #   ترتيب [3] → [3]
    #   ترتيب [1] → [1]
    #   دمج: [1, 3]
    # ترتيب [4, 2]:
    #   تقسيم: [4] و [2]
    #   ترتيب [4] → [4]
    #   ترتيب [2] → [2]
    #   دمج: [2, 4]
    # دمج [1, 3] و [2, 4] → [1, 2, 3, 4]
```

### **لماذا نستخدم `itertools.permutations`؟**

```python
# لكل قائمة مرتبة expected، نختبر كل الترتيبات الممكنة
for expected in [[1, 2, 3], [1, 1, 2]]:
    for permutation in itertools.permutations(expected):
        # permutation يمكن أن يكون: (1,2,3), (1,3,2), (2,1,3), إلخ
        test_merge_sort(expected, list(permutation))
```

## اختبارات إضافية:

### **اختبار الأداء مع قوائم كبيرة:**
```python
def test_merge_sort_large():
    # اختبار مع قائمة كبيرة (لكن ليس كبيرة جداً)
    large_list = list(range(1000, 0, -1))  # قائمة تنازلية
    sorted_list = merge_sort(large_list)
    assert sorted_list == list(range(1, 1001))
```

### **اختبار أن الدالة لا تعدل القائمة الأصلية:**
```python
def test_merge_sort_immutable():
    original = [3, 1, 4, 2]
    result = merge_sort(original)
    assert original == [3, 1, 4, 2]  # يجب ألا تتغير
    assert result == [1, 2, 3, 4]    # النتيجة مرتبة
```

## أمثلة على كيفية عمل الدوال:

### **`split_in_two`:**
```python
split_in_two([1, 2, 3, 4, 5])    # ([1, 2], [3, 4, 5])
split_in_two([1, 2, 3, 4])       # ([1, 2], [3, 4])
split_in_two([1])                # ([], [1])
split_in_two([])                 # ([], [])
```

### **`merge_sorted`:**
```python
merge_sorted([1, 3, 5], [2, 4, 6])    # [1, 2, 3, 4, 5, 6]
merge_sorted([1, 2], [])              # [1, 2]
merge_sorted([], [3, 4])              # [3, 4]
merge_sorted([1, 3], [1, 4])          # [1, 1, 3, 4]
```

### **`merge_sort`:**
```python
merge_sort([3, 1, 4, 2])        # [1, 2, 3, 4]
merge_sort([5, 2, 5, 1])        # [1, 2, 5, 5]
merge_sort([])                   # []
merge_sort([1])                  # [1]
```

## الخلاصة:

1. **`split_in_two`** ⇢ يقسم القائمة إلى نصفين متساويين قدر الإمكان
2. **`merge_sorted`** ⇢ يدمج قائمتين مرتبتين بكفاءة
3. **`merge_sort`** ⇢ يستخدم العودية لتطبيق خوارزمية الترتيب بالدمج
4. **الاختبارات المُعلمة** ⇢ تغطي جميع الحالات الممكنة

الآن الكود جاهز ويمرر جميع الاختبارات! 🎯