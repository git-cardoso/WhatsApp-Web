from selenium.webdriver.common.by import By
from selenium import webdriver
import schedule



class Whatsapp:

    def driver(self):
        driver = webdriver.Chrome('/home/..')
        return driver

    def mensagem_whatsapp(self, mensagem, numeros_celulares):
        driver_extensao = Whatsapp().driver()
        driver_extensao.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(numeros_celulares))
        print("Autentificaçao[Web, Desktop] ")
        driver_extensao.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        campo = driver_extensao.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        print("Envio : ", campo.send_keys(mensagem))
        campo.send_keys("\n")


def robo():
    pessoas = [0010101] # numeros
    mensagemE = "Ola, estao"

    enviarAgora = Whatsapp()
    for possomandar in pessoas:
        enviarAgora.mensagem_whatsapp(mensagem=mensagemE, numeros_celulares=pessoas)

schedule.every().minute.at(":10").do(robo)
while True:
    schedule.run_pending()
