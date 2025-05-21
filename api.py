from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import random
import os
from tsp import simulated_annealing, evalua_ruta

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

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
