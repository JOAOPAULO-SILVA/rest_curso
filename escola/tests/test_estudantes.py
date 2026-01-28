from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse("Estudantes-list")
        self.client.force_authenticate( user = self.usuario)
        # self.estudante_01 = Estudante.objects.create(
        #     nome = 'Teste estudante UM',
        #     email = 'testeestudante01@gmail.com',
        #     cpf = '94278815000',
        #     data_nasc = '2006-06-01',
        #     cel_num = '91 98745-0581'
        # )
        self.estudante_01 = Estudante.objects.get(pk=1)
        # self.estudante_02 = Estudante.objects.create(
        #     nome = 'Teste estudante DOIS',
        #     email = 'testeestudante02@gmail.com',
        #     cpf = '57744910052',
        #     data_nasc = '2014-09-21',
        #     cel_num = '91 98745-0581'
        # )
        self.estudante_02 = Estudante.objects.get(pk=2)

    def test_reqiusicao_get_para_listar_estudantes(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_reqiusicao_get_para_listar_um_estudante(self):
        """Teste de requisição GET para um estudante"""
        response = self.client.get(self.url + "1/")
        dados_estudantes = Estudante.objects.get(pk=1)
        dados_estudantes_serializados = EstudanteSerializer(instance = dados_estudantes).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dados_estudantes_serializados)
    def test_requisicao_POST_para_criar_um_estudante(self):
        """Teste de requisição POST para um estudante"""
        dados = {
            "nome": "teste",
            "email": "teste@teste.com",
            "cpf": "90703875060",
            "data_nasc" : "1988-09-28",
            "cel_num" : "91 99999-9999",
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_requisicao_DELETE_para_um_estudante(self):
        """Teste de requisição DELETE um estudante"""
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    def test_requisicao_PUT_para_atualizar_um_estudante(self):
        """Teste de requisição PUT para um estudante"""
        dados = {
            "nome": "teste",
            "email": "teste@teste.com",
            "cpf": "94278815000",
            "data_nasc" : "1988-09-28",
            "cel_num" : "91 99999-9999",
        }
        response = self.client.put(f"{self.url}1/",data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)