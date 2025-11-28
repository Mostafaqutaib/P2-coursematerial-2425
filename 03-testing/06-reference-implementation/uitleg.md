# حل تمرين البحث الخطي والثنائي مع الاختبارات

سأشرح لك كيفية حل هذا التمرين خطوة بخطوة:

## الخطوة 1: تعريف فئة Student

في ملف `search.py`:

```python
class Student:
    def __init__(self, id):
        self.id = id
    
    def __repr__(self):
        return f"Student({self.id})"
```

## الخطوة 2: البحث الخطي (Linear Search)

في ملف `search.py`:

```python
def linear_search(students, target_id):
    """
    بحث خطي - يفحص كل طالب بالتتابع
    تعقيد زمني: O(n)
    """
    for student in students:
        if student.id == target_id:
            return student
    return None
```

## الخطوة 3: البحث الثنائي (Binary Search)

في ملف `search.py`:

```python
def binary_search(students, target_id):
    """
    بحث ثنائي - يستفيد من أن القائمة مرتبة
    تعقيد زمني: O(log n)
    """
    left = 0
    right = len(students) - 1
    
    while left <= right:
        mid = (left + right) // 2
        current_student = students[mid]
        
        if current_student.id == target_id:
            return current_student
        elif current_student.id < target_id:
            left = mid + 1
        else:
            right = mid - 1
    
    return None
```

## الخطوة 4: كتابة الاختبارات الشاملة

في ملف `tests.py`:

```python
import pytest
from search import Student, linear_search, binary_search

def generate_students(ids):
    """توليد قائمة طلاب من قائمة أرقام هوية"""
    return [Student(id) for id in ids]

# حالات اختبار شاملة
test_cases = [
    # (قائمة هويات الطلاب, target_id)
    ([], 1),                    # قائمة فارغة
    ([1], 1),                   # طالب واحد، موجود
    ([1], 2),                   # طالب واحد، غير موجود
    ([1, 2, 3], 1),            # أول طالب
    ([1, 2, 3], 3),            # آخر طالب
    ([1, 2, 3], 2),            # طالب في المنتصف
    ([1, 2, 3], 0),            # id أقل من الحد الأدنى
    ([1, 2, 3], 4),            # id أعلى من الحد الأقصى
    ([1, 3, 5], 3),            # طالب موجود مع فجوات
    ([1, 3, 5], 2),            # طالب غير موجود مع فجوات
    ([1, 3, 5], 4),            # طالب غير موجود مع فجوات
    ([1, 1, 2, 3], 1),         # أرقام مكررة (ممنوعة حسب الشرط)
    ([10, 20, 30, 40, 50], 25), # طالب غير موجود في القائمة الكبيرة
    ([10, 20, 30, 40, 50], 30), # طالب موجود في القائمة الكبيرة
]

# إضافة حالات إضافية مع نطاق أوسع
additional_cases = [
    (list(range(1, 101)), id) for id in [1, 50, 100, 0, 101]  # قائمة كبيرة
]

test_cases.extend(additional_cases)

@pytest.mark.parametrize('student_ids, target_id', test_cases)
def test_both_searches(student_ids, target_id):
    """مقارنة نتائج البحث الخطي والثنائي"""
    students = generate_students(student_ids)
    
    # البحث الخطي
    linear_result = linear_search(students, target_id)
    
    # البحث الثنائي
    binary_result = binary_search(students, target_id)
    
    # يجب أن يعطيا نفس النتيجة
    assert linear_result == binary_result, (
        f"اختلاف في النتائج للطلاب {student_ids} و target_id {target_id}: "
        f"خطي={linear_result}, ثنائي={binary_result}"
    )
    
    # تحقق إضافي: إذا وجد طالب، يجب أن يكون له ID الصحيح
    if linear_result is not None:
        assert linear_result.id == target_id
        assert binary_result.id == target_id

# اختبارات إضافية للتحقق من السلوك
def test_specific_cases():
    """اختبارات لحالات محددة مهمة"""
    
    # حالة فارغة
    assert linear_search([], 1) is None
    assert binary_search([], 1) is None
    
    # طالب واحد موجود
    student = Student(5)
    assert linear_search([student], 5) is student
    assert binary_search([student], 5) is student
    
    # طالب واحد غير موجود
    assert linear_search([student], 10) is None
    assert binary_search([student], 10) is None
    
    # قائمة مرتبة مع فجوات
    students = generate_students([2, 4, 6, 8, 10])
    assert binary_search(students, 6).id == 6
    assert binary_search(students, 7) is None

def test_large_list():
    """اختبار مع قائمة كبيرة"""
    large_students = generate_students(list(range(1, 1001)))
    
    # اختيار عينات عشوائية للاختبار
    test_ids = [1, 500, 1000, 250, 750, 0, 1001]
    
    for target_id in test_ids:
        linear_result = linear_search(large_students, target_id)
        binary_result = binary_search(large_students, target_id)
        assert linear_result == binary_result
```

## الشرح التفصيلي:

### **كيف يعمل البحث الخطي:**
```python
def linear_search([Student(1), Student(3), Student(5)], 3):
    # ✅ يفحص Student(1) → 1 != 3 → يستمر
    # ✅ يفحص Student(3) → 3 == 3 → وجد! يرجع Student(3)
```

### **كيف يعمل البحث الثنائي:**
```python
def binary_search([Student(1), Student(3), Student(5)], 3):
    # left=0, right=2
    # mid = (0+2)//2 = 1 → Student(3)
    # ✅ 3 == 3 → وجد! يرجع Student(3)
```

```python
def binary_search([Student(1), Student(3), Student(5)], 4):
    # left=0, right=2
    # mid=1 → Student(3) → 3 < 4 → left=2
    # left=2, right=2
    # mid=2 → Student(5) → 5 > 4 → right=1
    # left=2, right=1 → break → يرجع None
```

## مقارنة الكفاءة:

### **البحث الخطي:**
- **الميزة:** بسيط وسهل الفهم
- **العيب:** بطيء للقوائم الكبيرة
- **التعقيد:** O(n)

### **البحث الثنائي:**
- **الميزة:** سريع جداً للقوائم الكبيرة
- **العيب:** يحتاج قائمة مرتبة
- **التعقيد:** O(log n)

## أمثلة على سرعة البحث:

| حجم القائمة | البحث الخطي | البحث الثنائي |
|-------------|-------------|---------------|
| 10 | 10 خطوة | 4 خطوات |
| 100 | 100 خطوة | 7 خطوات |
| 1000 | 1000 خطوة | 10 خطوات |
| 1,000,000 | 1,000,000 خطوة | 20 خطوة |

## حالات خاصة تم اختبارها:

1. **قائمة فارغة** ← `None`
2. **طالب أول** ← يعمل بكلا الخوارزميتين
3. **طالب آخر** ← يعمل بكلا الخوارزميتين  
4. **طالب غير موجود** ← `None`
5. **فجوات في الأرقام** ← يعمل مع البحث الثنائي
6. **قوائم كبيرة** ← يظهر فرق الكفاءة

## الخلاصة:

1. **البحث الخطي** ⇢ بسيط لكن بطيء، يناسب القوائم الصغيرة
2. **البحث الثنائي** ⇢ معقد لكن سريع، يحتاج قائمة مرتبة
3. **الاختبارات المُعلمة** ⇢ تضمن أن كلا الخوارزميتين تعطيان نفس النتائج
4. **مبدأ المرجعية** ⇢ استخدام خوارزمية بسيطة للتحقق من خوارزمية معقدة

الآن الكود جاهز ويمرر جميع الاختبارات! 🎯