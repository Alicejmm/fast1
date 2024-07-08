
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from .datavalidation import datavalidation_course, datavalidation_professor, datavalidation_student
from fastapi.responses import JSONResponse  




models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# STUDENT

@app.post("/create_student/", response_model=schemas.ret_student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    datavalidation_student.student_exists_check(db, student.stid)
    datavalidation_student.check_stid(db, student.stid)
    datavalidation_student.check_name(db, student.fname, student.lname, student.father)
    datavalidation_student.check_birth(db, student.birth)
    datavalidation_student.check_ids(db, student.ids)
    datavalidation_student.born_city(db, student.born_city)
    datavalidation_student.check_address(db, student.address)
    datavalidation_student.check_postalcode(db, student.postalcode)
    datavalidation_student.check_cphone(db, student.cphone)
    datavalidation_student.check_hphone(db, student.hphone)
    datavalidation_student.check_department(db, student.department)
    datavalidation_student.check_major(db, student.major)
    datavalidation_student.check_married(db, student.married)
    datavalidation_student.check_id(db, student.id)

    
    return crud.create_student(db=db, student=student)

@app.get("/get_student/{student_stid}", response_model=schemas.ret_student)
def read_student(student_stid: str, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_stid=student_stid)
    if db_student is None:
        
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.put("/update_student/{student_stid}", response_model=schemas.ret_student)
def update_student(student_stid: str, new_data: schemas.StudentCreate, db: Session = Depends(get_db)):
    #datavalidation_student.check_stid(db, new_data.stid)
    datavalidation_student.check_name(db, new_data.fname, new_data.lname, new_data.father)
    datavalidation_student.check_birth(db, new_data.birth)
    datavalidation_student.check_ids(db, new_data.ids)
    datavalidation_student.born_city(db, new_data.born_city)
    datavalidation_student.check_address(db, new_data.address)
    datavalidation_student.check_postalcode(db, new_data.postalcode)
    datavalidation_student.check_cphone(db, new_data.cphone)
    datavalidation_student.check_hphone(db, new_data.hphone)
    datavalidation_student.check_department(db, new_data.department)
    datavalidation_student.check_major(db, new_data.major)
    datavalidation_student.check_married(db, new_data.married)
    #datavalidation_student.check_id(db, new_data.id)
    db_student = crud.update_student(db, student_stid=student_stid, new_student_data=new_data)
    return db_student

@app.delete("/delete_student/{student_stid}", response_model=schemas.ret_student)
def delete_student(student_stid: str, db: Session = Depends(get_db)):
    
    delete_student = crud.delete_student(db, student_stid=student_stid)
    if delete_student :
        return {"message":"Delete successful"}
    raise HTTPException(status_code=404, detail="Student not found")

# PROFESSOR

@app.post("/create_professor/", response_model=schemas.ret_professor)
def create_professor(professor: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    datavalidation_professor.professor_exists_check(db, professor.lid)
    datavalidation_professor.check_lid(db, professor.lid)
    datavalidation_professor.check_name(db, professor.fname, professor.lname)
    datavalidation_professor.check_id(db, professor.id)
    datavalidation_professor.check_department(db, professor.department)
    datavalidation_professor.check_major(db, professor.major)
    datavalidation_professor.check_birth(db, professor.birth)
    datavalidation_professor.born_city(db, professor.born_city)
    datavalidation_professor.check_address(db, professor.address)
    datavalidation_professor.check_postalcode(db, professor.postalcode)
    datavalidation_professor.check_cphone(db, professor.cphone)
    datavalidation_professor.check_hphone(db, professor.hphone)


    return crud.create_professor(db=db, professor=professor)

@app.get("/get_professor/{professor_lid}", response_model=schemas.ret_professor)
def read_professor(professor_lid: str, db: Session = Depends(get_db)):
    db_professor = crud.get_professor(db, professor_lid=professor_lid)
    if db_professor is None:
        raise HTTPException(status_code=404, detail="Professor not found")
    return db_professor

@app.put("/update_professor/{professor_lid}", response_model=schemas.ret_professor)
def update_professor(professor_lid: str, new_data: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    #datavalidation_professor.check_lid(db, new_data.lid)
    datavalidation_professor.check_name(db, new_data.fname, new_data.lname)
    #datavalidation_professor.check_id(db, new_data.id)
    datavalidation_professor.check_department(db, new_data.department)
    datavalidation_professor.check_major(db, new_data.major)
    datavalidation_professor.check_birth(db, new_data.birth)
    datavalidation_professor.born_city(db, new_data.born_city)
    datavalidation_professor.check_address(db, new_data.address)
    datavalidation_professor.check_postalcode(db, new_data.postalcode)
    datavalidation_professor.check_cphone(db, new_data.cphone)
    datavalidation_professor.check_hphone(db, new_data.hphone)

    
    db_professor = crud.update_professor(db, professor_lid=professor_lid, new_professor_data=new_data)
    return db_professor

@app.delete("/delete_professor/{professor_lid}", response_model=schemas.Professor)
def delete_professor(professor_lid: int, db: Session = Depends(get_db)):
    
    delete_professor = crud.delete_professor(db, professor_lid=professor_lid)
    if delete_professor :
        return JSONResponse(content={"message":"Delete successful"} )
    raise HTTPException(status_code=404, detail="Professor not found")
    

# COURSE

@app.post("/create_course/", response_model=schemas.Course)
def create_course(course: schemas.Course, db: Session = Depends(get_db)):
    
    datavalidation_course.course_exists_check(db, course.cid)
    datavalidation_course.check_cid(db, course.cid)
    datavalidation_course.check_cname(db, course.cname)
    datavalidation_course.check_department_course(db, course.department)
    datavalidation_course.check_credit(db, course.credit)

    
    return crud.create_course(db=db, course=course)

@app.get("/get_course/{course_cid}", response_model=schemas.Course)
def read_course(course_cid: int, db: Session = Depends(get_db)):
    
    db_course = crud.get_course(db, course_cid=course_cid)
    if db_course is None: 
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@app.put("/update_course/{course_cid}", response_model=schemas.Course)
def update_course(course_cid: int, new_data: schemas.Course, db: Session = Depends(get_db)):
  
    #datavalidation_course.check_cid(db, new_data.cid)
    datavalidation_course.check_cname(db, new_data.cname)
    datavalidation_course.check_department_course(db, new_data.department)
    datavalidation_course.check_credit(db, new_data.credit)

    
    db_course = crud.update_course(db, course_cid=course_cid, new_course_data=new_data)
    return db_course

@app.delete("/delete_course/{course_cid}", response_model=schemas.Course)
def deletecourse(course_cid: int, db: Session = Depends(get_db)):
    delete_course = crud.delete_course(db, course_cid=course_cid)
    if delete_course:
        return {"message": "Delete successful"}
    raise HTTPException(status_code=404, detail="Course not found")
