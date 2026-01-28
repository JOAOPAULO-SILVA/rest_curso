from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from escola.models import Curso

class CursosTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse("Cursos-list")
        self.client.force_authenticate( user = self.usuario)
        # self.curso_01 = Curso.objects.create(
        #     codigo='CT01',descricao='Curso Teste 01',nivel='B'
        # )
        self.curso_01 = Curso.objects.get(codigo="08H")
        # self.curso_02 = Curso.objects.create(
        #     codigo='CT02',descricao='Curso Teste 02',nivel='I'
        # )
        # self.curso_01 = Curso.objects.get(codigo="CP001")
    
    def test_requisicao_get_listar_cursos(self):
        """Teste para verificar a requisição GET para listar os cursos"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    