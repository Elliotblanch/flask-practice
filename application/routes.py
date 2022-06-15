from application import app, db
from application.models import ToDo

@app.rout('/')
def index():
    todo = ToDo.query.first()
    return f'Task: {todo.task} Completed: {todo.completed}

@app.route('/add')
def add():
    return 'Added a new todo'
