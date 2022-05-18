from django.test import TestCase, RequestFactory
from animais.models import Animal

class ModelsTest(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'
        )
        self.factory = RequestFactory()
    
    def test_existencia(self):
        
        self.assertEqual(self.animal.nome_animal, 'Leão')