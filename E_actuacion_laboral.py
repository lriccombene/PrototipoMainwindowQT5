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
class E_actuacion_laboral(Base):
    __tablename__= "actuacion_laboral"    
    #id= Column(Integer, primary_key=True)
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_party= Column(Integer, ForeignKey('party_party.id'))
    ideareaprofesional= Column(Integer)

    def __init__(self,id):
        #self.id = id
        a=id

    def guardar(self,id_party, ideareaprofesional):
        engine=create_engine('postgresql://postgres:postgres@localhost:5432/psicologos')
        Session= sessionmaker(bind=engine) 
        session=Session()
        new_record = E_actuacion_laboral(1)
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        new_record.id_party = id_party
        new_record.ideareaprofesional = ideareaprofesional
        session.add(new_record)
        session.commit()

