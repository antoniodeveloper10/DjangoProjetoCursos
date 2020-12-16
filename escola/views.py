from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializer import AlunoSerializer,CursoSerializer



class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibir todos alunos """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
# Create your views here.

class CursosViewSet(viewsets.ModelViewSet):
    """ Exibir todos Cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer