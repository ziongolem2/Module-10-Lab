Saul
Resendiz

   	MODULE 10 LAB


   QUESTION 1:

# DEFINE OUR PET CLASS

class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name 
        self.__animal_type = animal_type
        self.__age = age
        
    def set_name(self, name):
        self.__name = name
            
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
        
    def set_age(self, age):
        self.__age = age
            
    def get_name(self):
        return self.__name
            
    def get_animal_type(self):
        return self.__animal_type
            
    def get_age(self):
        return self.__age


# Program creating an object of the class

# Get pet's name, type, and age
name = input("Enter your pet's name: ")
animal_type = input("Enter the type of animal it is: ")
age = int(input("Enter the age of your pet: "))  

# creating pet object
my_pet = Pet(name, animal_type, age)

# printing info to console
print("Here is the info that you entered: ")
print("Pet name:", my_pet.get_name())
print("Animal type:", my_pet.get_animal_type())
print("Age:", my_pet.get_age())


      QUESTION 2:

# DEFINE OUR CAR CLASS

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0  
        
    def accelerate(self):
        self.__speed += 5  
        
    def brake(self):
        self.__speed -= 5 
        
    def get_speed(self):
        return self.__speed  
        
# Create Car object
my_car_object = Car(2019, "Honda")

for x in range(5):
    my_car_object.accelerate()
    print(f'Car Speed: {my_car_object.get_speed()}')

for x in range(5):
    my_car_object.brake()
    print(f'Car Speed: {my_car_object.get_speed()}')


    QUESTION 3:

# Creating person info class
class PersonInfo:
    def __init__(self, name, address, age, phone_number):  
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number
        
    # SETTERS
    def set_name(self, name):
        self.__name = name 
        
    def set_address(self, address):
        self.__address = address 
        
    def set_age(self, age):
        self.__age = age
        
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
        
    # GETTERS
    def get_name(self):
        return self.__name
        
    def get_address(self):
        return self.__address
        
    def get_age(self):
        return self.__age
    
    def get_phone_number(self):
        return self.__phone_number
        
# Creating 3 instances of the class
my_person_object1 = PersonInfo("Spongebob", "Pineapple House", 20, "951-320-4920")
my_person_object2 = PersonInfo("Patrick", "Rock House", 25, "951-493-4950")
my_person_object3 = PersonInfo("Sandy", "Dome House", 30, "951-304-9459")


     QUESTION 4:

# Creating employee class
class Employee:
    def __init__(self, name, id_number, department, job_title):  
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title
        
    # Setter methods
    def set_name(self, name):
        self.__name = name
        
    def set_id_number(self, id_number):
        self.__id_number = id_number
        
    def set_department(self, department):
        self.__department = department 
        
    def set_job_title(self, job_title):
        self.__job_title = job_title 
        
    # Getter methods
    def get_name(self):
        return self.__name 
        
    def get_id_number(self):
        return self.__id_number
    
    def get_department(self):
        return self.__department
    
    def get_job_title(self):
        return self.__job_title
        
# Creating three employee objects
my_employee_object1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
my_employee_object2 = Employee("Mark Jones", 39119, "IT", "Programmer")
my_employee_object3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

# Display the Name, ID Number, Department, and Job Title for all 3 employees
print(f'{my_employee_object1.get_name()}, ID: {my_employee_object1.get_id_number()}, {my_employee_object1.get_department()}, {my_employee_object1.get_job_title()}')
print(f'{my_employee_object2.get_name()}, ID: {my_employee_object2.get_id_number()}, {my_employee_object2.get_department()}, {my_employee_object2.get_job_title()}')
print(f'{my_employee_object3.get_name()}, ID: {my_employee_object3.get_id_number()}, {my_employee_object3.get_department()}, {my_employee_object3.get_job_title()}')


    QUESTION 5:

# Creating RetailItem class
class RetailItem:
    def __init__(self, item_description, units, price):  
        self.__item_description = item_description  
        self.__units = units 
        self.__price = price
        
    # SETTERS    
    def set_item_description(self, item_description):
        self.__item_description = item_description
    
    def set_units(self, units):
        self.__units = units 
        
    def set_price(self, price):
        self.__price = price
        
    # GETTERS     
    def get_item_description(self):  
        return self.__item_description
        
    def get_units(self):
        return self.__units 
        
    def get_price(self):
        return self.__price
        

# Creating three retail item objects and initializing them
item_object1 = RetailItem("Jacket", 12, 59.95)
item_object2 = RetailItem("Designer Jeans", 40, 34.95)
item_object3 = RetailItem("Shirt", 20, 24.95)


  QUESTION 6:

# PATIENT CLASS
class Patient:
    def __init__(self, fname, mname, lname, address, city, state, zipcode, phone, emergname, emergphone):
        self.__fname = fname
        self.__mname = mname
        self.__lname = lname
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.__phone = phone
        self.__emergname = emergname
        self.__emergphone = emergphone

    # SETTERS
    def set_first_name(self, fname):
        self.__fname = fname

    def set_middle_name(self, mname):
        self.__mname = mname

    def set_last_name(self, lname):
        self.__lname = lname

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip_code(self, zipcode):
        self.__zipcode = zipcode

    def set_phone(self, phone):
        self.__phone = phone

    def set_emergency_contact_name(self, emergname):
        self.__emergname = emergname

    def set_emergency_contact_phone(self, emergphone):
        self.__emergphone = emergphone

    # GETTERS
    def get_fname(self):
        return self.__fname

    def get_mname(self):
        return self.__mname

    def get_lname(self):
        return self.__lname

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zipcode(self):
        return self.__zipcode

    def get_phone(self):
        return self.__phone

    def get_emergname(self):
        return self.__emergname

    def get_emergphone(self):
        return self.__emergphone
        
# PROCEDURE CLASS
class Procedure:
    def __init__(self, procedure_name, procedure_date, practitioner, charges):
        self.__procedure_name = procedure_name
        self.__procedure_date = procedure_date
        self.__practitioner = practitioner
        self.__charges = charges

    # SETTERS
    def set_procedure_name(self, procedure_name):
        self.__procedure_name = procedure_name

    def set_procedure_date(self, procedure_date):
        self.__procedure_date = procedure_date

    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner

    def set_charges(self, charges):
        self.__charges = charges

    # GETTERS
    def get_procedure_name(self):
        return self.__procedure_name

    def get_procedure_date(self):
        return self.__procedure_date

    def get_practitioner(self):
        return self.__practitioner

    def get_charges(self):
        return self.__charges
        
 # CREATING PATIENT OBJECT, INTIALIZED WITH DATA
patient_object1 = Patient("Mike", "Andres", "Resendiz","Elm Street", "Norco", "CA", "91850", "951-423-9586", "John Wright", "951-594-6842")

# CREATING 3 PROCEDURE OBJECTS, CREATING INITIALIZED WITH DATA
procedure_object1 = Procedure("Physical Exam", "2024-11-24", "Dr. Irvine", 250.00)
procedure_object2 = Procedure("X-ray", "2024-11-24", "Dr. Jamison", 500.00)
procedure_object3 = Procedure("Blood test", "2024-11-24", "Dr. Smith", 200.00)

# DISPLAYING PATIENT'S INFO, INFO ABOUT ALL 3 PROCEDURES, AND TOTAL CHARGES OF THE 3 PROCEDURES
print('Patient First, Middle, and Last Name:')
print(f'\n{patient_object1.get_fname()}, {patient_object1.get_mname()}, {patient_object1.get_fname()}')

print('Info about Procedure 1: ')
print(f'\n{procedure_object1.get_procedure_name()}, {procedure_object1.get_procedure_date()}, {procedure_object1.get_practitioner()}')

print('Info about Procedure 2: ')
print(f'\n{procedure_object2.get_procedure_name()}, {procedure_object2.get_procedure_date()}, {procedure_object2.get_practitioner()}')

print('Info about Procedure 3: ')
print(f'\n{procedure_object3.get_procedure_name()}, {procedure_object3.get_procedure_date()}, {procedure_object3.get_practitioner()}')

print('Procedure 1 Charges: ')
print(f'\n{procedure_object1.get_charges()}')

print('Procedure 2 Charges: ')
print(f'\n{procedure_object2.get_charges()}')

print('Procedure 3 Charges: ')
print(f'\n{procedure_object3.get_charges()}')

























































































































