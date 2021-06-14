
from pro.mod.M_Procesar_QR import *  # importar con los mismos nombres
from pro.mod.M_Peticion_Usuarios import *  # importar con los mismos nombres

import time


#revicion de conecion y pericon de Usuarios_Server
def Status_Redes():
	Estado_redes = GET_STatus_Red()
	if Estado_redes.find('C') != -1: 	return 1 #print 'hay red lan'
	else : 								return 0 #print 'No LAN'


if Status_Redes() == 1: Escrivir_Archivos(53, '1') #activar peticion de usuarios



print 'listos'
while 1:
	#------------------if PP_Mensajes:---------------------------------------
	#  Proceso 0: Tiempo de espera para disminuir proceso
	#---------------------------------------------------------
	time.sleep(0.05)
	#---------------------------------------------------------
    # Proceso 2: Actualizacion de usuarios del dispositivos
    #---------------------------------------------------------
	Eventos_Usuarios_Server()
	#---------------------------------------------------------
	# Proceso 4: Procesamiento del QR
	#---------------------------------------------------------
	Procesar_QR()







"""

#T_A = T_Actual()
T2 = T_Actual()
#print 'inicio: ' +T_A
#print 'Fin: ' +T2
print 'R: ' + Respuesta + ', T: ' + str(int(T2)-int(T_A))
#correo@gmail.# COMBAK: anderson amaya app_Actualizando

"""
