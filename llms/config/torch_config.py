import torch

print("CUDA available:", torch.cuda.is_available())  # Debería imprimir True si CUDA está disponible
print("GPU count:", torch.cuda.device_count())  # Número de GPUs disponibles
print("Current GPU:", torch.cuda.current_device())  # ID de la GPU actual
print("GPU name:", torch.cuda.get_device_name(torch.cuda.current_device()))  # Nombre de la GPU
