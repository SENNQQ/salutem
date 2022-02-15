from django.db import models


class Patients(models.Model):
    Sex = models.CharField(max_length=20, choices=(('Женский', 'Женский'), ('Мужской', 'Мужской')))
    Name = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    Patronymic = models.CharField(max_length=100)
    Date_of_birth = models.DateField(blank=True)
    Place_of_residence = models.CharField(max_length=100)
    Blood_type = models.CharField(max_length=10, choices=(('I+', 'I+'), ('II+', 'II+'), ('III+', 'III+'),
                                                         ('IV+', 'IV+'), ('I-', 'I-'), ('II-', 'II-'), ('III-',
                                                                                                        'III-'),
                                                         ('IV-', 'IV-')))
    Telephone = models.CharField(max_length=100)
    Email = models.CharField(max_length=30)
    # Medical_card = models.OneToOneField(on_delete=models.CASCADE)

    def __str__(self):
        return self.Name + self.Surname
