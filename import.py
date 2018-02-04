import csv,sys,os
project_dir="/C:/cygwin64/home/uday.n/demo/blog"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE']='blog.settings'
import django
django.setup()
import string
import random
def password_generator(size=10, chars=string.digits+ string.ascii_letters):
	return ''.join(random.choice(chars) for _ in range(size))
from accounts.forms import RegistrationForm
data=csv.reader(open("Uday_excel.csv"),delimiter=",")
for row in data:
    if row[0]!='username':
        a=RegistrationForm()
        a.username=row[0]
        a.email=row[1]
        a.password=password_generator()
        a.save()
        
