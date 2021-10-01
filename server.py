from flask import Flask, render_template, request, redirect,session

app = Flask(__name__)
app.secret_key="Pass123"

@app.route('/', methods=["GET"])
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/2', methods=["GET"])
def index2():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 2
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


#http://127.0.0.1:5000/



if __name__=="__main__":
    app.run(debug=True)