# حل تمرين Task و TaskList

سأشرح لك كيفية حل هذا التمرين خطوة بخطوة:

## الخطوة 1: فئة Task

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
```

## الخطوة 2: فئة TaskList

في ملف `tasks.py`:

```python
from datetime import date

class TaskList:
    def __init__(self):
        self._tasks = []
    
    def add_task(self, task):
        if task.due_date < date.today():
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
        today = date.today()
        return [task for task in self._tasks 
                if not task.finished and task.due_date < today]
```

## الكود الكامل في `tasks.py`:

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
    def __init__(self):
        self._tasks = []
    
    def add_task(self, task):
        if task.due_date < date.today():
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
        today = date.today()
        return [task for task in self._tasks 
                if not task.finished and task.due_date < today]
    
    def __repr__(self):
        return f"TaskList({len(self._tasks)} tasks)"
```

## الشرح التفصيلي:

### **خصائص Task:**

```python
task = Task('buy groceries', date(2024, 1, 15))
print(task.description)    # 'buy groceries'  (للقراءة فقط)
print(task.due_date)       # 2024-01-15       (للقراءة فقط)
print(task.finished)       # False            (قابل للتعديل)
task.finished = True       # ✅ يمكن تعديله
print(task.finished)       # True
```

### **سلوك TaskList:**

```python
tasks = TaskList()

# إضافة مهام
tomorrow = date.today() + date.resolution  # غداً
task1 = Task('task 1', tomorrow)
tasks.add_task(task1)

# التحقق من الطول
print(len(tasks))  # 1

# المهام المنتهية والملغاة
print(tasks.finished_tasks)  # []
print(tasks.due_tasks)       # [task1]

# جعل المهمة منتهية
task1.finished = True
print(tasks.finished_tasks)  # [task1]
print(tasks.due_tasks)       # []
```

## أمثلة على الاستخدام:

### **مثال 1: مهام مستقبلية**
```python
from datetime import date, timedelta

# إنشاء قائمة مهام
task_list = TaskList()

# مهام مستقبلية
future_date = date.today() + timedelta(days=7)
task1 = Task('Complete project', future_date)
task2 = Task('Buy supplies', future_date)

# إضافة المهام
task_list.add_task(task1)
task_list.add_task(task2)

print(f"Total tasks: {len(task_list)}")           # 2
print(f"Due tasks: {len(task_list.due_tasks)}")   # 2
print(f"Finished tasks: {len(task_list.finished_tasks)}")  # 0
print(f"Overdue tasks: {len(task_list.overdue_tasks)}")    # 0
```

### **مثال 2: منع إضافة مهام منتهية الصلاحية**
```python
from datetime import date, timedelta

task_list = TaskList()
past_date = date.today() - timedelta(days=1)
expired_task = Task('Expired task', past_date)

try:
    task_list.add_task(expired_task)
    print("Task added successfully")
except RuntimeError as e:
    print(f"Error: {e}")  # Error: Cannot add task with due date in the past
```

### **مثال 3: المهام المتأخرة**
```python
from datetime import date, timedelta

task_list = TaskList()

# مهمة مستقبلية
future_task = Task('Future task', date.today() + timedelta(days=2))

# مهمة منتهية الصلاحية (لكن نضيفها بطريقة خاصة للاختبار)
# في الواقع الفعلي، لا يمكن إضافتها عبر add_task
class TestTask:
    def __init__(self, desc, due, finished=False):
        self.description = desc
        self.due_date = due
        self.finished = finished

# محاكاة مهمة متأخرة
overdue_task = TestTask('Overdue task', date.today() - timedelta(days=1))

# إضافة إلى القائمة الداخلية مباشرة (لأغراض الاختبار فقط)
task_list._tasks.append(future_task)
task_list._tasks.append(overdue_task)

print(f"Due tasks: {len(task_list.due_tasks)}")       # 2 (كلاهما غير منتهي)
print(f"Overdue tasks: {len(task_list.overdue_tasks)}") # 1 (واحد فقط متأخر)
```

## حالات خاصة:

### **1. قائمة فارغة:**
```python
empty_list = TaskList()
print(len(empty_list))               # 0
print(empty_list.finished_tasks)     # []
print(empty_list.due_tasks)          # []
print(empty_list.overdue_tasks)      # []
```

### **2. جميع المهام منتهية:**
```python
task_list = TaskList()
task = Task('task', date.today() + timedelta(days=1))
task.finished = True
task_list.add_task(task)

print(task_list.finished_tasks)  # [task]
print(task_list.due_tasks)       # []
print(task_list.overdue_tasks)   # []
```

### **3. مهام مختلطة:**
```python
task_list = TaskList()
today = date.today()

task1 = Task('task1', today + timedelta(days=1))  # مستقبلية
task2 = Task('task2', today)                      # اليوم
task3 = Task('task3', today - timedelta(days=1))  # ماضية (لا يمكن إضافتها)

task1.finished = True  # منتهية

task_list.add_task(task1)
# task_list.add_task(task3)  # سترفع استثناء

print(f"Finished: {len(task_list.finished_tasks)}")  # 1
print(f"Due: {len(task_list.due_tasks)}")           # 0
```

## الخلاصة:

1. **Task** ⇢ يمثل مهمة فردية بوصف وموعد استحقاق وحالة إنجاز
2. **TaskList** ⇢ يدير مجموعة من المهام مع قيود التحقق
3. **التحقق من التاريخ** ⇢ يمنع إضافة مهام منتهية الصلاحية
4. **الخصائص المحسوبة** ⇢ توفر تصنيفات مختلفة للمهام

الكلاسات جاهزة للاستخدام في التمارين القادمة! 🎯