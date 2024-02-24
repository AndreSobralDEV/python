from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o driver do Chrome (certifique-se de ter o ChromeDriver instalado)
driver = webdriver.Edge()

# Abre o WhatsApp Web
try:
    driver.get("https://web.whatsapp.com/")
    time.sleep(60)  # Espera 10 segundos para você escanear o código QR
except:
    pass

if not driver.get_cookies():
    print("Por favor, escaneie o código QR do WhatsApp.")
    time.sleep(20)
    driver.get("https://web.whatsapp.com/")
    time.sleep(10)

# Encontra o campo de pesquisa e insere o nome do contato/grupo
contato = "Lucas Irmão"
campo_pesquisa = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"]')
campo_pesquisa.send_keys(contato)
campo_pesquisa.send_keys(Keys.ENTER)

# Espera um segundo para a conversa ser carregada
time.sleep(5)

# Encontra o campo de mensagem e envia a mensagem desejada
mensagem = "Teste Python"
campo_mensagem = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]')
campo_mensagem.send_keys(mensagem)
campo_mensagem.send_keys(Keys.ENTER)

# Fecha o navegador após o envio da mensagem
driver.quit()
