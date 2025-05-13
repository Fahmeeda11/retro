from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def page2():
    return 'Page 2'

if __name__ == '__main__':
    app.run(debug=True)