from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    # def teste_falha(self):
    #     self.fail('Teste falhou :(')

    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = "bruno",
            email = "teste@teste.com",
            cpf = "02544432063",
            data_nasc = "2006-06-01",
            cel_num = "91 98745-0581"
        )

    def test_verifica_atributos_de_estudantes(self):
        """Teste que verifica os atributos do modelo Estudante"""
        self.assertEqual(self.estudante.nome, 'bruno')
        self.assertEqual(self.estudante.email, 'teste@teste.com')
        self.assertEqual(self.estudante.cpf, '02544432063')
        self.assertEqual(self.estudante.data_nasc, '2006-06-01')
        self.assertEqual(self.estudante.cel_num, '91 98745-0581')

class ModelCursosTestCase(TestCase):

    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = "CH08F",
            descricao = "Java na Prática",
            nivel = "I"
        )
    def test_verifica_dados_do_curso(self):
        """ Teste que verifica os dados inseridos dos cursos """
        self.assertEqual(self.curso.codigo, "CH08F")
        self.assertEqual(self.curso.descricao, "Java na Prática")
        self.assertEqual(self.curso.nivel, "I")

class ModelMatriculasTestCase(TestCase):

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

    def test_verifica_dados_do_curso(self):
        """ Teste que verifica os dados inseridos dos cursos """
        self.assertEqual(self.matricula.estudante, self.estudante)
        self.assertEqual(self.matricula.curso, self.curso)
        self.assertEqual(self.matricula.turno, "N")