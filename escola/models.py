from django.db import models
objects = models.Manager()

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg   = models.CharField(max_length=9)
    cpf  = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B', 'Basico'),
        ('I', 'Intermediario'),
        ('A', 'Avancado')
    )
    codigo_curso = models.CharField(max_length=10)       
    descricao = models.CharField(max_length=100)       
    nivel_curso = models.CharField(max_length=1,choices=NIVEL,blank=False,null=False,default='B')  

    def __str__(self):
        return self.descricao    

class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'verpertino'),
        ('N', 'Noturno')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1,choices=PERIODO,blank=False,null=False,default='M')  
