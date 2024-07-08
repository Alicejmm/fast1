from pydantic import BaseModel


class Student(BaseModel):
    stid: str            
    fname: str           
    lname: str           
    father: str 
    
class StudentCreate(Student):
    birth: str           
    ids: str             
    born_city: str       
    address: str         
    postalcode: int       
    cphone: str           
    hphone: str           
    department: str      
    major: str            
    married: str          
    id: int               
    scourse_ids: int       
    lids: int   
class ret_student(Student):
    pass




class Professor(BaseModel):
    lid: str             
    fname: str           
    lname: str           
    id: int   
class ProfessorCreate(Professor):
    department: str      
    major: str           
    birth: str           
    born_city: str       
    address: str         
    postalcode: int      
    cphone: str          
    hphone: str          
    lcourse_ids: str  
class ret_professor(Professor):
    pass




class Course(BaseModel):
    cid: str            
    cname: str           
    department: str      
    credit: int         

