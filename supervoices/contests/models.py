from enum import Enum
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class State(Enum):
    INP = "En Progreso"
    CVD = "Convertido"
    CVG = "Convirtiendo"


class Profile(Enum):
    AD = "Admin"
    MK = "Marketing"
    AN = "Announcer"


class Image(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre de la Imagen')
    path = models.CharField(max_length=500, verbose_name='Nombre de la Imagen', null=True)
    creation_date = models.DateTimeField(verbose_name='Fecha Creación')
    creation_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Url(models.Model):
    url = models.CharField(max_length=500, verbose_name='Url', unique=True)
    creation_date = models.DateTimeField(verbose_name='Fecha Creación')
    creation_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.url


class Company(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre de la Empresa')
    creation_date = models.DateTimeField(verbose_name='Fecha Creación')

    def __str__(self):
        return self.name


class UserExtras(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.CharField(
      max_length=3,
      choices=[(tag, tag.value) for tag in Profile]
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Contest(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre del Concurso')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, verbose_name='Imagen')
    url = models.ForeignKey(Url, on_delete=models.CASCADE, verbose_name='Url')
    start_date = models.DateField(verbose_name='Fecha Inicio')
    start_time = models.TimeField(verbose_name='Hora Inicio')
    end_date = models.DateField(verbose_name='Fecha Fin')
    end_time = models.TimeField(verbose_name='Hora Fin')
    prize = models.BigIntegerField(verbose_name='Premio')
    script = models.CharField(max_length=500, verbose_name='Guión')
    advices = models.CharField(max_length=500, verbose_name='Consejos', null=True)
    creation_date = models.DateTimeField(verbose_name='Fecha Creación')
    creation_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario Creación')


class Voice(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, verbose_name='Concurso')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario Carga', null=True)
    user_first_name = models.CharField(max_length=250, verbose_name='Nombre', null=True)
    user_last_name = models.CharField(max_length=250, verbose_name='Apellido', null=True)
    email = models.EmailField(verbose_name='Email')
    state = models.CharField(
        max_length=3,
        choices=[(tag, tag.value) for tag in State]
    )
    winner = models.BooleanField(verbose_name='Es Ganador?')
    path_original = models.CharField(max_length=500, verbose_name='Ruta Archivo Original')
    path_converted = models.CharField(max_length=500, verbose_name='Ruta Archivo Convertido')
    notes = models.CharField(max_length=500, verbose_name='Observaciones', null=True)
    creation_date = models.DateTimeField(verbose_name='Fecha Creación')

