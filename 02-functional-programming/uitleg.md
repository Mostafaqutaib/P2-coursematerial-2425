````md
# 02-functional-programming — أهم ما جاء في المجلد (حسب ملفات الكورس فعليًا)

> الهدف من هذا الجزء في الكورس: **تخليك تكتب حلول “أعمّ” (General) بدل حلول مخصّصة**، وتتعامل مع البيانات كسلاسل قيم (iterables/iterators) بأدوات مثل **higher-order functions, lambdas, comprehensions, generators, itertools, recursion**.

---

## خريطة المجلد (02-functional-programming)
1. `01-higher-order-functions`
   - `01-generalizing.md`
   - `03-functions-as-arguments.md`
   - `06-generalizing-revisited.md`
   - Assignments: `generalizing`, `repeat`, `group_by`, `find`, `partition`, `take_while`, `indices_of`, `merge_dictionaries`
2. `02-nested-functions`
   - `01-nested-functions.md`
   - Assignment: nested-functions tasks
3. `03-lambdas`
   - `01-lambdas.md`
   - `03-sorting.md`
   - `05-min-max.md`
   - `07-lambas-vs-nested.md`
   - Assignments: lambdas, sorting, min-max
4. `04-comprehensions`
   - `01-mapping.md`
   - `03-filtering.md`
   - `05-set-comprehensions.md`
   - `07-dictionary-comprehension.md`
   - `09-flatten.md`
   - `11-builtin-functions.md`
   - Assignments: mapping, filtering, set/dict comprehension, flatten, builtin-functions, group-movies-by-year
5. `05-iterable`
   - `00-iterables.md`
   - `01-generators.md`
   - `06-generator-comprehension.md`
   - Assignments: repeat, cycle, fizzbuzz, rle, generate-primes
6. `06-itertools`
   - `01-itertools.md`
   - Assignments: total-distance, traveling-salesman, rle-revisited
7. `07-recursion`
   - `01-recursion.md`
   - Assignments: fibonacci, reverse, sum-numbers, count-x, find-maximum, fractals

---

# 01) Higher Order Functions + Generalizing

## 01.1 `01-generalizing.md` — Generalizing functions (مثال الأفلام)
الكورس يبدأ بمثال بسيط لكن “مقصود”:
- عندك كود يعدّ أفلام مخرج معيّن (مثل Spielberg) داخل loop.
- ثم تظهر المشكلة: نفس الفكرة تتكرر لمخرج آخر (Coen Brothers) → **تكرار**.

### الفكرة التعليمية
بدل ما تكتب:
- `count_movies_by_spielberg(movies)`
- `count_movies_by_coen_brothers(movies)`
تكتب **دالة واحدة عامّة**:
- `count_movies_by_director(movies, director)`

**الرسالة:**  
> أي شيء “hardcoded” داخل الدالة (اسم مخرج/سنة/شرط…) غالبًا مرشح أنك تحوله إلى **parameter**.

---

## 01.2 `03-functions-as-arguments.md` — Functions as variables + Example: performance testing
هنا الكورس يعمل قفزة مهمة: مش بس “قيم” تتعامل معها… حتى **الدوال نفسها** تقدر تحطها في متغير وتمريرها كـ argument.

### مثال Bubblesort (أداء/Timing)
الكورس يورّيك دالتين متشابهتين جدًا:
- `test_bubble_sort()` تقيس زمن `bubble_sort`
- `test_python_sort()` تقيس زمن `sorted`

المشكلة: **نفس الكود مكرر**، والاختلاف سطر واحد فقط (الدالة التي نختبرها).

### التعميم بنفس منطق Spielberg
- بدل hardcode `bubble_sort` داخل دالة الاختبار…
- نخليها parameter:
  - `test_sort(sorting_function)`

وبعدين تستدعي:
- `test_sort(bubble_sort)`
- `test_sort(sorted)`
- وأي sort أخرى لاحقًا بدون ما تكتب “نسخة ثالثة” من الاختبار.

### مصطلح الكورس
> Functions التي تأخذ Functions كـ arguments اسمها **Higher Order Functions**.

---

## 01.3 `06-generalizing-revisited.md` — Generalizing revisited (التعميم عبر “الشرط”)
هنا الكورس يثبت أن التعميم ليس فقط constants أو أسماء… حتى **الـ if-condition** نفسها يمكن تحويلها!

يعطي مثالين متشابهين:
- `count_children(people)` (شرط: `age < 18`)
- `count_even_numbers(numbers)` (شرط: `n % 2 == 0`)

### خطوة الكورس الذكية
حوّل الشرط إلى دالة:
- `is_even(number) -> bool`
- `is_child(person) -> bool`

ثم خلّي الدالة العامة:
- `count(collection, condition)`

وتستعملها:
- `count([1,2,3,4], is_even)`
- `count(people, is_child)`

**الرسالة الأساسية:**
> “أي كود” يمكن تحويله إلى function… وبعدها يصبح قابل للتمرير كـ argument → تعميم أعلى.

---

## Assignments (01-higher-order-functions) — ماذا يطلب منك؟
- **02-generalizing**
  - تعميم أمثلة (سنة/ممثل/فترة زمنية…)
  - مثل: `count_movies_from_year(movies, year)` بدل current year
  - `select_movies_with_actor(movies, actor)`
  - `sum_movie_duration_from_period(movies, start_year, end_year)`
  - `find_string_starting_with(strings, letter)`
  - `find_number_greater_than(numbers, threshold)`
- **04-repeat**
  - `repeat(function, n)` تنادي function (بدون arguments) عدد n مرات.
- **05-group-by**
  - `group_by(xs, key_function)` ترجع dict: المفتاح = ناتج key_function، والقيمة = قائمة العناصر التي لها نفس المفتاح.
- **07-find**
  - تعميم “find أول عنصر يحقق شرط” + إعادة كتابة المثال الأصلي باستخدام `find`.
- **08-partition**
  - تعميم تقسيم list إلى قائمتين حسب شرط.
- **09-take-while**
  - مشابه لـ partition لكن **يتوقف** عند أول عنصر الشرط يصبح False.
- **10-indices-of**
  - تعميم إرجاع indices للعناصر التي تحقق شرط (مع مثال palindromes).
- **11-merge-dictionaries**
  - دمج dicts مع التعامل مع المفاتيح المشتركة عبر `merge_function` (مرة “sum”، مرة “max”…).

---

# 02) Nested Functions

## `01-nested-functions.md` — لماذا نحتاج nested function؟
الكورس يرجع لمثال:
- عندنا `count(collection, condition)`، والشرط لازم يأخذ **عنصر واحد** فقط.

لكن في `count_movies_by_director(movies, director)` الشرط يحتاج “director” أيضًا.
كيف نمرر director للشرط بدون إضافة argument ثاني للشرط؟

الحل: **تعريف helper داخل scope** حيث director موجود:
```python
def count_movies_by_director(movies, director):
    def is_by_director(movie):
        return movie.director == director
    return count(movies, is_by_director)
````

### متى نستخدم nested حسب الكورس؟

* لما شرطك يحتاج “قيمة إضافية” (مثل director/min_age/target…)
  لكن واجهة الدالة العامة تقبل شرطًا بعنصر واحد فقط.

---

## Assignment (02-nested-functions)

* `count_older_than(people, min_age)` بالاعتماد على higher-order functions السابقة.
* `indices_of_cards_with_suit(cards, suit)` بنفس الفكرة (شرط يعتمد على suit).

---

# 03) Lambdas

## 03.1 `01-lambdas.md` — Lambdas = دوال قصيرة “anonymous” + هي expressions

الكورس يعطيك سبب عملي:
بدل تعريف helper function كل مرة…
تستخدم lambda:

* تعريف:

  * `lambda arguments: expression`
* أهم قاعدة: جسم lambda **expression واحدة** (بدون if/for/def… لأنها statements).
* لأن lambda هي **expression** تقدر تمررها مباشرة داخل call:

  * `count(xs, lambda x: ...)`

### جزء مهم في الملف: Expressions vs Statements

الكورس يفرق:

* expression: شيء يقيّم لقيمة (ثوابت/عمليات/استدعاء دوال…)
* statement: if/for/def/class… (لا يمكن وضعها داخل print كقيمة)

**الرسالة:**

> lambda نافعة لأنك تحتاج function “سريعة” مكان ما تنادي دالة أخرى مثل key/condition.

---

## 03.2 `03-sorting.md` — Sorting: `sorted` vs `list.sort` + `__lt__` + `key`

الكورس يشرح:

* `sorted(xs)` يرجع **قائمة جديدة**
* `xs.sort()` يرتب **in-place**

### كيف بايثون يعرف الترتيب؟

* افتراضيًا يعتمد على `<` (وبالتالي `__lt__` في objects).

لكن: تعريف `__lt__` واحد “يقيّدك” بترتيب واحد فقط.

### الحل المرن: `key=...`

تعطي sort دالة تُرجع “القيمة التي نرتب بها”:

* `cards.sort(key=lambda card: card.value)`
* `cards.sort(key=lambda card: card.suit)`

### Sorting by multiple values

الكورس يعتمد tuples:

* `key=lambda card: (card.suit, card.value)`
  لأن tuple تقارن عنصر-بعنصر.

---

## 03.3 `05-min-max.md` — `min`/`max` مع objects عبر `key`

مثل sort:

* `max(people, key=lambda p: p.age)` للحصول على الأكبر عمرًا
* وينطبق على `min` أيضًا.

---

## 03.4 `07-lambas-vs-nested.md` — Lambda vs Nested

الكورس يقول:

* lambda نوع من nested function (تتعرّف في نفس المكان).
* تُستخدم:

  1. عندما **تحتاج** nested function
  2. أو عندما تريد one-liner ستستخدمه مرة واحدة فقط.

---

## Assignments (03-lambdas)

* **02-lambdas**

  * grouping/partition على cards باستخدام lambdas + util.py
  * `group_by_suit`, `group_by_value`, `partition_by_color`
* **04-sorting**

  * دوال sort ترجع **قائمة جديدة** ولا تعدل الأصل
  * by age (صاعد/نازل) + by name + by (name, age)
* **06-min-max**

  * `closest(points, target_point)` باستخدام `min`/`key` (ومراعاة tie: أول عنصر في القائمة).

---

# 04) Comprehensions

## 04.1 `01-mapping.md` — Mapping → List comprehension

نمط متكرر:

* loop + append لتحويل كل عنصر إلى نتيجة
  الكورس يسميه mapping ويعطي الصيغة:
* `[map(element) for element in input_list]`

ويذكر أن comprehensions قد تكون أسرع (benchmark.py مثال).

---

## 04.2 `03-filtering.md` — Filtering + دمج map/filter

Filtering:

* `[item for item in input_list if condition(item)]`
  وممكن تجمع:
* `[person.name for person in people if person.age >= 18]`

الكورس يقترح كتابة comprehension متعددة الأسطر لتحسين القراءة.

---

## 04.3 `05-set-comprehensions.md` — Set comprehensions

* `{expr for x in xs}`
  ميزة set: إزالة التكرار تلقائيًا.

---

## 04.4 `07-dictionary-comprehension.md` — Dict comprehensions

* `{key_expr: value_expr for x in xs}`
  مثال: `students_by_id = {student.id: student for student in students}`

---

## 04.5 `09-flatten.md` — Nested loops داخل comprehension + Flatten

تحويل nested loops:

* `[f(x, y) for x in xs for y in ys]`
  ويشرح الفرق بين:
* قائمة مسطحة vs قائمة “قوائم داخلها” عند وجود `[[...]]`

ويطبقها على flatten:

* `[element for lst in argument for element in lst]`

ويحذر: كلما زاد if/for داخل comprehension صار الفهم أصعب → ارجع للـ for-loops لفهمها.

> ملاحظة داخل مثال طويل في الملف: عند تحويله لـ nested loops، يظهر سطر `result.append(result)` (واضح أنه المقصود `result.append(element)`؛ انتبه لهذه التفاصيل أثناء المذاكرة).

---

## 04.6 `11-builtin-functions.md` — Built-ins مهمة مع iterables

الكورس يسرد built-ins التي كثيرًا تأتي مع comprehensions:

* `len`
* `min`, `max` (لا تمرر empty collection)
* `sum`
* `all`, `any`
* `zip` (تجميع عناصر بزوج)
* `enumerate` (عنصر + index)

**الرسالة الذهبية في بدايته:**

> الدوال لا تهتم كيف بنيت collection… المهم أنها **iterable**.

---

## Assignments (04-comprehensions)

* **02-mapping**

  * `titles`, `titles_and_years`, `titles_and_actor_counts`, `reverse_words`
* **04-filtering**

  * `movies_from_year`, `movies_with_actor`, `divisors(n)` (مرتبة تصاعديًا)
* **06-set-comprehension**

  * `directors(movies)` + `common_elements(xs, ys)`
* **08-dictionary-comprehension**

  * `title_to_director`, `director_to_titles` (يمزج أكثر من comprehension)
* **10-flatten**

  * `genres(movies)` و `actors(movies)` (تجميع من قوائم داخل movie)
  * `repeat_consecutive(xs, n)` vs `repeat_alternating(xs, n)`
  * `cards(values, suits)` (set من Card)
* **12-builtin-functions**

  * مجموعة كبيرة تعتمد comprehensions + built-ins:

    * count/longest runtime/any-all/prime/increasing/weighted_sum/alternating_caps/find_repeated_words…
* **13-group-movies-by-year**

  * dict: year → list of titles

---

# 05) Iterable + Generators

## 05.1 `00-iterables.md` — ما معنى Iterable؟

الكورس يذكرك:

* Lists/Tuples/Strings/Sets/Dicts… مختلفة
  لكن القاسم المشترك: تقدر تعمل عليها `for element in coll`.

ويذكر أمثلة لدوال تعمل على أي iterable:

* `min/max/sum/all/any`
* comprehensions
* `" ".join(collection)`

---

## 05.2 `01-generators.md` — Generator functions (`yield`)

الكورس يشرح:

* `yield` يشبه `return` لكنه **يوقف التنفيذ** ويكمله عند طلب القيمة التالية.
* إذا كسرت loop بدري: باقي yields لن تُنفذ.
* مجرد استدعاء generator function بدون iteration: لا يحدث شيء (لا يبدأ التنفيذ).

### نقاط تركيز قوية في الملف

* توفير ذاكرة: generator لا يخزن كل القيم (مثال `sys.getsizeof`)
* `next(iterator)` لجلب القيم واحدة واحدة
* Generators لا نهائية ممكنة (مع `while True`)
* فرق مهم:

  * **iterable** يمكن تكراره أكثر من مرة
  * **generator/iterator** “ينصرف/يُستهلك” بعد مرور واحد (spent)

ويشرح أن `range` ليس generator function بل class تنفذ iterable protocol.

---

## 05.3 `06-generator-comprehension.md` — Generator Expressions

صيغة:

* `(expr for x in xs)`

الهدف:

* بدل ما تعمل list مؤقتة ثم ترميها بعد `min/sum/all`…
* مرّر generator expression لتقليل الذاكرة:

  * `sum(item.price for item in shopping_basket)`
  * وتقدر تحذف الأقواس غالبًا داخل هذه الدوال.

---

## Assignments (05-iterable)

* `repeat(value)` generator لا نهائي يكرر نفس القيمة.
* `cycle(xs)` generator يعيد عناصر xs للأبد.
* `fizzbuzz()` generator لا نهائي حسب قواعد fizz/buzz/fizzbuzz.
* `rle_encode(data)` و `rle_decode(data)` (كلاهما generator) ويشتغلان مع iterable أو iterator.
* `is_prime(n)` + `primes()` iterator لكل الأعداد الأولية.

---

# 06) Itertools

## `01-itertools.md`

ملف قصير لكنه واضح:

* `itertools` فيه وظائف “iterator-centric”
* يذكر `pairwise` كمثال:

  * `pairwise(range(5)) -> (0,1),(1,2),(2,3),(3,4)`
    ويطلب منك الاعتماد عليه في أول assignment، والباقي ابحث عن الدوال المناسبة داخل itertools.

## Assignments (06-itertools)

* `total_distance(path, distance)` باستخدام `pairwise` (path iterator).
* `find_shortest_path(distance, city_count)` (TSP) ويعطي hint: استخدم دالة من itertools (غالبًا permutations).
* `rle-revisited`: أعد كتابة encode/decode باستخدام itertools + generator comprehensions لتبسيط الحل.

---

# 07) Recursion

## `01-recursion.md` — Recursion = base case + recursive case

الكورس يشرح الهيكل الثابت لأي recursion:

* Base case: توقف
* Recursive case: تقلص المشكلة وتنادي نفسها

مثال factorial:

* `factorial_recursive(n) = n * factorial_recursive(n-1)`
  ويذكر:
* كل نداء يضيف stack frame على call stack حتى نصل للـ base case.

## Assignments (07-recursion)

* `fibonacci(number)` recursion + سؤال ضمني: لماذا النسخة البسيطة غير فعالة؟
* `reverse_from_left(text)` و `reverse_from_right(text)` (فكرتان مختلفتان لعكس النص recursively).
* `sum_numbers(number)` (جمع أرقام العدد حتى لو سالب مثل المثال).
* `countX(text)` عدد مرات x في النص.
* `findMaximum(list)` recursion (والقائمة الفارغة يجب أن تنتج IndexError).
* `fractals` باستخدام turtle (مذكور صراحة: turtle ليس ضمن الامتحان، لكنه تدريب recursion بصري).

---

# “قواعد تثبيت” سريعة للمذاكرة (بنَفَس الكورس)

1. **Hardcode؟ → Parameter** (Generalizing).
2. **الـ if شرط؟ → حوّله function** ثم مرره (Higher-order).
3. **شرط يحتاج قيمة إضافية؟ → Nested function أو lambda** داخل نفس scope.
4. **Sorting/Max/Min على objects؟ → استخدم key=lambda ...** بدل ما تربط نفسك بـ `__lt__`.
5. **Loop + append؟ → comprehension** (mapping/filtering/flatten).
6. **قوائم ضخمة أو “مؤقتة”؟ → generator expression** بدل list.
7. **Iterator vs Iterable**: iterator “يخلص”، iterable تعيد المرور عليه.
8. **Recursion = Base + Reduce** (لا recursion بدون base case واضح).

---

## سؤال واحد حتى نبدأ “اختبار فهم” سريع:

أي جزء تبغاه نعمل عليه تدريب قصير الآن: **higher-order**, ولا **comprehensions**, ولا **generators/itertools**, ولا **recursion**؟

```
```
