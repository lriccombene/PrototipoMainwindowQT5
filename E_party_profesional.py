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
class E_party_profesional(Base):
    __tablename__="party_profesional"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_party= Column(Integer, ForeignKey('party_party.id'))
    estado_civil = Column(String(100))
    nacionalidad =  Column(String(100))
    fecha_nac = Column(DateTime, default=func.now())
    lugar_nac =  Column(String(100))
    nro_legajo = Column(String(50))

    def __init__(self,id,id_party):
        a=id
        self.id_party= id_party

    def guardar(self,obj_N_datos_personales_prof):
        engine=create_engine('postgresql://postgres:postgres@localhost:5432/psicologos')
        Session= sessionmaker(bind=engine) 
        session=Session()
        new_record = E_party_profesional(1,1)
        new_record.estado_civil =obj_N_datos_personales_prof.estado_civil
        new_record.nacionalidad = obj_N_datos_personales_prof.nac
        new_record.fecha_nac = obj_N_datos_personales_prof.fec_nac
        new_record.lugar_nac = obj_N_datos_personales_prof.lugar_nac
        new_record.nro_legajo = obj_N_datos_personales_prof.nro_legajo
        session.add(new_record)
        session.commit()
        all_records = session.query(E_party_profesional).all()
        return all_records
