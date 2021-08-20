import getpass
import uuid
import json
import os
import datetime 
import unittest
class FileOps:


	def generate_user_date(self):
		print(datetime.datetime.now().time().strftime("%H:%M:%S"))	
		print(getpass.getuser())



	# class Testing(unittest.TestCase):
	# 	def tes_user_name(self):
	# 		self.assertEqual(display_names(),"yakul Khajuria")
	# Remove extra comments -- (REMOVE)
	def display_names(self,users_foldere):
		'''This function read all the names from different files and 
		give one list of all the names '''
		files_list = os.listdir(users_folder)
		for file_name in files_list:
			with open(users_folder+file_name,'r') as file:
				user_names_list.extend(file.readlines())
				print(user_names_list)
		return(user_names_list)
		




	def gen_UUID(self , user):
		# to generate unique id
		"""
		comment inside function should be in doc string
		"""
		return user[0]+str(uuid.uuid1())




	def gen_email(self,user_name):
		# to generate email id
		first_name = user_name[0]
		last_name = user_name[1]
		return(last_name+first_name[:2]+"@dummy.com")





	def generate_json(self,user_info):
		parsed=json.dumps(user_info)
		user_info=str(parsed)
		with open("file.json","w") as file:
			file.write(user_info)




	def strip_data(self,user_names_list):
		user_names = [user.strip() for user in user_names_list]
		# print(user_names)
		return user_names
if __name__=="__main__":
	# unittest.main()				
	PWD = os.getcwd()							#Read each file one by one and display the names of users in each file.
	users_folder = PWD+'/users/'
	user_names_list = []
	user_info = []
	# Remove unwanted comments - (REMOVE)
	# import pdb; pdb.set_trace()
	object=FileOps()
	object.generate_user_date()
	object.display_names(users_folder)
	user_names=object.strip_data(user_names_list)
	object.gen_UUID(user_names)
	for user_name in user_names:
		object.gen_email(user_names)
		user_info.append({object.gen_UUID(user_name):{"name":user_name,"email":object.gen_email(user_name)}})
	print(user_info)
	object.generate_json(user_info)