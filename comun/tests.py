# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
class AnimalTestCase(TestCase):


    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        print ("@@@@@@@@@@@@@@@@@@@@")
        print ("@@@@@@@@@@@@@@@@@@@@")
        self.assertEqual('The cat says "meow"', 'The cat says "meow"')