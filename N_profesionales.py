import sys
import datetime 
from E_party_profesional import E_party_profesional
from E_datos_academicos import E_datos_academicos
from E_datos_bancarios import E_datos_bancarios
from E_party_party import E_party_party
from E_party_address import E_party_address
from E_party_contacto import E_party_contacto
from E_actuacion_laboral import E_actuacion_laboral

from PyQt5.QtCore import pyqtRemoveInputHook


class N_datos_personales_prof(object):
    """docstring for ClassName"""
    apellido = ""
    nombre = ""
    genero = ""
    nac = ""
    tipo_doc = ""
    nro_doc =""
    fec_nac = datetime
    lugar_nac =  datetime
    estado_civil =""
    domicilio_personal = ""
    domi_personal_nro = ""
    localidad_personal = ""
    telefono_personal = ""
    email_personal = ""
    domicilio_profesional = ""
    numero_profesional = ""
    localidad_profesional = ""
    telefono_profesional = ""
    email_profesional = ""
    nro_legajo = ""
    active=True

    def __init__(self,apellido):
        self.apellido=apellido
        #def  __init__(self,apellido,nombre,genero,nac,tipo_doc,nro_doc,fec_nac,lugar_nac,estado_civil,domicilio_personal,domi_personal_nro,localidad_personal,telefono_personal,email_personal,domicilio_profesional,numero_profesional,localidad_profesional,telefono_profesional,email_profesional):

        #self.telefono_personal = telefono_personal
        #self.email_personal = email_personal
       
        #self.telefono_profesional = telefono_profesional
        #self.email_profesional = email_profesional

    def guardar(self, list_N_datos_academicos , N_datos_bancarios,obj_N_datos_personales_prof,obj_N_datos_profesionales):
        id_party=1
        
        # self.apellido = apellido
        # self.nombre = nombre
        # self.tipo_doc = tipo_doc
        # self.nro_doc = nro_doc
        # self.genero = genero
        obj_E_party_party = E_party_party(id_party)
        obj_E_party_party.guardar(obj_N_datos_personales_prof)
        id_party = obj_E_party_party.get_id_party(obj_N_datos_personales_prof.nro_doc)

        obj_E_actuacion_laboral=E_actuacion_laboral(1)
        if obj_N_datos_profesionales.psic_clin_vincular == True :
            obj_E_actuacion_laboral.guardar(id_party,1)

        if obj_N_datos_profesionales.psiconcologia == True :
            obj_E_actuacion_laboral.guardar(id_party,2)
            
        if obj_N_datos_profesionales.psic_lab_organizacional == True :
            obj_E_actuacion_laboral.guardar(id_party,3)

        if obj_N_datos_profesionales.investigacion == True :
            obj_E_actuacion_laboral.guardar(id_party,4)

        if obj_N_datos_profesionales.psic_educacional == True :
            obj_E_actuacion_laboral.guardar(id_party,5)

        if obj_N_datos_profesionales.neuropsic == True :
            obj_E_actuacion_laboral.guardar(id_party,6)

        if obj_N_datos_profesionales.psic_forense == True :
            obj_E_actuacion_laboral.guardar(id_party,7)

        if obj_N_datos_profesionales.psicoprofilaxis == True :
            obj_E_actuacion_laboral.guardar(id_party,9)

        if obj_N_datos_profesionales.docencia == True:
            obj_E_actuacion_laboral.guardar(id_party,10)
            if obj_N_datos_profesionales.nivel_medio == True :
                obj_E_actuacion_laboral.guardar(id_party,11)
            if obj_N_datos_profesionales.nivel_terciario == True :
                obj_E_actuacion_laboral.guardar(id_party,12)
            if obj_N_datos_profesionales.nivel_universitario == True :
                obj_E_actuacion_laboral.guardar(id_party,13)
        
        if obj_N_datos_profesionales.psic_clin_adultos == True :
            obj_E_actuacion_laboral.guardar(id_party,14)

        if obj_N_datos_profesionales.evaluacion_psic == True :
            obj_E_actuacion_laboral.guardar(id_party,15)

        if obj_N_datos_profesionales.psic_clin_nios == True :
            obj_E_actuacion_laboral.guardar(id_party,16)

        if obj_N_datos_profesionales.orient_psicoanalitica == True :
            obj_E_actuacion_laboral.guardar(id_party,17)

        if obj_N_datos_profesionales.orient_sistemica == True :
            obj_E_actuacion_laboral.guardar(id_party,18)

        if obj_N_datos_profesionales.orient_cognitivo == True :
            obj_E_actuacion_laboral.guardar(id_party,19)

        if obj_N_datos_profesionales.otras_orientaciones == True :
            obj_E_actuacion_laboral.guardar(id_party,20)



        #self.telefono_personal = telefono_personal
        #self.email_personal = email_personal
        #self.telefono_profesional = telefono_profesional
        #self.email_profesional = email_profesional

        obj_party_contacto= E_party_contacto(id_party)
        obj_party_contacto.guardar(obj_N_datos_personales_prof)
        
        #self.domicilio_profesional = domicilio_profesional
        #self.numero_profesional = numero_profesional
        #self.localidad_profesional = localidad_profesional
        #self.domicilio_personal =domicilio_profesiona
        #self.domi_personal_nro = domi_personal_nro
        #self.localidad_personal = localidad_personal
        obj_E_party_address = E_party_address(id_party)
        obj_E_party_address.guardar(obj_N_datos_personales_prof)

        #estado_civil,
        #self.nac = nac
        #self.fec_nac = fec_nac
        #self.lugar_nac = lugar_nac
        #self.nro_legajo = "" 
        obj_E_party_profesional= E_party_profesional(1,id_party)
        obj_E_party_profesional.guardar(obj_N_datos_personales_prof)

        obj_E_datos_academicos= E_datos_academicos(1,id_party)
        obj_E_datos_academicos.guardar(list_N_datos_academicos)
        
       #pyqtRemoveInputHook()
       # import pdb; pdb.set_trace()
        obj_E_datos_bancarios= E_datos_bancarios(1,id_party)
        obj_E_datos_bancarios.guardar(N_datos_bancarios)

class N_datos_profesionales(object):
    organismo=""
    funcion=""
    psic_clin_vincular=False
    psic_lab_organizacional=False
    psic_educacional =False
    neuropsic = False
    psicoprofilaxis =False
    psiconcologia=False
    investigacion =False
    evaluacion_psic=False
    psic_forense =False
    otros =""
    docencia= False
    nivel_medio =False
    nivel_terciario =False
    nivel_universitario =False
    psic_clin_adultos=False
    psic_clin_nios =False
    orient_psicoanalitica=False
    orient_sistemica=False
    orient_cognitivo=False
    otras_orientaciones=False
    trabaja_obra_social=False
    cuit = ""
    isnn = ""
    dec_jur_si =False


    def __init__(self, organismo):
         #funcion ,psic_clin_vincular,psic_lab_organizacional, psic_educacional ,neuropsic ,psicoprofilaxis, psiconcologia , investigacion, evaluacion_psic, psic_forense, otros ,nivel_medio,nivel_terciario , nivel_universitario, psic_clin_adultos, psic_clin_nios, orient_psicoanalitica,  orient_sistemica, orient_cognitivo ,otras_orientaciones, trabaja_obra_social, cuit ,isnn , dec_jur_si, nro_legajo
        self.organismo= organismo


        #estas faltannnnnnnnnnnnnnnnnnnnnnn!
        
        #self.funcion=funcion
        #self.otras_orientaciones=otras_orientaciones
        #self.trabaja_obra_social=trabaja_obra_social
        #self.cuit = cuit
        #self.isnn = isnn
        #self.dec_jur_si =dec_jur_si

    


class N_datos_academicos(object):
    import datetime 
    universidad=""
    fecha_titulo=datetime 
    fecha_min=datetime
    fecha_mej=datetime
    titulo= ""

    def __init__(self, universidad,fecha_mej,fecha_min,fecha_titulo,titulo):
        self.universidad=universidad
        self.fecha_titulo=fecha_titulo
        self.fecha_min=fecha_min
        self.fecha_mej=fecha_mej
        self.titulo= titulo


class N_dato_bancario(object):
    tipo_cuenta="" 
    banco=""
    nro_cuenta= ""
    cbu= ""


    def __int__(self):
        self.tipo_cuenta = ""
        #tipo_de_cuenta
        #self.banco= banco
        #self.nro_cuenta= nro_cuenta
        #self.cbu = cbu
