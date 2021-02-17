from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')


@app.route('/info', methods=['POST'])
def info():
    response = request.form
    return render_template('info.html', information=response)

if __name__ == '__main__':
    app.run(debug=True)
