# Importamos las librerías necesarias
import os
import time  
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
from os import remove, sep
import urllib.request
import pandas as pd
import numpy as np
import seaborn as sb

espacio='-------------'

print('SGIRPC')

dirtxt=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\SGIRPC.txt'
dircsv=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\SGIRPC.csv'

print(espacio)
url1 = 'http://189.254.33.151/stn/juarez/downld02.txt'
file1 = dirtxt
r = urllib.request.urlopen(url1)
f = open(file1,'wb')
f.write(r.read())
f.close()
#print(file1)
print('Datos de la estación SGIRPC obtenidos')

try:
    with open(dirtxt, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
          
        # pointer for position
        ptr = 1
      
        # opening in writing mode
        with open(dirtxt, 'w') as fw:
            for line in lines:
                
                # we want to remove 5th line
                if ptr != 1:
                    fw.write(line)
                ptr += 1
    print("Deleted")
      
except:
    print("Oops! No se pudo eliminar fila")

try:
    with open(dirtxt, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
          
        # pointer for position
        ptr = 1
      
        # opening in writing mode
        with open(dirtxt, 'w') as fw:
            for line in lines:
                
                # we want to remove 5th line
                if ptr != 2:
                    fw.write(line)
                ptr += 1
    print("Deleted")
      
except:
    print("Oops! No se pudo eliminar fila")


sgirpc=open(dirtxt)
texto0=sgirpc.read()

texto1=texto0.replace(" ",",")
texto2=texto1.replace("---","0")
texto3=texto2.replace(",,",",")
texto4=texto3.replace(",,,",",")
texto5=texto4.replace(",,,,",",")
#print(texto5)
sgirpc=open(dirtxt,"w")
sgirpc.write(texto5)
sgirpc.close()

sgirpc=open(dirtxt)
texto0=sgirpc.read()
texto1=texto0.replace(",,",",")
texto2=texto1.replace(",Date","Fecha")
#print(texto1)
sgirpc=open(dircsv,"w")
sgirpc.write(texto2)
sgirpc.closed
sgirpc.closed

sgirpc=open(dircsv)
nombrescol=sgirpc.read()
texto1=nombrescol.replace("Out","temperatura")
texto2=texto1.replace("Hum","humedadRelativa")
texto3=texto2.replace("Pt.","puntoRocio")
texto4=texto3.replace("Speed.1","velocidadRacha")
texto5=texto4.replace("Dir.1","direccionRacha")
texto6=texto5.replace("Speed","velocidadViento")
texto7=texto6.replace("Dir","direccionViento") 
texto8=texto7.replace("Bar","presionBar")
texto9=texto8.replace("Rain","lluvia")
sgirpc2=open(dircsv,"w")
sgirpc2.write(texto9)
sgirpc2.close()
sgirpc.close()

sgirpc=open(dircsv)
texto=sgirpc.read()
texto0=texto.replace("12:00a","00:00")
texto1=texto0.replace("12:10a","00:10")
texto2=texto1.replace("12:20a","00:20")
texto3=texto2.replace("12:30a","00:30")
texto4=texto3.replace("12:40a","00:40")
texto5=texto4.replace("12:50a","00:50")
texto6=texto5.replace("1:00a","1:00")
texto7=texto6.replace("1:10a","1:10")
texto8=texto7.replace("1:20a","1:20")
texto9=texto8.replace("1:30a","1:30")
texto10=texto9.replace("1:40a","1:40")
texto11=texto10.replace("1:50a","1:50")
texto12=texto11.replace("2:00a","2:00")
texto13=texto12.replace("2:10a","2:10")
texto14=texto13.replace("2:20a","2:20")
texto15=texto14.replace("2:30a","2:30")
texto16=texto15.replace("2:40a","2:40")
texto17=texto16.replace("2:50a","2:50")
texto18=texto17.replace("3:00a","3:00")
texto19=texto18.replace("3:10a","3:10")
texto20=texto19.replace("3:20a","3:20")
texto21=texto20.replace("3:30a","3:30")
texto22=texto21.replace("3:40a","3:40")
texto23=texto22.replace("3:50a","3:50")
texto24=texto23.replace("4:00a","4:00")
texto25=texto24.replace("4:10a","4:10")
texto26=texto25.replace("4:20a","4:20")
texto27=texto26.replace("4:30a","4:30")
texto28=texto27.replace("4:40a","4:40")
texto29=texto28.replace("4:50a","4:50")
texto30=texto29.replace("5:00a","5:00")
texto31=texto30.replace("5:10a","5:10")
texto32=texto31.replace("5:20a","5:20")
texto33=texto32.replace("5:30a","5:30")
texto34=texto33.replace("5:40a","5:40")
texto35=texto34.replace("5:50a","5:50")
texto36=texto35.replace("6:00a","6:00")
texto37=texto36.replace("6:10a","6:10")
texto38=texto37.replace("6:20a","6:20")
texto39=texto38.replace("6:30a","6:30")
texto40=texto39.replace("6:40a","6:40")
texto41=texto40.replace("6:50a","6:50")
texto42=texto41.replace("7:00a","7:00")
texto43=texto42.replace("7:10a","7:10")
texto44=texto43.replace("7:20a","7:20")
texto45=texto44.replace("7:30a","7:30")
texto46=texto45.replace("7:40a","7:40")
texto47=texto46.replace("7:50a","7:50")
texto48=texto47.replace("8:00a","8:00")
texto49=texto48.replace("8:10a","8:10")
texto50=texto49.replace("8:20a","8:20")
texto51=texto50.replace("8:30a","8:30")
texto52=texto51.replace("8:40a","8:40")
texto53=texto52.replace("8:50a","8:50")
texto54=texto53.replace("9:00a","9:00")
texto55=texto54.replace("9:10a","9:10")
texto56=texto55.replace("9:20a","9:20")
texto57=texto56.replace("9:30a","9:30")
texto58=texto57.replace("9:40a","9:40")
texto59=texto58.replace("9:50a","9:50")
texto60=texto59.replace("10:00a","10:00")
texto61=texto60.replace("10:10a","10:10")
texto62=texto61.replace("10:20a","10:20")
texto63=texto62.replace("10:30a","10:30")
texto64=texto63.replace("10:40a","10:40")
texto65=texto64.replace("10:50a","10:50")
texto66=texto65.replace("11:00a","11:00")
texto67=texto66.replace("11:10a","11:10")
texto68=texto67.replace("11:20a","11:20")
texto69=texto68.replace("11:30a","11:30")
texto70=texto69.replace("11:40a","11:40")
texto71=texto70.replace("11:50a","11:50")
texto72=texto71.replace("12:00p","12:00")
texto73=texto72.replace("12:10p","12:10")
texto74=texto73.replace("12:20p","12:20")
texto75=texto74.replace("12:30p","12:30")
texto76=texto75.replace("12:40p","12:40")
texto77=texto76.replace("12:50p","12:50")
texto78=texto77.replace("1:00p","13:00")
texto79=texto78.replace("1:10p","13:10")
texto80=texto79.replace("1:20p","13:20")
texto81=texto80.replace("1:30p","13:30")
texto82=texto81.replace("1:40p","13:40")
texto83=texto82.replace("1:50p","13:50")
texto84=texto83.replace("2:00p","14:00")
texto85=texto84.replace("2:10p","14:10")
texto86=texto85.replace("2:20p","14:20")
texto87=texto86.replace("2:30p","14:30")
texto88=texto87.replace("2:40p","14:40")
texto89=texto88.replace("2:50p","14:50")
texto90=texto89.replace("3:00p","15:00")
texto91=texto90.replace("3:10p","15:10")
texto92=texto91.replace("3:20p","15:20")
texto93=texto92.replace("3:30p","15:30")
texto94=texto93.replace("3:40p","15:40")
texto95=texto94.replace("3:50p","15:50")
texto96=texto95.replace("4:00p","16:00")
texto97=texto96.replace("4:10p","16:10")
texto98=texto97.replace("4:20p","16:20")
texto99=texto98.replace("4:30p","16:30")
texto100=texto99.replace("4:40p","16:40")
texto11=texto100.replace("4:50p","16:50")
texto12=texto11.replace("5:00p","17:00")
texto13=texto12.replace("5:10p","17:10")
texto14=texto13.replace("5:20p","17:20")
texto15=texto14.replace("5:30p","17:30")
texto16=texto15.replace("5:40p","17:40")
texto17=texto16.replace("5:50p","17:50")
texto18=texto17.replace("6:00p","18:00")
texto19=texto18.replace("6:10p","18:10")
texto110=texto19.replace("6:20p","18:20")
texto111=texto110.replace("6:30p","18:30")
texto112=texto111.replace("6:40p","18:40")
texto113=texto112.replace("6:50p","18:50")
texto114=texto113.replace("7:00p","19:00")
texto115=texto114.replace("7:10p","19:10")
texto116=texto115.replace("7:20p","19:20")
texto117=texto116.replace("7:30p","19:30")
texto118=texto117.replace("7:40p","19:40")
texto119=texto118.replace("7:50p","19:50")
texto120=texto119.replace("8:00p","20:00")
texto121=texto120.replace("8:10p","20:10")
texto122=texto121.replace("8:20p","20:20")
texto123=texto122.replace("8:30p","20:30")
texto124=texto123.replace("8:40p","20:40")
texto125=texto124.replace("8:50p","20:50")
texto126=texto125.replace("9:00p","21:00")
texto127=texto126.replace("9:10p","21:10")
texto128=texto127.replace("9:20p","21:20")
texto129=texto128.replace("9:30p","21:30")
texto130=texto129.replace("9:40p","21:40")
texto131=texto130.replace("9:50p","21:50")
texto132=texto131.replace("10:00p","22:00")
texto133=texto132.replace("10:10p","22:10")
texto134=texto133.replace("10:20p","22:20")
texto135=texto134.replace("10:30p","22:30")
texto136=texto135.replace("10:40p","22:40")
texto137=texto136.replace("10:50p","22:50")
texto138=texto137.replace("11:00p","23:00")
texto139=texto138.replace("11:10p","23:10")
texto140=texto139.replace("11:20p","23:20")
texto141=texto140.replace("11:30p","23:30")
texto142=texto141.replace("11:40p","23:40")
texto143=texto142.replace("11:50p","23:50")
texto144=texto143.replace("113:00","23:00")
texto145=texto144.replace("113:10","23:10")
texto146=texto145.replace("113:20","23:20")
texto147=texto146.replace("113:30","23:30")
texto148=texto147.replace("113:40","23:40")
texto149=texto148.replace("113:50","23:50")
sgirpc=open(dircsv,"w")
sgirpc.write(texto149)
sgirpc.closed
sgirpc.closed




sgirpctxt=open(dircsv)
sgirpc1=sgirpctxt.read()
cambio3=sgirpc1.replace("NNE","22.5")
cambio4=cambio3.replace("ENE","67.5")
cambio5=cambio4.replace("ESE","112.5")
cambio6=cambio5.replace("SSE","157.5")
cambio7=cambio6.replace("SSW","202.5")
cambio8=cambio7.replace("WSW","247.5")
cambio9=cambio8.replace("WNW","292.5")
cambio10=cambio9.replace("NNW","337.5")
cambio11=cambio10.replace("NE","45")
cambio12=cambio11.replace("SE","135")
cambio13=cambio12.replace("SW","225")
cambio14=cambio13.replace("NW","315")

#cambio1=sgirpc1.replace("N","360")
#print(cambio4)
sgirpc=open(dircsv,"w")
sgirpc.write(cambio14)
sgirpc.closed
sgirpctxt.closed



sgirpc=pd.read_csv(dircsv, usecols=(0,1,2,5,6,7,8,10,11,15,16), index_col=False, header=0)
#print(sgirpc)
sgirpc['fechaHora']=sgirpc['Fecha'].map(str)  + ' ' + sgirpc['Time'].map(str)
sgirpc
#print(sgirpc)
sgirpc.to_csv(dircsv)

sgirpc=open(dircsv)
texto=sgirpc.read()
cambio1=texto.replace("direccionViento.1","direccionRacha")
cambio2=cambio1.replace("velocidadViento.1","velocidadRacha")
#print(cambio14)
sgirpc=open(dircsv,"w")
sgirpc.write(cambio2)
sgirpc.closed

sgirpc=open(dircsv)
texto=sgirpc.read()
cambio1=texto.replace("N","360")
sgirpc=open(dircsv,"w")
sgirpc.write(cambio1)
sgirpc.closed

sgirpc=open(dircsv)
texto=sgirpc.read()
cambio1=texto.replace("E","90")
sgirpc=open(dircsv,"w")
sgirpc.write(cambio1)
sgirpc.closed

sgirpc=open(dircsv)
texto=sgirpc.read()
cambio1=texto.replace("S","180")
sgirpc=open(dircsv,"w")
sgirpc.write(cambio1)
sgirpc.closed

sgirpc=open(dircsv)
texto=sgirpc.read()
cambio1=texto.replace("W","270")
sgirpc=open(dircsv,"w")
sgirpc.write(cambio1)
sgirpc.closed

DF=pd.read_csv(dircsv, index_col=0)
DF['idEstacion']=np.where(DF['Time'] !='[]', 'sgirpc', ' ', )
#print(DF)
DF.to_csv(dircsv)

sgirpc=pd.read_csv(dircsv, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
print(sgirpc)
sgirpc.to_csv(dircsv)

print('Datos de la estación SGIRPC listos')

espacio='-------------'
print('Santa Fe')
dirtxt=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\Santa_Fe.txt'
dircsv=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\Santa_Fe.csv'

print(espacio)
url1 = 'http://189.254.33.151/stn/cuajimalpa/downld02.txt'
file1 = dirtxt
r = urllib.request.urlopen(url1)
f = open(file1,'wb')
f.write(r.read())
f.close()
#print(file1)
print('Datos de la estación Santa Fe obtenidos')

try:
    with open(dirtxt, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
          
        # pointer for position
        ptr = 1
      
        # opening in writing mode
        with open(dirtxt, 'w') as fw:
            for line in lines:
                
                # we want to remove 5th line
                if ptr != 1:
                    fw.write(line)
                ptr += 1
    print("Deleted")
      
except:
    print("Oops! No se pudo eliminar fila")

try:
    with open(dirtxt, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
          
        # pointer for position
        ptr = 1
      
        # opening in writing mode
        with open(dirtxt, 'w') as fw:
            for line in lines:
                
                # we want to remove 5th line
                if ptr != 2:
                    fw.write(line)
                ptr += 1
    print("Deleted")
      
except:
    print("Oops! No se pudo eliminar fila")


stfs=open(dirtxt)
texto0=stfs.read()

texto1=texto0.replace(" ",",")
texto2=texto1.replace("---","0")
texto3=texto2.replace(",,",",")
texto4=texto3.replace(",,,",",")
texto5=texto4.replace(",,,,",",")
#print(texto5)
stfs=open(dirtxt,"w")
stfs.write(texto5)
stfs.close()

stfs=open(dirtxt)
texto0=stfs.read()
texto1=texto0.replace(",,",",")
texto2=texto1.replace(",Date","Fecha")
#print(texto1)
stfs=open(dircsv,"w")
stfs.write(texto2)
stfs.closed
stfs.closed

stfs=open(dircsv)
nombrescol=stfs.read()
texto1=nombrescol.replace("Out","temperatura")
texto2=texto1.replace("Hum","humedadRelativa")
texto3=texto2.replace("Pt.","puntoRocio")
texto4=texto3.replace("Speed.1","velocidadRacha")
texto5=texto4.replace("Dir.1","direccionRacha")
texto6=texto5.replace("Speed","velocidadViento")
texto7=texto6.replace("Dir","direccionViento") 
texto8=texto7.replace("Bar","presionBar")
texto9=texto8.replace("Rain","lluvia")
stfs2=open(dircsv,"w")
stfs2.write(texto9)
stfs2.close()
stfs.close()

stfs=open(dircsv)
texto=stfs.read()
texto0=texto.replace("12:00a","00:00")
texto1=texto0.replace("12:10a","00:10")
texto2=texto1.replace("12:20a","00:20")
texto3=texto2.replace("12:30a","00:30")
texto4=texto3.replace("12:40a","00:40")
texto5=texto4.replace("12:50a","00:50")
texto6=texto5.replace("1:00a","1:00")
texto7=texto6.replace("1:10a","1:10")
texto8=texto7.replace("1:20a","1:20")
texto9=texto8.replace("1:30a","1:30")
texto10=texto9.replace("1:40a","1:40")
texto11=texto10.replace("1:50a","1:50")
texto12=texto11.replace("2:00a","2:00")
texto13=texto12.replace("2:10a","2:10")
texto14=texto13.replace("2:20a","2:20")
texto15=texto14.replace("2:30a","2:30")
texto16=texto15.replace("2:40a","2:40")
texto17=texto16.replace("2:50a","2:50")
texto18=texto17.replace("3:00a","3:00")
texto19=texto18.replace("3:10a","3:10")
texto20=texto19.replace("3:20a","3:20")
texto21=texto20.replace("3:30a","3:30")
texto22=texto21.replace("3:40a","3:40")
texto23=texto22.replace("3:50a","3:50")
texto24=texto23.replace("4:00a","4:00")
texto25=texto24.replace("4:10a","4:10")
texto26=texto25.replace("4:20a","4:20")
texto27=texto26.replace("4:30a","4:30")
texto28=texto27.replace("4:40a","4:40")
texto29=texto28.replace("4:50a","4:50")
texto30=texto29.replace("5:00a","5:00")
texto31=texto30.replace("5:10a","5:10")
texto32=texto31.replace("5:20a","5:20")
texto33=texto32.replace("5:30a","5:30")
texto34=texto33.replace("5:40a","5:40")
texto35=texto34.replace("5:50a","5:50")
texto36=texto35.replace("6:00a","6:00")
texto37=texto36.replace("6:10a","6:10")
texto38=texto37.replace("6:20a","6:20")
texto39=texto38.replace("6:30a","6:30")
texto40=texto39.replace("6:40a","6:40")
texto41=texto40.replace("6:50a","6:50")
texto42=texto41.replace("7:00a","7:00")
texto43=texto42.replace("7:10a","7:10")
texto44=texto43.replace("7:20a","7:20")
texto45=texto44.replace("7:30a","7:30")
texto46=texto45.replace("7:40a","7:40")
texto47=texto46.replace("7:50a","7:50")
texto48=texto47.replace("8:00a","8:00")
texto49=texto48.replace("8:10a","8:10")
texto50=texto49.replace("8:20a","8:20")
texto51=texto50.replace("8:30a","8:30")
texto52=texto51.replace("8:40a","8:40")
texto53=texto52.replace("8:50a","8:50")
texto54=texto53.replace("9:00a","9:00")
texto55=texto54.replace("9:10a","9:10")
texto56=texto55.replace("9:20a","9:20")
texto57=texto56.replace("9:30a","9:30")
texto58=texto57.replace("9:40a","9:40")
texto59=texto58.replace("9:50a","9:50")
texto60=texto59.replace("10:00a","10:00")
texto61=texto60.replace("10:10a","10:10")
texto62=texto61.replace("10:20a","10:20")
texto63=texto62.replace("10:30a","10:30")
texto64=texto63.replace("10:40a","10:40")
texto65=texto64.replace("10:50a","10:50")
texto66=texto65.replace("11:00a","11:00")
texto67=texto66.replace("11:10a","11:10")
texto68=texto67.replace("11:20a","11:20")
texto69=texto68.replace("11:30a","11:30")
texto70=texto69.replace("11:40a","11:40")
texto71=texto70.replace("11:50a","11:50")
texto72=texto71.replace("12:00p","12:00")
texto73=texto72.replace("12:10p","12:10")
texto74=texto73.replace("12:20p","12:20")
texto75=texto74.replace("12:30p","12:30")
texto76=texto75.replace("12:40p","12:40")
texto77=texto76.replace("12:50p","12:50")
texto78=texto77.replace("1:00p","13:00")
texto79=texto78.replace("1:10p","13:10")
texto80=texto79.replace("1:20p","13:20")
texto81=texto80.replace("1:30p","13:30")
texto82=texto81.replace("1:40p","13:40")
texto83=texto82.replace("1:50p","13:50")
texto84=texto83.replace("2:00p","14:00")
texto85=texto84.replace("2:10p","14:10")
texto86=texto85.replace("2:20p","14:20")
texto87=texto86.replace("2:30p","14:30")
texto88=texto87.replace("2:40p","14:40")
texto89=texto88.replace("2:50p","14:50")
texto90=texto89.replace("3:00p","15:00")
texto91=texto90.replace("3:10p","15:10")
texto92=texto91.replace("3:20p","15:20")
texto93=texto92.replace("3:30p","15:30")
texto94=texto93.replace("3:40p","15:40")
texto95=texto94.replace("3:50p","15:50")
texto96=texto95.replace("4:00p","16:00")
texto97=texto96.replace("4:10p","16:10")
texto98=texto97.replace("4:20p","16:20")
texto99=texto98.replace("4:30p","16:30")
texto100=texto99.replace("4:40p","16:40")
texto11=texto100.replace("4:50p","16:50")
texto12=texto11.replace("5:00p","17:00")
texto13=texto12.replace("5:10p","17:10")
texto14=texto13.replace("5:20p","17:20")
texto15=texto14.replace("5:30p","17:30")
texto16=texto15.replace("5:40p","17:40")
texto17=texto16.replace("5:50p","17:50")
texto18=texto17.replace("6:00p","18:00")
texto19=texto18.replace("6:10p","18:10")
texto110=texto19.replace("6:20p","18:20")
texto111=texto110.replace("6:30p","18:30")
texto112=texto111.replace("6:40p","18:40")
texto113=texto112.replace("6:50p","18:50")
texto114=texto113.replace("7:00p","19:00")
texto115=texto114.replace("7:10p","19:10")
texto116=texto115.replace("7:20p","19:20")
texto117=texto116.replace("7:30p","19:30")
texto118=texto117.replace("7:40p","19:40")
texto119=texto118.replace("7:50p","19:50")
texto120=texto119.replace("8:00p","20:00")
texto121=texto120.replace("8:10p","20:10")
texto122=texto121.replace("8:20p","20:20")
texto123=texto122.replace("8:30p","20:30")
texto124=texto123.replace("8:40p","20:40")
texto125=texto124.replace("8:50p","20:50")
texto126=texto125.replace("9:00p","21:00")
texto127=texto126.replace("9:10p","21:10")
texto128=texto127.replace("9:20p","21:20")
texto129=texto128.replace("9:30p","21:30")
texto130=texto129.replace("9:40p","21:40")
texto131=texto130.replace("9:50p","21:50")
texto132=texto131.replace("10:00p","22:00")
texto133=texto132.replace("10:10p","22:10")
texto134=texto133.replace("10:20p","22:20")
texto135=texto134.replace("10:30p","22:30")
texto136=texto135.replace("10:40p","22:40")
texto137=texto136.replace("10:50p","22:50")
texto138=texto137.replace("11:00p","23:00")
texto139=texto138.replace("11:10p","23:10")
texto140=texto139.replace("11:20p","23:20")
texto141=texto140.replace("11:30p","23:30")
texto142=texto141.replace("11:40p","23:40")
texto143=texto142.replace("11:50p","23:50")
texto144=texto143.replace("113:00","23:00")
texto145=texto144.replace("113:10","23:10")
texto146=texto145.replace("113:20","23:20")
texto147=texto146.replace("113:30","23:30")
texto148=texto147.replace("113:40","23:40")
texto149=texto148.replace("113:50","23:50")
stfs=open(dircsv,"w")
stfs.write(texto149)
stfs.closed
stfs.closed




stfstxt=open(dircsv)
stfs1=stfstxt.read()
cambio3=stfs1.replace("NNE","22.5")
cambio4=cambio3.replace("ENE","67.5")
cambio5=cambio4.replace("ESE","112.5")
cambio6=cambio5.replace("SSE","157.5")
cambio7=cambio6.replace("SSW","202.5")
cambio8=cambio7.replace("WSW","247.5")
cambio9=cambio8.replace("WNW","292.5")
cambio10=cambio9.replace("NNW","337.5")
cambio11=cambio10.replace("NE","45")
cambio12=cambio11.replace("SE","135")
cambio13=cambio12.replace("SW","225")
cambio14=cambio13.replace("NW","315")

#cambio1=stfs1.replace("N","360")
#print(cambio4)
stfs=open(dircsv,"w")
stfs.write(cambio14)
stfs.closed
stfstxt.closed



stfs=pd.read_csv(dircsv, usecols=(0,1,2,5,6,7,8,10,11,15,16), index_col=False, header=0)
#print(stfs)
stfs['fechaHora']=stfs['Fecha'].map(str)  + ' ' + stfs['Time'].map(str)
stfs
#print(stfs)
stfs.to_csv(dircsv)

stfs=open(dircsv)
texto=stfs.read()
cambio1=texto.replace("direccionViento.1","direccionRacha")
cambio2=cambio1.replace("velocidadViento.1","velocidadRacha")
#print(cambio14)
stfs=open(dircsv,"w")
stfs.write(cambio2)
stfs.closed

stfs=open(dircsv)
texto=stfs.read()
cambio1=texto.replace("N","360")
stfs=open(dircsv,"w")
stfs.write(cambio1)
stfs.closed

stfs=open(dircsv)
texto=stfs.read()
cambio1=texto.replace("E","90")
stfs=open(dircsv,"w")
stfs.write(cambio1)
stfs.closed

stfs=open(dircsv)
texto=stfs.read()
cambio1=texto.replace("S","180")
stfs=open(dircsv,"w")
stfs.write(cambio1)
stfs.closed

stfs=open(dircsv)
texto=stfs.read()
cambio1=texto.replace("W","270")
stfs=open(dircsv,"w")
stfs.write(cambio1)
stfs.closed

DF=pd.read_csv(dircsv, index_col=0)
DF['idEstacion']=np.where(DF['Time'] !='[]', 'stfs', ' ', )
#print(DF)
DF.to_csv(dircsv)

stfs=pd.read_csv(dircsv, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
print(stfs)
stfs.to_csv(dircsv)
print('Datos de la estacion Santa Fe listos')

espacio='-------------'
print('Cuautepec')

dirtxt=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\Cuautepec.txt'
dircsv=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\Cuautepec.csv'

print(espacio)
url1 = 'http://189.254.33.151/stn/cuautepec/downld02.txt'
file1 = dirtxt
r = urllib.request.urlopen(url1)
f = open(file1,'wb')
f.write(r.read())
f.close()
#print(file1)
print('Datos de la estación Cuautepec obtenidos')

try:
    with open(dirtxt, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
          
        # pointer for position
        ptr = 1
      
        # opening in writing mode
        with open(dirtxt, 'w') as fw:
            for line in lines:
                
                # we want to remove 5th line
                if ptr != 1:
                    fw.write(line)
                ptr += 1
    print("Deleted")
      
except:
    print("Oops! No se pudo eliminar fila")

try:
    with open(dirtxt, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
          
        # pointer for position
        ptr = 1
      
        # opening in writing mode
        with open(dirtxt, 'w') as fw:
            for line in lines:
                
                # we want to remove 5th line
                if ptr != 2:
                    fw.write(line)
                ptr += 1
    print("Deleted")
      
except:
    print("Oops! No se pudo eliminar fila")


cuaus=open(dirtxt)
texto0=cuaus.read()

texto1=texto0.replace(" ",",")
texto2=texto1.replace("---","0")
texto3=texto2.replace(",,",",")
texto4=texto3.replace(",,,",",")
texto5=texto4.replace(",,,,",",")
#print(texto5)
cuaus=open(dirtxt,"w")
cuaus.write(texto5)
cuaus.close()

cuaus=open(dirtxt)
texto0=cuaus.read()
texto1=texto0.replace(",,",",")
texto2=texto1.replace(",Date","Fecha")
#print(texto1)
cuaus=open(dircsv,"w")
cuaus.write(texto2)
cuaus.closed
cuaus.closed

cuaus=open(dircsv)
nombrescol=cuaus.read()
texto1=nombrescol.replace("Out","temperatura")
texto2=texto1.replace("Hum","humedadRelativa")
texto3=texto2.replace("Pt.","puntoRocio")
texto4=texto3.replace("Speed.1","velocidadRacha")
texto5=texto4.replace("Dir.1","direccionRacha")
texto6=texto5.replace("Speed","velocidadViento")
texto7=texto6.replace("Dir","direccionViento") 
texto8=texto7.replace("Bar","presionBar")
texto9=texto8.replace("Rain","lluvia")
cuaus2=open(dircsv,"w")
cuaus2.write(texto9)
cuaus2.close()
cuaus.close()

cuaus=open(dircsv)
texto=cuaus.read()
texto0=texto.replace("12:00a","00:00")
texto1=texto0.replace("12:10a","00:10")
texto2=texto1.replace("12:20a","00:20")
texto3=texto2.replace("12:30a","00:30")
texto4=texto3.replace("12:40a","00:40")
texto5=texto4.replace("12:50a","00:50")
texto6=texto5.replace("1:00a","1:00")
texto7=texto6.replace("1:10a","1:10")
texto8=texto7.replace("1:20a","1:20")
texto9=texto8.replace("1:30a","1:30")
texto10=texto9.replace("1:40a","1:40")
texto11=texto10.replace("1:50a","1:50")
texto12=texto11.replace("2:00a","2:00")
texto13=texto12.replace("2:10a","2:10")
texto14=texto13.replace("2:20a","2:20")
texto15=texto14.replace("2:30a","2:30")
texto16=texto15.replace("2:40a","2:40")
texto17=texto16.replace("2:50a","2:50")
texto18=texto17.replace("3:00a","3:00")
texto19=texto18.replace("3:10a","3:10")
texto20=texto19.replace("3:20a","3:20")
texto21=texto20.replace("3:30a","3:30")
texto22=texto21.replace("3:40a","3:40")
texto23=texto22.replace("3:50a","3:50")
texto24=texto23.replace("4:00a","4:00")
texto25=texto24.replace("4:10a","4:10")
texto26=texto25.replace("4:20a","4:20")
texto27=texto26.replace("4:30a","4:30")
texto28=texto27.replace("4:40a","4:40")
texto29=texto28.replace("4:50a","4:50")
texto30=texto29.replace("5:00a","5:00")
texto31=texto30.replace("5:10a","5:10")
texto32=texto31.replace("5:20a","5:20")
texto33=texto32.replace("5:30a","5:30")
texto34=texto33.replace("5:40a","5:40")
texto35=texto34.replace("5:50a","5:50")
texto36=texto35.replace("6:00a","6:00")
texto37=texto36.replace("6:10a","6:10")
texto38=texto37.replace("6:20a","6:20")
texto39=texto38.replace("6:30a","6:30")
texto40=texto39.replace("6:40a","6:40")
texto41=texto40.replace("6:50a","6:50")
texto42=texto41.replace("7:00a","7:00")
texto43=texto42.replace("7:10a","7:10")
texto44=texto43.replace("7:20a","7:20")
texto45=texto44.replace("7:30a","7:30")
texto46=texto45.replace("7:40a","7:40")
texto47=texto46.replace("7:50a","7:50")
texto48=texto47.replace("8:00a","8:00")
texto49=texto48.replace("8:10a","8:10")
texto50=texto49.replace("8:20a","8:20")
texto51=texto50.replace("8:30a","8:30")
texto52=texto51.replace("8:40a","8:40")
texto53=texto52.replace("8:50a","8:50")
texto54=texto53.replace("9:00a","9:00")
texto55=texto54.replace("9:10a","9:10")
texto56=texto55.replace("9:20a","9:20")
texto57=texto56.replace("9:30a","9:30")
texto58=texto57.replace("9:40a","9:40")
texto59=texto58.replace("9:50a","9:50")
texto60=texto59.replace("10:00a","10:00")
texto61=texto60.replace("10:10a","10:10")
texto62=texto61.replace("10:20a","10:20")
texto63=texto62.replace("10:30a","10:30")
texto64=texto63.replace("10:40a","10:40")
texto65=texto64.replace("10:50a","10:50")
texto66=texto65.replace("11:00a","11:00")
texto67=texto66.replace("11:10a","11:10")
texto68=texto67.replace("11:20a","11:20")
texto69=texto68.replace("11:30a","11:30")
texto70=texto69.replace("11:40a","11:40")
texto71=texto70.replace("11:50a","11:50")
texto72=texto71.replace("12:00p","12:00")
texto73=texto72.replace("12:10p","12:10")
texto74=texto73.replace("12:20p","12:20")
texto75=texto74.replace("12:30p","12:30")
texto76=texto75.replace("12:40p","12:40")
texto77=texto76.replace("12:50p","12:50")
texto78=texto77.replace("1:00p","13:00")
texto79=texto78.replace("1:10p","13:10")
texto80=texto79.replace("1:20p","13:20")
texto81=texto80.replace("1:30p","13:30")
texto82=texto81.replace("1:40p","13:40")
texto83=texto82.replace("1:50p","13:50")
texto84=texto83.replace("2:00p","14:00")
texto85=texto84.replace("2:10p","14:10")
texto86=texto85.replace("2:20p","14:20")
texto87=texto86.replace("2:30p","14:30")
texto88=texto87.replace("2:40p","14:40")
texto89=texto88.replace("2:50p","14:50")
texto90=texto89.replace("3:00p","15:00")
texto91=texto90.replace("3:10p","15:10")
texto92=texto91.replace("3:20p","15:20")
texto93=texto92.replace("3:30p","15:30")
texto94=texto93.replace("3:40p","15:40")
texto95=texto94.replace("3:50p","15:50")
texto96=texto95.replace("4:00p","16:00")
texto97=texto96.replace("4:10p","16:10")
texto98=texto97.replace("4:20p","16:20")
texto99=texto98.replace("4:30p","16:30")
texto100=texto99.replace("4:40p","16:40")
texto11=texto100.replace("4:50p","16:50")
texto12=texto11.replace("5:00p","17:00")
texto13=texto12.replace("5:10p","17:10")
texto14=texto13.replace("5:20p","17:20")
texto15=texto14.replace("5:30p","17:30")
texto16=texto15.replace("5:40p","17:40")
texto17=texto16.replace("5:50p","17:50")
texto18=texto17.replace("6:00p","18:00")
texto19=texto18.replace("6:10p","18:10")
texto110=texto19.replace("6:20p","18:20")
texto111=texto110.replace("6:30p","18:30")
texto112=texto111.replace("6:40p","18:40")
texto113=texto112.replace("6:50p","18:50")
texto114=texto113.replace("7:00p","19:00")
texto115=texto114.replace("7:10p","19:10")
texto116=texto115.replace("7:20p","19:20")
texto117=texto116.replace("7:30p","19:30")
texto118=texto117.replace("7:40p","19:40")
texto119=texto118.replace("7:50p","19:50")
texto120=texto119.replace("8:00p","20:00")
texto121=texto120.replace("8:10p","20:10")
texto122=texto121.replace("8:20p","20:20")
texto123=texto122.replace("8:30p","20:30")
texto124=texto123.replace("8:40p","20:40")
texto125=texto124.replace("8:50p","20:50")
texto126=texto125.replace("9:00p","21:00")
texto127=texto126.replace("9:10p","21:10")
texto128=texto127.replace("9:20p","21:20")
texto129=texto128.replace("9:30p","21:30")
texto130=texto129.replace("9:40p","21:40")
texto131=texto130.replace("9:50p","21:50")
texto132=texto131.replace("10:00p","22:00")
texto133=texto132.replace("10:10p","22:10")
texto134=texto133.replace("10:20p","22:20")
texto135=texto134.replace("10:30p","22:30")
texto136=texto135.replace("10:40p","22:40")
texto137=texto136.replace("10:50p","22:50")
texto138=texto137.replace("11:00p","23:00")
texto139=texto138.replace("11:10p","23:10")
texto140=texto139.replace("11:20p","23:20")
texto141=texto140.replace("11:30p","23:30")
texto142=texto141.replace("11:40p","23:40")
texto143=texto142.replace("11:50p","23:50")
texto144=texto143.replace("113:00","23:00")
texto145=texto144.replace("113:10","23:10")
texto146=texto145.replace("113:20","23:20")
texto147=texto146.replace("113:30","23:30")
texto148=texto147.replace("113:40","23:40")
texto149=texto148.replace("113:50","23:50")
cuaus=open(dircsv,"w")
cuaus.write(texto149)
cuaus.closed
cuaus.closed


cuaustxt=open(dircsv)
cuaus1=cuaustxt.read()
cambio3=cuaus1.replace("NNE","22.5")
cambio4=cambio3.replace("ENE","67.5")
cambio5=cambio4.replace("ESE","112.5")
cambio6=cambio5.replace("SSE","157.5")
cambio7=cambio6.replace("SSW","202.5")
cambio8=cambio7.replace("WSW","247.5")
cambio9=cambio8.replace("WNW","292.5")
cambio10=cambio9.replace("NNW","337.5")
cambio11=cambio10.replace("NE","45")
cambio12=cambio11.replace("SE","135")
cambio13=cambio12.replace("SW","225")
cambio14=cambio13.replace("NW","315")

#cambio1=cuaus1.replace("N","360")
#print(cambio4)
cuaus=open(dircsv,"w")
cuaus.write(cambio14)
cuaus.closed
cuaustxt.closed



cuaus=pd.read_csv(dircsv, usecols=(0,1,2,5,6,7,8,10,11,15,16), index_col=False, header=0)
#print(cuaus)
cuaus['fechaHora']=cuaus['Fecha'].map(str)  + ' ' + cuaus['Time'].map(str)
cuaus
#print(cuaus)
cuaus.to_csv(dircsv)

cuaus=open(dircsv)
texto=cuaus.read()
cambio1=texto.replace("direccionViento.1","direccionRacha")
cambio2=cambio1.replace("velocidadViento.1","velocidadRacha")
#print(cambio14)
cuaus=open(dircsv,"w")
cuaus.write(cambio2)
cuaus.closed

cuaus=open(dircsv)
texto=cuaus.read()
cambio1=texto.replace("N","360")
cuaus=open(dircsv,"w")
cuaus.write(cambio1)
cuaus.closed

cuaus=open(dircsv)
texto=cuaus.read()
cambio1=texto.replace("E","90")
cuaus=open(dircsv,"w")
cuaus.write(cambio1)
cuaus.closed

cuaus=open(dircsv)
texto=cuaus.read()
cambio1=texto.replace("S","180")
cuaus=open(dircsv,"w")
cuaus.write(cambio1)
cuaus.closed

cuaus=open(dircsv)
texto=cuaus.read()
cambio1=texto.replace("W","270")
cuaus=open(dircsv,"w")
cuaus.write(cambio1)
cuaus.closed

DF=pd.read_csv(dircsv, index_col=0)
DF['idEstacion']=np.where(DF['Time'] !='[]', 'cuaus', ' ', )
#print(DF)
DF.to_csv(dircsv)

cuaus=pd.read_csv(dircsv, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
print(cuaus)
cuaus.to_csv(dircsv)
print('Datos de la estacion Cuautepec listos')


espacio='-------------'
print('Agricola Oriental')

dirtxt=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\Agricola_Oriental.txt'
dircsv=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\Agricola_Oriental.csv'

print(espacio)
url1 = 'http://189.254.33.151/stn/iztacalco/downld02.txt'
file1 = dirtxt
r = urllib.request.urlopen(url1)
f = open(file1,'wb')
f.write(r.read())
f.close()
#print(file1)
print('Datos de la estación Agricola Oriental obtenidos')

try:
    with open(dirtxt, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
          
        # pointer for position
        ptr = 1
      
        # opening in writing mode
        with open(dirtxt, 'w') as fw:
            for line in lines:
                
                # we want to remove 5th line
                if ptr != 1:
                    fw.write(line)
                ptr += 1
    print("Deleted")
      
except:
    print("Oops! No se pudo eliminar fila")

try:
    with open(dirtxt, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
          
        # pointer for position
        ptr = 1
      
        # opening in writing mode
        with open(dirtxt, 'w') as fw:
            for line in lines:
                
                # we want to remove 5th line
                if ptr != 2:
                    fw.write(line)
                ptr += 1
    print("Deleted")
      
except:
    print("Oops! No se pudo eliminar fila")


agos=open(dirtxt)
texto0=agos.read()

texto1=texto0.replace(" ",",")
texto2=texto1.replace("---","0")
texto3=texto2.replace(",,",",")
texto4=texto3.replace(",,,",",")
texto5=texto4.replace(",,,,",",")
#print(texto5)
agos=open(dirtxt,"w")
agos.write(texto5)
agos.close()

agos=open(dirtxt)
texto0=agos.read()
texto1=texto0.replace(",,",",")
texto2=texto1.replace(",Date","Fecha")
#print(texto1)
agos=open(dircsv,"w")
agos.write(texto2)
agos.closed
agos.closed

agos=open(dircsv)
nombrescol=agos.read()
texto1=nombrescol.replace("Out","temperatura")
texto2=texto1.replace("Hum","humedadRelativa")
texto3=texto2.replace("Pt.","puntoRocio")
texto4=texto3.replace("Speed.1","velocidadRacha")
texto5=texto4.replace("Dir.1","direccionRacha")
texto6=texto5.replace("Speed","velocidadViento")
texto7=texto6.replace("Dir","direccionViento") 
texto8=texto7.replace("Bar","presionBar")
texto9=texto8.replace("Rain","lluvia")
agos2=open(dircsv,"w")
agos2.write(texto9)
agos2.close()
agos.close()

agos=open(dircsv)
texto=agos.read()
texto0=texto.replace("12:00a","00:00")
texto1=texto0.replace("12:10a","00:10")
texto2=texto1.replace("12:20a","00:20")
texto3=texto2.replace("12:30a","00:30")
texto4=texto3.replace("12:40a","00:40")
texto5=texto4.replace("12:50a","00:50")
texto6=texto5.replace("1:00a","1:00")
texto7=texto6.replace("1:10a","1:10")
texto8=texto7.replace("1:20a","1:20")
texto9=texto8.replace("1:30a","1:30")
texto10=texto9.replace("1:40a","1:40")
texto11=texto10.replace("1:50a","1:50")
texto12=texto11.replace("2:00a","2:00")
texto13=texto12.replace("2:10a","2:10")
texto14=texto13.replace("2:20a","2:20")
texto15=texto14.replace("2:30a","2:30")
texto16=texto15.replace("2:40a","2:40")
texto17=texto16.replace("2:50a","2:50")
texto18=texto17.replace("3:00a","3:00")
texto19=texto18.replace("3:10a","3:10")
texto20=texto19.replace("3:20a","3:20")
texto21=texto20.replace("3:30a","3:30")
texto22=texto21.replace("3:40a","3:40")
texto23=texto22.replace("3:50a","3:50")
texto24=texto23.replace("4:00a","4:00")
texto25=texto24.replace("4:10a","4:10")
texto26=texto25.replace("4:20a","4:20")
texto27=texto26.replace("4:30a","4:30")
texto28=texto27.replace("4:40a","4:40")
texto29=texto28.replace("4:50a","4:50")
texto30=texto29.replace("5:00a","5:00")
texto31=texto30.replace("5:10a","5:10")
texto32=texto31.replace("5:20a","5:20")
texto33=texto32.replace("5:30a","5:30")
texto34=texto33.replace("5:40a","5:40")
texto35=texto34.replace("5:50a","5:50")
texto36=texto35.replace("6:00a","6:00")
texto37=texto36.replace("6:10a","6:10")
texto38=texto37.replace("6:20a","6:20")
texto39=texto38.replace("6:30a","6:30")
texto40=texto39.replace("6:40a","6:40")
texto41=texto40.replace("6:50a","6:50")
texto42=texto41.replace("7:00a","7:00")
texto43=texto42.replace("7:10a","7:10")
texto44=texto43.replace("7:20a","7:20")
texto45=texto44.replace("7:30a","7:30")
texto46=texto45.replace("7:40a","7:40")
texto47=texto46.replace("7:50a","7:50")
texto48=texto47.replace("8:00a","8:00")
texto49=texto48.replace("8:10a","8:10")
texto50=texto49.replace("8:20a","8:20")
texto51=texto50.replace("8:30a","8:30")
texto52=texto51.replace("8:40a","8:40")
texto53=texto52.replace("8:50a","8:50")
texto54=texto53.replace("9:00a","9:00")
texto55=texto54.replace("9:10a","9:10")
texto56=texto55.replace("9:20a","9:20")
texto57=texto56.replace("9:30a","9:30")
texto58=texto57.replace("9:40a","9:40")
texto59=texto58.replace("9:50a","9:50")
texto60=texto59.replace("10:00a","10:00")
texto61=texto60.replace("10:10a","10:10")
texto62=texto61.replace("10:20a","10:20")
texto63=texto62.replace("10:30a","10:30")
texto64=texto63.replace("10:40a","10:40")
texto65=texto64.replace("10:50a","10:50")
texto66=texto65.replace("11:00a","11:00")
texto67=texto66.replace("11:10a","11:10")
texto68=texto67.replace("11:20a","11:20")
texto69=texto68.replace("11:30a","11:30")
texto70=texto69.replace("11:40a","11:40")
texto71=texto70.replace("11:50a","11:50")
texto72=texto71.replace("12:00p","12:00")
texto73=texto72.replace("12:10p","12:10")
texto74=texto73.replace("12:20p","12:20")
texto75=texto74.replace("12:30p","12:30")
texto76=texto75.replace("12:40p","12:40")
texto77=texto76.replace("12:50p","12:50")
texto78=texto77.replace("1:00p","13:00")
texto79=texto78.replace("1:10p","13:10")
texto80=texto79.replace("1:20p","13:20")
texto81=texto80.replace("1:30p","13:30")
texto82=texto81.replace("1:40p","13:40")
texto83=texto82.replace("1:50p","13:50")
texto84=texto83.replace("2:00p","14:00")
texto85=texto84.replace("2:10p","14:10")
texto86=texto85.replace("2:20p","14:20")
texto87=texto86.replace("2:30p","14:30")
texto88=texto87.replace("2:40p","14:40")
texto89=texto88.replace("2:50p","14:50")
texto90=texto89.replace("3:00p","15:00")
texto91=texto90.replace("3:10p","15:10")
texto92=texto91.replace("3:20p","15:20")
texto93=texto92.replace("3:30p","15:30")
texto94=texto93.replace("3:40p","15:40")
texto95=texto94.replace("3:50p","15:50")
texto96=texto95.replace("4:00p","16:00")
texto97=texto96.replace("4:10p","16:10")
texto98=texto97.replace("4:20p","16:20")
texto99=texto98.replace("4:30p","16:30")
texto100=texto99.replace("4:40p","16:40")
texto11=texto100.replace("4:50p","16:50")
texto12=texto11.replace("5:00p","17:00")
texto13=texto12.replace("5:10p","17:10")
texto14=texto13.replace("5:20p","17:20")
texto15=texto14.replace("5:30p","17:30")
texto16=texto15.replace("5:40p","17:40")
texto17=texto16.replace("5:50p","17:50")
texto18=texto17.replace("6:00p","18:00")
texto19=texto18.replace("6:10p","18:10")
texto110=texto19.replace("6:20p","18:20")
texto111=texto110.replace("6:30p","18:30")
texto112=texto111.replace("6:40p","18:40")
texto113=texto112.replace("6:50p","18:50")
texto114=texto113.replace("7:00p","19:00")
texto115=texto114.replace("7:10p","19:10")
texto116=texto115.replace("7:20p","19:20")
texto117=texto116.replace("7:30p","19:30")
texto118=texto117.replace("7:40p","19:40")
texto119=texto118.replace("7:50p","19:50")
texto120=texto119.replace("8:00p","20:00")
texto121=texto120.replace("8:10p","20:10")
texto122=texto121.replace("8:20p","20:20")
texto123=texto122.replace("8:30p","20:30")
texto124=texto123.replace("8:40p","20:40")
texto125=texto124.replace("8:50p","20:50")
texto126=texto125.replace("9:00p","21:00")
texto127=texto126.replace("9:10p","21:10")
texto128=texto127.replace("9:20p","21:20")
texto129=texto128.replace("9:30p","21:30")
texto130=texto129.replace("9:40p","21:40")
texto131=texto130.replace("9:50p","21:50")
texto132=texto131.replace("10:00p","22:00")
texto133=texto132.replace("10:10p","22:10")
texto134=texto133.replace("10:20p","22:20")
texto135=texto134.replace("10:30p","22:30")
texto136=texto135.replace("10:40p","22:40")
texto137=texto136.replace("10:50p","22:50")
texto138=texto137.replace("11:00p","23:00")
texto139=texto138.replace("11:10p","23:10")
texto140=texto139.replace("11:20p","23:20")
texto141=texto140.replace("11:30p","23:30")
texto142=texto141.replace("11:40p","23:40")
texto143=texto142.replace("11:50p","23:50")
texto144=texto143.replace("113:00","23:00")
texto145=texto144.replace("113:10","23:10")
texto146=texto145.replace("113:20","23:20")
texto147=texto146.replace("113:30","23:30")
texto148=texto147.replace("113:40","23:40")
texto149=texto148.replace("113:50","23:50")
agos=open(dircsv,"w")
agos.write(texto149)
agos.closed
agos.closed




agostxt=open(dircsv)
agos1=agostxt.read()
cambio3=agos1.replace("NNE","22.5")
cambio4=cambio3.replace("ENE","67.5")
cambio5=cambio4.replace("ESE","112.5")
cambio6=cambio5.replace("SSE","157.5")
cambio7=cambio6.replace("SSW","202.5")
cambio8=cambio7.replace("WSW","247.5")
cambio9=cambio8.replace("WNW","292.5")
cambio10=cambio9.replace("NNW","337.5")
cambio11=cambio10.replace("NE","45")
cambio12=cambio11.replace("SE","135")
cambio13=cambio12.replace("SW","225")
cambio14=cambio13.replace("NW","315")

#cambio1=agos1.replace("N","360")
#print(cambio4)
agos=open(dircsv,"w")
agos.write(cambio14)
agos.closed
agostxt.closed



agos=pd.read_csv(dircsv, usecols=(0,1,2,5,6,7,8,10,11,15,16), index_col=False, header=0)
#print(agos)
agos['fechaHora']=agos['Fecha'].map(str)  + ' ' + agos['Time'].map(str)
agos
#print(agos)
agos.to_csv(dircsv)

agos=open(dircsv)
texto=agos.read()
cambio1=texto.replace("direccionViento.1","direccionRacha")
cambio2=cambio1.replace("velocidadViento.1","velocidadRacha")
#print(cambio14)
agos=open(dircsv,"w")
agos.write(cambio2)
agos.closed

agos=open(dircsv)
texto=agos.read()
cambio1=texto.replace("N","360")
agos=open(dircsv,"w")
agos.write(cambio1)
agos.closed

agos=open(dircsv)
texto=agos.read()
cambio1=texto.replace("E","90")
agos=open(dircsv,"w")
agos.write(cambio1)
agos.closed

agos=open(dircsv)
texto=agos.read()
cambio1=texto.replace("S","180")
agos=open(dircsv,"w")
agos.write(cambio1)
agos.closed

agos=open(dircsv)
texto=agos.read()
cambio1=texto.replace("W","270")
agos=open(dircsv,"w")
agos.write(cambio1)
agos.closed

DF=pd.read_csv(dircsv, index_col=0)
DF['idEstacion']=np.where(DF['Time'] !='[]', 'agos', ' ', )
#print(DF)
DF.to_csv(dircsv)

agos=pd.read_csv(dircsv, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
print(agos)
agos.to_csv(dircsv)
print('Datos de la estacion Agricola Oriental listos')


espacio='-------------'
print('Legaria')

dirtxt=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\Legaria.txt'
dircsv=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\Legaria.csv'

print(espacio)
url1 = 'http://189.254.33.151/stn/miguelhidalgo/downld02.txt'
file1 = dirtxt
r = urllib.request.urlopen(url1)
f = open(file1,'wb')
f.write(r.read())
f.close()
#print(file1)
print('Datos de la estación Legaria obtenidos')

try:
    with open(dirtxt, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
          
        # pointer for position
        ptr = 1
      
        # opening in writing mode
        with open(dirtxt, 'w') as fw:
            for line in lines:
                
                # we want to remove 5th line
                if ptr != 1:
                    fw.write(line)
                ptr += 1
    print("Deleted")
      
except:
    print("Oops! No se pudo eliminar fila")

try:
    with open(dirtxt, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
          
        # pointer for position
        ptr = 1
      
        # opening in writing mode
        with open(dirtxt, 'w') as fw:
            for line in lines:
                
                # we want to remove 5th line
                if ptr != 2:
                    fw.write(line)
                ptr += 1
    print("Deleted")
      
except:
    print("Oops! No se pudo eliminar fila")


legs=open(dirtxt)
texto0=legs.read()

texto1=texto0.replace(" ",",")
texto2=texto1.replace("---","0")
texto3=texto2.replace(",,",",")
texto4=texto3.replace(",,,",",")
texto5=texto4.replace(",,,,",",")
#print(texto5)
legs=open(dirtxt,"w")
legs.write(texto5)
legs.close()

legs=open(dirtxt)
texto0=legs.read()
texto1=texto0.replace(",,",",")
texto2=texto1.replace(",Date","Fecha")
#print(texto1)
legs=open(dircsv,"w")
legs.write(texto2)
legs.closed
legs.closed

legs=open(dircsv)
nombrescol=legs.read()
texto1=nombrescol.replace("Out","temperatura")
texto2=texto1.replace("Hum","humedadRelativa")
texto3=texto2.replace("Pt.","puntoRocio")
texto4=texto3.replace("Speed.1","velocidadRacha")
texto5=texto4.replace("Dir.1","direccionRacha")
texto6=texto5.replace("Speed","velocidadViento")
texto7=texto6.replace("Dir","direccionViento") 
texto8=texto7.replace("Bar","presionBar")
texto9=texto8.replace("Rain","lluvia")
legs2=open(dircsv,"w")
legs2.write(texto9)
legs2.close()
legs.close()

legs=open(dircsv)
texto=legs.read()
texto0=texto.replace("12:00a","00:00")
texto1=texto0.replace("12:10a","00:10")
texto2=texto1.replace("12:20a","00:20")
texto3=texto2.replace("12:30a","00:30")
texto4=texto3.replace("12:40a","00:40")
texto5=texto4.replace("12:50a","00:50")
texto6=texto5.replace("1:00a","1:00")
texto7=texto6.replace("1:10a","1:10")
texto8=texto7.replace("1:20a","1:20")
texto9=texto8.replace("1:30a","1:30")
texto10=texto9.replace("1:40a","1:40")
texto11=texto10.replace("1:50a","1:50")
texto12=texto11.replace("2:00a","2:00")
texto13=texto12.replace("2:10a","2:10")
texto14=texto13.replace("2:20a","2:20")
texto15=texto14.replace("2:30a","2:30")
texto16=texto15.replace("2:40a","2:40")
texto17=texto16.replace("2:50a","2:50")
texto18=texto17.replace("3:00a","3:00")
texto19=texto18.replace("3:10a","3:10")
texto20=texto19.replace("3:20a","3:20")
texto21=texto20.replace("3:30a","3:30")
texto22=texto21.replace("3:40a","3:40")
texto23=texto22.replace("3:50a","3:50")
texto24=texto23.replace("4:00a","4:00")
texto25=texto24.replace("4:10a","4:10")
texto26=texto25.replace("4:20a","4:20")
texto27=texto26.replace("4:30a","4:30")
texto28=texto27.replace("4:40a","4:40")
texto29=texto28.replace("4:50a","4:50")
texto30=texto29.replace("5:00a","5:00")
texto31=texto30.replace("5:10a","5:10")
texto32=texto31.replace("5:20a","5:20")
texto33=texto32.replace("5:30a","5:30")
texto34=texto33.replace("5:40a","5:40")
texto35=texto34.replace("5:50a","5:50")
texto36=texto35.replace("6:00a","6:00")
texto37=texto36.replace("6:10a","6:10")
texto38=texto37.replace("6:20a","6:20")
texto39=texto38.replace("6:30a","6:30")
texto40=texto39.replace("6:40a","6:40")
texto41=texto40.replace("6:50a","6:50")
texto42=texto41.replace("7:00a","7:00")
texto43=texto42.replace("7:10a","7:10")
texto44=texto43.replace("7:20a","7:20")
texto45=texto44.replace("7:30a","7:30")
texto46=texto45.replace("7:40a","7:40")
texto47=texto46.replace("7:50a","7:50")
texto48=texto47.replace("8:00a","8:00")
texto49=texto48.replace("8:10a","8:10")
texto50=texto49.replace("8:20a","8:20")
texto51=texto50.replace("8:30a","8:30")
texto52=texto51.replace("8:40a","8:40")
texto53=texto52.replace("8:50a","8:50")
texto54=texto53.replace("9:00a","9:00")
texto55=texto54.replace("9:10a","9:10")
texto56=texto55.replace("9:20a","9:20")
texto57=texto56.replace("9:30a","9:30")
texto58=texto57.replace("9:40a","9:40")
texto59=texto58.replace("9:50a","9:50")
texto60=texto59.replace("10:00a","10:00")
texto61=texto60.replace("10:10a","10:10")
texto62=texto61.replace("10:20a","10:20")
texto63=texto62.replace("10:30a","10:30")
texto64=texto63.replace("10:40a","10:40")
texto65=texto64.replace("10:50a","10:50")
texto66=texto65.replace("11:00a","11:00")
texto67=texto66.replace("11:10a","11:10")
texto68=texto67.replace("11:20a","11:20")
texto69=texto68.replace("11:30a","11:30")
texto70=texto69.replace("11:40a","11:40")
texto71=texto70.replace("11:50a","11:50")
texto72=texto71.replace("12:00p","12:00")
texto73=texto72.replace("12:10p","12:10")
texto74=texto73.replace("12:20p","12:20")
texto75=texto74.replace("12:30p","12:30")
texto76=texto75.replace("12:40p","12:40")
texto77=texto76.replace("12:50p","12:50")
texto78=texto77.replace("1:00p","13:00")
texto79=texto78.replace("1:10p","13:10")
texto80=texto79.replace("1:20p","13:20")
texto81=texto80.replace("1:30p","13:30")
texto82=texto81.replace("1:40p","13:40")
texto83=texto82.replace("1:50p","13:50")
texto84=texto83.replace("2:00p","14:00")
texto85=texto84.replace("2:10p","14:10")
texto86=texto85.replace("2:20p","14:20")
texto87=texto86.replace("2:30p","14:30")
texto88=texto87.replace("2:40p","14:40")
texto89=texto88.replace("2:50p","14:50")
texto90=texto89.replace("3:00p","15:00")
texto91=texto90.replace("3:10p","15:10")
texto92=texto91.replace("3:20p","15:20")
texto93=texto92.replace("3:30p","15:30")
texto94=texto93.replace("3:40p","15:40")
texto95=texto94.replace("3:50p","15:50")
texto96=texto95.replace("4:00p","16:00")
texto97=texto96.replace("4:10p","16:10")
texto98=texto97.replace("4:20p","16:20")
texto99=texto98.replace("4:30p","16:30")
texto100=texto99.replace("4:40p","16:40")
texto11=texto100.replace("4:50p","16:50")
texto12=texto11.replace("5:00p","17:00")
texto13=texto12.replace("5:10p","17:10")
texto14=texto13.replace("5:20p","17:20")
texto15=texto14.replace("5:30p","17:30")
texto16=texto15.replace("5:40p","17:40")
texto17=texto16.replace("5:50p","17:50")
texto18=texto17.replace("6:00p","18:00")
texto19=texto18.replace("6:10p","18:10")
texto110=texto19.replace("6:20p","18:20")
texto111=texto110.replace("6:30p","18:30")
texto112=texto111.replace("6:40p","18:40")
texto113=texto112.replace("6:50p","18:50")
texto114=texto113.replace("7:00p","19:00")
texto115=texto114.replace("7:10p","19:10")
texto116=texto115.replace("7:20p","19:20")
texto117=texto116.replace("7:30p","19:30")
texto118=texto117.replace("7:40p","19:40")
texto119=texto118.replace("7:50p","19:50")
texto120=texto119.replace("8:00p","20:00")
texto121=texto120.replace("8:10p","20:10")
texto122=texto121.replace("8:20p","20:20")
texto123=texto122.replace("8:30p","20:30")
texto124=texto123.replace("8:40p","20:40")
texto125=texto124.replace("8:50p","20:50")
texto126=texto125.replace("9:00p","21:00")
texto127=texto126.replace("9:10p","21:10")
texto128=texto127.replace("9:20p","21:20")
texto129=texto128.replace("9:30p","21:30")
texto130=texto129.replace("9:40p","21:40")
texto131=texto130.replace("9:50p","21:50")
texto132=texto131.replace("10:00p","22:00")
texto133=texto132.replace("10:10p","22:10")
texto134=texto133.replace("10:20p","22:20")
texto135=texto134.replace("10:30p","22:30")
texto136=texto135.replace("10:40p","22:40")
texto137=texto136.replace("10:50p","22:50")
texto138=texto137.replace("11:00p","23:00")
texto139=texto138.replace("11:10p","23:10")
texto140=texto139.replace("11:20p","23:20")
texto141=texto140.replace("11:30p","23:30")
texto142=texto141.replace("11:40p","23:40")
texto143=texto142.replace("11:50p","23:50")
texto144=texto143.replace("113:00","23:00")
texto145=texto144.replace("113:10","23:10")
texto146=texto145.replace("113:20","23:20")
texto147=texto146.replace("113:30","23:30")
texto148=texto147.replace("113:40","23:40")
texto149=texto148.replace("113:50","23:50")
legs=open(dircsv,"w")
legs.write(texto149)
legs.closed
legs.closed




legstxt=open(dircsv)
legs1=legstxt.read()
cambio3=legs1.replace("NNE","22.5")
cambio4=cambio3.replace("ENE","67.5")
cambio5=cambio4.replace("ESE","112.5")
cambio6=cambio5.replace("SSE","157.5")
cambio7=cambio6.replace("SSW","202.5")
cambio8=cambio7.replace("WSW","247.5")
cambio9=cambio8.replace("WNW","292.5")
cambio10=cambio9.replace("NNW","337.5")
cambio11=cambio10.replace("NE","45")
cambio12=cambio11.replace("SE","135")
cambio13=cambio12.replace("SW","225")
cambio14=cambio13.replace("NW","315")

#cambio1=legs1.replace("N","360")
#print(cambio4)
legs=open(dircsv,"w")
legs.write(cambio14)
legs.closed
legstxt.closed



legs=pd.read_csv(dircsv, usecols=(0,1,2,5,6,7,8,10,11,15,16), index_col=False, header=0)
#print(legs)
legs['fechaHora']=legs['Fecha'].map(str)  + ' ' + legs['Time'].map(str)
legs
#print(legs)
legs.to_csv(dircsv)

legs=open(dircsv)
texto=legs.read()
cambio1=texto.replace("direccionViento.1","direccionRacha")
cambio2=cambio1.replace("velocidadViento.1","velocidadRacha")
#print(cambio14)
legs=open(dircsv,"w")
legs.write(cambio2)
legs.closed

legs=open(dircsv)
texto=legs.read()
cambio1=texto.replace("N","360")
legs=open(dircsv,"w")
legs.write(cambio1)
legs.closed

legs=open(dircsv)
texto=legs.read()
cambio1=texto.replace("E","90")
legs=open(dircsv,"w")
legs.write(cambio1)
legs.closed

legs=open(dircsv)
texto=legs.read()
cambio1=texto.replace("S","180")
legs=open(dircsv,"w")
legs.write(cambio1)
legs.closed

legs=open(dircsv)
texto=legs.read()
cambio1=texto.replace("W","270")
legs=open(dircsv,"w")
legs.write(cambio1)
legs.closed

DF=pd.read_csv(dircsv, index_col=0)
DF['idEstacion']=np.where(DF['Time'] !='[]', 'legs', ' ', )
#print(DF)
DF.to_csv(dircsv)

legs=pd.read_csv(dircsv, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
print(legs)
legs.to_csv(dircsv)
print('Datos de la estacion Legaria listos')


espacio='-------------'
print('Topilejo')

dirtxt=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\Topilejo.txt'
dircsv=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\Topilejo.csv'

print(espacio)
url1 = 'http://189.254.33.151/stn/topilejo/downld02.txt'
file1 = dirtxt
r = urllib.request.urlopen(url1)
f = open(file1,'wb')
f.write(r.read())
f.close()
#print(file1)
print('Datos de la estación Topilejo obtenidos')

try:
    with open(dirtxt, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
          
        # pointer for position
        ptr = 1
      
        # opening in writing mode
        with open(dirtxt, 'w') as fw:
            for line in lines:
                
                # we want to remove 5th line
                if ptr != 1:
                    fw.write(line)
                ptr += 1
    print("Deleted")
      
except:
    print("Oops! No se pudo eliminar fila")

try:
    with open(dirtxt, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
          
        # pointer for position
        ptr = 1
      
        # opening in writing mode
        with open(dirtxt, 'w') as fw:
            for line in lines:
                
                # we want to remove 5th line
                if ptr != 2:
                    fw.write(line)
                ptr += 1
    print("Deleted")
      
except:
    print("Oops! No se pudo eliminar fila")


tpjs=open(dirtxt)
texto0=tpjs.read()

texto1=texto0.replace(" ",",")
texto2=texto1.replace("---","0")
texto3=texto2.replace(",,",",")
texto4=texto3.replace(",,,",",")
texto5=texto4.replace(",,,,",",")
#print(texto5)
tpjs=open(dirtxt,"w")
tpjs.write(texto5)
tpjs.close()

tpjs=open(dirtxt)
texto0=tpjs.read()
texto1=texto0.replace(",,",",")
texto2=texto1.replace(",Date","Fecha")
#print(texto1)
tpjs=open(dircsv,"w")
tpjs.write(texto2)
tpjs.closed
tpjs.closed

tpjs=open(dircsv)
nombrescol=tpjs.read()
texto1=nombrescol.replace("Out","temperatura")
texto2=texto1.replace("Hum","humedadRelativa")
texto3=texto2.replace("Pt.","puntoRocio")
texto4=texto3.replace("Speed.1","velocidadRacha")
texto5=texto4.replace("Dir.1","direccionRacha")
texto6=texto5.replace("Speed","velocidadViento")
texto7=texto6.replace("Dir","direccionViento") 
texto8=texto7.replace("Bar","presionBar")
texto9=texto8.replace("Rain","lluvia")
tpjs2=open(dircsv,"w")
tpjs2.write(texto9)
tpjs2.close()
tpjs.close()

tpjs=open(dircsv)
texto=tpjs.read()
texto0=texto.replace("12:00a","00:00")
texto1=texto0.replace("12:10a","00:10")
texto2=texto1.replace("12:20a","00:20")
texto3=texto2.replace("12:30a","00:30")
texto4=texto3.replace("12:40a","00:40")
texto5=texto4.replace("12:50a","00:50")
texto6=texto5.replace("1:00a","1:00")
texto7=texto6.replace("1:10a","1:10")
texto8=texto7.replace("1:20a","1:20")
texto9=texto8.replace("1:30a","1:30")
texto10=texto9.replace("1:40a","1:40")
texto11=texto10.replace("1:50a","1:50")
texto12=texto11.replace("2:00a","2:00")
texto13=texto12.replace("2:10a","2:10")
texto14=texto13.replace("2:20a","2:20")
texto15=texto14.replace("2:30a","2:30")
texto16=texto15.replace("2:40a","2:40")
texto17=texto16.replace("2:50a","2:50")
texto18=texto17.replace("3:00a","3:00")
texto19=texto18.replace("3:10a","3:10")
texto20=texto19.replace("3:20a","3:20")
texto21=texto20.replace("3:30a","3:30")
texto22=texto21.replace("3:40a","3:40")
texto23=texto22.replace("3:50a","3:50")
texto24=texto23.replace("4:00a","4:00")
texto25=texto24.replace("4:10a","4:10")
texto26=texto25.replace("4:20a","4:20")
texto27=texto26.replace("4:30a","4:30")
texto28=texto27.replace("4:40a","4:40")
texto29=texto28.replace("4:50a","4:50")
texto30=texto29.replace("5:00a","5:00")
texto31=texto30.replace("5:10a","5:10")
texto32=texto31.replace("5:20a","5:20")
texto33=texto32.replace("5:30a","5:30")
texto34=texto33.replace("5:40a","5:40")
texto35=texto34.replace("5:50a","5:50")
texto36=texto35.replace("6:00a","6:00")
texto37=texto36.replace("6:10a","6:10")
texto38=texto37.replace("6:20a","6:20")
texto39=texto38.replace("6:30a","6:30")
texto40=texto39.replace("6:40a","6:40")
texto41=texto40.replace("6:50a","6:50")
texto42=texto41.replace("7:00a","7:00")
texto43=texto42.replace("7:10a","7:10")
texto44=texto43.replace("7:20a","7:20")
texto45=texto44.replace("7:30a","7:30")
texto46=texto45.replace("7:40a","7:40")
texto47=texto46.replace("7:50a","7:50")
texto48=texto47.replace("8:00a","8:00")
texto49=texto48.replace("8:10a","8:10")
texto50=texto49.replace("8:20a","8:20")
texto51=texto50.replace("8:30a","8:30")
texto52=texto51.replace("8:40a","8:40")
texto53=texto52.replace("8:50a","8:50")
texto54=texto53.replace("9:00a","9:00")
texto55=texto54.replace("9:10a","9:10")
texto56=texto55.replace("9:20a","9:20")
texto57=texto56.replace("9:30a","9:30")
texto58=texto57.replace("9:40a","9:40")
texto59=texto58.replace("9:50a","9:50")
texto60=texto59.replace("10:00a","10:00")
texto61=texto60.replace("10:10a","10:10")
texto62=texto61.replace("10:20a","10:20")
texto63=texto62.replace("10:30a","10:30")
texto64=texto63.replace("10:40a","10:40")
texto65=texto64.replace("10:50a","10:50")
texto66=texto65.replace("11:00a","11:00")
texto67=texto66.replace("11:10a","11:10")
texto68=texto67.replace("11:20a","11:20")
texto69=texto68.replace("11:30a","11:30")
texto70=texto69.replace("11:40a","11:40")
texto71=texto70.replace("11:50a","11:50")
texto72=texto71.replace("12:00p","12:00")
texto73=texto72.replace("12:10p","12:10")
texto74=texto73.replace("12:20p","12:20")
texto75=texto74.replace("12:30p","12:30")
texto76=texto75.replace("12:40p","12:40")
texto77=texto76.replace("12:50p","12:50")
texto78=texto77.replace("1:00p","13:00")
texto79=texto78.replace("1:10p","13:10")
texto80=texto79.replace("1:20p","13:20")
texto81=texto80.replace("1:30p","13:30")
texto82=texto81.replace("1:40p","13:40")
texto83=texto82.replace("1:50p","13:50")
texto84=texto83.replace("2:00p","14:00")
texto85=texto84.replace("2:10p","14:10")
texto86=texto85.replace("2:20p","14:20")
texto87=texto86.replace("2:30p","14:30")
texto88=texto87.replace("2:40p","14:40")
texto89=texto88.replace("2:50p","14:50")
texto90=texto89.replace("3:00p","15:00")
texto91=texto90.replace("3:10p","15:10")
texto92=texto91.replace("3:20p","15:20")
texto93=texto92.replace("3:30p","15:30")
texto94=texto93.replace("3:40p","15:40")
texto95=texto94.replace("3:50p","15:50")
texto96=texto95.replace("4:00p","16:00")
texto97=texto96.replace("4:10p","16:10")
texto98=texto97.replace("4:20p","16:20")
texto99=texto98.replace("4:30p","16:30")
texto100=texto99.replace("4:40p","16:40")
texto11=texto100.replace("4:50p","16:50")
texto12=texto11.replace("5:00p","17:00")
texto13=texto12.replace("5:10p","17:10")
texto14=texto13.replace("5:20p","17:20")
texto15=texto14.replace("5:30p","17:30")
texto16=texto15.replace("5:40p","17:40")
texto17=texto16.replace("5:50p","17:50")
texto18=texto17.replace("6:00p","18:00")
texto19=texto18.replace("6:10p","18:10")
texto110=texto19.replace("6:20p","18:20")
texto111=texto110.replace("6:30p","18:30")
texto112=texto111.replace("6:40p","18:40")
texto113=texto112.replace("6:50p","18:50")
texto114=texto113.replace("7:00p","19:00")
texto115=texto114.replace("7:10p","19:10")
texto116=texto115.replace("7:20p","19:20")
texto117=texto116.replace("7:30p","19:30")
texto118=texto117.replace("7:40p","19:40")
texto119=texto118.replace("7:50p","19:50")
texto120=texto119.replace("8:00p","20:00")
texto121=texto120.replace("8:10p","20:10")
texto122=texto121.replace("8:20p","20:20")
texto123=texto122.replace("8:30p","20:30")
texto124=texto123.replace("8:40p","20:40")
texto125=texto124.replace("8:50p","20:50")
texto126=texto125.replace("9:00p","21:00")
texto127=texto126.replace("9:10p","21:10")
texto128=texto127.replace("9:20p","21:20")
texto129=texto128.replace("9:30p","21:30")
texto130=texto129.replace("9:40p","21:40")
texto131=texto130.replace("9:50p","21:50")
texto132=texto131.replace("10:00p","22:00")
texto133=texto132.replace("10:10p","22:10")
texto134=texto133.replace("10:20p","22:20")
texto135=texto134.replace("10:30p","22:30")
texto136=texto135.replace("10:40p","22:40")
texto137=texto136.replace("10:50p","22:50")
texto138=texto137.replace("11:00p","23:00")
texto139=texto138.replace("11:10p","23:10")
texto140=texto139.replace("11:20p","23:20")
texto141=texto140.replace("11:30p","23:30")
texto142=texto141.replace("11:40p","23:40")
texto143=texto142.replace("11:50p","23:50")
texto144=texto143.replace("113:00","23:00")
texto145=texto144.replace("113:10","23:10")
texto146=texto145.replace("113:20","23:20")
texto147=texto146.replace("113:30","23:30")
texto148=texto147.replace("113:40","23:40")
texto149=texto148.replace("113:50","23:50")
tpjs=open(dircsv,"w")
tpjs.write(texto149)
tpjs.closed
tpjs.closed




tpjstxt=open(dircsv)
tpjs1=tpjstxt.read()
cambio3=tpjs1.replace("NNE","22.5")
cambio4=cambio3.replace("ENE","67.5")
cambio5=cambio4.replace("ESE","112.5")
cambio6=cambio5.replace("SSE","157.5")
cambio7=cambio6.replace("SSW","202.5")
cambio8=cambio7.replace("WSW","247.5")
cambio9=cambio8.replace("WNW","292.5")
cambio10=cambio9.replace("NNW","337.5")
cambio11=cambio10.replace("NE","45")
cambio12=cambio11.replace("SE","135")
cambio13=cambio12.replace("SW","225")
cambio14=cambio13.replace("NW","315")

#cambio1=tpjs1.replace("N","360")
#print(cambio4)
tpjs=open(dircsv,"w")
tpjs.write(cambio14)
tpjs.closed
tpjstxt.closed



tpjs=pd.read_csv(dircsv, usecols=(0,1,2,5,6,7,8,10,11,15,16), index_col=False, header=0)
#print(tpjs)
tpjs['fechaHora']=tpjs['Fecha'].map(str)  + ' ' + tpjs['Time'].map(str)
tpjs
#print(tpjs)
tpjs.to_csv(dircsv)

tpjs=open(dircsv)
texto=tpjs.read()
cambio1=texto.replace("direccionViento.1","direccionRacha")
cambio2=cambio1.replace("velocidadViento.1","velocidadRacha")
#print(cambio14)
tpjs=open(dircsv,"w")
tpjs.write(cambio2)
tpjs.closed

tpjs=open(dircsv)
texto=tpjs.read()
cambio1=texto.replace("N","360")
tpjs=open(dircsv,"w")
tpjs.write(cambio1)
tpjs.closed

tpjs=open(dircsv)
texto=tpjs.read()
cambio1=texto.replace("E","90")
tpjs=open(dircsv,"w")
tpjs.write(cambio1)
tpjs.closed

tpjs=open(dircsv)
texto=tpjs.read()
cambio1=texto.replace("S","180")
tpjs=open(dircsv,"w")
tpjs.write(cambio1)
tpjs.closed

tpjs=open(dircsv)
texto=tpjs.read()
cambio1=texto.replace("W","270")
tpjs=open(dircsv,"w")
tpjs.write(cambio1)
tpjs.closed

DF=pd.read_csv(dircsv, index_col=0)
DF['idEstacion']=np.where(DF['Time'] !='[]', 'tpjs', ' ', )
#print(DF)
DF.to_csv(dircsv)

tpjs=pd.read_csv(dircsv, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
print(tpjs)
tpjs.to_csv(dircsv)
print('Datos de la estacion Topilejo listos')



espacio='-------------'
print('Tulyehualco')

dirtxt=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\Tulyehualco.txt'
dircsv=r'C:\Users\meteorologia\Documents\Mapas\EstacionesSGIRPC\Tulyehualco.csv'

print(espacio)
url1 = 'http://189.254.33.151/stn/xochimilco/downld02.txt'
file1 = dirtxt
r = urllib.request.urlopen(url1)
f = open(file1,'wb')
f.write(r.read())
f.close()
#print(file1)
print('Datos de la estación Tulyehualco obtenidos')

try:
    with open(dirtxt, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
          
        # pointer for position
        ptr = 1
      
        # opening in writing mode
        with open(dirtxt, 'w') as fw:
            for line in lines:
                
                # we want to remove 5th line
                if ptr != 1:
                    fw.write(line)
                ptr += 1
    print("Deleted")
      
except:
    print("Oops! No se pudo eliminar fila")

try:
    with open(dirtxt, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
          
        # pointer for position
        ptr = 1
      
        # opening in writing mode
        with open(dirtxt, 'w') as fw:
            for line in lines:
                
                # we want to remove 5th line
                if ptr != 2:
                    fw.write(line)
                ptr += 1
    print("Deleted")
      
except:
    print("Oops! No se pudo eliminar fila")


tlhs=open(dirtxt)
texto0=tlhs.read()

texto1=texto0.replace(" ",",")
texto2=texto1.replace("---","0")
texto3=texto2.replace(",,",",")
texto4=texto3.replace(",,,",",")
texto5=texto4.replace(",,,,",",")
#print(texto5)
tlhs=open(dirtxt,"w")
tlhs.write(texto5)
tlhs.close()

tlhs=open(dirtxt)
texto0=tlhs.read()
texto1=texto0.replace(",,",",")
texto2=texto1.replace(",Date","Fecha")
#print(texto1)
tlhs=open(dircsv,"w")
tlhs.write(texto2)
tlhs.closed
tlhs.closed

tlhs=open(dircsv)
nombrescol=tlhs.read()
texto1=nombrescol.replace("Out","temperatura")
texto2=texto1.replace("Hum","humedadRelativa")
texto3=texto2.replace("Pt.","puntoRocio")
texto4=texto3.replace("Speed.1","velocidadRacha")
texto5=texto4.replace("Dir.1","direccionRacha")
texto6=texto5.replace("Speed","velocidadViento")
texto7=texto6.replace("Dir","direccionViento") 
texto8=texto7.replace("Bar","presionBar")
texto9=texto8.replace("Rain","lluvia")
tlhs2=open(dircsv,"w")
tlhs2.write(texto9)
tlhs2.close()
tlhs.close()

tlhs=open(dircsv)
texto=tlhs.read()
texto0=texto.replace("12:00a","00:00")
texto1=texto0.replace("12:10a","00:10")
texto2=texto1.replace("12:20a","00:20")
texto3=texto2.replace("12:30a","00:30")
texto4=texto3.replace("12:40a","00:40")
texto5=texto4.replace("12:50a","00:50")
texto6=texto5.replace("1:00a","1:00")
texto7=texto6.replace("1:10a","1:10")
texto8=texto7.replace("1:20a","1:20")
texto9=texto8.replace("1:30a","1:30")
texto10=texto9.replace("1:40a","1:40")
texto11=texto10.replace("1:50a","1:50")
texto12=texto11.replace("2:00a","2:00")
texto13=texto12.replace("2:10a","2:10")
texto14=texto13.replace("2:20a","2:20")
texto15=texto14.replace("2:30a","2:30")
texto16=texto15.replace("2:40a","2:40")
texto17=texto16.replace("2:50a","2:50")
texto18=texto17.replace("3:00a","3:00")
texto19=texto18.replace("3:10a","3:10")
texto20=texto19.replace("3:20a","3:20")
texto21=texto20.replace("3:30a","3:30")
texto22=texto21.replace("3:40a","3:40")
texto23=texto22.replace("3:50a","3:50")
texto24=texto23.replace("4:00a","4:00")
texto25=texto24.replace("4:10a","4:10")
texto26=texto25.replace("4:20a","4:20")
texto27=texto26.replace("4:30a","4:30")
texto28=texto27.replace("4:40a","4:40")
texto29=texto28.replace("4:50a","4:50")
texto30=texto29.replace("5:00a","5:00")
texto31=texto30.replace("5:10a","5:10")
texto32=texto31.replace("5:20a","5:20")
texto33=texto32.replace("5:30a","5:30")
texto34=texto33.replace("5:40a","5:40")
texto35=texto34.replace("5:50a","5:50")
texto36=texto35.replace("6:00a","6:00")
texto37=texto36.replace("6:10a","6:10")
texto38=texto37.replace("6:20a","6:20")
texto39=texto38.replace("6:30a","6:30")
texto40=texto39.replace("6:40a","6:40")
texto41=texto40.replace("6:50a","6:50")
texto42=texto41.replace("7:00a","7:00")
texto43=texto42.replace("7:10a","7:10")
texto44=texto43.replace("7:20a","7:20")
texto45=texto44.replace("7:30a","7:30")
texto46=texto45.replace("7:40a","7:40")
texto47=texto46.replace("7:50a","7:50")
texto48=texto47.replace("8:00a","8:00")
texto49=texto48.replace("8:10a","8:10")
texto50=texto49.replace("8:20a","8:20")
texto51=texto50.replace("8:30a","8:30")
texto52=texto51.replace("8:40a","8:40")
texto53=texto52.replace("8:50a","8:50")
texto54=texto53.replace("9:00a","9:00")
texto55=texto54.replace("9:10a","9:10")
texto56=texto55.replace("9:20a","9:20")
texto57=texto56.replace("9:30a","9:30")
texto58=texto57.replace("9:40a","9:40")
texto59=texto58.replace("9:50a","9:50")
texto60=texto59.replace("10:00a","10:00")
texto61=texto60.replace("10:10a","10:10")
texto62=texto61.replace("10:20a","10:20")
texto63=texto62.replace("10:30a","10:30")
texto64=texto63.replace("10:40a","10:40")
texto65=texto64.replace("10:50a","10:50")
texto66=texto65.replace("11:00a","11:00")
texto67=texto66.replace("11:10a","11:10")
texto68=texto67.replace("11:20a","11:20")
texto69=texto68.replace("11:30a","11:30")
texto70=texto69.replace("11:40a","11:40")
texto71=texto70.replace("11:50a","11:50")
texto72=texto71.replace("12:00p","12:00")
texto73=texto72.replace("12:10p","12:10")
texto74=texto73.replace("12:20p","12:20")
texto75=texto74.replace("12:30p","12:30")
texto76=texto75.replace("12:40p","12:40")
texto77=texto76.replace("12:50p","12:50")
texto78=texto77.replace("1:00p","13:00")
texto79=texto78.replace("1:10p","13:10")
texto80=texto79.replace("1:20p","13:20")
texto81=texto80.replace("1:30p","13:30")
texto82=texto81.replace("1:40p","13:40")
texto83=texto82.replace("1:50p","13:50")
texto84=texto83.replace("2:00p","14:00")
texto85=texto84.replace("2:10p","14:10")
texto86=texto85.replace("2:20p","14:20")
texto87=texto86.replace("2:30p","14:30")
texto88=texto87.replace("2:40p","14:40")
texto89=texto88.replace("2:50p","14:50")
texto90=texto89.replace("3:00p","15:00")
texto91=texto90.replace("3:10p","15:10")
texto92=texto91.replace("3:20p","15:20")
texto93=texto92.replace("3:30p","15:30")
texto94=texto93.replace("3:40p","15:40")
texto95=texto94.replace("3:50p","15:50")
texto96=texto95.replace("4:00p","16:00")
texto97=texto96.replace("4:10p","16:10")
texto98=texto97.replace("4:20p","16:20")
texto99=texto98.replace("4:30p","16:30")
texto100=texto99.replace("4:40p","16:40")
texto11=texto100.replace("4:50p","16:50")
texto12=texto11.replace("5:00p","17:00")
texto13=texto12.replace("5:10p","17:10")
texto14=texto13.replace("5:20p","17:20")
texto15=texto14.replace("5:30p","17:30")
texto16=texto15.replace("5:40p","17:40")
texto17=texto16.replace("5:50p","17:50")
texto18=texto17.replace("6:00p","18:00")
texto19=texto18.replace("6:10p","18:10")
texto110=texto19.replace("6:20p","18:20")
texto111=texto110.replace("6:30p","18:30")
texto112=texto111.replace("6:40p","18:40")
texto113=texto112.replace("6:50p","18:50")
texto114=texto113.replace("7:00p","19:00")
texto115=texto114.replace("7:10p","19:10")
texto116=texto115.replace("7:20p","19:20")
texto117=texto116.replace("7:30p","19:30")
texto118=texto117.replace("7:40p","19:40")
texto119=texto118.replace("7:50p","19:50")
texto120=texto119.replace("8:00p","20:00")
texto121=texto120.replace("8:10p","20:10")
texto122=texto121.replace("8:20p","20:20")
texto123=texto122.replace("8:30p","20:30")
texto124=texto123.replace("8:40p","20:40")
texto125=texto124.replace("8:50p","20:50")
texto126=texto125.replace("9:00p","21:00")
texto127=texto126.replace("9:10p","21:10")
texto128=texto127.replace("9:20p","21:20")
texto129=texto128.replace("9:30p","21:30")
texto130=texto129.replace("9:40p","21:40")
texto131=texto130.replace("9:50p","21:50")
texto132=texto131.replace("10:00p","22:00")
texto133=texto132.replace("10:10p","22:10")
texto134=texto133.replace("10:20p","22:20")
texto135=texto134.replace("10:30p","22:30")
texto136=texto135.replace("10:40p","22:40")
texto137=texto136.replace("10:50p","22:50")
texto138=texto137.replace("11:00p","23:00")
texto139=texto138.replace("11:10p","23:10")
texto140=texto139.replace("11:20p","23:20")
texto141=texto140.replace("11:30p","23:30")
texto142=texto141.replace("11:40p","23:40")
texto143=texto142.replace("11:50p","23:50")
texto144=texto143.replace("113:00","23:00")
texto145=texto144.replace("113:10","23:10")
texto146=texto145.replace("113:20","23:20")
texto147=texto146.replace("113:30","23:30")
texto148=texto147.replace("113:40","23:40")
texto149=texto148.replace("113:50","23:50")
tlhs=open(dircsv,"w")
tlhs.write(texto149)
tlhs.closed
tlhs.closed




tlhstxt=open(dircsv)
tlhs1=tlhstxt.read()
cambio3=tlhs1.replace("NNE","22.5")
cambio4=cambio3.replace("ENE","67.5")
cambio5=cambio4.replace("ESE","112.5")
cambio6=cambio5.replace("SSE","157.5")
cambio7=cambio6.replace("SSW","202.5")
cambio8=cambio7.replace("WSW","247.5")
cambio9=cambio8.replace("WNW","292.5")
cambio10=cambio9.replace("NNW","337.5")
cambio11=cambio10.replace("NE","45")
cambio12=cambio11.replace("SE","135")
cambio13=cambio12.replace("SW","225")
cambio14=cambio13.replace("NW","315")

#cambio1=tlhs1.replace("N","360")
#print(cambio4)
tlhs=open(dircsv,"w")
tlhs.write(cambio14)
tlhs.closed
tlhstxt.closed



tlhs=pd.read_csv(dircsv, usecols=(0,1,2,5,6,7,8,10,11,15,16), index_col=False, header=0)
#print(tlhs)
tlhs['fechaHora']=tlhs['Fecha'].map(str)  + ' ' + tlhs['Time'].map(str)
tlhs
#print(tlhs)
tlhs.to_csv(dircsv)

tlhs=open(dircsv)
texto=tlhs.read()
cambio1=texto.replace("direccionViento.1","direccionRacha")
cambio2=cambio1.replace("velocidadViento.1","velocidadRacha")
#print(cambio14)
tlhs=open(dircsv,"w")
tlhs.write(cambio2)
tlhs.closed

tlhs=open(dircsv)
texto=tlhs.read()
cambio1=texto.replace("N","360")
tlhs=open(dircsv,"w")
tlhs.write(cambio1)
tlhs.closed

tlhs=open(dircsv)
texto=tlhs.read()
cambio1=texto.replace("E","90")
tlhs=open(dircsv,"w")
tlhs.write(cambio1)
tlhs.closed

tlhs=open(dircsv)
texto=tlhs.read()
cambio1=texto.replace("S","180")
tlhs=open(dircsv,"w")
tlhs.write(cambio1)
tlhs.closed

tlhs=open(dircsv)
texto=tlhs.read()
cambio1=texto.replace("W","270")
tlhs=open(dircsv,"w")
tlhs.write(cambio1)
tlhs.closed

DF=pd.read_csv(dircsv, index_col=0)
DF['idEstacion']=np.where(DF['Time'] !='[]', 'tlhs', ' ', )
#print(DF)
DF.to_csv(dircsv)

tlhs=pd.read_csv(dircsv, usecols=(3,4,5,6,7,8,9,10,11,12,13), index_col=0, header=0)
print(tlhs)
tlhs.to_csv(dircsv)
print('Datos de la estacion Tulyehualco listos')

