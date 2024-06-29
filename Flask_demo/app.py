from flask import Flask , render_template , jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'this is about page'

@app.route('/contact')
def contact():
    return 'this is contact page'

@app.route('/first')
def first():
    return render_template("index.html")

@app.route('/second')
def second():
    return render_template("abc.html")

@app.route('/firstapi')
def firstapi():
    return jsonify({"name":"govind","age":26})

 

if __name__ == "__main__":
    app.run(port=5555)