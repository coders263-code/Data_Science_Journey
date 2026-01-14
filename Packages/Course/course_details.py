import os,sys
from os.path import dirname,abspath,join
sys.path.insert(0,abspath(join(dirname(__file__),'..')))

from payment import payment_details

def course_details():
    print("Its course details")

course_details()
payment_details.payment()
