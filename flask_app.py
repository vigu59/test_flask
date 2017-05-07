
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<html><body> <h1>Hello 2 from  Vincent Flask</h1></body></html>'

if __name__ == "__main__":
    app.run()
