#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Your index() view should be routed to at the base URL with /. It should Contain an h1 element that contains the title of this application, "Python Operations with Flask Routing and Views".

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return f'{param}'

@app.route('/count/<int:param>')
def count(param):
    numbers = [str(number) for number in range(param)]
    return '\n'.join(numbers) + '\n'

@app.route('/math/<num1>/<op>/<num2>')
def math(num1, op, num2):
    if op == '+':
        return str(int(num1) + int(num2))
    elif op == '-':
        return str(int(num1) - int(num2))
    elif op == '*':
        return str(int(num1) * int(num2))
    elif op == 'div':
        if num2 != 0:
            return str(int(num1) / int(num2))
        else:
            return "NO"
    elif op == '%':
        return str(int(num1) % int(num2))


if __name__ == '__main__':
    app.run(port=5556, debug=True)
