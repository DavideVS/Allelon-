"""
   Titulo: ALLELON++, Davide Vegnier & Leo Jiménez Iglesias,
   elemntos de importar en el proyecto tanto
   como valores que librerias i datos."""
import machine
from machine import Pin, ADC, I2C
import ssd1306
from time import sleep
from array import frases2

#Inicialización Pin para el sensor Yl-69 en la posición ADC 34
Yl = ADC(Pin(34))
Yl.atten(ADC.ATTN_11DB)
#Inicialización i2c para la pantalla OLED en la posición sda21 y scl22
i2c = I2C(-1, scl=Pin(22), sda=Pin(21))
#variable para la pantalla OLED
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
#Inicialización Pin para el buzzer en la posición 23
p23 = machine.Pin(23, machine.Pin.OUT)
#variable para el buzzer
buzzer = machine.PWM(p23)
#frequencia sonido buzzer
buzzer.freq(1047)
"""
   empiezo bucle while que al infinito
   realiza varias operaciones del programa ALLELON++
"""
while True:
    #color negro que limpia la pantalla OLED cada vez
    oled.fill(0)
    #lectura valores sensor Yl-69
    Yl_valor = Yl.read()
    """calculo matematico de mapeo de los valores del sensor que se
       limitan entre 0 y 100, para imprimir el porcentaje de cada valor
    """
    calculo = (Yl_valor*100)/4095
    #adición de signo de porcentaje
    H = '%'
    #Transformación del cálculo de int a string, costomización
    porcentaje = str(int(calculo)) + H
    #tiempo de espera
    sleep(0.5)
    """
       Inicio del ciclo for que recoge el valor del sensor y lo asocia a un
       string almacenado en una matriz, creada en un archivo de nombre de frases
    """
    #bucle for que empieza de un valor variable i hasta la longitud total de la matriz de frases
    for i in range(len(frases2)):
        # if que me permite asociar a cada valor la frase correspondiente que posee el mismo número e índice
        if calculo < (i+1)*100/len(frases2):
            """if calculo == 100:
                buzzer.duty(10)"""
            #impresión del valor i de la matriz de frases
            print(frases2[i])
            #impresión del valor porcentaje
            print (porcentaje)
            #parada del ciclo
            break
    #texto del valor porcentaje en la pantalla OLED
    oled.text(porcentaje, 0, 0)
    #texto del valor i de la matriz de frases en la pantalla OLED
    oled.text(frases2[i], 0, 20)
    #volumen sonido buzzer, encendido
    buzzer.duty(40)
    #tiempo de espera
    sleep(1)
    #volumen sonido buzzer, apagado
    buzzer.duty(0)
    #tiempo de espera
    sleep(0.5)
    #impresión valores en la pantalla OLED
    oled.show()