from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET', 'POST'])
def index_python():
    if request.method == 'POST':
        code = request.form['code.py']
        try:
            # Compila y ejecuta el código Python
            result = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            result = e.output

        return render_template('indexPy.html', code=code, result=result)
    return render_template('indexPy.html', code='', result='')

@app.route('/cpp', methods=['GET', 'POST'])
def index_cpp():
    if request.method == 'POST':
        code = request.form['code.cpp']
        try:
            # Guarda el código en un archivo temporal
            with open('temp.cpp', 'w') as file:
                file.write(code)
            
            # Compila el código C++
            subprocess.check_output(['g++', 'temp.cpp', '-o', 'temp'], stderr=subprocess.STDOUT)
            
            # Ejecuta el programa compilado
            result = subprocess.check_output(['./temp'], stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            result = e.output

        return render_template('indexC.html', code=code, result=result)
    return render_template('indexC.html', code='', result='')

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
