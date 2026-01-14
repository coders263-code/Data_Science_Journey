# packages are diractory
# Modules or inner files 
# # syntex 
# from pack_name import file_name
# link https://drive.google.com/file/d/1_b8_0kNRfUVjQclzmyw01e0Bq630DEq7/view
""" This method is used to cover error due to paths
import os,sys
from os.path import dirname,abspath,join
sys.path.insert(0,abspath(join(dirname(__file__),'..')))"""
"""




***Example***
import os,sys
from os.path import dirname,abspath,join
sys.path.insert(0,abspath(join(dirname(__file__),'..')))
from payment import payment_details

def course_details():
    print("Its course details")

course_details()
payment_details.payment()
"""