import sys
import os
import time
import pyautogui
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

Num1 = None 
Num2 = None 
operacao = None
resultado = None
janela = None


def dividiro_por_zero():
    vetor=[0]
    lista_zeros = []
    for i in range(1, 6):
        lista_zeros.append("0" * i)
        Valor_Exibido(lista_zeros[i-1])
        time.sleep(0.2)
    pyautogui.alert(text='Bro??? tu ta dividindo por 0???', title='Bro??', button='Sim :P')
    time.sleep(0.3)
    pyautogui.alert(text='Isso n faz sentido mano', title='Bro??', button='é verdade :P')
    abrir_navegador("https://www.calculadoraonline.com.br/basica")
    pyautogui.alert(text='DESISTO usa esse bagui ai', title='Bro??')

def Valor_Exibido(Valor):
    QApplication.processEvents()
    janela.lcdNumber.display(Valor)

def abrir_navegador(Links):
    global nova_janela 
    nova_janela = QMainWindow()
    nova_janela.setWindowTitle("SOU Burro demais pra dividir por 0")
    nova_janela.resize(800, 600)
    browser = QWebEngineView()
    browser.setUrl(QUrl(Links))
    
    nova_janela.setCentralWidget(browser)
    nova_janela.show()



def set_defaults():
    global Num1, Num2, operacao, resultado
    Num1 = None
    Num2 = None
    operacao = None
    resultado = None



def definir_valores(num: int): 
    global Num1, Num2
    if Num1 is None:
        Num1 = num
        print(f"Numero1 é {Num1}")
        janela.lcdNumber.display(Num1)
    else:
        Num2 = num
        print(f"Numero2 é {Num2}")
        janela.lcdNumber.display(Num2)

def mudar_operacao(tipo):
    global operacao
    operacao = tipo
    print(f"Operação é {operacao}")

def calc():
    global Num1, Num2, operacao , resultado
    print(f"Numeros {Num1}, {Num2} e operação {operacao}")
    if Num1 is None or Num2 is None or operacao is None:
        print("Faltam valores para realizar o cálculo.")
    else:
        match operacao:
            case "Soma":
                resultado = Num1 + Num2
                print(f"Resultado: {resultado}")
                janela.lcdNumber.display(resultado)
                return resultado
            case "Subtracao":
                resultado = Num1 - Num2
                print(f"Resultado: {resultado}")
                janela.lcdNumber.display(resultado)
                
                return resultado
            case "Multiplicacao":
                resultado = Num1 * Num2
                print(f"Resultado: {resultado}")
                janela.lcdNumber.display(resultado)
                return resultado
            case "Divisao":
                if Num2 != 0:
                    resultado = Num1 / Num2
                    print(f"Resultado: {resultado}")
                    janela.lcdNumber.display(resultado)
                    return resultado
                else:
                    print("Erro: Divisão por zero.")
                    dividiro_por_zero()
                    return None
            case _:
                raise ValueError("Operação inválida.")


def definir_interacoes(janela: QMainWindow): 
    janela.BTN0.clicked.connect(lambda: definir_valores(0)) 
    janela.BTN1.clicked.connect(lambda: definir_valores(1)) 
    janela.BTN2.clicked.connect(lambda: definir_valores(2)) 
    janela.BTN3.clicked.connect(lambda: definir_valores(3)) 
    janela.BTN4.clicked.connect(lambda: definir_valores(4)) 
    janela.BTN5.clicked.connect(lambda: definir_valores(5)) 
    janela.BTN6.clicked.connect(lambda: definir_valores(6)) 
    janela.BTN7.clicked.connect(lambda: definir_valores(7)) 
    janela.BTN8.clicked.connect(lambda: definir_valores(8)) 
    janela.BTN9.clicked.connect(lambda: definir_valores(9))
    janela.BTNMais.clicked.connect(lambda: mudar_operacao("Soma"))
    janela.BTNMenos.clicked.connect(lambda: mudar_operacao("Subtracao"))
    janela.BTNDividir.clicked.connect(lambda: mudar_operacao("Divisao"))
    janela.BTNVezes.clicked.connect(lambda: mudar_operacao("Multiplicacao"))
    janela.BTNIgual.clicked.connect(lambda: calc())
    janela.BTNIgual.clicked.connect(lambda: set_defaults())


class MainWindow(QMainWindow):
    def __init__(self, caminho_ui):
        super().__init__()
        uic.loadUi(caminho_ui, self)
        definir_interacoes(self)

def abrir_tela(nome_ui: str):
    global janela
    app = QApplication(sys.argv)

    local = os.path.dirname(__file__)
    caminho_ui = os.path.join(local, nome_ui)

    janela = MainWindow(caminho_ui)
    janela.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    abrir_tela("MAIN.ui")


# def abrir_tela(nome_ui: str):
#    """Abre uma janela a partir de um arquivo .ui"""
#    app = QApplication(sys.argv)
#    local = os.path.dirname(__file__)
#    caminho_ui = os.path.join(local, nome_ui)
#    class MainWindow(QMainWindow):
#        def __init__(self):
#            super().__init__()
#            uic.loadUi(caminho_ui, self)
#    janela = MainWindow()
#    janela.show()
#    sys.exit(app.exec())