# -*- coding: utf-8 -*-

# $Id:$


import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from ..django_model_factory import DjangoFactory
from arv.factory.api import Gen, lazy
from tests.models import PersonModel, PetModel


class TestDjangoFactory(TestCase):

    def setUp(self):
        class PetFactory(DjangoFactory):
            defaults = {
                "name": lazy(Gen, ["rocky", "tobby", "bailey", "max"]),
            }
            constructor = PetModel

        class PersonFactory(DjangoFactory):
            defaults = {
                "name": lazy(Gen, ["bob", "alice", "ann"]),
                "pet": PetFactory,
            }
            constructor = PersonModel

        self.PetFactory = PetFactory
        self.PersonFactory = PersonFactory
        self.pet_factory = PetFactory()
        self.person_factory = PersonFactory()

    def test_object_gets_persisted(self):
        self.assertFalse(PetModel.objects.exists())
        pet = self.pet_factory.make()
        self.assertEqual(PetModel.objects.count(), 1)
        new_pet = PetModel.objects.all()[0]
        self.assertEqual(pet.id, new_pet.id)
        self.assertEqual(pet.name, new_pet.name)

    def test_subobject_gets_persisted(self):
        self.assertFalse(PersonModel.objects.exists())
        self.assertFalse(PetModel.objects.exists())

        person = self.person_factory.make()

        self.assertEqual(PersonModel.objects.count(), 1)
        new_person = PersonModel.objects.all()[0]
        self.assertEqual(person.id, new_person.id)
        self.assertEqual(person.name, new_person.name)

        self.assertEqual(PetModel.objects.count(), 1)
        new_pet = PetModel.objects.all()[0]
        self.assertEqual(person.pet.id, new_pet.id)
        self.assertEqual(person.pet.name, new_pet.name)

    def test_m2m_bug(self):
        class UserFactory(DjangoFactory):
            defaults = {
                "username": "username",
                "first_name": "first",
                "last_name": "last",
                "email": "username@example.com",
                "is_staff": False,
                "is_active": True,
                "date_joined": datetime.date.today(),
            }
            constructor = User
        factory = UserFactory()
        factory.make()
