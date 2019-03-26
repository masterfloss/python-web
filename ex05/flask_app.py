from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def render_static():
    return render_template('form.html')

@app.route('/save/', methods=['GET', 'POST'])
def index():
	data = request.form['Author']+" - "+request.form['Phrase']
	fo= open("test1.txt", "a+")
	fo.write(data+"\n")
	fo.close()
	return "thank you"	

if __name__ == '__main__':
    app.run(debug = True)
