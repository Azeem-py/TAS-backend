#this file contains a all the priviledges and authorization of the master administrator


from DBcm import UseDB
from hashlib import md5


class MasterAdmin:
    def __init__(self) -> None:
        self.email = "masteradmin@tas.com"
        self.password = "masterAdminPassword"


    def AddLocation(self):
        self.newLocationData = [] #this variable contains all the info of the new location/branch

        #this will basically insert the info of the new branch into the table
        with UseDB() as cursor:
            _SQL = '''insert into branch_info (Name, email, password, IP, browser_string)
                    values (%s, %s, %s, %s, %s)'''

            cursor.execute(_SQL, ())


    def DeleteLocation(self):
        self.newLocationData = [] #this variable contains all the info of the new location/branch

        #this will basically insert the info of the new branch into the table
        with UseDB() as cursor:

            #this delete or deactivates a location

            branchName = ""
            _SQL = '''delete from branch_info where branchName = %'''
            cursor.execute(_SQL, (branchName))


    def classLists(self):
        with UseDB() as cursor:
            _SQL = '''select password from classLists'''
            cursor.execute(_SQL)
            classLists = cursor.fetchall()
            return classLists


    def addAdminAccount(self):
        newAdminInfo = []
        with UseDB() as cursor:
            _SQL = '''''' #query to insert new admin info into the database 
            cursor.execute(_SQL)

    def viewAdmins(self):
        with UseDB(self.config) as cursor:
            _SQL = '''''' #query to select admins info from the database
            cursor.execute(_SQL)
            adminData = cursor.fetchall()
            return adminData

    def reports(self):
        #the function will be available later
        pass

    def bulkMessage(self):
        #the function will be available later
        pass




