from application import db
from application import __init__

db.create_all()

sample_todo = ToDo(
    task = "Sample todo",
    completed = False
)
db.session.add(sample_todo)
db.session.commit()