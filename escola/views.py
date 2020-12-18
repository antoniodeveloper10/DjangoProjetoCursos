from rest_framework import viewsets,generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer,CursoSerializer,MatriculaSerializer,ListaMAtriculasALunoSerializer,ListaALunoEmUmCursoSerializer



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

class ListaMAtriculasALuno(generics.ListAPIView):  
    """ Listanfo  todas Matriculas """
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMAtriculasALunoSerializer    

class ListaALunoCurso(generics.ListAPIView):  
    """ Listanfo  todas alunos do curso """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaALunoEmUmCursoSerializer    