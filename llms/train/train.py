import json
from datasets import Dataset
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling

# Cargar los datos de entrenamiento
with open('./files/training_data.json', 'r') as infile:
    training_data = json.load(infile)

# Convertir los datos a un formato adecuado para Hugging Face
train_dataset = Dataset.from_dict({
    'prompt': [item['prompt'] for item in training_data],
    'completion': [item['completion'] for item in training_data]
})

# Cargar el tokenizador y el modelo
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Asignar el token de padding
tokenizer.pad_token = tokenizer.eos_token


# Función para tokenizar los datos
def tokenize_function(examples):
    inputs = [ex + tokenizer.eos_token for ex in examples['prompt']]
    outputs = [ex + tokenizer.eos_token for ex in examples['completion']]
    model_inputs = tokenizer(inputs, max_length=512, truncation=True, padding='max_length')
    labels = tokenizer(outputs, max_length=512, truncation=True, padding='max_length')["input_ids"]
    model_inputs["labels"] = labels
    return model_inputs


# Tokenizar el conjunto de datos
tokenized_dataset = train_dataset.map(tokenize_function, batched=True, remove_columns=["prompt", "completion"])

# Definir los argumentos de entrenamiento
training_args = TrainingArguments(
    output_dir='../results',
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
    logging_dir='./logs',
    logging_steps=10,
    report_to="none"
)

# Usar un data collator que maneje el padding de manera adecuada
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,
)

# Crear el objeto Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
)

# Entrenar el modelo
trainer.train()
