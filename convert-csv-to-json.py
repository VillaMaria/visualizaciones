"""
PY3
Convertir el CSV derivado de lo que libera el municipio al JSON que usa la visualizacion
"""

# origina
csv_origen = "dendrograma/funcionarios-villa-maria.csv"
# destino
json_destino = "dendrograma/funcionarios-villa-maria.json"

import json
import csv
resultados = {"count": 0, "results": []}

with open(csv_origen) as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		# objeto funconario
		func = {}
		func["id"] = row["id"]
		func["funcionario"] = {}
		func["funcionario"]["nombre"] = row["Nombre"]
		func["funcionario"]["apellido"] = ""
		func["funcionario"]["nombrepublico"] = row["Nombre"]
		func["funcionario"]["franjaetaria"] = ""
		func["funcionario"]["genero"] = row["genero"]
		func["funcionario"]["edad"] = 0
		func["funcionario"]["url"] = ""
		func["funcionario"]["foto"] = {"original": "https://goo.gl/7k97nP", "thumbnail_32x32": "https://goo.gl/7k97nP", "thumbnail":"https://goo.gl/7k97nP"}
		func["funcionario"]["uniqueid"] = ""
		func["cargo"] = {}
		func["cargo"]["id"] = row["id"]
		func["cargo"]["categoria"] = {}
		func["cargo"]["categoria"]["id"] = row["id"]  # no usamos
		func["cargo"]["categoria"]["nombre"] = row["Cargo"]  # no usamos
		func["cargo"]["categoria"]["requiere_declaracion_jurada"] = True  # no usamos
		func["cargo"]["categoria"]["nombre_corto"] = row["Cargo"]  # no usamos
		func["cargo"]["categoria"]["orden"] = 10
		func["cargo"]["nombre"] = row["Cargo"]
		func["cargo"]["depende_de"] = row["depende_de"]
		func["cargo"]["electivo"] = False  # no usamos
		func["cargo"]["superioresids"] = []  # no usamos
		func["cargo"]["oficina"] = row["Cargo"]
		func["fecha_inicio"] = ""
		func["fecha_fin"] = ""
		func["decreto_nro"] = None
		func["decreto_pdf"] = ""

		resultados["results"].append(func)
	

to_file = json.dumps(resultados)

f = open(json_destino, 'w')
f.write(to_file)
f.close()