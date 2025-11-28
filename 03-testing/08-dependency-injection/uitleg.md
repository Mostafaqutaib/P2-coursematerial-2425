# حل تمرين Dependency Injection مع Calendar

سأشرح لك كيفية حل هذا التمرين خطوة بخطوة:

## الخطوة 1: تحديث فئة TaskList

في ملف `tasks.py`:

```python
from datetime import date

class Task:
    def __init__(self, description, due_date):
        self._description = description
        self._due_date = due_date
        self._finished = False
    
    @property
    def description(self):
        return self._description
    
    @property
    def due_date(self):
        return self._due_date
    
    @property
    def finished(self):
        return self._finished
    
    @finished.setter
    def finished(self, value):
        self._finished = value
    
    def __repr__(self):
        return f"Task('{self.description}', {self.due_date}, finished={self.finished})"

class TaskList:
    def __init__(self, calendar):
        self._tasks = []
        self._calendar = calendar
    
    def add_task(self, task):
        if task.due_date < self._calendar.today:
            raise RuntimeError("Cannot add task with due date in the past")
        self._tasks.append(task)
    
    def __len__(self):
        return len(self._tasks)
    
    @property
    def finished_tasks(self):
        return [task for task in self._tasks if task.finished]
    
    @property
    def due_tasks(self):
        return [task for task in self._tasks if not task.finished]
    
    @property
    def overdue_tasks(self):
        today = self._calendar.today
        return [task for task in self._tasks 
                if not task.finished and task.due_date < today]
    
    def __repr__(self):
        return f"TaskList({len(self._tasks)} tasks)"
```

## الخطوة 2: إنشاء فئتي Calendar و CalendarStub

في ملف `calendars.py`:

```python
from datetime import date

class Calendar:
    """Calendar للإنتاج - يستخدم التاريخ الحقيقي"""
    
    @property
    def today(self):
        return date.today()

class CalendarStub:
    """Calendar للاختبار - يمكن التحكم في التاريخ"""
    
    def __init__(self, initial_date):
        self._today = initial_date
    
    @property
    def today(self):
        return self._today
    
    @today.setter
    def today(self, value):
        self._today = value
```

## الخطوة 3: كتابة الاختبارات

في ملف `tests.py`:

```python
import pytest
from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import Calendar, CalendarStub

def test_task_becomes_overdue():
    """اختبار أن المهمة تصبح متأخرة مع مرور الوقت"""
    # إنشاء Calendar مزيف للاختبار
    initial_date = date(2024, 1, 1)
    calendar = CalendarStub(initial_date)
    
    # إنشاء قائمة مهام باستخدام Calendar المزيف
    task_list = TaskList(calendar)
    
    # إنشاء مهمة مستقبلية
    tomorrow = initial_date + timedelta(days=1)
    task = Task('Complete project', tomorrow)
    
    # إضافة المهمة (يجب أن تنجح لأن التاريخ مستقبلي)
    task_list.add_task(task)
    
    # التحقق من أن المهمة ليست متأخرة بعد
    assert task_list.overdue_tasks == []
    assert task_list.due_tasks == [task]
    
    # محاكاة مرور يومين
    calendar.today = initial_date + timedelta(days=2)
    
    # التحقق من أن المهمة أصبحت متأخرة
    assert task_list.overdue_tasks == [task]
    assert task_list.due_tasks == [task]  # لا تزال مستحقة (ولكن متأخرة)

def test_finished_task_is_not_overdue():
    """اختبار أن المهمة المنتهية لا تعتبر متأخرة"""
    calendar = CalendarStub(date(2024, 1, 1))
    task_list = TaskList(calendar)
    
    # مهمة منتهية ولكن متأخرة
    yesterday = calendar.today - timedelta(days=1)
    task = Task('Late but finished task', yesterday)
    task.finished = True
    
    # إضافة المهمة (يجب أن تفشل لأنها في الماضي)
    # لكن لأغراض الاختبار، نضيفها مباشرة إلى القائمة الداخلية
    task_list._tasks.append(task)
    
    # التحقق من أنها لا تظهر في المهام المتأخرة
    assert task_list.overdue_tasks == []
    assert task in task_list.finished_tasks

def test_cannot_add_past_due_task():
    """اختبار أنه لا يمكن إضافة مهمة منتهية الصلاحية"""
    calendar = CalendarStub(date(2024, 1, 1))
    task_list = TaskList(calendar)
    
    # محاولة إضافة مهمة في الماضي
    yesterday = calendar.today - timedelta(days=1)
    task = Task('Expired task', yesterday)
    
    with pytest.raises(RuntimeError, match="Cannot add task with due date in the past"):
        task_list.add_task(task)

def test_calendar_in_production():
    """اختبار أن Calendar الحقيقي يعمل في بيئة الإنتاج"""
    calendar = Calendar()
    task_list = TaskList(calendar)
    
    # إضافة مهمة مستقبلية
    future_date = calendar.today + timedelta(days=7)
    task = Task('Future task', future_date)
    
    task_list.add_task(task)
    assert len(task_list) == 1
    assert task_list.due_tasks == [task]

def test_multiple_date_changes():
    """اختبار تغييرات التاريخ المتعددة"""
    calendar = CalendarStub(date(2024, 1, 1))
    task_list = TaskList(calendar)
    
    # إضافة مهام بمواعيد مختلفة
    task1 = Task('Task in 2 days', date(2024, 1, 3))
    task2 = Task('Task in 5 days', date(2024, 1, 6))
    
    task_list.add_task(task1)
    task_list.add_task(task2)
    
    # التاريخ: 2024-01-01 - لا توجد مهام متأخرة
    assert task_list.overdue_tasks == []
    
    # التاريخ: 2024-01-04 - المهمة الأولى متأخرة
    calendar.today = date(2024, 1, 4)
    assert task_list.overdue_tasks == [task1]
    assert task_list.due_tasks == [task1, task2]
    
    # التاريخ: 2024-01-07 - كلا المهمتين متأخرتين
    calendar.today = date(2024, 1, 7)
    assert task_list.overdue_tasks == [task1, task2]
    
    # إنهاء المهمة الأولى
    task1.finished = True
    assert task_list.overdue_tasks == [task2]  # فقط الثانية متأخرة
    assert task_list.finished_tasks == [task1]
```

## الشرح التفصيلي:

### **مبدأ Dependency Injection:**

**بدون DI (مشكلة):**
```python
class TaskList:
    def __init__(self):
        self._tasks = []
    
    @property
    def overdue_tasks(self):
        return [task for task in self._tasks 
                if not task.finished and task.due_date < date.today()]  # ⚠️ مرتبط مباشرة
```

**مع DI (حل):**
```python
class TaskList:
    def __init__(self, calendar):  # ✅ نمرر dependency
        self._tasks = []
        self._calendar = calendar
    
    @property
    def overdue_tasks(self):
        return [task for task in self._tasks 
                if not task.finished and task.due_date < self._calendar.today]  # ✅ مرن
```

### **كيف يعمل الاختبار:**

```python
def test_task_becomes_overdue():
    # 🎯 نتحكم في الزمن
    calendar = CalendarStub(date(2024, 1, 1))
    task_list = TaskList(calendar)
    
    # 📅 مهمة لموعد غد
    task = Task('task', date(2024, 1, 2))
    task_list.add_task(task)
    
    # ⏰ نسرع الزمن يومين
    calendar.today = date(2024, 1, 3)
    
    # ✅ المهمة أصبحت متأخرة
    assert task_list.overdue_tasks == [task]
```

## أمثلة على الاستخدام:

### **في بيئة الإنتاج:**
```python
# استخدام Calendar الحقيقي
real_calendar = Calendar()
task_list = TaskList(real_calendar)

# يعمل مع التاريخ الفعلي
task = Task('Real task', date.today() + timedelta(days=1))
task_list.add_task(task)
```

### **في الاختبارات:**
```python
# استخدام Calendar مزيف
fake_calendar = CalendarStub(date(2024, 1, 1))
task_list = TaskList(fake_calendar)

# يمكننا محاكاة أي سيناريو زمني
fake_calendar.today = date(2024, 12, 31)  # القفز إلى نهاية العام
```

## فوائد Dependency Injection:

1. **إمكانية الاختبار** ⇢ يمكن محاكاة الوقت دون الانتظار الفعلي
2. **المرونة** ⇢ يمكن تبديل implementaions مختلفة
3. **فصل الاهتمامات** ⇢ TaskList لا تهتم بكيفية الحصول على التاريخ
4. **إعادة الاستخدام** ⇢ يمكن استخدام نفس الكود في بيئات مختلفة

## الخلاصة:

1. **Calendar** ⇢ للاستخدام في بيئة الإنتاج
2. **CalendarStub** ⇢ للاستخدام في الاختبارات
3. **Dependency Injection** ⇢ يجعل الكود أكثر قابلية للاختبار
4. **الاختبارات السريعة** ⇢ لا حاجة للانتظار الفعلي

الآن الاختبارات تعمل بسرعة ويمكنها محاكاة أي سيناريو زمني! 🎯