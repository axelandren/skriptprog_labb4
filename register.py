from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    register_dict = request.form.to_dict()
    return register_dict

if __name__ == '__main__':
    app.run(debug=True)
