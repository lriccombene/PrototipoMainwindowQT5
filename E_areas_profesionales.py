from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy. import Column, Interger, String, Datatime, Boolean

base = declarative_base()
class areas_profesionales(areas_profesionales):
    tablename__= "areas_profesionales"  
    id = Column(Integer, primary_key=True, autoincrement=True)
    descripcion= Column(String(100))

    def __init__(self,id,descripcion):
    a = id
    self.descripcion = descripcions

    
