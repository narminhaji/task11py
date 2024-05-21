import os 
from pathlib import Path

subdirect = 'task/Example/subdirect/'
os.makedirs(subdirect, exist_ok=True)

with open('test.txt', encoding='utf-8', mode='w') as text:
    text.write('yeni')
    os.rename(text.name, subdirect + text.name)

with open('photo.png', mode='w') as photo:
    os.rename(photo.name, subdirect + photo.name)
example = 'task/Example/'
for file in Path(subdirect).iterdir():
    if (file.is_file() and file.name.endswith('.txt')):
        os.rename(subdirect + file.name, example + file.name)