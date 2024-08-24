from database.database import db


class Todo:
    def __init__(self, todo_name, priority_level, deadline_date, deadline_time, status, id=None, created_at=None):
        self.id = id
        self.todo_name = todo_name
        self.priority_level = priority_level
        self.deadline_date = deadline_date
        self.deadline_time = deadline_time
        self.created_at = created_at
        self.status = status

    @staticmethod
    def get_all_todos():
        """
        get_all_todos method will fetch all todos from the database and convert it into a list of Todo's object
        """
        cursor = db.cursor()
        cursor.execute("SELECT * FROM todos ORDER BY created_at DESC")
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

        cursor.execute(f"INSERT INTO todos(todo_name, priority_level, deadline_date, deadline_time) VALUES('{
                       self.todo_name}', '{self.priority_level}', '{self.deadline_date}','{self.deadline_time}')")

        db.commit()

    @staticmethod
    def delete_todo(id):
        cursor = db.cursor()
        cursor.execute(f"DELETE FROM todos WHERE id = {id}")
        db.commit()

    @staticmethod
    def complete_todo(id):
        cursor = db.cursor()
        cursor.execute(
            f"UPDATE todos  SET status = 'completed' where id = {id}")
        db.commit()
        return "todo completed"
