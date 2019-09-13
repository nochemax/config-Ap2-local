# Creador Smp_A
# Fecha 11.09.2019
# Nombre programa Laugh room
# Tipo phyton3
# server apache2 localhot con dominio SsL

import os 
import time
import sys
import threading
import shutil

from subprocess import Popen, PIPE, STDOUT
from netdiscover import *

import pandas as pd
from io import open

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  variables  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

listamenu=["Menu de Opciones:", "1--Nombre web ", "2--Ip del equipo ", "3--star server", "4--stop server", "5--Exit"]#Menu Princcipal
exit=False
key=0

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Funciones menu $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def menu():

  print("\033[1;31;1m ")
  os.system('figlet Laugh room')
  print("\033[1;37;1m ")
  print("            "+listamenu[0])
  print("\033[1;37;m ")
  print("            "+listamenu[1])
  print("            "+listamenu[2])
  print("            "+listamenu[3])
  print("            "+listamenu[4])
  print("            "+listamenu[5])
 
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Funcion Nombre web $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def Nombweb():

  global N_web
  
  while True:
    try:

      N_web1=(str(input("Escriba el nombre de la web -(sin: www .com)- : ")))
      N_web=N_web1+'.com' 
      print(N_web)
      print("creando directorio ")
      os.system('mkdir -p /var/www/'+N_web+'/public_html')# 
      print("concediendo permisos de usuario")
      os.system('chown -R $USER:$USER /var/www/'+N_web+'/public_html')# 
      os.system('chmod -R 755 /var/www')#
      shutil.copy2('/root/virtualserver/index/config.txt', '/var/www/'+N_web+'/public_html/index.html')
      
      return N_web  

    except TypeError:
      print("error ")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Funciones operativa $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def confweb(N_web):

  global ip_pc
  
  while True:

    try:

      ip_pc=input(str("introduzca la ip de su equipo : "))
      print(str(ip_pc))

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Archivo COnf
      line1='<VirtualHost '+ip_pc+':443>'
      line2="    SSLEngine on"
      line3='    SSLCertificateFile /etc/apache2/ssl/'+N_web+'.pem'
      line4='    SSLCertificateKeyFile /etc/apache2/ssl/'+N_web+'.key'
      line5=""
      line6='    ServerAdmin admin@'
      line7='    ServerName '
      line8='    ServerAlias www.'
      line9='    DocumentRoot /var/www/'+N_web+'/public_html'
      line10="   ErrorLog ${APACHE_LOG_DIR}/error.log"
      line11="   CustomLog ${APACHE_LOG_DIR}/access.log combined"
      line12="</VirtualHost>"
      ruta_conf=(str('/etc/apache2/sites-available/'+N_web+'.conf'))
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Archivo hosts      
      line13="127.0.0.1 localhost"
      line14=ip_pc+'    '+N_web
      line15=ip_pc+'    '+'www.'+N_web
      line16=ip_pc+'    '+'http://www.'+N_web
      line16=ip_pc+'    '+'https://www.'+N_web
      ruta_host=(str('/etc/hosts'))
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Archivo Port
      line17="# /etc/apache2/sites-enabled/000-default.conf"
      line18="#NameVirtualHost *:443"
      line19=""
      line20="Listen 443"
      ruta_ports=(str('/etc/apache2/ports.conf'))
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
      
      pase=input(str("tiene ya certificado? : ")) #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ certificado
  
      if(pase=="N"):

        print("creando carpeta y certificado")
        os.system('mkdir /etc/apache2/ssl')         
        os.system('openssl req -x509 -nodes -days 1095 -newkey rsa:2048 -out /etc/apache2/ssl/'+N_web+'.pem -keyout /etc/apache2/ssl/'+N_web+'.key')
        os.system('chmod -R 600 /etc/apache2/ssl')
        os.system('systemctl restart apache2')
        print("certificado creado")

      else:

        print("creando certificado")
        os.system('openssl req -x509 -nodes -days 1095 -newkey rsa:2048 -out /etc/apache2/ssl/'+N_web+'.pem -keyout /etc/apache2/ssl/'+N_web+'.key')
        os.system('chmod -R 600 /etc/apache2/ssl')
        os.system('systemctl restart apache2')
        print("certificado creado")
                                            #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ fin certificado

                                            #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Archivo Conf
      print("creado archivo conf")
      archivo_conf=open(ruta_conf,"a")
      archivo_conf.write(line1+'\n')
      archivo_conf.write(line2+'\n')
      archivo_conf.write(line3+'\n')
      archivo_conf.write(line4+'\n')
      archivo_conf.write(line5+'\n')
      archivo_conf.write(line6+N_web+'\n')
      archivo_conf.write(line7+N_web+'\n')
      archivo_conf.write(line8+N_web+'\n')
      archivo_conf.write(line9+'\n')
      archivo_conf.write(line10+'\n')
      archivo_conf.write(line11+'\n')
      archivo_conf.write(line12+'\n')
      archivo_conf.close()

      print("Archivo Conf creado")              #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ fin Conf
      print("")
      print("Modificando archivo hosts")        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Archivo hosts
      
      os.system('unlink '+ruta_host)
      archivo_hosts=open(ruta_host,"a")
      archivo_hosts.write(line13+'\n')
      archivo_hosts.write(line14+'\n')
      archivo_hosts.write(line15+'\n')
      archivo_hosts.close()
 
      print("Archivo Hosts creado")             #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ fin hosts
      print("")
      print("Modificando archivo ports")        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Archivo ports

      os.system('unlink '+ruta_ports)
      archivo_ports=open(ruta_ports,"a")
      archivo_ports.write(line16+'\n')
      archivo_ports.write(line17+'\n')
      archivo_ports.write(line18+'\n')
      archivo_ports.write(line19+'\n')
      archivo_ports.write(line20+'\n')
      archivo_ports.close()

      print("Configurado arcchivo ports")                #$$$$$$$$$$$$$$$$$$$$$$$$$$ fin ports
      print("")
      print("Activando modulo Ssl Apache2")
      os.system('cd /etc/apache2/mods-available | a2enmod ssl') #$$$$$$$$$$$$$$$$$$$$$$$$$$ Activa modulo ssl apache2
      os.system('a2ensite '+N_web+'.conf')
      os.system('systemctl reload apache2')
      os.system('service apache2 reload')
      
      print("Moduloo  Activado")

      break

    except TypeError:
      print("error proc ")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ funciones de activacion $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  
def actserver(N_web):

  os.system('systemctl start apache2')# 
  os.system('service apache2 start')# 
  os.system('apache2ctl -t')# 
 


def offserver(N_web):

  os.system('systemctl stop apache2')# 
  os.system('service apache2 stop')# 

def iptable():
  
  print("configurando iptables") 

  os.system('iptables -F')
  os.system('iptables -X')
  os.system('iptables -Z')
  os.system('iptables -t nat -F') 
  os.system('iptables -A INPUT -p tcp -m tcp --dport 443 -j ACCEPT')
  os.system('iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT')
  os.system('iptables -A INPUT -p tcp -m tcp --dport 8080 -j ACCEPT')
  os.system('iptables-save > /etc/iptables.up.rules')

  print("configuracion iptables terminada")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ loop program $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

while exit==False:
  
  menu()
  key=(int(input("            "+"Select: ")))
  
  if (key==1):

    Nombweb()
    iptable()

  elif (key==2):
    confweb(N_web)
  
  elif (key==3):

    actserver(N_web)

  elif (key==4):
    offserver(N_web)

  elif (key==5):
    exit=True
  
print("\033[1;31;1m ")  
print("Smp_A byTe_Dey_bYte_HackiNg")
print("\033[1;31;m ")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
