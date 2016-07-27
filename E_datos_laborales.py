from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy. import Column, Interger, String, Datatime, Boolean

base = declarative_base()
class datos_laborales(datos_laborales):
    tablename__= "datos_laborales"  
    id = Column(Integer, primary_key=True, autoincrement=True)
    organismo= Column()
    funcion= Column()
    id_party= Column(Integer, ForeignKey('party_party.id'))

    def __init__(self,id,organismo,funcion,id_party):
    a = id
    self.organismo = organismo
    self.funcion = funcion
    self.id_party = id_party