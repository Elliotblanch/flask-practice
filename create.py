from application import db
from application.models import Todo
from application import __init__

db.drop_all()
db.create_all()

sample_todo = Todo(
    task = "Sample todo",
    completed = False
)
db.session.add(sample_todo)
db.session.commit()