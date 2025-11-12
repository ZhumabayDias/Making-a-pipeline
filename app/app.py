from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    # простая страничка
    return "Hello, Sec CI!"

@app.route('/unsafe')
def unsafe():
    expr = request.args.get('expr', '2+2')
    result = eval(expr)
    return f"Result: {result}"
