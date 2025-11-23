
class TaskService:
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def get_all(self):
        return self.tasks
    
    def create(self, data):
        task = {
            "id": self.counter,
            "title": data.get("title"),
            "done": False
        }
        self.counter += 1
        self.tasks.append(task)
        return task
    
    def get(self, task_id):
        return next((task for task in self.tasks if task["id"] == task_id), None)

    def update(self, task_id, data):
        task = self.get(task_id)
        if not task:
            return None
        task["title"] = data.get("title")
        task["done"] = data.get("done")
        return task

    def delete(self, task_id):
        task = self.get(task_id)
        if not task:
            return False
        print(task)
        self.tasks.remove(task)
        return True
