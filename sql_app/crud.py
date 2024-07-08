from sqlalchemy.orm import Session
from . import models, schemas  
from fastapi import HTTPException  
from fastapi.responses import JSONResponse  

#emtehan push baray eraee dars barname nevisi pishrafte

# STUDENT

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(
        stid=student.stid,
        fname=student.fname,
        lname=student.lname,
        father=student.father,
        birth=student.birth,
        ids=student.ids,
        born_city=student.born_city,
        address=student.address,
        postalcode=student.postalcode,
        cphone=student.cphone,
        hphone=student.hphone,
        department=student.department,
        major=student.major,
        married=student.married,
        id=student.id,
        scourse_ids=student.scourse_ids,
        lids=student.lids
    )
    db.add(db_student)  
    db.commit()  
    db.refresh(db_student)  
    return db_student  


def get_student(db: Session, student_stid: str) -> models.Student:
    return db.query(models.Student).filter(models.Student.stid == student_stid).first()


def update_student(db: Session, student_stid: str, new_student_data: schemas.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.stid == student_stid).first()
    if db_student:
        for attr, value in vars(new_student_data).items():
            setattr(db_student, attr, value)
        db.commit()  
        db.refresh(db_student)  
        return db_student  
    else:
        raise HTTPException(status_code=404, detail="stid not found")



def delete_student(db: Session, student_stid: str):
    db_student = db.query(models.Student).filter(models.Student.stid == student_stid).first()
    if db_student:
        db.delete(db_student)  
        db.commit() 
        return db_student
    return None 

    


# PROFESSOR

def create_professor(db: Session, professor: schemas.ProfessorCreate):
    db_professor = models.Professor(
        lid=professor.lid,
        fname=professor.fname,
        lname=professor.lname,
        id=professor.id,
        department=professor.department,
        major=professor.major,
        birth=professor.birth,
        born_city=professor.born_city,
        address=professor.address,
        postalcode=professor.postalcode,
        cphone=professor.cphone,
        hphone=professor.hphone,
        lcourse_ids=professor.lcourse_ids,
    )
    db.add(db_professor)  
    db.commit() 
    db.refresh(db_professor)  
    return db_professor  


def get_professor(db: Session, professor_lid: str) -> models.Professor:
    return db.query(models.Professor).filter(models.Professor.lid == professor_lid).first()


def update_professor(db: Session, professor_lid: str, new_professor_data: schemas.ProfessorCreate):
    db_professor = db.query(models.Professor).filter(models.Professor.lid == professor_lid).first()
    if db_professor:
       
        for attr, value in vars(new_professor_data).items():
            setattr(db_professor, attr, value)
        db.commit()  
        db.refresh(db_professor) 
        return db_professor 
    raise HTTPException(status_code=404, detail="lid not found")


def delete_professor(db: Session, professor_lid: str):
    db_professor = db.query(models.Professor).filter(models.Professor.lid == professor_lid).first()
    if db_professor:
        db.delete(db_professor) 
        db.commit() 
        return db_professor
    return None
       


# COURSE

def create_course(db: Session, course: schemas.Course):
    db_course = models.Course(
        cid=course.cid,
        cname=course.cname,
        department=course.department,
        credit=course.credit
    )
    db.add(db_course) 
    db.commit()  
    db.refresh(db_course) 
    return db_course


def get_course(db: Session, course_cid: str) -> models.Course:
    return db.query(models.Course).filter(models.Course.cid == course_cid).first()


def update_course(db: Session, course_cid: str, new_course_data: schemas.Course):
    db_course = db.query(models.Course).filter(models.Course.cid == course_cid).first()
    if db_course:
        
        for attr, value in vars(new_course_data).items():
            setattr(db_course, attr, value)
        db.commit()  
        db.refresh(db_course) 
        return db_course  
    raise HTTPException(status_code=404, detail="cid not found")


def delete_course(db: Session, course_cid: str):
    db_course = db.query(models.Course).filter(models.Course.cid == course_cid).first()
    if db_course:
        db.delete(db_course) 
        db.commit()  
        return db_course
    raise None
