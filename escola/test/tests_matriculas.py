from rest_framework.test import APITestCase
from escola.models import Matricula, Aluno, Curso
from django.urls import reverse

class MatriculasTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Matriculas-list')
        self.aluno = Aluno.objects.create(
            nome='João',
            rg='9999999',
            cpf='99999999999',
            data_nascimento='2000-05-10'
        ),
        self.curso = Curso.objects.create(
            codigo_curso='CTT1',
            descricao='Curso Teste 1',
            nivel='B'
        )
        self.matricula = Matricula.objects.create(
		    periodo="M",
		    aluno=Aluno.objects.get(id=1),
		    curso=Curso.objects.get(id=1)
        )

    def test_requisicao_get_para_listar_matriculas(self):
        """Teste para verificar a requisição GET para listar as matrículas"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_requisicao_post_para_criar_matricula(self):
        """Teste para verificar a requisição POST para criar uma matrícula"""
        data = {
            "id": 2,
            "periodo": "M",
            "aluno": 1,
            "curso": 1
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, 201)

    def test_requisicao_para_dar_method_not_allowed_para_deletar_matricula(self):
        """Teste para verificar a requisição DELETE para deletar uma matrícula"""
        response = self.client.delete('/matriculas/1/')
        self.assertEquals(response.status_code, 405)

    def test_requisicao_para_atualizar_matricula(self):
        """Teste para verificar a requisição PUT para atualizar uma matrícula"""
        data = {
            "id": 1,
            "periodo": "V",
            "aluno": 1,
            "curso": 1
        }
        response = self.client.put('/matriculas/1/', data=data)
        self.assertEquals(response.status_code, 200)
