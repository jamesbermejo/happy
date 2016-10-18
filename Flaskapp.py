@app.route('/root')
def root():
    return "hello flask"
@app.route('/greet')
def greet(name):
	return "Hello" + name"
