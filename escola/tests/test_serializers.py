from django.test import TestCase
from escola.models import Curso, Estudante, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer

class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome = "bruno",
            email = "teste@teste.com",
            cpf = "02544432063",
            data_nasc = "2006-06-01",
            cel_num = "91 98745-0581"
        )
        self.serializer_estudante = EstudanteSerializer(instance = self.estudante)

    def test_verifica_campos_serializados_de_estudante(self):
        """Teste que verifica os campos que estão sendo serializados dos estudantes"""
        dados = self.serializer_estudante.data
        self.assertEqual(dados.keys(), set(['id','cpf','email','nome', 'data_nasc','cel_num']))
    def test_verifica_dados_serializados_de_estudante(self):
        """Teste que verifica o conteúdo dos campos que estão sendo serializados dos estudantes"""
        dados = self.serializer_estudante.data
        self.assertEqual(dados['id'], self.estudante.id)
        self.assertEqual(dados['cpf'], self.estudante.cpf)
        self.assertEqual(dados['nome'], self.estudante.nome)
        self.assertEqual(dados['data_nasc'], self.estudante.data_nasc)
        self.assertEqual(dados['cel_num'], self.estudante.cel_num)
    
class SerializerCursosTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = "CH08F",
            descricao = "Java na Prática",
            nivel = "I"
        )
        self.serializer_curso = CursoSerializer(instance = self.curso)
    def test_verifica_campos_serializados_de_curso(self):
        """Teste que verifica os campos que estão sendo serializados dos cursos"""
        dados = self.serializer_curso.data
        self.assertEqual(dados.keys(), set(['codigo','descricao','nivel']))
    def test_verifica_dados_serializados_de_curso(self):
        """Teste que verifica o conteúdo dos campos que estão sendo serializados dos cursos"""
        dados = self.serializer_curso.data
        self.assertEqual(dados['codigo'], self.curso.codigo)
        self.assertEqual(dados['descricao'], self.curso.descricao)
        self.assertEqual(dados['nivel'], self.curso.nivel)

class SerializerMatriculasTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = "bruno",
            email = "teste@teste.com",
            cpf = "02544432063",
            data_nasc = "2006-06-01",
            cel_num = "91 98745-0581"
        )
        self.curso = Curso.objects.create(
            codigo = "CH08F",
            descricao = "Java na Prática",
            nivel = "I"
        )
        self.matricula = Matricula.objects.create(
            estudante = self.estudante,
            curso = self.curso,
            turno = "N"
        )
        self.serializer_matricula = MatriculaSerializer(instance = self.matricula)

    def test_verifica_campos_serializados_de_matricula(self):
        """Teste que verifica os campos que estão sendo serializados dos matriculas"""
        dados = self.serializer_matricula.data
        self.assertEqual(dados.keys(), set(['id','estudante','curso','turno']))

    def test_verifica_dados_serializados_de_matricula(self):
        """Teste que verifica o conteúdo dos campos que estão sendo serializados dos matriculas"""
        dados = self.serializer_matricula.data
        self.assertEqual(dados['id'], self.matricula.id)
        self.assertEqual(dados['estudante'], self.matricula.estudante.id)
        self.assertEqual(dados['curso'], self.matricula.curso.codigo)
        self.assertEqual(dados['turno'], self.matricula.turno)