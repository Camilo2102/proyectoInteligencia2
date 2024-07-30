import json

# Cargar ejemplos emparejados
with open('../files/paired_functions_data.json', 'r') as infile:
    paired_data = json.load(infile)

# Preparar datos en el formato adecuado para el entrenamiento
training_data = []
for pair in paired_data:
    input_text = f"Translate the following {pair['input_language']} method to {pair['output_language']}:\n\n{pair['input_method']['method_description']}"
    output_text = f"{pair['output_method']['method_description']}"
    training_data.append({
        'prompt': input_text,
        'completion': output_text
    })

# Guardar los datos de entrenamiento en un archivo JSON
with open('./files/training_data.json', 'w') as outfile:
    json.dump(training_data, outfile, indent=4)