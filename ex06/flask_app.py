from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/save/', methods=['GET', 'POST'])
def write():
	data = request.form['Author']+" - "+request.form['Phrase']
	fo= open("test1.txt", "a+")
	fo.write(data+"\n")
	fo.close()
	return render_template('index.html')
	
@app.route('/read/')
def read():	
	fo= open("test1.txt", "r")
	data1=fo.read()
	fo.close()
	return data1
	

@app.route('/')
def render_static():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug = True)

#app.run(debug = True)