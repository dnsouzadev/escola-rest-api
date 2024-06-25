from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse

class CursosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1',
            descricao='Curso Teste 1',
            nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2',
            descricao='Curso Teste 2',
            nivel='A'
        )

    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar a requisição GET para listar os cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_requisicao_post_para_criar_curso(self):
        """Teste para verificar a requisição POST para criar um curso"""
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso Teste 3',
            'nivel': 'A'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, 201)

    def test_requisicao_delete_para_deletar_curso(self):
        """Teste para verificar a requisição DELETE para deletar um curso"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, 204)


    def test_requisicao_put_para_atualizar_curso(self):
        """Teste para verificar a requisição PUT para atualizar um curso"""
        data = {
            'codigo_curso': 'CTT1',
            'descricao': 'Curso Teste 1',
            'nivel': 'I'
        }
        response = self.client.put('/cursos/1/', data=data)
        self.curso_1.refresh_from_db()
        self.assertEquals(self.curso_1.nivel, 'I')
