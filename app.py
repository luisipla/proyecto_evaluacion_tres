from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        try:
            notas = [int(request.form[f'nota{i}']) for i in range(1, 4)]
            asistencia = int(request.form['asistencia'])
            promedio = sum(notas) / len(notas)
            estado = "Felicidades, Aprobado" if promedio >= 40 and asistencia >= 75 else "lo siento, Reprobado"
            resultado = {'promedio': promedio, 'estado': estado}
        except ValueError:
            resultado = {'error': 'Por favor, ingresa números válidos.'}
    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    if request.method == 'POST':
        nombres = [request.form[f'nombre{i}'] for i in range(1, 4)]
        nombre_mas_largo = max(nombres, key=len)
        resultado = {'nombre': nombre_mas_largo, 'caracteres': len(nombre_mas_largo)}
    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
