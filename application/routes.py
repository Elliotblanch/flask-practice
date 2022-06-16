from application import app, db
from application.models import ToDo
from flask import redirect, url_for, render_template

@app.rout('/')
def index():
    todo = ToDo.query.query.all()
    #empstr = ""
    #for name in todo:
        #empstr += f'{name} {name.completed} <br>'

    #return empstr
    reteurn render_template("task.html", todos=todo)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/add/<name>')
def add(name):
    todo = ToDo(task = name)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<name>')
def complete(name):
    todo = ToDo.query.filter_by(task=name).first()
    todo.complete = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<name>')
def incomplete(name):
    todo = ToDo.query.filter_by(task=name).first()
    todo.complete = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<oldName>/<newName>')
def update(name):
    todo = ToDo.query.filter_by(task=oldName).first()
    todo.task = newName
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<name>')
def delete(name):
    todo = ToDo.query.filter_by(task=name).first()
    db.session.delete()
    return redirect(url_for('index'))