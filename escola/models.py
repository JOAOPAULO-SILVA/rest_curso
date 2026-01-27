from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Estudante(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    data_nasc = models.DateField()
    cel_num = models.CharField(max_length=14)

    def __str__(self):
        return self.nome
    

class Curso(models.Model):
    NIVEL = (
        ("B", "Basico"),
        ("I", "Intermediario"),
        ("S", "Avançado"),
    )

    codigo = models.CharField(max_length=10, primary_key=True, unique=True, validators=[MinLengthValidator(3)])
    descricao = models.CharField(max_length=100, blank=False)
    nivel = models.CharField(max_length=1, blank=False, null=False)

    def __str__(self):
        return self.codigo
    
class Matricula(models.Model):
    TURNO = (
        ("M", "manha",),
        ("T","tarde",),
        ("N","noite",),
    )
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    turno = models.CharField(max_length=1, choices=TURNO, blank=False, null=False, default='M')