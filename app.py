from flask import Flask, render_template,request,redirect,url_for
from forms import Todo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'

@app.route('/',methods=['GET','POST'])
def index():
    request_method = request.method
    if request.method == 'POST':
        print('-------')
        print(dict(request.form))
        first_name = request.form['first_name']
        print('-------')
        return redirect(url_for('name', first_name=first_name))
    return render_template('index.html', request_method=request_method)

@app.route('/name/<string:first_name>')
def name(first_name):
    return first_name


@app.route('/todo', methods=['GET','POST'])
def todo():
    todo_form = Todo()
    if todo_form.validate_on_submit():
        print(todo_form.content.data)
        return redirect('/')
    return render_template('todo.html', form=todo_form)

# if this file is run directly, run in debug mode
if __name__ == '__main__':
    app.run(debug=True)