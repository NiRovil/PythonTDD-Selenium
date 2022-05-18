from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal

class IndexViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal = 'Cachorro',
            predador = 'Não',
            venenoso = 'Não',
            domestico = 'Sim'
        )

    def test_index(self):
        response = self.client.get('/', {'buscar':'Cachorro'})
        caracteristica = response.context['caracteristicas']
        self.assertIs(type(response.context['caracteristicas']), QuerySet)
        self.assertEqual(caracteristica[0].nome_animal, 'Cachorro')
