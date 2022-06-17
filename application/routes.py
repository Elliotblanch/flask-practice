from application import app, db
from application.models import Todo
from application.forms import TaskForm
from flask import redirect, url_for, render_template, request

@app.route('/')
def index():
    todo = Todo.query.all()
    #empstr = ""
    #for name in Todo:
        #empstr += f'{name} {name.completed} <br>'

    #return empstr
    return render_template('task.html', todos=todo)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/add', methods = ['GET','POST'])
def add():
    form = TaskForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            taskData = Todo(
                task = form.task.data,
                completed = form.completed.data
            )
            db.session.add(taskData)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('addtask.html', form=form)

@app.route('/complete/<name>')
def complete(name):
    todo = Todo.query.filter_by(task=name).first()
    todo.complete = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<name>')
def incomplete(name):
    todo = Todo.query.filter_by(task=name).first()
    todo.complete = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<oldName>/<newName>')
def update(name):
    todo = Todo.query.filter_by(task=oldName).first()
    todo.task = newName
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))