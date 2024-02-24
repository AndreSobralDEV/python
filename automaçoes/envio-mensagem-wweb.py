from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o driver do Chrome (certifique-se de ter o ChromeDriver instalado)
driver = webdriver.Edge()

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com/")
time.sleep(20)  # Espera 10 segundos para você escanear o código QR

# Encontra o campo de pesquisa e insere o nome do contato/grupo
search_box = driver.find_element_by_xpath('//div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"]')
search_box.send_keys("Lucas Irmão" + Keys.ENTER)

# Espera um segundo para a conversa ser carregada
time.sleep(1)

# Encontra o campo de mensagem e envia a mensagem desejada
message_box = driver.find_element_by_xpath('//div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]')
message_box.send_keys("Teste Python" + Keys.ENTER)

# Fecha o navegador após o envio da mensagem
driver.quit()
