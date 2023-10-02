import os
import subprocess

# Obtenha o caminho da pasta atual (diretório de trabalho)
caminho_atual = os.getcwd()



# pasta do .aab ////////////////////////////////////

# Diretório onde você deseja procurar arquivos .aab
diretorio_procura = caminho_atual

# Lista de arquivos com a extensão .aab
arquivos_aab = [f for f in os.listdir(diretorio_procura) if f.endswith('.aab')]

# Exibe a lista de arquivos .aab encontrados
for arquivo in arquivos_aab:
    caminho_aab = os.path.join(diretorio_procura, arquivo)
    print(f'Encontrado arquivo .aab: {caminho_aab}')
    



# //////////////////////////////////////////////////////////////////








# Caminho para o arquivo AAB dentro da pasta atual
#caminho_aab = os.path.join(caminho_atual, 'app.aab')

# Caminho para o APK de destino dentro da pasta atual
caminho_apk = os.path.join(caminho_atual, 'seu_app.apks')

# Caminho para o bundletool (substitua pelo caminho real)
caminho_bundletool = os.path.join(caminho_atual, 'bundletool.jar')

# Comando para converter o AAB em APK usando o bundletool
comando = (
    f'java -jar "{caminho_bundletool}" build-apks --bundle="{caminho_aab}" '
    f'--output="{caminho_apk}" --overwrite --mode=universal'
)

# Execute o comando usando o subprocess
subprocess.run(comando, shell=True, check=True)

print(f'O arquivo APK foi gerado em: {caminho_apk}')




# ///////////////  extrair /////////////////////////


import time
import zipfile

# Nome do arquivo ZIP que você deseja extrair
nome_arquivo_zip = 'seu_app.apks'

# Diretório de destino para extrair o conteúdo
diretorio_destino = 'pasta_d0_apk'

# Crie um objeto ZipFile
with zipfile.ZipFile(nome_arquivo_zip, 'r') as arquivo_zip:
    # Extraia todo o conteúdo para o diretório de destino
    arquivo_zip.extractall(diretorio_destino)

print(f'Arquivo {nome_arquivo_zip} extraído para {diretorio_destino}.')




# ///////////////apagar/////////////////////////
time.sleep(4)

import os

# Especifique o caminho completo para o arquivo que deseja excluir
caminho_para_arquivo = os.path.join(caminho_atual, 'seu_app.apks')

# Verifique se o arquivo existe antes de tentar excluí-lo
if os.path.exists(caminho_para_arquivo):
    # Exclua o arquivo
    os.remove(caminho_para_arquivo)
    print(f'O arquivo {caminho_para_arquivo} foi excluído com sucesso.')
else:
    print(f'O arquivo {caminho_para_arquivo} não foi encontrado.')
