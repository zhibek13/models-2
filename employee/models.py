from django.db import models


class AbstractPerson(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.IntegerField()

    class Meta:
        abstract = True

    def get_age(self):
        year = 2022 - self.birth_date.year
        return year

    def __str__(self):
        return self.name


class Employee(AbstractPerson):
    position = models.CharField(max_length=100)
    salary = models.IntegerField()
    work_experience = models.IntegerField()

    def __str__(self):
        return self.position


class Passport(models.Model):
    inn = models.CharField(max_length=100)
    id_card = models.CharField(max_length=100)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def get_gender(self):
        if self.inn.startswith('1'):
            return 'Female'
        if self.inn.startswith('2'):
            return 'Male'

    def __str__(self):
        return self.inn


class WorkProject(models.Model):
    project_name = models.CharField(max_length=100)
    employee = models.ManyToManyField(Employee, through='Membership')

    def __str__(self):
        return self.project_name


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.IntegerField()

    def __str__(self):
        return f'{self.employee} - {self.work_project} - {self.date_joined}'


class Client(AbstractPerson):
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.address


class VIPClient(Client):
    vip_status_start = models.IntegerField()
    donation_amount = models.IntegerField()

    def __str__(self):
        return self.vip_status_start



