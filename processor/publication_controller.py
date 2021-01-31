from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello/')
def hello():
    return render_template('hello.html', name="name")


@app.route('/loop/')
def loop():
    l = [str(f"These are few {i}") for i in range(11)]
    return render_template('loop.html', rows=l)


if __name__ == "__main__":
    app.run()
