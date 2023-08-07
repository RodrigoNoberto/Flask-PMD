from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    
@app.route('/calcular', methods=['POST'])
def calcular():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    resultado = num1 + num2
    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run()
