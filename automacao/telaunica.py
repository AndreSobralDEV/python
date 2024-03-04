from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import zipfile
import time

# Inicialize o driver do navegador (neste caso, Edge)
driver = webdriver.Edge()

# Entre no site
driver.get('https://pegasus:4443/TelaUnica')

# Encontre os campos de usuário e senha e insira suas credenciais
username = driver.find_element(By.NAME, 'Email')
password = driver.find_element(By.NAME, 'Password')
username.send_keys('m.andre.sobral')
password.send_keys('sucesso//2024')

# Pressione Enter para fazer login
password.send_keys(Keys.RETURN)

# Navegue até a página de download
driver.get('https://contactcenter6.aec.com.br/Orbi/modulo-relatorios/visualizar/operacional-tim-base-analitica-de-indicadores-filesystem')

wait = WebDriverWait(driver, 60)  # espera até 10 segundos

# Espera até que a div com o atributo 'data-filesystem-target' seja visível na página
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-filesystem-target="\\Tim - Base Analítica Nps"]')))

# Clique na div
element.click()

# Espera até que a div com o atributo 'data-filesystem-target' seja visível na página
element = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-filesystem-target="Tim - Base Analítica Nps\\2024"]')))

# Clique na div
element.click()

# Espera até que a div com o atributo 'data-filesystem-target' seja visível na página
element = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-filesystem-target="Tim - Base Analítica Nps\\2024\\03 - Março"]')))

# Clique na div
element.click()

# Espera até que a div com o atributo 'data-filesystem-target' seja visível na página
element = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@data-filesystem-target="Tim - Base Analítica Nps\\2024\\03 - Março\\Base_analitica_Nps_03_2024.zip"]')))

# Clique na div
element.click()

# Aguarde alguns segundos para que a página carregue completamente
time.sleep(5)  # Espere por 5 segundos

# Feche o navegador
driver.quit()

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
