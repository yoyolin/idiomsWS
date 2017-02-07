# -*- coding: utf-8 -*-
import pandas as pd
from models import *
from django.test import TestCase

MODELS = [Idioms]

class IdiomsTest(TestCase):
    def test_setUp(self):
        idioms = pd.read_csv("./static/idioms_with_levels.csv")
        print len(idioms.index)

        idioms_junior = idioms[idioms["level"] == 1]["idioms"]
        idioms_middle = idioms[idioms["level"] == 2]["idioms"]

        Idioms.objects.create(idiom=idioms_junior[0].replace("\r\n","").decode("utf-8-sig"),level=1)
        Idioms.objects.create(idiom=idioms_middle[0].replace("\r\n","").decode("utf-8-sig"),level=2)


    def test_read(self):
        idiom = Idioms.object.all()
        print idiom