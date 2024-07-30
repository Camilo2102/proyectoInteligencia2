import json

from llms.database.dbConnection import get_mongo_database

db = get_mongo_database()

base_name = "methodEval"

high_level_languages = [
    "Python",
    "JavaScript",
    "Java",
    "C#",
    "PHP",
    "Kotlin"
]

data = {}

for language in high_level_languages:
    collection_name = base_name + language
    collection = db[collection_name]
    data[language] = []
    for doc in collection.find():
        data[language].append({
            'method_name': doc.get('method_name'),
            'method_description': doc.get('method_description'),
            'test_code': doc.get('test_code')
        })

paired_data = []

for lang1 in high_level_languages:
    for func1 in data[lang1]:
        for lang2 in high_level_languages:
            if lang1 != lang2:
                for func2 in data[lang2]:
                    if func1['method_name'] == func2['method_name']:
                        paired_data.append({
                            'input_language': lang1,
                            'input_method': func1,
                            'output_language': lang2,
                            'output_method': func2
                        })

with open('./files/paired_functions_data.json', 'w') as outfile:
    json.dump(paired_data, outfile, indent=4)
