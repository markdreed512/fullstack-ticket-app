from flask import Flask, render_template,request,redirect,url_for
from forms import Todo
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
db = SQLAlchemy(app)

class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(240))

    def __str__(self):
        # will return string representation of the model:
        return f'{self.content}, {self.id}'

# db.create_all()
# todo = TodoModel(content='learn flask')
# db.session.add(todo)
# db.session.commit()
# todos= TodoModel.query.filter_by(content='learn flask').first()
# print(todos.id)
# print(todos.content)

@app.route('/',methods=['GET','POST'])
def index():
    request_method = request.method
    todo = TodoModel.query.all()
    if request.method == 'POST':
        first_name = request.form['first_name']
        return redirect(url_for('name', first_name=first_name))
    return render_template('index.html', request_method=request_method, todo=todo)

@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/name/<string:first_name>')
def name(first_name):
    return first_name


@app.route('/todo', methods=['GET','POST'])
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