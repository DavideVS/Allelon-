"""
   Titulo: ALLELON++, Davide Vegnier & Leo Jiménez Iglesias,
   elemntos de importar en el proyecto tanto
   como valores que librerias i datos."""
try:
  import usocket as socket
except:
  import socket
import network
from machine import Pin, ADC, I2C
import ssd1306
from time import sleep
from allelon import *
from frases import frase2

#importacion gc
import gc
gc.collect()

#definizion ssid y password de la propria conexion
ssid = 'El nombre de tu Wifi' #ONOEB14
password = 'la password de tu Wifi' #RMabjCFTUQcJ

"""s = socket(AF_INET, SOCK_STREAM)
s.connect(('smtp.upv.es',25))
print(s.recv(100))
s.close()"""

#declaracion variable wifi
wifi = network.WLAN(network.STA_IF)
#activacion a la red elejida
wifi.active(True)
#conexion a la red definida anteriormente
wifi.connect(ssid, password)

"""pequeño bucle while que imprime la string 'Conexion correcta'
   en caso de conexion a la red y configura la misma como red
"""
while wifi.isconnected() == False:
  pass
print('Conexion correcta')
print(wifi.ifconfig())

"""
   definicion variable pagina web que desarolla el archivo.html
   y que sarà el que se visualizarà en el motor de busqueda
"""
def pagina_web():
  html = """<!DOCTYPE HTML><html>
<head>
  <meta http-equiv=\"refresh\" content=\"10\">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
  <style>
    html {
     font-family: Arial;
     display: inline-block;
     margin: 0px auto;
     text-align: center;
    }
    h2 { font-size: 3.0rem; }
    p { font-size: 3.0rem; }
    .units { font-size: 1.2rem; }
    .dht-labels{
      font-size: 1.5rem;
      vertical-align:middle;
      padding-bottom: 15px;
    }
  </style>
</head>
<body>
  <h2>Datos de sensor</h2>
  <p>
    <i class="fas fa-thermometer-half" style="color:#059e8a;"></i> 
    <span class="dht-labels">Temperatura</span> 
    <span>"""+str(porcentaje)+"""</span>
    <sup class="units">&deg;C</sup>
  </p>
  <p>
    <i class="fas fa-tint" style="color:#00add6;"></i> 
    <span class="dht-labels">Humedad</span>
    <span>"""+str(frase1)+"""</span>
    <sup class="units">%</sup>
  </p>
</body>
</html>"""
  return html

#comunicacion por socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 23))
s.listen(1)

#bucle while que recarga la pagina y actualiza los datos enviados
while True:
  conexion, direccion = s.accept()
  #Aquì se pondrà el bucle for del archivo allelon
  request = conexion.recv(1024)
  respuesta = pagina_web()
  conexion.send('HTTP/1.1 200 OK\r\n')
  conexion.send('Content-Type: text/html\r\n')
  conexion.send('Connection: close\r\n\r\n')
  conexion.sendall(respuesta)
  conexion.close()