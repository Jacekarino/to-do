from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=True)
    completed = db.Column(db.Integer, default=0)
    position = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, headline, content=None):
        self.headline = headline
        self.content = content

    def __repr__(self):
        return f'<Task {self.id}>'

@app.route('/')
def index():
    sort_by = request.args.get('sort', 'pos_asc')
    base_query = Todo.query.filter_by(completed=0)
    if sort_by == 'id_asc':
        tasks_todo = base_query.order_by(Todo.id.asc()).all()
    elif sort_by == 'id_desc':
        tasks_todo = base_query.order_by(Todo.id.desc()).all()
    elif sort_by == 'len_asc':
        tasks_todo = base_query.order_by(func.length(Todo.content).asc()).all()
    elif sort_by == 'len_desc':
        tasks_todo = base_query.order_by(func.length(Todo.content).desc()).all()
    elif sort_by == 'headline_asc':
        tasks_todo = base_query.order_by(Todo.headline.asc()).all()
    elif sort_by == 'headline_desc':
        tasks_todo = base_query.order_by(Todo.headline.desc()).all()
    else:
        tasks_todo = base_query.order_by(Todo.position.asc()).all()
    tasks_done = Todo.query.filter_by(completed=1).all()
    return render_template('index.html', tasks=tasks_todo, done=tasks_done, current_sort=sort_by)

@app.route('/reorder', methods=['POST'])
def reorder():
    order = request.get_json()
    for index, task_id in enumerate(order):
        task = Todo.query.get(int(task_id))
        if task:
            task.position = index
    db.session.commit()
    return 'OK'

@app.route('/add', methods=['POST'])
def add():
    task_headline = request.form.get('headline')
    task_content = request.form.get('content', '')
    
    if not task_headline:
        return redirect(url_for('index'))

    new_task = Todo(headline=task_headline, content=task_content)
    try:
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
    except:
        return 'An error occurred while adding the task'

@app.route('/complete/<int:id>')
def complete(id):
    task = Todo.query.get_or_404(id)
    task.completed = 1 if task.completed == 0 else 0
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'An error occurred while deleting the task'

@app.route('/delete_completed')
def delete_completed():
    Todo.query.filter_by(completed=1).delete()
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=5001)