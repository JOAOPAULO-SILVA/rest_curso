from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso, Estudante, Matricula

class MatriculasTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse("Matriculas-list")
        self.client.force_authenticate( user = self.usuario)
        self.estudante = Estudante.objects.create(
            nome='Estudante Teste',
            email='estudante@gmail.com',
            cpf='77567543010',
            data_nasc='2003-02-02',
            cel_num='11 98765-4321'
        )
        self.curso = Curso.objects.create(
            codigo='CTT',descricao='Curso Teste',nivel='B'
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            turno='M'
        )
    def test_requisicao_get_listar_matriculas(self):
        """Teste para verificar a requisição GET para listar os matriculas"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_DELETE_para_um_estudante(self):
        """Teste de requisição DELETE um estudante"""
        response = self.client.delete(f'{self.url}1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    def test_requisicao_PUT_para_atualizar_uma_matricula(self):
        """Teste de requisição PUT para uma matricula"""
        dados = {
            "curso": self.curso,
            "estudante": self.estudante,
            "turno": "N",
        }
        response = self.client.put(f"{self.url}1/",data=dados)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
