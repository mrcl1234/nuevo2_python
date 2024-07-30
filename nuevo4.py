from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
import sys
import os
import time

# Configuración del pin GPIO
PIN = "50"
GPIOPATH = '/sys/class/gpio/'

def setup_gpio():
    """Configura el GPIO para el LED."""
    if not os.path.exists(GPIOPATH + "gpio" + PIN):
        with open(GPIOPATH + "export", "w") as f:
            f.write(PIN)
    
    with open(GPIOPATH + "gpio" + PIN + "/direction", "w") as f:
        f.write("out")

def turn_led_on():
    """Enciende el LED."""
    with open(GPIOPATH + "gpio" + PIN + "/value", "w") as f:
        f.write("1")

def turn_led_off():
    """Apaga el LED."""
    with open(GPIOPATH + "gpio" + PIN + "/value", "w") as f:
        f.write("0")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo PyQt5")

        # Configurar la ventana a pantalla completa
        self.showFullScreen()

        # Configurar el GPIO
        setup_gpio()

        # Inicializar el estado del LED
        self.led_on = False

        # Crear un botón y conectar su señal al método
        self.button = QPushButton("LED")
        self.button.clicked.connect(self.on_button_click)
        
        # Ajustar el tamaño mínimo del botón
        self.button.setFixedSize(200, 100)

        # Configurar el diseño de la ventana
        layout = QHBoxLayout()
        layout.addWidget(self.button)
        layout.setAlignment(Qt.AlignCenter)  # Centrar el botón
        self.setLayout(layout)

    def on_button_click(self):
        """Alternar el estado del LED."""
        if self.led_on:
            turn_led_off()
            self.led_on = False
        else:
            turn_led_on()
            self.led_on = True

        print("¡Botón clickeado! LED estado:", "Encendido" if self.led_on else "Apagado")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.close()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())