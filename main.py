class Person:
    def __init__(self,name:str,age : int):
        self.name = name
        self.age = age
    def show_details(self):
        return f" The name is {self.name} and age is {self.age}"
    
    
    
class Student(Person):
    def __init__(self, name:str, age:int , student_id:int,branch:str):
        self.student_id = student_id
        self.branch = branch
        super().__init__(name, age)
    def show_details(self):
        return super().show_details() + f" student id id {self.student_id} and branch is {self.branch}"
    
    

class Employee (Person):
    def __init__(self, name:str , age:int,emp_id:int,dept:str , subjects:list[str],salary:int):
        self.emp_id = emp_id
        self.dept = dept
        self.subject = subjects
        self.salary = salary
        super().__init__(name,age)
    def show_details(self):
        return super().show_details() +  f" employee id is {self.emp_id} and dept is {self.dept} subject is {self.subject} and salary is {self.salary}"
    
    
    
class University:
    student_Table = {}
    employee_Table = {}
    def __init__(self,name:str,course:str):
        self.name = name
        self.course = course

    def add_student(self,student_obj:Student):
        if student_obj.student_id not in self.student_table:
            self.student_table[student_obj.student_id] = [student_obj.name,student_obj.age,student_obj.branch]
        else:
            return "Student already exists"
        

    def add_employee(self,employee_obj:Employee):
        if employee_obj.employee_id not in self.employee_table:
            self.employee_table[employee_obj.employee_id] = [employee_obj.name,employee_obj.age,employee_obj.dept,employee_obj.subject,employee_obj.salary]
        else:
            return "Employee already exists"

        
    def course(self,new_course):
        if new_course not in self.course:
            self.course.append(new_course)
            return f"{new_course} added successfully"
        
        
    def total_student_details(self,id:str = None,branch:str = None):
        if id:
            return self.student_table[id]
        elif branch:
            for item in self.student_table.items():
                if item[1][2] == branch:
                    print(f"{item[0]} - {item[1]}")
        else:
            for item in self.student_table.items():
                print(f"{item[0]} - {item[1]}")
        

    def total_employee_details(self):
        for item in self.employee_table.items():
            print(f"{item[0]} - {item[1]}")

        



#main
if __name__ == "__main__":
    uni = University("Codegnan university",["PFS","JFS","DS","DA"])
    s1 =  Student("John",21,101,"DS")
    s2 =  Student("Hari",25,324,"DA")
    s3  =  Student("John",21,105,"PFS")
    uni.add_student(s1)
    uni.add_student(s2)
    uni.add_student(s3)
    uni.total_student_details()
    


    
    



        
        



    
    
        