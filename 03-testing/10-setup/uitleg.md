# حل تمرين Setup Function لتنظيم الاختبارات

سأشرح لك كيفية استخدام `setup_function` لتنظيم الكود المتكرر في الاختبارات:

## الخطوة 1: تحديث ملف الاختبارات مع setup_function

في ملف `tests.py`:

```python
import pytest
from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import CalendarStub

# متغيرات عامة سيتم تعيينها في setup_function
today = None
tomorrow = None
yesterday = None
calendar = None
sut = None

def setup_function():
    """يتم استدعاؤها قبل كل اختبار لإعداد البيانات المشتركة"""
    global today, tomorrow, yesterday, calendar, sut
    
    today = date(2000, 1, 1)
    tomorrow = today + timedelta(days=1)
    yesterday = today - timedelta(days=1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)

def teardown_function():
    """يتم استدعاؤها بعد كل اختبار للتنظيف"""
    # في هذا المثال، لا نحتاج لتنظيف خاص
    # ولكن يمكن استخدامها لإغلاق اتصالات أو حذف ملفات مؤقتة
    pass

def test_creation():
    # Arrange - تم الإعداد في setup_function
    
    # Act - لا حاجة لعمل إضافي
    
    # Assert
    assert len(sut) == 0
    assert sut.due_tasks == []
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []

def test_adding_task_with_due_day_in_future():
    # Arrange - تم الإعداد في setup_function
    task = Task('Future task', tomorrow)
    
    # Act
    sut.add_task(task)
    
    # Assert
    assert len(sut) == 1
    assert sut.due_tasks == [task]
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []
    assert task in sut.due_tasks

def test_adding_task_with_due_day_in_past():
    # Arrange - تم الإعداد في setup_function
    task = Task('Past task', yesterday)
    
    # Act & Assert
    with pytest.raises(RuntimeError, match="Cannot add task with due date in the past"):
        sut.add_task(task)
    
    # التأكد من أن المهمة لم تُضاف
    assert len(sut) == 0
    assert sut.due_tasks == []

def test_task_becomes_finished():
    # Arrange - تم الإعداد في setup_function
    task = Task('Task to finish', tomorrow)
    sut.add_task(task)
    
    # التأكد من الحالة الأولية
    assert task in sut.due_tasks
    assert task not in sut.finished_tasks
    assert len(sut.due_tasks) == 1
    assert len(sut.finished_tasks) == 0
    
    # Act
    task.finished = True
    
    # Assert
    assert task not in sut.due_tasks
    assert task in sut.finished_tasks
    assert len(sut.due_tasks) == 0
    assert len(sut.finished_tasks) == 1
```

## الخطوة 2: إضافة اختبارات إضافية مع البيانات المشتركة

```python
def test_multiple_tasks_categorization():
    # Arrange - تم الإعداد في setup_function
    task1 = Task('Future task', tomorrow + timedelta(days=1))
    task2 = Task('Finished task', tomorrow + timedelta(days=2))
    task3 = Task('Another future task', tomorrow)
    
    task2.finished = True
    
    # Act
    sut.add_task(task1)
    sut.add_task(task2)
    sut.add_task(task3)
    
    # Assert
    assert len(sut) == 3
    assert sut.due_tasks == [task1, task3]  # المهام غير المنتهية
    assert sut.finished_tasks == [task2]    # المهام المنتهية فقط
    assert sut.overdue_tasks == []          # لا توجد مهام متأخرة بعد

def test_overdue_after_time_passes():
    # Arrange - تم الإعداد في setup_function
    next_week = today + timedelta(days=7)
    task = Task('Soon due task', tomorrow)
    sut.add_task(task)
    
    # التأكد من الحالة الأولية
    assert task in sut.due_tasks
    assert task not in sut.overdue_tasks
    
    # Act
    calendar.today = next_week
    
    # Assert
    assert task in sut.overdue_tasks
    assert task in sut.due_tasks  # لا تزال مستحقة (لكن متأخرة)
    assert task not in sut.finished_tasks

def test_finished_task_not_overdue_even_if_late():
    # Arrange - تم الإعداد في setup_function
    # إنشاء مهمة منتهية ولكن متأخرة (لا يمكن إضافتها عادةً)
    task = Task('Late but finished', yesterday)
    task.finished = True
    
    # إضافة مباشرة للقائمة الداخلية لأغراض الاختبار
    sut._tasks.append(task)
    
    # Act - لا حاجة لتنفيذ أي عمل إضافي
    
    # Assert
    assert task in sut.finished_tasks
    assert task not in sut.due_tasks
    assert task not in sut.overdue_tasks  # المهام المنتهية لا تعتبر متأخرة

def test_task_becomes_overdue():
    # Arrange - تم الإعداد في setup_function
    next_week = today + timedelta(days=7)
    task = Task('description', tomorrow)
    sut.add_task(task)
    
    # Act
    calendar.today = next_week
    
    # Assert
    assert [task] == sut.overdue_tasks
```

## الخطوة 3: اختبارات تتطلب بيانات مختلفة

```python
def test_different_date_scenarios():
    # Arrange - نعيد تعيين البيانات لهذا الاختبار المحدد
    custom_today = date(2024, 6, 15)
    custom_calendar = CalendarStub(custom_today)
    custom_sut = TaskList(custom_calendar)
    
    custom_task = Task('Custom date task', date(2024, 6, 20))
    
    # Act
    custom_sut.add_task(custom_task)
    
    # Assert
    assert len(custom_sut) == 1
    assert custom_task in custom_sut.due_tasks

def test_edge_case_last_day_of_month():
    # Arrange - اختبار حالة خاصة (آخر يوم في الشهر)
    last_day = date(2000, 1, 31)
    next_month = date(2000, 2, 1)
    edge_calendar = CalendarStub(last_day)
    edge_sut = TaskList(edge_calendar)
    
    task = Task('End of month task', next_month)
    
    # Act
    edge_sut.add_task(task)
    
    # Assert
    assert len(edge_sut) == 1
    assert task in edge_sut.due_tasks
```

## الشرح التفصيلي:

### **كيف يعمل setup_function:**

```python
# 🔄 قبل كل اختبار:
setup_function()  # يعيد تعيين جميع المتغيرات
test_function()   # يشغل الاختبار
teardown_function()  # ينظف إذا لزم الأمر
```

### **لماذا نستخدم `global`؟**

```python
def setup_function():
    global today  # ⬅️ بدون هذا، today سيكون متغيراً محلياً فقط
    today = date(2000, 1, 1)

def test_example():
    print(today)  # ✅ يعمل لأن today معرف عالمياً
```

### **فوائد استخدام setup_function:**

1. **إزالة التكرار** ⇢ لا حاجة لنسخ نفس الكود في كل اختبار
2. **الاتساق** ⇢ جميع الاختبارات تبدأ بنفس الحالة الأولية
3. **عزل الاختبارات** ⇢ كل اختبار يبدأ بحالة نظيفة
4. **سهولة الصيانة** ⇢ تغيير واحد يطبق على جميع الاختبارات

## أمثلة على ما يحدث في الخلفية:

### **بدون setup_function:**
```python
def test_1():
    today = date(2000, 1, 1)        # ⚠️ كود مكرر
    calendar = CalendarStub(today)  # ⚠️ كود مكرر
    sut = TaskList(calendar)        # ⚠️ كود مكرر
    # ... باقي الاختبار

def test_2():
    today = date(2000, 1, 1)        # ⚠️ كود مكرر
    calendar = CalendarStub(today)  # ⚠️ كود مكرر  
    sut = TaskList(calendar)        # ⚠️ كود مكرر
    # ... باقي الاختبار
```

### **مع setup_function:**
```python
def setup_function():
    global today, calendar, sut
    today = date(2000, 1, 1)        # ✅ كود مركزي
    calendar = CalendarStub(today)  # ✅ كود مركزي
    sut = TaskList(calendar)        # ✅ كود مركزي

def test_1():
    # ✅ جميع المتغيرات جاهزة
    # ... باقي الاختبار

def test_2():
    # ✅ جميع المتغيرات جاهزة
    # ... باقي الاختبار
```

## حالات خاصة:

### **اختبارات تحتاج بيانات مختلفة:**
```python
def test_special_case():
    # إذا احتجنا بيانات مختلفة، ننشئها محلياً
    special_today = date(1999, 12, 31)
    special_calendar = CalendarStub(special_today)
    special_sut = TaskList(special_calendar)
    
    # استخدام البيانات الخاصة لهذا الاختبار
    # ...
```

### **إعادة تعيين حالة معينة:**
```python
def test_with_reset():
    # Arrange - نستخدم البيانات المشتركة ولكن نعيد تعيين حالة معينة
    sut = TaskList(calendar)  # ننشئ نسخة جديدة إذا لزم الأمر
    
    # ... باقي الاختبار
```

## الخلاصة:

1. **`setup_function`** ⇢ تعمل قبل كل اختبار لإعداد البيانات المشتركة
2. **`teardown_function`** ⇢ تعمل بعد كل اختبار للتنظيف
3. **`global`** ⇢ ضروري لجعل المتغيرات مرئية للاختبارات
4. **العزل** ⇢ كل اختبار يبدأ بحالة نظيفة ومتسقة

الآن الاختبارات أكثر تنظيماً وأقل تكراراً! 🎯