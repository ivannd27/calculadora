from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def hola():
    peso = 0
    altura = 0
    imc = 0
    try:
        if (request.method == "POST"):
            peso = float(request.form.get("peso"))
            altura = float(request.form.get("altura"))
            imc = (peso/(altura*altura))
        if imc < 18.5:
            mensaje = "Peso bajo"
        elif imc > 18.5 and imc < 24.9:
            mensaje = "Peso normal"
        elif imc > 24.9 and imc < 29.9:
            mensaje = "Sobrepeso"
        elif imc > 30:
            mensaje = "Obesidad"
    except ValueError:
         return render_template("index.html", errornum = "No puedes meter valores NO numericos")
    except ZeroDivisionError:
        return render_template("index.html", error0 = "0 no puede ser un valor para peso y altura")
    return render_template("index.html", peso=peso, altura=altura, imc=imc, mensaje=mensaje)
app.run()
