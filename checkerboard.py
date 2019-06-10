from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default():
    return render_template("checkerboard.html", x_value = 8, y_value = 8)

@app.route('/4')
def checkerboard_8_x_4():
    return render_template("checkerboard.html", x_value = int(8), y_value = int(4))

@app.route('/<x>/<y>')
def checkerboard_x_y(x, y):
    return render_template("checkerboard.html", x_value = int(x), y_value = int(y))

@app.route('/<x>/<y>/<c1>/<c2>')
def checkerboard_x_y_c1_c2(x, y, c1, c2):
    return render_template("checkerboard.html", x_value = int(x), y_value = int(y), color1 = c1, color2 = c2 )

if __name__ == "__main__":
    app.run(debug=True)