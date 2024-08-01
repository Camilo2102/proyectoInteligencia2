from llms.services.function_translate_service import generate_function
from llms.utils.validation import validate_function


def translate_function(function, input_language, output_language):
    if input_language == output_language: return "La funcion ya se encuentra en este idioma"

    is_valid = validate_function(function, input_language)

    if not is_valid: return "No es una funcion valida del lenguage " + input_language

    return generate_function(function, input_language, output_language)
