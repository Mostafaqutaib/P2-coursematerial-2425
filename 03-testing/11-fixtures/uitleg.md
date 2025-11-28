# حل تمرين Fixtures لتنظيم الاختبارات

سأشرح لك كيفية استخدام `@fixture` بدلاً من `setup_function` لتنظيم الاختبارات بشكل أفضل:

## الخطوة 1: تحديث ملف الاختبارات مع Fixtures

في ملف `tests.py`:

```python
import pytest
from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import CalendarStub

@pytest.fixture
def today():
    """Fixture لتاريخ اليوم"""
    return date(2000, 1, 1)

@pytest.fixture
def tomorrow(today):
    """Fixture لتاريخ الغد (يعتمد على today)"""
    return today + timedelta(days=1)

@pytest.fixture
def yesterday(today):
    """Fixture لتاريخ الأمس (يعتمد على today)"""
    return today - timedelta(days=1)

@pytest.fixture
def calendar(today):
    """Fixture للتقويم (يعتمد على today)"""
    return CalendarStub(today)

@pytest.fixture
def sut(calendar):
    """Fixture للنظام قيد الاختبار (يعتمد على calendar)"""
    return TaskList(calendar)

@pytest.fixture
def task(tomorrow):
    """Fixture لمهمة مستقبلية (يعتمد على tomorrow)"""
    return Task('Test task', tomorrow)
```

## الخطوة 2: تحديث الاختبارات لاستخدام Fixtures

```python
def test_creation(sut):
    # Arrange - تم الإعداد عبر fixtures
    
    # Act - لا حاجة لعمل إضافي
    
    # Assert
    assert len(sut) == 0
    assert sut.due_tasks == []
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []

def test_adding_task_with_due_day_in_future(sut, task):
    # Arrange - تم الإعداد عبر fixtures
    
    # Act
    sut.add_task(task)
    
    # Assert
    assert len(sut) == 1
    assert sut.due_tasks == [task]
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []
    assert task in sut.due_tasks

def test_adding_task_with_due_day_in_past(sut, yesterday):
    # Arrange
    past_task = Task('Past task', yesterday)
    
    # Act & Assert
    with pytest.raises(RuntimeError, match="Cannot add task with due date in the past"):
        sut.add_task(past_task)
    
    # التأكد من أن المهمة لم تُضاف
    assert len(sut) == 0
    assert sut.due_tasks == []

def test_task_becomes_finished(sut, task):
    # Arrange
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

## الخطوة 3: إضافة اختبارات إضافية مع Fixtures

```python
def test_multiple_tasks_categorization(sut, tomorrow):
    # Arrange
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

def test_overdue_after_time_passes(sut, calendar, tomorrow, today):
    # Arrange
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

def test_finished_task_not_overdue_even_if_late(sut, yesterday):
    # Arrange
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

def test_task_becomes_overdue(sut, calendar, tomorrow, today):
    # Arrange
    next_week = today + timedelta(days=7)
    task = Task('description', tomorrow)
    sut.add_task(task)
    
    # Act
    calendar.today = next_week
    
    # Assert
    assert [task] == sut.overdue_tasks
```

## الخطوة 4: إضافة Fixtures متقدمة

```python
@pytest.fixture
def next_week(today):
    """Fixture للأسبوع القادم"""
    return today + timedelta(days=7)

@pytest.fixture
def multiple_tasks(tomorrow):
    """Fixture لمجموعة مهام متنوعة"""
    return [
        Task('Task 1', tomorrow),
        Task('Task 2', tomorrow + timedelta(days=1)),
        Task('Task 3', tomorrow + timedelta(days=2)),
    ]

@pytest.fixture
def task_list_with_tasks(sut, multiple_tasks):
    """Fixture لقائمة مهام مع مهام مسبقة الإضافة"""
    for task in multiple_tasks:
        sut.add_task(task)
    return sut

def test_task_list_with_prepopulated_tasks(task_list_with_tasks, multiple_tasks):
    # Arrange - تم الإعداد عبر fixture
    
    # Act - لا حاجة لعمل إضافي
    
    # Assert
    assert len(task_list_with_tasks) == 3
    assert task_list_with_tasks.due_tasks == multiple_tasks
    assert task_list_with_tasks.finished_tasks == []
    assert task_list_with_tasks.overdue_tasks == []

def test_mark_all_tasks_finished(task_list_with_tasks, multiple_tasks):
    # Arrange
    assert len(task_list_with_tasks.due_tasks) == 3
    assert len(task_list_with_tasks.finished_tasks) == 0
    
    # Act
    for task in multiple_tasks:
        task.finished = True
    
    # Assert
    assert len(task_list_with_tasks.due_tasks) == 0
    assert len(task_list_with_tasks.finished_tasks) == 3
```

## الشرح التفصيلي:

### **كيف تعمل Fixtures:**

```python
@pytest.fixture
def today():           # ⬅️ fixture بسيط
    return date(2000, 1, 1)

@pytest.fixture  
def tomorrow(today):   # ⬅️ fixture يعتمد على fixture آخر
    return today + timedelta(days=1)

def test_example(tomorrow):  # ⬅️ اختبار يعتمد على fixture
    # pytest ينفذ: today() → tomorrow(today) → test_example(tomorrow)
    assert tomorrow == date(2000, 1, 2)
```

### **مقارنة بين setup_function و fixtures:**

**مع setup_function:**
```python
def setup_function():
    global today, calendar, sut  # ⚠️ جميع المتغيرات تُنشأ دائماً
    today = date(2000, 1, 1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)

def test_simple():  # ⚠️ حتى لو لم تستخدم جميع المتغيرات
    assert True  #但仍然 تم إنشاء today, calendar, sut
```

**مع fixtures:**
```python
@pytest.fixture
def today(): return date(2000, 1, 1)        # ✅ يُنشأ فقط عند الطلب

@pytest.fixture  
def calendar(today): return CalendarStub(today)  # ✅ يُنشأ فقط عند الطلب

def test_simple():  # ✅ لا يتم إنشاء أي fixtures
    assert True

def test_with_fixtures(sut):  # ✅ يتم إنشاء sut فقط (وبالتالي today و calendar)
    assert len(sut) == 0
```

### **فوائد استخدام Fixtures:**

1. **الكفاءة** ⇢ يتم إنشاء الكائنات فقط عند الحاجة إليها
2. **المرونة** ⇢ يمكن للاختبارات اختيار ما تحتاجه فقط
3. **التجميع** ⇢ يمكن تجميع fixtures معاً
4. **إعادة الاستخدام** ⇢ يمكن استخدام fixtures في اختبارات متعددة
5. **العزل** ⇢ فشل fixture لا يؤثر على اختبارات أخرى

## أمثلة على تبعيات Fixtures:

### **تبعيات مباشرة:**
```python
@pytest.fixture
def A(): return "A"

@pytest.fixture
def B(A): return f"B({A})"  # B تعتمد على A

@pytest.fixture  
def C(B): return f"C({B})"  # C تعتمد على B

def test_chain(C):
    assert C == "C(B(A))"  # A → B → C → test
```

### **تبعيات متعددة:**
```python
def test_multiple_dependencies(today, calendar, sut):
    # يتم إنشاء جميع الـ fixtures المطلوبة
    assert today == date(2000, 1, 1)
    assert isinstance(calendar, CalendarStub)
    assert isinstance(sut, TaskList)
```

## حالات خاصة:

### **Fixtures مع منطق معقد:**
```python
@pytest.fixture
def complex_task_list(sut, multiple_tasks, tomorrow):
    """Fixture مع منطق إعداد معقد"""
    # إضافة بعض المهام
    for task in multiple_tasks[:2]:
        sut.add_task(task)
    
    # إنهاء بعض المهام
    multiple_tasks[0].finished = True
    
    # تغيير التاريخ
    sut._calendar.today = tomorrow + timedelta(days=5)
    
    return sut

def test_complex_scenario(complex_task_list, multiple_tasks):
    # الاختبار يبدأ بحالة معقدة مُعدة مسبقاً
    assert len(complex_task_list.finished_tasks) == 1
    assert len(complex_task_list.overdue_tasks) == 1
```

## الخلاصة:

1. **`@pytest.fixture`** ⇢ تحدد كائنات يمكن إعادة استخدامها في الاختبارات
2. **التبعيات** ⇢ fixtures يمكنها الاعتماد على fixtures أخرى
3. **الكفاءة** ⇢ يتم إنشاء الكائنات فقط عند الحاجة
4. **المرونة** ⇢ كل اختبار يختار ما يحتاجه فقط

الآن الاختبارات أكثر كفاءة ومرونة! 🎯