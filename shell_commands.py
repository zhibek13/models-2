from employee.models import *

e1 = Employee.objects.create(name='Zhibek', birth_date=2000, position='assistant', salary=20000, work_experience=1)
e2 = Employee.objects.create(name='Mar', birth_date=1995, position='manager', salary=25000, work_experience=3)
e3 = Employee.objects.create(name='Aibek', birth_date=1996, position='mentor', salary=40000, work_experience=2)
e4 = Employee.objects.create(name='Seina', birth_date=2001, position='adviser', salary=25000, work_experience=2)

p1 = Passport.objects.create(inn='11309200000707', id_card='ID101705', employee=e1)
p2 = Passport.objects.create(inn='21508199500505', id_card='ID202909', employee=e2)
p3 = Passport.objects.create(inn='21409199600363', id_card='ID606848', employee=e3)
p4 = Passport.objects.create(inn='10902200100255', id_card='ID874563', employee=e4)

to_delete_employee = Employee.objects.get(id=4)
to_delete_employee.delete()
to_delete_passport = Passport.objects.get(id=4)
to_delete_passport.delete()

wp = WorkProject(project_name='Batman', employee=e1)
wp.save()

Membership.employee.set(employee=[e2, e3], project_name='Mercury', through_defaults={'date_joined': '2022-05-27'})

e5 = Employee.objects.create(name='Ariana', birth_date=2001, position='adviser', salary=25000, work_experience=2)

c1 = Client.objects.create(name='Gulya', birth_date=2000, address='Bishkek', phone_number='0701627937')
c2 = Client.objects.create(name='Omar', birth_date=1996, address='Bishkek', phone_number='0505236945')
c3 = Client.objects.create(name='Bek', birth_date=2002, address='Bishkek', phone_number='0703549693')

v = VIPClient.objects.create(name='Bektur', birth_date=1985, address='Bishkek', phone_number='0703549693', vip_status_start=2022, donation_amount=40500)

to_delete_client = Client.objects.get(id=3)
to_delete_client.delete()

Employee.objects.all()

for p in Passport.objects.all():
    print(p.employee)
    print(p.inn)
    print(p.id_card)

WorkProject.objects.all()

for w in WorkProject.objects.get(id=1):
    print(w.employee)
    print(w.work_project)

Client.objects.all()
VIPClient.objects.all()