from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_World():
    return 'first assignments'

@app.route('/test')
def test_template():
    return render_template('test.html') 


app.run(debug=True)