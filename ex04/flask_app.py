from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def render_static():
    return render_template('form.html')
	
@app.route('/save/', methods=['GET', 'POST'])
def hello():
    return 'Hello!!!'	
	
if __name__ == "__main__":
    app.run()
