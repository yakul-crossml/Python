import unittest
import os
PWD = os.getcwd()             
users_folder = PWD+'/users/'



def display_names(users_folder):
  user_names_list =[]
  files_list = os.listdir(users_folder)
  for file_name in files_list:
    with open(users_folder+file_name,'r') as file:
      user_names_list.extend(file.readlines())
  # print(user_names_list)
  return user_names_list[0].strip()




class Testing(unittest.TestCase):
  def test_user_name(self):
    self.assertEqual(display_names("users/"),"yakul khajuria")

unittest.main()
