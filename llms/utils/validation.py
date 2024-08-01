from llms.services.gpt_service import use_model


def validate_function(function_code, language):
    prompt = f"""
    You are an evaluator for code snippets. Your task is to determine if the provided code is a function in the specified programming language and not a class or any other code. 

    Here are the instructions:
    1. The code provided should be evaluated to check if it is a function in the given language.
    2. It should not be a class or any other type of code.
    3. You must only return "True" if the code is a function and it matches the specified language. Otherwise, return "False".

    Code:
    {function_code}

    Language:
    {language}

    Return only "True" or "False".
    """

    response = use_model(prompt)
    is_valid = response.strip() == "True"

    return is_valid

