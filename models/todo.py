from database.database import db


class Todo:
    def __init__(self, id, todo_name, priority_level, deadline_date, deadline_time, status, created_at):
        self.id = id
        self.todo_name = todo_name
        self.priority_level = priority_level
        self.deadline_date = deadline_date
        self.deadline_time = deadline_time
        self.created_at = created_at
        self.status = status

    @staticmethod
    def get_all_todos():
        cursor = db.cursor()
        cursor.execute("SELECT * FROM todos")
        todo_list = cursor.fetchall()
        final_todos = []
        for todo in todo_list:
            todo_obj = Todo(
                id=todo[0],
                todo_name=todo[1],
                priority_level=todo[2],
                deadline_date=todo[3],
                deadline_time=todo[4],
                status=todo[5],
                created_at=todo[6]
            )
            final_todos.append(todo_obj)
        return final_todos

    def create_todo(self):
        cursor = db.cursor()
        cursor.execute(f'insert into todos ("{self.id}", "{self.todo_name}", "{self.priority_level}"," {self.deadline_date}"," {self.deadline_time}"," {
                       self.status}", "{self.created_at}") values("1", "cook", "medium", "20 Aug 2024" , "6: 00 PM" ,"pending", "19 Aug 2024")')
        db.commit()
        return "todo added"

    @staticmethod
    def delete_todo(id):
        cursor = db.cursor()
        cursor.execute(f"delete from todo where id = {id}")
        db.commit()
        return "todo deleted"

    @staticmethod
    def complete_todo(id):
        cursor = db.cursor()
        cursor.execute(f"update todo where id = {id} set status = 'completed'")
        db.commit()
        return "todo completed"
