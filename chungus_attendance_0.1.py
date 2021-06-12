
def transition(option):
    '''Function to Transition from select screen to selected function'''
    print(option)
    if option == 'a' or 'A':
        new_class()
    elif option == 'b' or 'B':
        add_student()
    elif option == 'c' or 'C':
        edit_name()
    elif option == 'd' or 'D':
        exit()
def select():
    '''Select Function to choose desired function'''
    option = input("A. Create Class, B. Add/Remove Student, C. Edit Student Name, D. Exit\n")
    valid_options = ("a",'b','c','d','A','B','C','D')
    valid = option in valid_options
    if valid is False:
        input("Invalid response, press enter to try again.\n")
        select()
    if valid is True:
        transition(option)
def new_class():
    '''Function to create newclass'''
    input('Press Enter to Begin Making a New Class\n')
    class1 = []
    def addname():
        name = input("Please type in name and press enter for each student, type 'exit' to return to select screen, type 'done' to save and view class.\n")
        if name == 'done' or name == 'Done' or name == 'DONE':
            print(f'Class: {class1}')
            input('Press Enter to Return to Select Screen\n')
            select()
        elif name == 'exit' or name == 'Exit' or name == 'EXIT':
            select()
        else:
            class1.append(name)
            addname()      
    addname()
def add_student(class1):
    '''Function to Add Student to Prexisting List'''
    def add()
    
    ar = input('Type in 1 to add student and 2 to remove student.\n')
    if ar == '1':
        add()
    elif ar == '2':
        remove()
    else:
        input("Invalid response, press enter to try again.\n")
def edit_name():
    '''Function to Edit Name of Student'''
    input('Welcome to the Student Editing Interface\n')
def start():
    input("Welcome, Press Enter to access the Chungus Attendence Management System\n")
    print("Please type the cooresponding number of which function you'd like to use\n")
    select()
start()
