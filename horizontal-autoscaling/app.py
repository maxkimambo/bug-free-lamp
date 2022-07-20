import sys
import flask 
from flask import Flask, jsonify, request

app = flask.Flask(__name__)

sys.setrecursionlimit(100000)

@app.route('/<n>', methods=['GET'])
def calculate_fibonacci(n=0):

    v = int(n)
    result = _fib(v)
    return jsonify({v: str(result)})


def _fib(n):
    '''
        Inefficient fibonacci implementation to trigger cpu load
    '''
    if n <= 1:
        return n
    return _fib(n-1) + _fib(n-2)


if __name__ == "__main__":
    app.run()
