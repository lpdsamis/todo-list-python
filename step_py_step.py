 # a تجزئة كود To-Do List خطوة بخطوة للمبتدئين

# a1 استيراد المكتبات (الأدوات المساعدة)

# todo.py - الجزء 1 من 7


import json      # مكتبة للتعامل مع ملفات JSON (حفظ المهام)
import os        # مكتبة للتعامل مع نظام الملفات (التحقق من وجود الملفات)
from datetime import datetime  # مكتبة للتعامل مع التواريخ والأوقات

#b1 شرح:
# - json: تساعدنا في تحويل المهام من/إلى ملف التخزين
# - os: نتحقق منها إذا كان ملف tasks.json موجود أم لا
# - datetime: نسجل وقت إضافة المهمة ووقت إكمالها

# a2 إنشاء هيكل الكلاس (الصندوق السحري)

# todo.py - الجزء 2 من 7
#a2 تعريف الكلاس TodoList (مثل قالب لصنع قائمة مهام)

class TodoList:
    """
    هذا الكلاس مسؤول عن إدارة قائمة المهام.
    يحتوي على:
    - مكان تخزين المهام (filename)
    - قائمة المهام (tasks)
    - دوال للتعامل مع المهام (add, show, complete, delete)
    """
    
    #a2 دالة البناء (تشتغل تلقائياً عند إنشاء كائن جديد)
    def __init__(self, filename="tasks.json"):
        """
        filename: اسم ملف التخزين (tasks.json هو الاسم الافتراضي)
        """
        self.filename = filename  # نخزن اسم الملف في الكائن
        self.tasks = self.load_tasks()  # نحمل المهام من الملف (أو نبدأ بقائمة فارغة)
        
# a2 شرح بسيط للطالب:

class = قالب لصنع كائنات (مثل قالب الكعك)

__init__ = دالة خاصة تشتغل عند إنشاء الكائن

self = يشير إلى الكائن نفسه (مثل "أنا")

self.tasks = خاصية خاصة بالكائن (قائمة المهام)

#a2 جرب إنشاء كائن من الكلاس

my_list = TodoList()
print(my_list.filename)  # ماذا سيطبع؟
print(my_list.tasks)     # ماذا سيطبع؟

#================= a3 دالتا الحفظ والتحميل (الذاكرة) ============================

# todo.py - الجزء 3 من 7
#a3 دالتان للتعامل مع ملف التخزين (tasks.json)

def load_tasks(self):
    """
    تحميل المهام المخزنة من ملف JSON
    الإرجاع: قائمة المهام (أو قائمة فارغة إذا لم يوجد ملف)
    """
    # هل الملف موجود؟
    if os.path.exists(self.filename):
        # افتح الملف للقراءة (r = read)
        with open(self.filename, 'r', encoding='utf-8') as file:
            # json.load تحول JSON من الملف إلى قائمة Python
            return json.load(file)
    # إذا لم يوجد ملف، نرجع قائمة فارغة
    return []

def save_tasks(self):
    """
    حفظ المهام الحالية في ملف JSON
    """
    # افتح الملف للكتابة (w = write)
    with open(self.filename, 'w', encoding='utf-8') as file:
        # json.dump تحول قائمة Python إلى JSON وتحفظها في الملف
        # ensure_ascii=False: يسمح بكتابة العربية
        # indent=2: يجعل الملف منسقاً وجميلاً
        json.dump(self.tasks, file, ensure_ascii=False, indent=2)
        
# a3 شرح بسيط:

os.path.exists() = هل الملف موجود؟

with open(...) as file = افتح الملف وأغلقه تلقائياً بعد الانتهاء

'r' = قراءة، 'w' = كتابة

json.load() = اقرأ JSON وحوله إلى Python

json.dump() = حول Python إلى JSON واحفظه

## ===== a3 تمرين للطالب: =========

# a3  جرب حفظ واسترجاع بيانات
test_list = TodoList()
test_list.tasks = [{"id": 1, "title": "تعلم Python"}]
test_list.save_tasks()  # سيُنشئ ملف tasks.json

#a3 افتح ملف tasks.json وشاهد محتواه
#a3 ثم عدل الملف يدوياً وشغل load_tasks()

# ===== a4  إضافة مهمة جديدة (القلب النابض) ========

# todo.py - الجزء 4 من 7
#a4 دالة إضافة مهمة جديدة

def add_task(self, title, priority="medium"):
    """
    إضافة مهمة جديدة إلى القائمة
    title: عنوان المهمة (نص)
    priority: الأولوية (high, medium, low) - افتراضياً medium
    """
    # a4 بناء قاموس (dictionary) يمثل المهمة
    task = {
        "id": len(self.tasks) + 1,     # رقم تلقائي (طول القائمة + 1)
        "title": title,                 # عنوان المهمة
        "priority": priority,           # الأولوية
        "status": "pending",            # الحالة: pending (قيد الانتظار)
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # وقت الإضافة
    }
    
    #a4 نضيف المهمة إلى قائمة المهام
    self.tasks.append(task)
    
    #a4 نحفظ التغييرات في الملف
    self.save_tasks()
    
    #a4 نطبع رسالة تأكيد للمستخدم
    print(f"✅ تمت إضافة المهمة: {title}")
    
# ======== a4 شرح تفصيلي: ========

a4 القاموس (dictionary): مثل جدول يحتوي مفاتيح وقيم

"id" → الرقم التسلسلي

"title" → عنوان المهمة

"priority" → الأولوية

"status" → هل أُكملت أم لا؟

"created_at" → وقت الإضافة

len(self.tasks) + 1: عدد المهام الحالي + 1 ليعطي رقماً جديداً

datetime.now().strftime(...): الوقت الحالي بصيغة معينة

#========== a4 تمرين للطالب: =====================

#a4 جرب إضافة مهمة
my_todo = TodoList()
my_todo.add_task("شراء الخبز", "high")
my_todo.add_task("دراسة Python", "medium")

#a4 شاهد قائمة المهام
print(my_todo.tasks)

# ===== a5 عرض المهام (الشاشة الرئيسية) =========

# todo.py - الجزء 5 من 7
#a5 دالة عرض المهام بطريقة جميلة ومنظمة

def list_tasks(self):
    """
    عرض جميع المهام في جدول منظم
    """
    #a5 إذا كانت القائمة فارغة
    if not self.tasks:
        print("📭 لا توجد مهام حالياً")
        return
    
    #a5 طباعة رأس الجدول
    print("\n" + "="*70)
    print(f"{'ID':<5} {'الحالة':<10} {'الأولوية':<10} {'المهمة':<40}")
    print("="*70)
    
    #a5 المرور على كل مهمة في القائمة
    for task in self.tasks:
        #a5 تحديد رمز الحالة (✅ للـ completed, ⏳ للـ pending)
        if task["status"] == "completed":
            status_icon = "✅"
        else:
            status_icon = "⏳"
        
        #a5 تحديد رمز الأولوية
        if task["priority"] == "high":
            priority_icon = "🔴 عالية"
        elif task["priority"] == "medium":
            priority_icon = "🟡 متوسطة"
        else:  # low
            priority_icon = "🟢 عادية"
        
        #a5 طباعة المهمة في صف
        print(f"{task['id']:<5} {status_icon:<10} {priority_icon:<15} {task['title']:<40}")
    
    #a5 طباعة خط فاصل في النهاية
    print("="*70 + "\n")
 
 # ===== a6 إكمال وحذف المهام (التحكم) ===========
 
 # todo.py - الجزء 6 من 7
#a6 دالتين لتعديل المهام (إكمال وحذف)

def complete_task(self, task_id):
    """
    تحديد مهمة كمكتملة بناءً على رقمها
    task_id: رقم المهمة
    """
    #a6 نبحث في قائمة المهام
    for task in self.tasks:
        if task["id"] == task_id:  # وجدنا المهمة
            task["status"] = "completed"  # نغير الحالة
            #a6 نسجل وقت الإكمال
            task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_tasks()  # نحفظ التغييرات
            print(f"🎉 مبروك! تم إكمال: {task['title']}")
            return  # نخرج من الدالة
    #a6 إذا وصلنا هنا، لم نجد المهمة
    print(f"❌ لا توجد مهمة برقم {task_id}")

def delete_task(self, task_id):
    """
    حذف مهمة من القائمة
    task_id: رقم المهمة
    """
    #a6 نبحث باستخدام index (رقم الموقع في القائمة)
    for i, task in enumerate(self.tasks):
        if task["id"] == task_id:
            #a6 نحذف المهمة من القائمة
            deleted = self.tasks.pop(i)
            #a6 نعيد ترقيم المهام (لأننا حذفنا واحدة)
            self._renumber_tasks()
            #a6 نحفظ التغييرات
            self.save_tasks()
            print(f"🗑️ تم حذف: {deleted['title']}")
            return
    print(f"❌ لا توجد مهمة برقم {task_id}")

def _renumber_tasks(self):
    """
    إعادة ترقيم المهام (تسمى بعد الحذف)
    _ قبل الاسم يعني: دالة داخلية لا تستخدم خارج الكلاس
    """
    for i, task in enumerate(self.tasks, start=1):
        task["id"] = i  # نعيد كتابة الأرقام من 1 إلى N
 
# ========= a6 شرح دوال بايثون المستخدمة: =======

# ===== enumerate(list) = يعطي رقم الفهرس والعنصر معاً ======

for i, item in enumerate(["a", "b", "c"]):
    print(i, item)  # 0 a, 1 b, 2 c

# ======= list.pop(index) = يحذف العنصر ويرجعه ========
# ======== _renumber_tasks = دالة خاصة (underscore) يستخدمها الكلاس داخلياً فقط ====

#========== a6 تمرين للطالب: =====================

#a6 جرب إكمال وحذف المهام

my_todo = TodoList()
my_todo.add_task("مهمة 1", "high")
my_todo.add_task("مهمة 2", "medium")
my_todo.add_task("مهمة 3", "low")

my_todo.list_tasks()        # شاهد المهام
my_todo.complete_task(2)    # أكمل المهمة رقم 2
my_todo.list_tasks()        # شاهد التغيير
my_todo.delete_task(1)      # احذف المهمة رقم 1
my_todo.list_tasks()        # ماذا بقي؟

# ========= a7 واجهة المستخدم (القائمة والتفاعل) ========================

# todo.py - الجزء 7 من 7
# واجهة سطر الأوامر للمستخدم

def display_menu():
    """عرض قائمة الخيارات للمستخدم"""
    print("\n" + "="*40)
    print("📋 قائمة إدارة المهام")
    print("="*40)
    print("1. ➕ إضافة مهمة جديدة")
    print("2. 📋 عرض جميع المهام")
    print("3. ✅ تحديد مهمة كمكتملة")
    print("4. 🗑️ حذف مهمة")
    print("5. 🚪 خروج")
    print("="*40)

def main():
    """
    الدالة الرئيسية - تشغل التطبيق وتستقبل اختيارات المستخدم
    """
    print("🎯 مرحباً بك في تطبيق To-Do List!")
    
    #a7 ننشئ كائن TodoList واحد ونستخدمه طوال البرنامج
    todo = TodoList()
    
    #a7 حلقة لا نهائية (تكرر حتى يختار المستخدم الخروج)
    while True:
        display_menu()  # نعرض القائمة
        
        #a7 نطلب من المستخدم إدخال رقم
        choice = input("اختر رقم (1-5): ")
        
        #a7 نفحص الاختيار
        if choice == "1":
            #a7 إضافة مهمة
            title = input("أدخل عنوان المهمة: ").strip()
            
            if title:  # إذا العنوان ليس فارغاً
                print("\nاختر الأولوية:")
                print("1. عالية 🔴")
                print("2. متوسطة 🟡")
                print("3. عادية 🟢")
                
                priority_choice = input("اختر (1-3): ")
                
                #a7 تحويل رقم الاختيار إلى نص الأولوية
                if priority_choice == "1":
                    priority = "high"
                elif priority_choice == "2":
                    priority = "medium"
                else:
                    priority = "low"
                
                todo.add_task(title, priority)
            else:
                print("⚠️ عنوان المهمة لا يمكن أن يكون فارغاً!")
        
        elif choice == "2":
            #a7 عرض المهام
            todo.list_tasks()
        
        elif choice == "3":
            #a7 إكمال مهمة
            try:
                task_id = int(input("أدخل رقم المهمة المكتملة: "))
                todo.complete_task(task_id)
            except ValueError:
                print("❌ الرجاء إدخال رقم صحيح!")
        
        elif choice == "4":
            #a7 حذف مهمة
            try:
                task_id = int(input("أدخل رقم المهمة للحذف: "))
                todo.delete_task(task_id)
            except ValueError:
                print("❌ الرجاء إدخال رقم صحيح!")
        
        elif choice == "5":
            #a7 خروج
            print("👋 شكراً لاستخدام التطبيق! إلى اللقاء.")
            break  # نخرج من الحلقة (while)
        
        else:
            print("❌ اختيار غير صحيح! الرجاء المحاولة مرة أخرى.")

#a7 هذه الجملة تشغل البرنامج إذا نُفذ الملف مباشرة (وليس عند استيراده)
if __name__ == "__main__":
    main()

# ==========a7 شرح المكونات الجديدة: ==============

while True: = حلقة لا نهائية (تستمر حتى break)

.strip() = يزيل المسافات من بداية ونهاية النص

try/except = يمسك الأخطاء (مثل إدخال حرف بدل رقم)

int() = يحول النص إلى رقم

break = يخرج من الحلقة

# ========================= c جدول تلخيصي لجميع الدوال ====================


c الدالة	متى تُستخدم	ماذا تفعل                 	  ماذا ترجع
__init__()	عند إنشاء الكائن	تحضير الكائن	        None
load_tasks()	داخلياً عند البداية	تحميل المهام      	   قائمة (list)
save_tasks()	بعد كل تغيير	حفظ المهام	        None
add_task()	يطلب المستخدم	إضافة مهمة	        None
list_tasks()	يعرض المستخدم	عرض المهام	        None
complete_task()	يطلب المستخدم	إكمال مهمة	        None
delete_task()	يطلب المستخدم	حذف مهمة	        None
_renumber_tasks()	بعد الحذف	إعادة ترقيم	None
display_menu()	كل مرة	عرض القائمة	                None
main()	بداية البرنامج	تشغيل البرنامج	                None

