from datetime import datetime
from flask import Flask, render_template,request,redirect,url_for, jsonify
from sqlalchemy.orm import backref
from forms import Todo
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/database.db'
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(240))
    tickets = db.relationship('Ticket', backref='author', lazy=True)
    def __repr__(self):
        return f"User ('{self.username}', '{self.id}')"

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(240), nullable=False)
    body = db.Column(db.Text())
    assigned_to = db.Column(db.String(240))
    completed = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Ticket( '{self.id}', '{self.title}', '{self.assigned_to}', '{self.completed}')"
# db.create_all()
# user = UserModel(username='mark', password='passwerd')
# db.session.add(user)
# db.session.commit()
# todos= TodoModel.query.filter_by(content='learn flask').first()
# print(todos.id)
# print(todos.content)

@app.route('/')
def index():
    request_method = request.method
    user = User.query.all()
    # if request.method == 'POST':
    #     first_name = request.form['first_name']
    #     return redirect(url_for('name', first_name=first_name))
    return render_template('index.html')
    # return render_template('index.html', request_method=request_method, todo=todo)

# @app.tickets('/tickets')
# def tickets():
#     re

@app.route('/signup')
def signup():
    return jsonify({"username": "mark", "password": "passwerd", "id": 1})

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/register')
def register():
    success = False
    if success == True:
        return render_template('success.html')
    else:
        return render_template('failure.html')

@app.route('/name/<string:first_name>')
def name(first_name):
    return first_name


@app.route('/users', methods=['POST'])
def todo():
    todo_form = Todo()
    if todo_form.validate_on_submit():
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        print(todo_form.content.data)
        todo = TodoModel(content="just some test string") 
       
        # db.session.add(todo) 
        # print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        # db.session.commit()
       
        return redirect('/')
    return render_template('todo.html', form=todo_form)

# if this file is run directly, run in debug mode
if __name__ == '__main__':
    app.run(debug=True)