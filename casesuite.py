# -*- coding: UTF-8 -*-
import unittest
import ddt
import config
from pylog import Pylog
from prerequest import PreRequest
from predata import Predata

@ddt.ddt
class Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Pylog.debug("START")
        cls.req = PreRequest()
        # cls.req.login(name='admin')

    @classmethod
    def tearDownClass(cls):
        Pylog.debug("STOP")

    @ddt.data(*Predata().get_data())
    def test(self,data):
        self.req.request(data)
        self.assertEquals(self.req.reps.status_code,200)

