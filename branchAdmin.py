#this file contains the branch admin features

from DBcm import UseDB


class BranchAdmin:
    def __init__(self) -> None:
        self.config = [] #this contains the access data of the database

    #this method here will create 
    def addFamily(self):
        newFamilyData = [] #this list will contain the data of the new family


        with UseDB(self.config) as cursor:
            _SQL = ''''''  #the sql query here will add data into the table
            cursor.execute(_SQL)


    #this method here will return the list of all families
    def viewFamily(self):
        with UseDB(self.config) as cursor:
            _SQL = ''''''
            cursor.execute(_SQL)
            AllFamilyInfo = cursor.fetchall()
            return AllFamilyInfo
    


    def addTutor(self):
        newTutorData = [] #this list will contain the data of the new tutor


        with UseDB(self.config) as cursor:
            _SQL = ''''''  #the sql query here will add data into the table
            cursor.execute(_SQL)
    
    def viewTutor(self):
        with UseDB(self.config) as cursor:
            _SQL = ''''''
            cursor.execute(_SQL)
            AllTutorInfo = cursor.fetchall()
            return AllTutorInfo

