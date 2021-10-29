from hashlib import md5
from DBcm import UseDB

data = (request.form['name'], request.form['email'], md5(request.form['password'].encode('ascii')).hexdigest(), md5(request.form['con_password'].encode('ascii')).hexdigest(), request.remote_addr, request.user_agent.browser)


email = "admin@email.com"
password = "mypassword"

#Note: the data here will be changed later on these ones are just for testing sake
MasterAdmin = [["tasAdmin@tas.com", "tasadminpassword"]]
BranchAdmin = [["branchAdmin@tas.com", "branchadminpassword"]]
Tutor = [["tastutor@tas.com", "tutorpassword"]]
Family = [["fam1_Admin@tas.com", "password"], ["fam3_Admin@tas.com", "password"], ["fam2_Admin@tas.com", "password"]]
def login(email, password):
	if email in MasterAdmin:
		MasterAdminLogin()
	elif email in BranchAdmin:
		BranchAdminLogin()
	elif email in Tutor:
		TutorLogin()
	elif email in Family:
		FamilyLogin()

if email:
	if password:
		if email in MasterAdmin:
			login(email, password)
	else:
		"Enter your password"
else:
	"Enter your email"
	
	
	
		
		
		
def MasterAdminLogin():
	return masterPriviledges
	
def BranchAdminLogin():
	return adminPriviledges
	
def TutorLogin():
	return tutorPriviledges
	
def FamilyLogin():
	return FamilyPriviledge
	
	

	
	

		
	
		
	