import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib
import time

# Carregar os dados do Excel
contatos_df = pd.read_excel("Enviar.xlsx")

# Inicializar o navegador
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

# Aguardar até que o código QR seja escaneado e o WhatsApp Web seja carregado
print("Por favor, escaneie o código QR e aguarde o carregamento do WhatsApp Web...")
wait = WebDriverWait(navegador, 60)
wait.until(EC.visibility_of_element_located((By.ID, "side")))

print("WhatsApp Web carregado com sucesso. Iniciando o envio de mensagens...")

# Iterar sobre os contatos e enviar mensagens
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    
    # Aguardar até que o chat com o contato seja carregado
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')))
    
    # Enviar a mensagem
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    
    # Aguardar um intervalo de tempo entre o envio de cada mensagem
    time.sleep(5)

print("Envio de mensagens concluído.")




