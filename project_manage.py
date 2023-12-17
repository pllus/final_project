# import database module

from database import CSV, Database, Table
import csv
import datetime

# define a funcion called initializing
DB = Database()
csv1 = CSV()

class Student:
    def __init__(self, id, username, role):
        self.id = id
        self.user = username
        self.role = role

    def see_invite(self):
        pass
    def accept_invite(self):
        pass

    def deny_invite(self):
        pass


class Lead(Student):
    def __init__(self):
        pass

    def create_project(self):
        pass

    def see_project(self):
        all_project = DB.search('project')
        print(all_project)


    def sent_invite(self):
        pass

    def accept_invite(self):
        pass

    def deny_invite(self):
        pass

    def add_member(self):
        pass

    def remove_member(self):
        pass

    def modify_project(self):
        pass

    def send_request_advisor(self):
        pass

    def status(self):
        pass

    def summit(self):
        pass


class Member:
    def see_project(self):
        pass

    def modify_project(self):
        pass

class Advisor:
    def see_request_supervisor(self):
        pass
    def manage_request(self):
        pass

    def see_project(self):
        pass

class Admin:
    pass

class Faculty:
    pass


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
    login_table = Table('login', csv_login)
    DB.insert(login_table)

    csv_person = csv1.read_csv('persons.csv')
    person_table = Table('persons', csv_person)
    DB.insert(person_table)

    csv_project = csv1.read_csv('project.csv')
    project_table = Table('project', csv_project)
    DB.insert(project_table)

    csv_advisor = csv1.read_csv('Advisor_pending_request.csv')
    advisor_table = Table('persons', csv_advisor)
    DB.insert(advisor_table)

    csv_member = csv1.read_csv('Member_pending_request.csv')
    member_table = Table('persons', csv_member)
    DB.insert(member_table)


def login_base():
    print("Welcome to Senior_Project Report Program")
    data_login = DB.search('login')
    print(data_login)
    username = input('Enter Username: ')
    password = input('Enter Password: ')
    # data_login = DB.search('login')
    for each in data_login:
        if username == each['username'] and password == each['password']:
            return each['ID'], each['role']
    else:
        return None

print(login_base())

# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None

# define a function called exit
def exit():
    login = open('login.csv', 'w')
    login_writer = csv.writer(login)
    login_writer.writerow(['ID', 'username', 'password', 'role'])
    for each in DB.database[0].table:
        login_writer.writerow(each.values())
    login.close()

    person = open('persons.csv', 'w')
    person_writer = csv.writer(person)
    person_writer.writerow(['ID', 'first', 'last', 'type'])
    for each in DB.database[1].table:
        person_writer.writerow(each.values())
    person.close()

    project = open('project.csv', 'w')
    project_writer = csv.writer(project)
    project_writer.writerow(['ProjectID', 'Title', 'Lead', 'Member1', 'Member2', 'Advisor', 'Status'])
    for each in DB.database[2].table:
        person_writer.writerow(each.values())
    person.close()

    advisor_pending = open('Advisor_pending_request.csv', 'w')
    advisor_pending_writer = csv.writer(advisor_pending)
    advisor_pending_writer.writerow(['ProjectID', 'Advisor_Request', 'Response', 'Response_date'])
    for each in DB.database[3].table:
        person_writer.writerow(each.values())
    person.close()

    member_pending = open('member_pending_request.csv', 'w')
    member_pending_writer = csv.writer(member_pending)
    member_pending_writer.writerow(['ProjectID', 'Member_Request', 'Response', 'Response_date'])
    for each in DB.database[4].table:
        person_writer.writerow(each.values())
    person.close()

    print('\n Program Exit')


def project_id():
    pass


# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above
print(DB.database)
initializing()
val = login_base()

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] == 'admin':
#     pass
# elif val[1] == 'student':
#     pass
# elif val[1] == 'member':
#     pass
# elif val[1] == 'lead':
#     pass
# elif val[1] == 'faculty':
#     pass
# elif val[1] == 'advisor':
#     pass

# once everyhthing is done, make a call to the exit function
exit()
