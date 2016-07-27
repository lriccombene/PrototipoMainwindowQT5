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
class E_party_contacto(Base):
    __tablename__="party_contacto"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_party = Column(Integer, ForeignKey('party_party.id'))
    create_uid = Column(DateTime, default=func.now())
    create_date = Column(DateTime, default=func.now())
    write_date  = Column(DateTime, default=func.now())
    value = Column(String(100))
    comment = Column(String(200))
    type_contacto = Column(String(100))

    def __init__(self,id_party):
        self.id_party=id_party
        #self.comment=comment
        #self.create_uid=create_uid
        #self.create_date=create_date
        #self.value=value
        #self.write_date=write_date
        #self.activo=activo
        #self.type_contacto= type_contacto

    def guardar(self,obj_N_datos_personales):
        engine=create_engine('postgresql://postgres:postgres@localhost:5432/psicologos')
        Session= sessionmaker(bind=engine) 
        session=Session()
        pyqtRemoveInputHook()
        import pdb; pdb.set_trace() 

        new_record = E_party_contacto(1,1)
        new_record.id = 1
        new_record.id_party =1
        new_record.create_uid = 1
        new_record.create_date = func.now()
        new_record.write_date = func.now()
        new_record.value = obj_N_datos_personales.telefono_personal
        new_record.comment= ""
        new_record.type_contacto= "telefono personal"
        session.add(new_record)
        session.commit()

        new_record2 = E_party_contacto(1,1)
        new_record2.id = 2
        new_record2.id_party =1
        new_record2.create_uid = 1
        new_record2.create_date = func.now()
        new_record2.write_date = func.now()
        new_record2.value = obj_N_datos_personales.email_personal
        new_record2.comment= ""
        new_record2.type_contacto= "email personal"
        session.add(new_record2)
        session.commit()

        new_record3 = E_party_contacto(1,1)
        new_record3.id = 3
        new_record3.id_party =1
        new_record3.create_uid = 1
        new_record3.create_date = func.now()
        new_record3.write_date = func.now()
        new_record3.value = obj_N_datos_personales.telefono_profesional
        new_record3.comment= ""
        new_record3.type_contacto= "telefono profesional"
        session.add(new_record3)
        session.commit()

        new_record4 = E_party_contacto(1,1)
        new_record4.id = 4
        new_record4.id_party =1
        new_record4.create_uid = 1
        new_record4.create_date = func.now()
        new_record4.write_date = func.now()
        new_record4.value = obj_N_datos_personales.telefono_profesional
        new_record4.comment= ""
        new_record4.type_contacto= "email profesional"
        session.add(new_record4)
        session.commit()
