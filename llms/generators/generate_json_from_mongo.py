from concurrent.futures import ThreadPoolExecutor, as_completed
from openai import OpenAI
from llms.database.dbConnection import get_mongo_database

db = get_mongo_database()
base_collection = db["classEvalPython"]

client = OpenAI(
    api_key="sk-proj-AG6ODNGho1SBTgI6hkDtT3BlbkFJmFJJKKJLW08Z5sVt1kn6",
)

high_level_languages = [
    "Python",
    "JavaScript",
    "Java",
    "C#",
    "PHP",
    "Kotlin"
]


def use_model(data, language):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Can you take this data: " + data + " and make his equivalent to this " + language + " saying nothing in the message, dont use markdown just the response, if not possible give an empty string",
            }
        ],
        model="gpt-3.5-turbo",
    )
    response = chat_completion.choices[0].message.content
    return response


def process_method(language, method):
    collection = db['methodEval' + language]

    method_description = use_model(method['method_description'], language)
    test_code = use_model(method['test_code'], language)
    solution_code = use_model(method['solution_code'], language)

    dependencies = method['dependencies']
    lib_dependencies = [use_model(dep, language) for dep in dependencies['lib_dependencies']]
    field_dependencies = [use_model(dep, language) for dep in dependencies['field_dependencies']]
    method_dependencies = [use_model(dep, language) for dep in dependencies['method_dependencies']]

    data = {
        'method_name': method['method_name'],
        'method_description': method_description,
        'test_code': test_code,
        'solution_code': solution_code,
        'dependencies': {
            'lib_dependencies': lib_dependencies,
            'field_dependencies': field_dependencies,
            'method_dependencies': method_dependencies
        }
    }

    print(f"Ready to insert data for method: {method['method_name']} in language: {language} with data {data}")
    collection.insert_one(data)


def create_dataset():
    values = base_collection.find()

    with ThreadPoolExecutor(max_workers=10) as executor:  # Ajusta el número de workers según tu sistema
        futures = []
        for value in values:
            methods = value['methods_info']
            for language in high_level_languages:
                for method in methods:
                    collection = db['methodEval' + language]

                    existing_method = collection.find_one({'method_name': method['method_name']})
                    if existing_method:
                        continue

                    futures.append(executor.submit(process_method, language, method))

        for future in as_completed(futures):
            try:
                future.result()  # Obtener el resultado del future
            except Exception as e:
                print(f"An error occurred: {e}")

