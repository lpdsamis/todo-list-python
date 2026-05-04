import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """تحميل المهام من ملف JSON"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    
    def save_tasks(self):
        """حفظ المهام في ملف JSON"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)
    
    def add_task(self, title, priority="عادية"):
        """إضافة مهمة جديدة"""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "priority": priority,
            "status": "pending",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ تم إضافة المهمة: {title}")
    
    def list_tasks(self, status=None):
        """عرض المهام"""
        if not self.tasks:
            print("📭 لا توجد مهام حالياً")
            return
        
        tasks_to_show = self.tasks
        if status:
            tasks_to_show = [t for t in self.tasks if t["status"] == status]
        
        print("\n" + "="*60)
        print(f"{'ID':<5} {'الحالة':<10} {'الأولوية':<10} {'المهمة':<30}")
        print("="*60)
        
        for task in tasks_to_show:
            status_icon = "✅" if task["status"] == "completed" else "⏳"
            priority_icon = "🔴" if task["priority"] == "عالية" else "🟡" if task["priority"] == "متوسطة" else "🟢"
            print(f"{task['id']:<5} {status_icon:<10} {priority_icon:<10} {task['title']:<30}")
        print("="*60 + "\n")
    
    def complete_task(self, task_id):
        """تحديد مهمة كمكتملة"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "completed"
                task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_tasks()
                print(f"🎉 تم إكمال المهمة: {task['title']}")
                return
        print(f"❌ لم يتم العثور على مهمة بالرقم {task_id}")
    
    def delete_task(self, task_id):
        """حذف مهمة"""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                deleted = self.tasks.pop(i)
                self.renumber_tasks()
                self.save_tasks()
                print(f"🗑️ تم حذف المهمة: {deleted['title']}")
                return
        print(f"❌ لم يتم العثور على مهمة بالرقم {task_id}")
    
    def renumber_tasks(self):
        """إعادة ترقيم المهام بعد الحذف"""
        for i, task in enumerate(self.tasks, start=1):
            task["id"] = i

def main():
    todo = TodoList()
    
    while True:
        print("\n📋 نظام إدارة المهام")
        print("1. ➕ إضافة مهمة")
        print("2. 📋 عرض جميع المهام")
        print("3. ⏳ عرض المهام غير المكتملة")
        print("4. ✅ عرض المهام المكتملة")
        print("5. ✔️ تحديد مهمة كمكتملة")
        print("6. 🗑️ حذف مهمة")
        print("7. 🚪 خروج")
        
        choice = input("\nاختر خيار (1-7): ")
        
        if choice == "1":
            title = input("أدخل عنوان المهمة: ")
            if title:
                print("اختر الأولوية:")
                print("1. عالية 🔴")
                print("2. متوسطة 🟡")
                print("3. عادية 🟢 (افتراضي)")
                priority_choice = input("اختر (1-3): ")
                
                priority_map = {"1": "عالية", "2": "متوسطة", "3": "عادية"}
                priority = priority_map.get(priority_choice, "عادية")
                
                todo.add_task(title, priority)
            else:
                print("⚠️ عنوان المهمة لا يمكن أن يكون فارغاً")
        
        elif choice == "2":
            todo.list_tasks()
        
        elif choice == "3":
            todo.list_tasks(status="pending")
        
        elif choice == "4":
            todo.list_tasks(status="completed")
        
        elif choice == "5":
            try:
                task_id = int(input("أدخل رقم المهمة التي تريد إكمالها: "))
                todo.complete_task(task_id)
            except ValueError:
                print("❌ الرجاء إدخال رقم صحيح")
        
        elif choice == "6":
            try:
                task_id = int(input("أدخل رقم المهمة التي تريد حذفها: "))
                todo.delete_task(task_id)
            except ValueError:
                print("❌ الرجاء إدخال رقم صحيح")
        
        elif choice == "7":
            print("👋 مع السلامة!")
            break
        
        else:
            print("❌ خيار غير صحيح، حاول مرة أخرى")

if __name__ == "__main__":
    main()
