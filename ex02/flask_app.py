from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World (in index paage)'

@app.route('/hello')
def hello():
    return 'Hello, World (in hello page)'	
	
	
if __name__ == "__main__":
    app.run()