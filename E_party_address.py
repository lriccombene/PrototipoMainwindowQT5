import sys 
#import datetime
#from N_profesionales import N_datos_academicos
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean
#from coneccion import Coneccion
from PyQt5.QtCore import pyqtRemoveInputHook

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
class E_party_address(Base):
    __tablename__="party_address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    localidad = Column(String(100))
    create_date = Column(DateTime, default=func.now())
    zip = Column(String(100))
    create_uid = Column(DateTime, default=func.now())
    provincia =  Column(String(100))
    pais =  Column(String(100))
    street =    Column(String(100))
    nro_street =Column(String(100))
    id_party =  Column(Integer, ForeignKey('party_party.id'))


    def __init__(self,id_party):
       # a = id
        #self.localidad = localidad
        #self.create_date =create_date
        #self.nro_street = nro_street
        #self.zip = zip
        #self.create_uid = create_uid
        #self.street = street
        self.id_party = id_party
        
    def guardar(self,obj_N_datos_personales_prof):
        engine=create_engine('postgresql://postgres:postgres@localhost:5432/psicologos')
        Session= sessionmaker(bind=engine) 
        session=Session()
        new_record = E_party_address(1,1)
        pyqtRemoveInputHook()
        import pdb; pdb.set_trace() 
        new_record.id = 1
        new_record.id_party =1
        new_record.create_uid = 1
        new_record.localidad = obj_N_datos_personales_prof.localidad_personal
        new_record.zip = 8500
        new_record.street = obj_N_datos_personales_prof.domicilio_personal
        new_record.nro_street = obj_N_datos_personales_prof.domi_personal_nro
        new_record.provincia= "Río Negro"
        session.add(new_record)
        session.commit()
        
        new_record2 = E_party_address(2,1)
        new_record2.id = 2
        new_record2.id_party = 1
        new_record2.create_uid = 1
        new_record2.localidad = obj_N_datos_personales_prof.localidad_profesional
        new_record2.zip = 8500
        new_record2.street = obj_N_datos_personales_prof.domicilio_profesional
        new_record2.nro_street = obj_N_datos_personales_prof.numero_profesional
        new_record2.provincia= "Río Negro"
        session.add(new_record2)
        session.commit()





