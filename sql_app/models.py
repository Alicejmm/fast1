# ایمپورت کامپوننت های مورد نیاز از SQLAlchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# ایمپورت Base از ماژول database
# Base از SQLAlchemy برای تعریف پایه‌ای که برای ساخت مدل‌های داده‌ای و جداول در پایگاه داده استفاده می‌شود، وارد می‌شود.
from . database import Base
from sqlalchemy.orm import relationship




# STUDENT
class Student(Base):
    
    
    __tablename__ = "student"
    index = Column(Integer, primary_key=True, autoincrement=True)
    stid = Column(String)         
    fname = Column(String)                          
    lname = Column(String)                          
    father = Column(String)                         
    birth = Column(String)                          
    ids = Column(String)                            
    born_city = Column(String)                      
    address = Column(String)                        
    postalcode = Column(Integer)                    
    cphone = Column(String)                         
    hphone = Column(String)                         
    department = Column(String)                    
    major = Column(String)                          
    married = Column(String)                       
    id = Column(Integer)                            
    scourse_ids = Column(Integer)                   
    lids = Column(Integer)                          


# PROFESSOR
class Professor(Base):
    
    
    __tablename__ = 'professor'
    index = Column(Integer, primary_key=True, autoincrement=True)
    lid = Column(String)          
    fname = Column(String)                          
    lname = Column(String)                           
    id = Column(Integer)                           
    department = Column(String)                     
    major = Column(String)                         
    birth = Column(String)                          
    born_city = Column(String)                      
    address = Column(String)                        
    postalcode = Column(Integer)                    
    cphone = Column(String)                         
    hphone = Column(String)                        
    lcourse_ids = Column(String)                   


# COURSE
class Course(Base):
    
    
    
    __tablename__ = "course"
    index = Column(Integer, primary_key=True, autoincrement=True)
    cid = Column(String)    
    cname = Column(String)                               
    department = Column(String)                           
    credit = Column(Integer)                              