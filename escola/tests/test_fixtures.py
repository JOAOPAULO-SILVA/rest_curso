from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']

    def teste_carregamento_da_fixtures(self):
        """Teste que verifica o carregamento da fixtures"""
        estudante = Estudante.objects.get(pk=1)
        curso = Curso.objects.get(pk="08H")
        self.assertEqual(estudante.cel_num, "92987450581")
        self.assertEqual(curso.nivel,"B")