from flask import flask

app=Flask(__name__)




@app.route('/')
def homepage():
    return "Hellow Universer"


if __name__ == '__main__':
    app.run(debug=True)