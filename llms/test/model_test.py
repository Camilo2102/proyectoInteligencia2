from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Cargar el tokenizador y el modelo entrenado
tokenizer = GPT2Tokenizer.from_pretrained('../results/checkpoint-8880')
model = GPT2LMHeadModel.from_pretrained('../results/checkpoint-8880')

# Función para generar texto
def generate_text(prompt, max_length=150):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Probar el modelo con nuevas entradas
prompts = [
    "Translate the following Python method to PHP:\n\ndef example_method(self, input):\n    return input * 2",
    "Translate the following Java method to Python:\n\npublic int multiply(int a, int b) {\n    return a * b;\n}",
]

for prompt in prompts:
    generated_text = generate_text(prompt)
    print(f"Prompt: {prompt}")
    print(f"Generated: {generated_text}")
    print('-' * 50)
