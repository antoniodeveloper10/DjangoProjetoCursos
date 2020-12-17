from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer,CursoSerializer,MatriculaSerializer



class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibir todos alunos """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
# Create your views here.

class CursosViewSet(viewsets.ModelViewSet):
    """ Exibir todos Cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):  
    """ Exibir todas Matriculas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer