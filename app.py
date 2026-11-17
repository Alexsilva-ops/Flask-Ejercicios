## Importamos flask
from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
CORS(app)

## Definimos la ruta principal
@app.route("/")
def HolaFlask():
    return "<h1>¡Hola Flask!</h1> <hr>"

## Ahora tomamos la segunda ruta y la reemplazamos por el siguiente ejemplo
## 1.) Haga un programa que calcule el promedio de notas sabiendo que tienen un valor de
## 30%, 30% y 40% respectivamente.
@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0, nota2=0, nota3=0):
    resultado = (nota1*30)/100+(nota2*30)/100+(nota3*40)/100
    return f"<h1>El resultado es: {resultado}</h1> <hr>"

## Tomamos la tercera ruta y la reemplazamos por el siguiente ejemplo
## 2.) Un programa que al capturar la edad de una persona diga si es:
## Menor de edad (Menor a 18 años)
## Adulto (Mayor o igual a 18 años y menor a 60 años)
## Adulto mayor (Mayor o igual a 60 años)
@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad=0):
    if edad < 18:
        R = "Menor de edad"
    elif edad < 60:
        R = "Adulto"
    else:
        R = "Adulto mayor"
    return f"<h1>La persona es: {R}</h1> <hr>"

## Creamos otra ruta ruta relizamos el siguiente ejemplo
## 3.) Programa que crea arreglos con valores aleatorios
## Importamos la libreria numpy si no existe la instalamos con: pip install numpy
import numpy as np
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0, columnas=0, filas=0):
    if filas==0:
        arreglo=np.random.randint(valores, size=columnas)
    else:
        arreglo=np.random.randint(valores, size=(filas,columnas))

    return f"<h1>El arreglo aleatorio es: {arreglo}</h1> <hr>"

## Creamos otra ruta ruta relizamos el siguiente ejemplo
## Ejercicios propuestos
## 1.) Haga un programa que calcule la siguiente ecuación: Y = X * Z + Z + X
@app.route("/ecuacion")
@app.route("/ecuacion/<x>/<z>")
def ecuacion(x=0, z=0):
    x = float(x)
    z = float(z)
    y = x * z + z + x
    return f"<h1>El resultado de Y es: {y}</h1> <hr>"

## Creamos otra ruta ruta relizamos el siguiente ejemplo
## 2.) Realizar programa que, capturado un número, realice la tabla de multiplicar de ese número hasta el 10.
@app.route("/tabla")
@app.route("/tabla/<int:numero>")
def tabla(numero=0):
    resultado = ""
    for i in range(1, 11):
        resultado += f"{numero} x {i} = {numero * i}<br>"
    return f"<h1>Tabla del {numero}:</h1><h3>{resultado}</h3> <hr>"

## Creamos otra ruta ruta relizamos el siguiente ejemplo
## 3.) Realizar el programa que calcule las áreas de un círculo, cuadrado y triangulo
import math
@app.route("/areas")
@app.route("/areas/<int:figura>/<v1>")
@app.route("/areas/<int:figura>/<v1>/<v2>")
def areas(figura=0, v1=0, v2=0):
    v1 = float(v1)
    v2 = float(v2)
    if figura == 1:
        area = math.pi * (v1 ** 2)
        R = f"Círculo: {area}"
    elif figura == 2:
        area = v1 ** 2
        R = f"Cuadrado: {area}"
    elif figura == 3:
        area = (v1 * v2) / 2
        R = f"Triángulo: {area}"
    else:
        R = "Figura no válida"
    return f"<h1>El área del {R}</h1> <hr>"

if __name__ == '__main__':
    ## El valor True indica que la app se deja en modo debug
    app.run(debug=True)