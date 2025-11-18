def cycle(xs):
    while True:        # ⚠️ حلقة لا نهائية
        for x in xs:   # 🔁 تمرير على كل عناصر القائمة
            yield x    # ⏸️ نرجع العنصر ونتوقف