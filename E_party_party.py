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
class E_party_party(Base):
    __tablename__="party_party"
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_date = Column(DateTime, default=func.now())
    write_uid =Column(Integer, ForeignKey('usuario.id'))
    write_date = Column(DateTime, default=func.now())
    active =  Column(Boolean)
    nombre =  Column(String(100))
    apellido =  Column(String(100))
    tipo_doc =  Column(String(50))
    nro_doc =  Column(String(100))
    genero = Column(String(100))


    def __init__(self,id):
        a = id
        self.create_date =func.now()
        self.write_date = func.now()

    def guardar(self,obj_N_datos_personales_prof):

        engine=create_engine('postgresql://postgres:postgres@localhost:5432/psicologos')
        Session= sessionmaker(bind=engine) 
        session=Session()
        new_record = E_party_party(1)
        new_record.write_uid = 2
        new_record.active = obj_N_datos_personales_prof.active
        new_record.nombre = obj_N_datos_personales_prof.nombre
        new_record.apellido = obj_N_datos_personales_prof.apellido
        new_record.tipo_doc = obj_N_datos_personales_prof.tipo_doc
        new_record.nro_doc = obj_N_datos_personales_prof.nro_doc
        new_record.genero = obj_N_datos_personales_prof.genero
        session.add(new_record)
        session.commit()

    def cant_party(self):
        engine=create_engine('postgresql://postgres:postgres@localhost:5432/psicologos')
        Session= sessionmaker(bind=engine) 
        session=Session()
        return session.query(E_party_party).count()

    def get_id_party(self, nro_doc):
        engine=create_engine('postgresql://postgres:postgres@localhost:5432/psicologos')
        Session= sessionmaker(bind=engine)
        session=Session()
        #pyqtRemoveInputHook()
        #import pdb; pdb.set_trace()
        obj_party_party = session.query(E_party_party).filter_by(nro_doc=nro_doc).first()
        return obj_party_party.id
        #all_records = session.query(party_party).all()
        
        #return all_records
    def get_grilla_alta_profesional(self):
        engine=create_engine('postgresql://postgres:postgres@localhost:5432/psicologos')
        Session= sessionmaker(bind=engine)
        session=Session()
        query = (session.query(Ip, func.count(Client.id)).
                 outerjoin(ClientIp, ClientIp.ip_id==Ip.id).
                 outerjoin(Client, Client.id==ClientIp.client_id).
                 group_by(Ip.id)
                )
         

