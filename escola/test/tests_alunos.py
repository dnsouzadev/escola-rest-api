from rest_framework.test import APITestCase
from escola.models import Aluno
from django.urls import reverse

class AlunosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Alunos-list')
        self.aluno_1 = Aluno.objects.create(
            nome='João',
            rg='999999934',
            cpf='99999999999',
            data_nascimento='2000-05-10'
        )
        self.aluno_2 = Aluno.objects.create(
            nome='Maria',
            rg='888888832',
            cpf='88888888888',
            data_nascimento='1990-10-05'
        )

    def test_requisicao_get_para_listar_alunos(self):
        """Teste para verificar a requisição GET para listar os alunos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

    def test_requisicao_post_para_criar_aluno(self):
        """Teste para verificar a requisição POST para criar um aluno"""
        data = {
            'nome': 'José',
            'rg': '7777777',
            'cpf': '77777777777',
            'data_nascimento': '1980-03-20'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, 201)

    def test_requisicao_delete_para_deletar_aluno(self):
        """Teste para verificar a requisição DELETE para deletar um aluno"""
        response = self.client.delete('/alunos/1/')
        self.assertEquals(response.status_code, 204)

    def test_requisicao_put_para_atualizar_aluno(self):
        """Teste para verificar a requisição PUT para atualizar um aluno"""
        data = {
            'nome': 'João',
            'rg': '9999999',
            'cpf': '99999999999',
            'data_nascimento': '2000-05-10'
        }
        response = self.client.put('/alunos/1/', data=data)
        self.aluno_1.refresh_from_db()
        self.assertEquals(self.aluno_1.nome, 'João')
