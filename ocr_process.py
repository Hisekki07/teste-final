

import pytesseract
from PIL import Image
import os

# Configurando o caminho do Tesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'

# Caminho para a pasta inputs
input_dir = 'D:/Git/teste-final/inputs'

# Caminho para a pasta output
output_dir = 'D:/Git/teste-final/output'

# Garantindo que a pasta de saída exista
os.makedirs(output_dir, exist_ok=True)

# Percorrendo todos os arquivos na pasta inputs
for filename in os.listdir(input_dir):
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
        image_path = os.path.join(input_dir, filename)
        text = pytesseract.image_to_string(Image.open(image_path))

        # Salvando o texto extraído em um arquivo na pasta output
        output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)


