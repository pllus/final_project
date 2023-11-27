# import database module
import os, csv, random
from final_project.final_project.database import Table, DB

# define a funcion called initializing
my_DB = DB()

def initializing():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    persons = []
    with open(os.path.join(__location__, 'persons.csv')) as f:
        rows = csv.DictReader(f)
        for r in rows:
            persons.append(dict(r))

    table1 = Table('persons', persons)
    my_DB.insert(table1)

# here are things to do in this function:

# create an object to read all csv files that will serve as a persistent state for this program

# create all the corresponding tables for those csv files
    login = []
    table_login = Table('login',login)

    for id in table1.table:
        random_digit = (str(random.randint(0, 9)) + str(random.randint(0, 9))
                        + str(random.randint(0, 9)) + str(random.randint(0, 9)))
        role = 'Admin'
        if id['type'] == 'student':
            role = 'Member'
        elif id['type'] == 'faculty':
            role = 'Faculty'
        table_login.insert({f'person_id': id['ID'], 'username': id['fist']+'.'+id['last'][0],
                        'password': random_digit, 'role': role})
    my_DB.insert(table_login)
# see the guide how many tables are needed

# add all these tables to the database


# define a funcion called login

def login():
    data = my_DB.search('login')
    print(data.table)
    user = input('Username: ')
    password = input('Password: ')
    for i in data.table:
        print(i["username"], i["password"])
        if (i['username']) == user and (i['password']) == password:
            return (i['person_id']), (i['role'])
        else:
            return None


# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None

# define a function called exit
def exit():
    pass


# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()
print(val)

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
# see and do admin related activities
# elif val[1] = 'student':
# see and do student related activities
# elif val[1] = 'member':
# see and do member related activities
# elif val[1] = 'lead':
# see and do lead related activities
# elif val[1] = 'faculty':
# see and do faculty related activities
# elif val[1] = 'advisor':
# see and do advisor related activities

# once everyhthing is done, make a call to the exit function
exit()
