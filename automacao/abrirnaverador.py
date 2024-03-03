from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyunpack import Archive
from selenium.webdriver.common.by import By

# Inicialize o driver do navegador (neste caso, Edge)
driver = webdriver.Edge()

# Entre no site
driver.get('https://contactcenter6.aec.com.br/Orbi/')

# Encontre os campos de usuário e senha e insira suas credenciais
username = driver.find_element(By.NAME, 'Email')
password = driver.find_element(By.NAME, 'Password')
username.send_keys('m.andre.sobral')
password.send_keys('sucesso//2024')

# Pressione Enter para fazer login
password.send_keys(Keys.RETURN)

# Navegue até a página de download
driver.get('https://contactcenter6.aec.com.br/Orbi/modulo-relatorios/visualizar/operacional-tim-base-analitica-de-indicadores-filesystem')
wait = WebDriverWait(driver, 5)

# Encontre o div com o id específico
wait = WebDriverWait(driver, 5)  # Espere até 10 segundos
div = wait.until(EC.presence_of_element_located((By.ID, '1c6f31ae-f02b-4e0f-a37b-5abfaf43b865')))

# Clique no div para iniciar o download
div.click()

# Feche o navegador
driver.quit()

# Use pyunpack para extrair o arquivo WinRAR
Archive('/path/to/winrar/file.rar').extractall('/path/to/extract/to')
