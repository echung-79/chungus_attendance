def new_class(class1):
    '''Function to create newclass'''
    input('Press Enter to Begin Making a New Class\n')
    class1 = []
    def addname():
        name = input("Please type in name and press enter for each student, type 'exit' to return to select screen, type 'done' to save and view class.\n")
        if name == 'done' or name == 'Done' or name == 'DONE':
            print(f'Class: {class1}')
            input('Press enter to save and return to select screen\n')
            select(class1)
        elif name == 'exit' or name == 'Exit' or name == 'EXIT':
            select(class1)
        else:
            class1.append(name)
            addname()
    addname()
def add_student(class1):
    '''Function to Add Student to Prexisting List'''
    def add():
        name = input("Please type in name to add to class and than press enter, type 'exit' to return to select screen, type 'done' to save and view class.\n")
        if name == 'done' or name == 'Done' or name == 'DONE':
            print(f'Class: {class1}')
            input('Press enter to save and return to select screen\n')
            select(class1)
        elif name == 'exit' or name == 'Exit' or name == 'EXIT':
            select(class1)
        else:
            
    def rem():
        print('remove')    
    ar = input("Type in '1' to add student and '2' to remove student.\n")
    if ar == '1':
        add()
    elif ar == '2':
        rem()
    else:
        input("Invalid response, press enter to try again.\n")

def edit_name():
    '''Function to Edit Name of Student'''
    input('Welcome to the Student Editing Interface\n')

def select(class1):
    '''Select Function to choose desired function'''
    option = input("A. Create Class, B. Add/Remove Student, C. Edit Student Name, D. Exit\n")
    valid_options = ("a",'b','c','d','A','B','C','D')
    valid = option in valid_options
    if valid is False:
        input("Invalid response, press enter to try again.\n")
        select()
    if option == 'a' or option =='A':
        new_class(class1)
    if option == 'b' or option == 'B':
        add_student(class1)
    if option == 'c' or option == 'C':
        edit_name()
    if option == 'd' or option =='D':
       exit()

def start():
    '''Welcome Screen to direct user to select screen'''
    class1 = []
    input("Welcome, Press Enter to access the Chungus Attendence Management System\n")
    print("Please type the cooresponding number of which function you'd like to use\n")
    select(class1) 
start()