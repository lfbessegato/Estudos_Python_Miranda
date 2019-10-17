import os
import shutil

caminho_original = 'D:/temp/'
caminho_novo = 'D:/temp2/'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        print(new_file_path)

        #shutil.move(old_file_path,new_file_path)
        #print(f'Arquivo {file} movido com sucesso.')

        #shutil.copy(old_file_path, new_file_path)
        #print(f'Arquivo {file} copiado com sucesso.')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        print(new_file_path)

        os.remove(new_file_path)
        print(f'Arquivo {file} apagado com sucesso.')