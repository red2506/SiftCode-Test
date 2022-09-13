==============================================
Prerequisites to run the automation tests
==============================================
1) python(>=3.6)
2) selenium (pip install selenium)
3) pandas (pip install pandas)
4) openpyxl (pip install openpyxl)

==============================================
Changes to be made while running
==============================================
1) A tag by the name 'GK' must be created from the admin account before running the tests file
2) Questions must be added by uploading the Excel file present in the path Questions\questions.xlsx
3) The paths to the pdf and the image present in UserDocuments for uploding must be changed in files UserInfoTest\UserInfoPages\uploadDocuments.py
4) The path to add the Excel file in User_credentials folder must be changes in the file CreateTest\TestFunctions\CreateUser.py
5) The admin account must be changed in the Excel file (User_credentials\Users_add.xlsx)
6) The user accounts must be changed in the Excel file (User_credentials\Users.xlsx)

==============================================
How to run the tests
==============================================
1) Run the main.py file to run all the test in the order Test creation, Login-Logout test, User-info test, Test submisssion and
   Test deletion. (Optionally there is a signup test which is commented but can be uncommented)