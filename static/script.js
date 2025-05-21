const coord = {
    'Jiloyork':[19.916012, -99.580580],
    'Toluca':[19.289165, -99.655697],
    'Atlacomulco':[19.799520, -99.873844],
    'Guadalajara':[20.677754, -103.346253],
    'Monterrey':[25.691611, -100.321838],
    'QuintanaRoo':[21.163111, -86.802315],
    'Michohacan':[19.701400, -101.208296],
    'Aguascalientes':[21.876410, -102.264386],
    'CDMX':[19.432713, -99.133183],
    'QRO':[20.597194, -100.386670]
  };
  
  window.onload = () => {
    const origen = document.getElementById("origen");
    const destino = document.getElementById("destino");
    for (const ciudad in coord) {
      origen.innerHTML += `<option value="${ciudad}">${ciudad}</option>`;
      destino.innerHTML += `<option value="${ciudad}">${ciudad}</option>`;
    }
  };
  
  async function resolverTSP(event) {
    event.preventDefault();
  
    const tempInicial = parseFloat(document.getElementById("tempInicial").value);
    const tempMin = parseFloat(document.getElementById("tempMin").value);
    const velocidad = parseFloat(document.getElementById("velocidad").value);
    const origen = document.getElementById("origen").value;
    const destino = document.getElementById("destino").value;
  
    const res = await axios.post("http://127.0.0.1:5000/resolver-tsp", {
      coordenadas: coord,
      temperatura: tempInicial,
      temp_min: tempMin,
      velocidad: velocidad,
      origen: origen,
      destino: destino
    });
  
    const data = res.data;
    document.getElementById("resultado").innerHTML = `
      <p><strong>Ruta:</strong> ${data.ruta.join(" → ")}</p>
      <p><strong>Distancia Total:</strong> ${data.distancia.toFixed(4)}</p>
    `;
  }
  
