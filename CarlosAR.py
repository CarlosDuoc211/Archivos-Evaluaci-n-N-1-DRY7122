import json

# Abrir el archivo JSON y cargarlo en un string
with open('myfile.json', 'r') as f:
    ourjson = json.load(f)

# Imprimir el contenido del string
print(ourjson)
