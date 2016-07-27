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
class E_datos_bancarios(Base):
    __tablename__="datos_bancarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_party = Column(Integer, ForeignKey('party_party.id'))
    tipo_cuenta = Column(String)
    banco = Column(String)
    nro_cuenta = Column(String)
    cbu = Column(String)
    
    def __init__(self,id,id_party):
        a=id
        self.id_party= id_party

    def guardar(self, item):
        #Session= Coneccion()
        engine=create_engine('postgresql://postgres:postgres@localhost:5432/psicologos')
        Session= sessionmaker(bind=engine) 
        session=Session()
        new_record = E_datos_bancarios(3,1)
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace() 
        new_record.tipo_cuenta =item.tipo_cuenta
        new_record.banco = item.banco
        new_record.nro_cuenta = item.nro_cuenta
        new_record.cbu = item.cbu
        session.add(new_record)
        session.commit()
        
        all_records = session.query(E_datos_bancarios).all()
        
        return all_records
