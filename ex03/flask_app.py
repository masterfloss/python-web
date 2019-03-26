from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_static():
    return render_template('form.html')

@app.route('/hello')
def hello():
    return 'Hello, World (in hello page)'	
	
	
if __name__ == "__main__":
    app.run()