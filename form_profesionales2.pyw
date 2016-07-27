import sys
from PyQt5.QtWidgets import QApplication,QDialog, QTableWidget, QTableWidgetItem
from PyQt5 import uic
from form_profesionales import Ui_form_profesionales
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5 import QtGui
from N_profesionales import N_datos_academicos ,N_datos_profesionales, N_datos_personales_prof,N_dato_bancario

class Dialogo(QDialog):
    
    obj_form= Ui_form_profesionales()
    
    apellido = ""
    nombre = ""
    genero = ""
    list_titulos_prof=list()


    def __init__(self):
        #super(Dialogo,self).__init__(parent)
        QDialog.__init__(self)
        self.obj_form = Ui_form_profesionales(self)
        self.obj_form.setupUi(self)
        self.obj_form.boton_guardar.clicked.connect(self.guardar)
        self.obj_form.boton_agregar.clicked.connect(self.agregar)
        self.show()    

    def guardar(self):
        pyqtRemoveInputHook()
        import pdb; pdb.set_trace()
        self.form_profesionales=QDialog()
        apellido = self.obj_form.lne_apellido.text()
        obj_N_datos_personales_prof  =N_datos_personales_prof(apellido)
        obj_N_datos_personales_prof.nombre = self.obj_form.lne_nombre.text()
        obj_N_datos_personales_prof.genero = self.obj_form.cbx_genero.currentText()
        obj_N_datos_personales_prof.nac = self.obj_form.cbx_nacionalidad.currentText()
 
 #       pyqtRemoveInputHook()
  #      import pdb; pdb.set_trace()

        obj_N_datos_personales_prof.domicilio_personal = self.obj_form.lne_domicilio_personal.text()
        obj_N_datos_personales_prof.domi_personal_nro = self.obj_form.lne_numero_domicilio_personal.text()
        obj_N_datos_personales_prof.localidad_personal = self.obj_form.lne_localidad_personal.text()
        obj_N_datos_personales_prof.telefono_personal = self.obj_form.lne_telefono_personal.text()
        obj_N_datos_personales_prof.email_personal2 = self.obj_form.lne_correo_personal.text()
        obj_N_datos_personales_prof.domicilio_profesional = self.obj_form.lne_domicilio_profesional.text()
        obj_N_datos_personales_prof.numero_profesional = self.obj_form.lne_numero_profesional.text()
        obj_N_datos_personales_prof.localidad_profesional = self.obj_form.lne_localidad_profesional.text()
        obj_N_datos_personales_prof.telefono_profesional = self.obj_form.lne_telefono_profesional.text()
        obj_N_datos_personales_prof.email_profesional = self.obj_form.lne_email_profesional.text()

        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_N_datos_personales_prof.tipo_doc = self.obj_form.cbx_tipo_doc.currentText()
        obj_N_datos_personales_prof.nro_doc = self.obj_form.lne_numero_doc.text()
        obj_N_datos_personales_prof.fec_nac = self.obj_form.dte_fecha_nacimiento.text()
        obj_N_datos_personales_prof.lugar_nac = self.obj_form.lne_lugar_nacimiento.text()
        obj_N_datos_personales_prof.estado_civil = self.obj_form.cbx_estado_civil.currentText()
        obj_N_datos_personales_prof.nro_legajo = self.obj_form.lne_nro_legajo.text()

        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        organismo = self.obj_form.cbx_organismo.currentText()
        obj_datos_profesionales = N_datos_profesionales(organismo)


        obj_datos_profesionales.funcion = self.obj_form.cbx_funcion.currentText()
        
        if self.obj_form.ckbx_psic_clin_vincular.isChecked():
            obj_datos_profesionales.psic_clin_vincular =True
           

        if self.obj_form.ckbx_psic_lab_organizacional.isChecked():
            obj_datos_profesionales.psic_lab_organizacional = True    
        
        if self.obj_form.ckbx_psic_educacional.isChecked():
           obj_datos_profesionales.psic_educacional = True


        if self.obj_form.ckbx_neuropsic.isChecked():
            obj_datos_profesionales.neuropsic = True

        if self.obj_form.ckbx_psicoprofilaxis.isChecked():
            obj_datos_profesionales.psicoprofilaxis =  True
        

        if self.obj_form.ckbx_psiconcologia.isChecked():
            obj_datos_profesionales.psiconcologia =  True

        if self.obj_form.ckbx_investigacion.isChecked():
            obj_datos_profesionales.investigacion =  True
        
        if self.obj_form.ckbx_evaluacion_psic.isChecked():
            obj_datos_profesionales.evaluacion_psic =  True
         
        if self.obj_form.ckbx_psic_forense.isChecked():
            obj_datos_profesionales.psic_forense =  True
        
        if self.obj_form.ckbx_otros.isChecked():
             obj_datos_profesionales.otros =  True
         
        obj_datos_profesionales.nivel_medio = False
        obj_datos_profesionales.nivel_terciario = False
        obj_datos_profesionales.nivel_universitario = False
        obj_datos_profesionales.docencia = False

        if self.obj_form.ckbx_docencia.isChecked():
            obj_datos_profesionales.docencia = True
            if self.obj_form.ckbx_nivel_medio.isChecked():
                obj_datos_profesionales.nivel_medio = True
            if self.obj_form.ckbx_nivel_terciario.isChecked():
                obj_datos_profesionales.nivel_terciario = True
            if self.obj_form.ckbx_nivel_universitario.isChecked():
                obj_datos_profesionales.nivel_universitario = True
            
            #self.obj_form.resultado.setText(nivel_medio)

        if self.obj_form.ckbx_psic_clin_adultos.isChecked():
            obj_datos_profesionales.psic_clin_adultos = True

        if self.obj_form.ckbx_psic_clin_nios.isChecked():
            obj_datos_profesionales.psic_clin_nios = True
        
        if self.obj_form.ckbx_orient_psicoanalitica.isChecked():
            if self.obj_form.ckbx_orient_psicoanalitica.isChecked():
                obj_datos_profesionales.orient_psicoanalitica = True
            if self.obj_form.ckbx_orient_cognitivo.isChecked():
                obj_datos_profesionales.orient_cognitivo = True
            if self.obj_form.ckbx_orient_sistemica.isChecked():
                obj_datos_profesionales.orient_sistemica = True

            if self.obj_form.ckbx_otras_orientaciones.isChecked():
                obj_datos_profesionales.otras_orientaciones = self.obj_form.lne_otras_orientaciones.text()

        trabaja_obra_social = False
        if self.obj_form.ckbx_si.isChecked():
            obj_datos_profesionales.trabaja_obra_social = True

        obj_datos_profesionales.cuit = self.obj_form.lne_cuit.text()
        obj_datos_profesionales.isnn = self.obj_form.lne_isnn.text()
        if self.obj_form.cbx_dec_jur_si.isChecked():
            obj_datos_profesionales.dec_jur_si = True

        # obj_N_datos_profesionales = N_datos_profesionales(organismo, funcion ,psic_clin_vincular,psic_lab_organizacional, psic_educacional ,neuropsic ,psicoprofilaxis, psiconcologia , investigacion, evaluacion_psic, psic_forense, otros ,nivel_medio,nivel_terciario , nivel_universitario, psic_clin_adultos, psic_clin_nios, orient_psicoanalitica,  orient_sistemica, orient_cognitivo ,otras_orientaciones, trabaja_obra_social, cuit ,isnn , dec_jur_si)
       
        datos_bancarios= N_dato_bancario()

        datos_bancarios.nro_cuenta = self.obj_form.lne_nro_cuenta.text()
        datos_bancarios.cbu = self.obj_form.lne_cbu.text()
        datos_bancarios.tipo_cuenta=self.obj_form.cbx_tipo_de_cuenta.currentText()
        datos_bancarios.banco = self.obj_form.cbx_banco.currentText()

        #import pdb; pdb.set_trace()
        #lista de titulos profesionales aguardar
        obj_personales_prof = N_datos_personales_prof(apellido)
        obj_personales_prof.guardar(self.list_titulos_prof,datos_bancarios,obj_N_datos_personales_prof,obj_datos_profesionales)
        #self.listregistros =self.obj_form.tw_registrotitulos


        for item in self.list_titulos_prof: 
            item.universidad
        #for nro in range(self.obj_form.tw_registrotitulos.rowCount()):
         #   result = self.obj_form.tw_registrotitulos.row[nro].column[1]


    def agregar(self):
        titulo_grado = self.obj_form.cbx_titulo_grado.currentText()
        universidad_grado = self.obj_form.cbx_universidad_grado.currentText()
        dte_fecha_titulo_grado = self.obj_form.dte_fecha_titulo_grado.text()
        dte_fecha_aut_min_educ_grado = self.obj_form.dte_fecha_aut_min_educ_grado.text()
        dte_fecha_aut_min_int_grado = self.obj_form.dte_fecha_aut_min_int_grado.text()   
                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        obj_datos_Academicos = N_datos_academicos(universidad_grado,dte_fecha_aut_min_educ_grado,dte_fecha_aut_min_int_grado,dte_fecha_titulo_grado,titulo_grado)

        self.list_titulos_prof.append(obj_datos_Academicos)
        

        #AGREGAR REGISTROS EN LA GRILLA
        rowPosition = self.obj_form.tw_registrotitulos.rowCount()
        self.obj_form.tw_registrotitulos.insertRow(rowPosition)
        self.obj_form.tw_registrotitulos.setItem(rowPosition , 0, QTableWidgetItem(titulo_grado))
        self.obj_form.tw_registrotitulos.setItem(rowPosition , 1, QTableWidgetItem(universidad_grado))
        self.obj_form.tw_registrotitulos.setItem(rowPosition , 2, QTableWidgetItem(str(dte_fecha_titulo_grado)))
        self.obj_form.tw_registrotitulos.setItem(rowPosition , 3, QTableWidgetItem(str(dte_fecha_aut_min_educ_grado)))
        self.obj_form.tw_registrotitulos.setItem(rowPosition , 4, QTableWidgetItem(str(dte_fecha_aut_min_int_grado)))




app = QApplication(sys.argv)
dialogo= Dialogo()
dialogo.show()
app.exec_()
