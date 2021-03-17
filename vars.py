from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<string:name>')
def greet(name):
    return render_template('index.html', list_of_names=["Mark","Sherman","Carrie"])


if __name__=='__main__':
    app.run(debug=True)