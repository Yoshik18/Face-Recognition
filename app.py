from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index(name=None):
    if request.method == "POST":
        face_id = request.form['face_id']
        import dataset
        render_template('index.html',name=name)
    else:
        return render_template('index.html',name=name)

@app.route('/train')
def parse(name=None):
    import training
    print("done")
    return render_template('index.html',name=name)

@app.route('/recognize')
def parse1(name=None):
	import recognize
	print("done")
	return render_template('index.html',name=name)

if __name__ == '__main__':
    app.run(debug=True)