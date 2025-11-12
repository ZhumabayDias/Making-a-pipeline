from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # простая страничка
    return "Hello, Sec CI!"

if __name__ == "__main__":
    app.run()