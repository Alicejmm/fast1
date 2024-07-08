from fastapi import HTTPException
from sqlalchemy.orm import Session
from .import crud, models, schemas





# STUDENT

class datavalidation_student:
    def student_exists_check(db: Session, stid: str):
        student_stid = db.query(models.Student).filter(models.Student.stid == stid).first()
        if student_stid is not None:
            raise HTTPException(status_code=409, detail="student already exists.")

    
    def check_stid(db: Session, stid: str):
        if len(stid) != 11:
            return "stid is not 11 digits"
        if int(stid[0:3]) > 402 or int(stid[0:3]) < 400:
            return "year invalid"
        if int(stid[3:9]) != 114150:
            return "بخش ثابت شماره دانشجویی نادرست است ا"
        if int(stid[9:11]) == 0:
            return "ایندکس شماره دانشجوییی نادرست است"
        else:
            return "Entered student ID is correct."

    def check_name(db: Session, fname: str, lname: str, father: str):
        if len(fname) > 11 or len(lname) > 11 or len(father) > 11:
            raise HTTPException(status_code=400, detail="نامونام خانوادگی و نام پدر دانشجو نباید بیشتر از 10 کاراکتر باشد")

        if not all('آ' <= char <= 'ی' or char == ' ' for char in (fname + lname + father)):
            raise HTTPException(status_code=400,detail="در نام و نام خانوادگی و نام پدر دانشجو فقط حروف فارسی بدون کاراکترخاص صحیح است")
     
    def check_birth(db: Session, birth: str):
        if len(birth) != 10:
            raise HTTPException(status_code=400, detail="تاریخ تولد فقط 10 کاراکتر دارد")
        parts = birth.split('/')
        if len(parts) != 3:
            raise HTTPException(status_code=400, detail="فرمت تاریخ تولد دانشجو صحیح نیست لطفا فرمت را بعه شکل روز/ماه/سال وارد کنید")
        year, month, day = parts
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            raise HTTPException(status_code=400, detail="The date entered must contain numbers")

        year = int(year)
        month = int(month)
        day = int(day)
    
        if not (1<= year <= 1402):
            raise HTTPException(status_code=400, detail="سال تولد باید بین 1 تا 1403 باشد")

        if not (1 <= month <= 12):
            raise HTTPException(status_code=400, detail="ماه تولد باید بین 1 تا 12 باشد")

        if (1 <= month <= 6) and not (1 <= day <= 31):
            raise HTTPException(status_code=400, detail="روز تولد باید بین 1 تا 31 باشد")

        if (7 <= month <= 12) and not (1 <= day <= 30):
            raise HTTPException(status_code=400, detail="روز تولد باید بین 1 تا")

    
    def check_ids(db: Session, ids: str):
        parts = ids.split('.')
        if len(parts) != 3:
            raise HTTPException(status_code=400, detail="سریال شناسنامه باید سه بخش باشد")

        first = parts[0]
        second = parts[1]
        third = parts[2]

        if not len(first) != 6:
            raise HTTPException(status_code=400, detail= "سریال شناسنامه با یک عدد 6 رقمی شروع میشود")
        
        if not first.isdigit():
            raise HTTPException(status_code=400, detail="Invalid  student ids .The first numberic part of ids is incorrect.")
        
        if len(second) != 1:
            raise HTTPException(status_code=400, detail="بخش دوم سریال شناسنامه باید یکی از حروف الفبای فارسی باشد")
        
        for chr in second:
            if not ('آ' <= chr <= 'ی'):
                raise HTTPException(status_code=400, detail= "Invalid student ids. The alphabetical part of ids incorrect .Please enter a Persian letter.")
        if len(third) != 2:
            raise HTTPException(status_code=400, detail="Invalid student ids.Please enter a 9-character string.")
        if not second.isdigit():
            raise HTTPException (status_code=400, detail="Invalid student ids.The second numberic part of ids is incorrect.")
   
    def born_city(db: Session, born_city: str):
        city = ["اراک", "خرم آباد", "تهران", "اردبیل", "تبریز", "اصفهان", "اهواز", "ایلام", "بجنورد", "بیرجند", "مشهد",
                  "بندرعباس", "بوشهر", "ارومیه", "رشت", "زاهدان", "زنجان", "سمنان", "سنندج", "شیراز", "شهرکرد", "قزوین",
                  "قم", "کرج", "کرمان", "کرمانشاه", "گرگان", "همدان", "یاسوج", "یزد"]
        if not (born_city in city):
            raise HTTPException(status_code=400, detail="شهر محل تولد مرکز استان نیست")
    def check_address(db: Session, address: str):
        if len(address) > 100:
            raise HTTPException(status_code=400, detail="آدرس دانشجو نباید بیشتر از 100 کاراکتر باشد.")
    
    def check_postalcode(db: Session, postalcode: int):
        strpostalcode = str(postalcode)
        if len(strpostalcode) != 10 or not strpostalcode.isdigit():
            raise HTTPException(status_code=400, detail="postalcode must be 10 digits")

    
    
    def check_cphone(db: Session, cphone: str):
        if len(cphone) != 14 or not cphone[4:].isdigit():
            raise HTTPException(status_code=400, detail="شماره تلفن همراه دانشجو صحیح نیست")
        if cphone[0:4] != "+98-":
            raise HTTPException(status_code=400, detail="The cphone number must start with +98")

    
    def check_hphone(db: Session, hphone: str):
        if hphone.count('_') != 1:
            raise HTTPException(status_code=400, detail="The entered hphone number must have two parts prefix"
                                                        " and fixed number and separated by _")

        parts = hphone.split('_')
        first = parts[0]
        second = parts[1]

        if len(first) != 3 or len(second) != 8 or not first[0] != 0 :
            raise HTTPException(status_code=400, detail="invalid Student homephone ,The hphone must be 11 digits and must start with zero")
        if not (first.isdigit() and second.isdigit()):
            raise HTTPException(status_code=400, detail="The hphone number must be INTIGER")

    
    def check_department(db: Session, department: str):
        dep = {
            "فنی و مهندسی",
            "علوم پایه",
            "علوم انسانی",
            "دامپزشکی",
            "اقتصاد",
            "کشاورزی",
            "منابع طبیعی"
        }

        if department not in dep:
            raise HTTPException(status_code=400, detail="The department is invalid")

    
    def check_major(db: Session, major: str):
        majors = ["مهندسی کامپیوتر", "مهندسی برق", "مهندسی مکانیک و پلیمر",
                        "مهندسی معدن", "مهندسی عمران", "مهندسی شهرسازی"]
        if major not in majors:
            raise HTTPException(status_code=400, detail="رشته باید یکی از رشته های دانشکده فنی و مهندسی باشد")

    
    def check_married(db: Session, married: str):
        if not (married == "single" or married == "marrided"):
            raise HTTPException(status_code=400, detail="Invalid marital status.")

    
    def check_id(db: Session, id: int):
        student = db.query(models.Student).filter(models.Student.id == id).first()
        if student is not None:
            raise HTTPException(status_code=400, detail="This ID already exists")

        id = str(id)
        if not len(id) == 10 or not id.isdigit():
            raise HTTPException(status_code=400, detail="کد ملی دانشجو صحیح نیست ")

        check = int(id[9])
        sum = 0
        for i in range(9):
            sum += int(id[i]) * (10 - i)
        c = sum % 11

        if not (c < 2 and check == c or c >= 2 and check == 11 - c):
            raise HTTPException(status_code=400, detail="Invalid ID number")



# PROFESSOR
class datavalidation_professor:

    
    def professor_exists_check(db: Session, lid: str):
        professor_lid = db.query(models.Professor).filter(models.Professor.lid == lid).first()
        if professor_lid is not None:
            raise HTTPException(status_code=409, detail="lid already exists")


    def check_lid(db: Session, lid: str):
        if len(lid) != 6:
            raise HTTPException(status_code=400, detail="lid must be 6 characters")
        if not lid.isdigit():
            raise HTTPException(status_code=400, detail="lid must be number")

    
    def check_name(db: Session, fname: str, lname: str):
        if len(fname)>10  or   len(lname)> 10 :
            raise HTTPException(status_code=400, detail="نام و نام خانوادگی استاد نباید بیشتر از 10 کاراکتر باشد ")

        if not all('آ' <= char <= 'ی' or char == ' ' for char in (fname + lname)):
            raise HTTPException(status_code=400,detail="در نام استاد  فقط حروف فارسی بدون کاراکتر خاص مورد قبول است")

    def check_id(db: Session, id: int):
        professor = db.query(models.Professor).filter(models.Professor.id == id).first()
        if professor is not None:
            raise HTTPException(status_code=400, detail="This ID already exists")

        id_str= str(id)
        if len(id_str) != 10 or not id_str.isdigit():
            raise HTTPException(status_code=400, detail="invalid professor id format ")

        check = int(id_str[9])
        sum = 0
        for i in range(9):
            sum += int(id_str[i]) * (10 - i)
        c = sum % 11

        if not (c < 2 and check == c or c >= 2 and check == 11 - c):
            raise HTTPException(status_code=400, detail="Invalid ID number")

   
    def check_department(db: Session, department: str):
        dp = {
            "فنی و مهندسی",
            "علوم پایه",
            "علوم انسانی",
            "دامپزشکی",
            "اقتصاد",
            "کشاورزی",
            "منابع طبیعی"
        }

        if department not in dp:
            raise HTTPException(status_code=400, detail="دانشکده ی استاد باید از لیست دانشکده های مجاز باشد")

    
    def check_major(db: Session, major: str):
        majors = ["مهندسی کامپیوتر", "مهندسی برق", "مهندسی برق", "مهندسی مکانیک و پلیمر",
                        "مهندسی معدن", "مهندسی عمران", "مهندسی شهرسازی"]
        if major not in majors:
            raise HTTPException(status_code=400, detail="The major is invalid")
    def check_birth(db:Session ,birth:str ):
        birth = db.query(models.Professor).filter(models.Professor.birth==birth).first()
        parts = birth.split('/')
        if len(parts) != 3:
            raise HTTPException(status_code=400, detail="فرمت تاریخ تولد استاد صحیح نیست")
        day, month, year = parts
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            raise HTTPException(status_code=400, detail="تاریخ تولد استاد صحیح معتبر نیست لطفا یک تاریخ تولد معتبر براساس غالب شمسی وارد کنید")
        year = int(year)
        month = int(month)
        day = int(day)

        if not (1300 <= year <= 1402):
            raise HTTPException(status_code=400, detail="سال تولد صحیح نیست")

        if not (1 <= month <= 12):
            raise HTTPException(status_code=400, detail="ماه تولد باید بین 1 تا12 باشد")

        if (1 <= month <= 6) and not (1 <= day <= 31):
            raise HTTPException(status_code=400, detail="روز تولد باید بین 1 تا 31 باشد")

        if (7 <= month <= 12) and not (1 <= day <= 30):
            raise HTTPException(status_code=400, detail="روز تولد باید بین 1 تا 30 باشد")

    
    def born_city(db: Session, born_city: str):
        markaz = ["اراک", "خرم آباد", "تهران", "اردبیل", "تبریز", "اصفهان", "اهواز", "ایلام", "بجنورد", "بیرجند", "مشهد",
                  "بندرعباس", "بوشهر", "ارومیه", "رشت", "زاهدان", "زنجان", "سمنان", "سنندج", "شیراز", "شهرکرد", "قزوین",
                  "قم", "کرج", "کرمان", "کرمانشاه", "گرگان", "همدان", "یاسوج", "یزد"]
        if not (born_city in markaz):
            raise HTTPException(status_code=400, detail="شهر محل تولد مرکز استان نیست")
    
    def check_address(db: Session, address: str):
        if len(address) > 100:
            raise HTTPException(status_code=400, detail="آدرس نباید بیشتر از 100 کاراکتر باشد.")

    
    def check_postalcode(db: Session, postalcode: int):
        strpostalcode = str(postalcode)
        if len(strpostalcode) != 10 or not strpostalcode.isdigit():
            raise HTTPException(status_code=400, detail="postalcode must be 10 digits")

    
    def check_cphone(db: Session, cphone: str):
        if len(cphone) != 14 or not cphone[5:].isdigit():
            raise HTTPException(status_code=400, detail="The cphone number entered is not valid")
        if cphone[0:4] != "+98-":
            raise HTTPException(status_code=400, detail="The cphone number must start with +98")

    
    def check_hphone(db: Session, hphone: str):
        if hphone.count('-') != 1:
            raise HTTPException(status_code=400, detail="شماره تلفن همراه استاد صحیح نیست")
        parts = hphone.split('_')
        first = parts[0]
        second = parts[1]

        if len(first) != 3 or len(second) != 8 and first[0] != 0:
            raise HTTPException(status_code=400, detail="invalid professor homephone ,The hphone must be 11 digits and must start with zero")
        if not (first.isdigit() and second.isdigit()):
            raise HTTPException(status_code=400, detail="invalid professor homephone ,homephone must be INTEGER")



#COURSE
class datavalidation_course:

    
    def course_exists_check(db: Session, cid: str):
        course_cid = db.query(models.Course).filter(models.Course.cid == cid).first()
        if course_cid is not None:
            raise HTTPException(status_code=409, detail="cid already exists")

    
    def check_cid(db: Session, cid: str):
        if len(cid) != 5:
            raise HTTPException(status_code=400, detail="cid must be 5 characters")
        if not cid.isdigit():
            raise HTTPException(status_code=400, detail="cid must be number")

    
    def check_cname(db: Session, cname: str):
        
        if len(cname) > 25:
            raise HTTPException(status_code=400, detail="طول نام درس نباید بیشتر از 25 کاراکتر باشد")

        
        for char in cname:
            if not ('آ' <= char <= 'ی' or char == ' '):
                raise HTTPException(status_code=400,
                                    detail="نام درس باید فقظ شامل حروف فارسی باشد")

    
    def check_department_course(db: Session, department: str):
        
        dpartment = {
            "فنی و مهندسی",
            "علوم پایه",
            "علوم انسانی",
            "دامپزشکی",
            "اقتصاد",
            "کشاورزی",
            "منابع طبیعی"
        }

        if department not in dpartment:
            raise HTTPException(status_code=400, detail="دانشکده باید یکی از دانشکده های مجاز باشد")


    def check_credit(db: Session, credit: int):
        if not (1 <= credit <= 4):
            raise HTTPException (status_code=400 ,detail="invalid credit , credit must be >= 1 and <=4 .")


