from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random
from tsp import simulated_annealing, evalua_ruta

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")  # busca en /templates/index.html

@app.route("/resolver-tsp", methods=["POST"])
def resolver_tsp():
    datos = request.json
    coord = datos["coordenadas"]
    T = datos["temperatura"]
    T_MIN = datos["temp_min"]
    V_enfriamiento = int(datos["velocidad"])
    origen = datos["origen"]
    destino = datos["destino"]

    ciudades = list(coord.keys())
    ciudades.remove(origen)
    ciudades.remove(destino)
    random.shuffle(ciudades)

    ruta = [origen] + ciudades + [destino]

    mejor_ruta = simulated_annealing(ruta, coord, T, T_MIN, V_enfriamiento)
    distancia_total = evalua_ruta(mejor_ruta, coord)

    return jsonify({"ruta": mejor_ruta, "distancia": distancia_total})

if __name__ == "__main__":
    app.run(debug=True)
