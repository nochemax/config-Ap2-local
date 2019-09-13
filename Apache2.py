
# Creador Smp_A
# Fecha 08.09.2019
# Nombre programa Laugh room
# Tipo phyton3
# simple server apache2 localhot con dominio

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

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Funciones operativas $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

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


def confweb(N_web):

  global ip_pc
  
  ip_pc=input(str("introduzca la ip de su equipo : "))
  print(str(ip_pc))

  line='<VirtualHost '+ip_pc+':80>'
  line1="    ServerAdmin admin@"
  line2="    ServerName "
  line3="    ServerAlias www."
  line4='    DocumentRoot /var/www/'+N_web+'/public_html'
  line5="    ErrorLog ${APACHE_LOG_DIR}/error.log"
  line6="    CustomLog ${APACHE_LOG_DIR}/access.log combined"
  line7="</VirtualHost>"
  ruta_conf=(str('/etc/apache2/sites-available/'+N_web+'.conf'))

  archivo_conf=open(ruta_conf,"a")
  archivo_conf.write(line+'\n')
  archivo_conf.write(line1+N_web+'\n')
  archivo_conf.write(line2+N_web+'\n')
  archivo_conf.write(line3+N_web+'\n')
  archivo_conf.write(line4+'\n')
  archivo_conf.write(line5+'\n')
  archivo_conf.write(line6+'\n')
  archivo_conf.write(line7+'\n')
  archivo_conf.close()
  print("Archivo Conf creado")
  line8=ip_pc+'    '+N_web
  line9=ip_pc+'    '+'www'+N_web
  ruta_host=(str('/etc/hosts'))
  archivo_hosts=open(ruta_host,"a")
  archivo_hosts.write(line8+'\n')
  archivo_hosts.close()
  print("Archivo Hosts creado")


def actserver(N_web):

  os.system('a2ensite '+N_web+'.conf')#
  os.system('systemctl start apache2')# 
  os.system('service apache2 start')# 
  os.system('apache2ctl -t')# 
  os.system('service apache2 reload')# 


def offserver(N_web):

  os.system('a2ensite '+N_web+'.conf')#
  os.system('systemctl stop apache2')# 
  os.system('service apache2 stop')# 


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ loop program $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

while exit==False:
  
  menu()
  key=(int(input("            "+"Select: ")))
  
  if (key==1):
    Nombweb()

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
