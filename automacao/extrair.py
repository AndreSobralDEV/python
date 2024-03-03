import os
import zipfile


# Caminho para o arquivo ZIP baixado
caminho_arquivo_zip = 'C:\\Users\\andre\\Downloads\\Base_analitica_Nps_03_2024.zip'

# Caminho para o diretório de extração
caminho_destino = 'C:\\Users\\andre\\Downloads'

# Verifique se o arquivo ZIP existe
if os.path.exists(caminho_arquivo_zip):
    # Crie uma instância do objeto ZipFile
    with zipfile.ZipFile(caminho_arquivo_zip, 'r') as zf:
        # Liste o conteúdo do arquivo ZIP
        print("Conteúdo do arquivo ZIP:")
        print(zf.namelist())
        
        # Extraia o conteúdo do arquivo ZIP para o diretório de destino
        zf.extractall(caminho_destino)
        
        print("Arquivo extraído com sucesso.")
else:
    print("O arquivo ZIP não existe.")