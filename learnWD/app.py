from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def day1():
	return render_template('day1.html')
	
@app.route('/day2')
def day2():
	return render_template('day2.html')

@app.route('/day3')
def day3():
	return render_template('day3.html')


if __name__ == '__main__':
	app.run(debug=True)
