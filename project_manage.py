# import database module

from database import CSV, Database, Table
import csv

# define a funcion called initializing
DB = Database()
csv1 = CSV()

def initializing():
    """
    here are things to do in this function:
    create an object to read all csv files that will serve
    as a persistent state for this program
    create all the corresponding tables for those csv files
    see the guide how many tables are needed
    add all these tables to the database
    """
    csv_login = csv1.read_csv('login.csv')
    csv_person = csv1.read_csv('persons.csv')
    login_table = Table('login', csv_login)
    person_table = Table('persons', csv_person)
    DB.insert(login_table)
    DB.insert(person_table)
    for i in csv_login:
        print(i['username'])


# initializing()
# define a function called login

def login():
    username = input('Enter Username: ')
    password = input('Enter Password: ')
    data_login = DB.database[0].table
    for each in data_login:
        if username == each['username'] and password == each['password']:
            return each['ID'], each['role']
    else:
        return None


# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None

# define a function called exit
def exit():
    with open('persons.csv.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'username', 'password', 'role'])
        for each in DB.database[0].table:
            writer.writerow(each.values())


# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

if val[1] == 'admin':
    pass
elif val[1] == 'student':
    pass
elif val[1] == 'member':
    pass
elif val[1] == 'lead':
    pass
elif val[1] == 'faculty':
    pass
elif val[1] == 'advisor':
    pass

# once everyhthing is done, make a call to the exit function
exit()
