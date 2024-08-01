from llms.services.generated_model_service import use_model

def generate_function_in_language(data, language):
    prompt = f"""
    Convert the following code into the specified programming language:

    Code:
    {data}

    Target Language:
    {language}

    Please provide only the translated code in the specified language. Do not use markdown or any additional text. If it is not possible to translate, return an empty string.
    """

    return use_model(prompt)


def generate_function(data, input_language, output_language):
    prompt = f"""
    You are a function translator. Translate the following function from {input_language} to {output_language}:

    Function:
    {data}

    Provide only the translated function code in {output_language}. Do not use markdown or include any extra text. If translation is not possible, return an empty string.
    """

    return use_model(prompt)
