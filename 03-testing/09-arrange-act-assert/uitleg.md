# حل تمرين Arrange-Act-Assert مع اختبارات منظمة

سأشرح لك كيفية كتابة الاختبارات باستخدام هيكل Arrange-Act-Assert:

## الخطوة 1: كتابة الاختبارات المنظمة

في ملف `tests.py`:

```python
import pytest
from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import CalendarStub

def test_creation():
    # Arrange
    calendar = CalendarStub(date(2024, 1, 1))
    
    # Act
    sut = TaskList(calendar)
    
    # Assert
    assert len(sut) == 0
    assert sut.due_tasks == []
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []

def test_adding_task_with_due_day_in_future():
    # Arrange
    today = date(2024, 1, 1)
    tomorrow = today + timedelta(days=1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)
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
    # Arrange
    today = date(2024, 1, 1)
    yesterday = today - timedelta(days=1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)
    task = Task('Past task', yesterday)
    
    # Act & Assert
    with pytest.raises(RuntimeError, match="Cannot add task with due date in the past"):
        sut.add_task(task)
    
    # التأكد من أن المهمة لم تُضاف
    assert len(sut) == 0
    assert sut.due_tasks == []

def test_task_becomes_finished():
    # Arrange
    today = date(2024, 1, 1)
    tomorrow = today + timedelta(days=1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)
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

## الخطوة 2: إضافة اختبارات إضافية

```python
def test_multiple_tasks_categorization():
    # Arrange
    today = date(2024, 1, 1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)
    
    task1 = Task('Future task', today + timedelta(days=2))
    task2 = Task('Finished task', today + timedelta(days=3))
    task3 = Task('Another future task', today + timedelta(days=1))
    
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
    # Arrange
    today = date(2024, 1, 1)
    tomorrow = today + timedelta(days=1)
    next_week = today + timedelta(days=7)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)
    
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
    # Arrange
    today = date(2024, 1, 1)
    yesterday = today - timedelta(days=1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)
    
    # إنشاء مهمة منتهية ولكن متأخرة (لا يمكن إضافتها عادةً)
    task = Task('Late but finished', yesterday)
    task.finished = True
    
    # إضافة مباشرة للقائمة الداخلية لأغراض الاختبار
    sut._tasks.append(task)
    
    # Act
    # لا حاجة لتنفيذ أي عمل إضافي
    
    # Assert
    assert task in sut.finished_tasks
    assert task not in sut.due_tasks
    assert task not in sut.overdue_tasks  # المهام المنتهية لا تعتبر متأخرة

def test_empty_task_list_properties():
    # Arrange
    calendar = CalendarStub(date(2024, 1, 1))
    sut = TaskList(calendar)
    
    # Act
    # لا حاجة لتنفيذ أي عمل إضافي
    
    # Assert
    assert len(sut) == 0
    assert sut.due_tasks == []
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []
    
    # التأكد أن الخصائص ترجع قوائم فارغة وليست None
    assert isinstance(sut.due_tasks, list)
    assert isinstance(sut.overdue_tasks, list)
    assert isinstance(sut.finished_tasks, list)
```

## الشرح التفصيلي:

### **هيكل Arrange-Act-Assert:**

```python
def test_example():
    # 📋 Arrange - إعداد البيئة
    # إنشاء الكائنات، تعيين القيم الأولية
    calendar = CalendarStub(date(2024, 1, 1))
    sut = TaskList(calendar)
    task = Task('test', date(2024, 1, 2))
    
    # 🎬 Act - تنفيذ الإجراء
    # تنفيذ العملية التي نريد اختبارها
    sut.add_task(task)
    
    # ✅ Assert - التحقق من النتائج
    # التأكد من أن النتائج متوقعة
    assert len(sut) == 1
    assert task in sut.due_tasks
```

### **لماذا نستخدم `sut`؟**

- **`sut`** = System Under Test (النظام قيد الاختبار)
- يجعل من الواضح أي كائن نختبر سلوكه
- يحسن قابلية قراءة الكود

### **اختبار الاستثناءات:**

```python
def test_exception():
    # Arrange
    calendar = CalendarStub(date(2024, 1, 1))
    sut = TaskList(calendar)
    task = Task('task', date(2023, 12, 31))  # تاريخ ماضي
    
    # Act & Assert في سطر واحد
    with pytest.raises(RuntimeError):
        sut.add_task(task)
```

## أمثلة على حالات الاختبار المختلفة:

### **اختبار الحالة الأولية:**
```python
def test_initial_state():
    # Arrange & Act
    calendar = CalendarStub(date(2024, 1, 1))
    sut = TaskList(calendar)
    
    # Assert
    assert len(sut) == 0
    assert sut.due_tasks == []
    # ... إلخ
```

### **اختبار التحولات:**
```python
def test_state_transition():
    # Arrange
    calendar = CalendarStub(date(2024, 1, 1))
    sut = TaskList(calendar)
    task = Task('task', date(2024, 1, 2))
    sut.add_task(task)
    
    # Act
    task.finished = True  # تحول الحالة
    
    # Assert
    assert task in sut.finished_tasks
    assert task not in sut.due_tasks
```

### **اختبار القيود:**
```python
def test_constraints():
    # Arrange
    calendar = CalendarStub(date(2024, 1, 1))
    sut = TaskList(calendar)
    past_task = Task('past', date(2023, 12, 31))
    
    # Act & Assert
    with pytest.raises(RuntimeError):
        sut.add_task(past_task)  # يجب أن يفشل
```

## فوائد هيكل AAA:

1. **الوضوح** ⇢ يسهل فهم ما يفعله الاختبار
2. **التنظيم** ⇢ يمنع الخلط بين الإعداد والتنفيذ والتحقق
3. **الصيانة** ⇢ يسهل تعديل الاختبارات لاحقاً
4. **التصحيح** ⇢ يسهل تحديد مكان المشكلة عند فشل الاختبار

## الخلاصة:

1. **Arrange** ⇢ إعداد البيانات والكائنات اللازمة
2. **Act** ⇢ تنفيذ العملية المطلوب اختبارها
3. **Assert** ⇢ التحقق من النتائج المتوقعة
4. **sut** ⇢ تحديد النظام قيد الاختبار بوضوح

الآن الاختبارات منظمة وسهلة القراءة والصيانة! 🎯