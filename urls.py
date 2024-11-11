"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from weather_checker.models import ZipCode



urlpatterns = [
    # path('', include("helloworld.urls") ),
    path('weather/', include('weather_checker.urls')),
    path('admin/', admin.site.urls),
 #   path('registration/', views.some_function )

]


def load_zipcodes_if_needed():

    if len(ZipCode.objects.all()) > 0:
        return

    with open('my_project/USA-Zip.csv', 'r') as FILE:
        for line in FILE:
            records = line.split(',,')
            for record in records:
                if len(record) > 0:

                    details = record.split(',')
                    if len(details) == 4:
                        zipcode = ZipCode.objects.create(zip=details[0].strip(),town=details[1].strip(), state=details[2].strip(), st_abbr=details[3].strip())
                        zipcode.save()
                        print("zipcode is loaded " + record)
                    else:
                        print('this record is not saved because of data error.' + record )


# def load_students():
#
#     with open('my_project/students.csv', 'r') as FILE:
#         for student in FILE:
#             student_info = student.split(',')
#             first_name = student_info[1].strip()
#             last_name = student_info[0].strip()
#             id = student[2].strip()
#
#             student = Student.objects.create(firstname = first_name, lastname = last_name, studentID=id)
#             student.save()
#
#print('start to load zipcodes......')
#load_zipcodes_if_needed()
#load_students()
#print('zipcode loading is done.')
