from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyunpack import Archive

# Inicialize o driver do navegador (neste caso, Edge)
driver = webdriver.Edge()

# Entre no site
driver.get('https://contactcenter6.aec.com.br/Orbi/')

# Encontre os campos de usuário e senha e insira suas credenciais
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
username.send_keys('m.andre.sobral')
password.send_keys('sucesso//2024')

# Pressione Enter para fazer login
password.send_keys(Keys.RETURN)

# Navegue até a página de download
driver.get('https://contactcenter6.aec.com.br/Orbi/modulo-relatorios/visualizar/operacional-tim-base-analitica-de-indicadores-filesystem')

# Encontre o div com o id específico
div = driver.find_element_by_id('166d8565-631a-4b78-8327-885ffcc4e5d7')

# Clique no div para iniciar o download
div.click()

# Feche o navegador
driver.quit()

# Use pyunpack para extrair o arquivo WinRAR
Archive('/path/to/winrar/file.rar').extractall('/path/to/extract/to')
