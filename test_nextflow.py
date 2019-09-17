#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import os
import shutil
import nextflow
import unittest
import subprocess
from bin import flagstat

class TestPipeline(unittest.TestCase):
    # def setUp(self):
    # """
    # normally the setup commands would go here but they get run for every test
    # """

    @classmethod
    def setUpClass(cls):
        """
        setUp class for the tests; this will only execute once and will be available for
        the tests to access the results
        """
        super(TestPipeline, cls).setUpClass()
        cls.process = nextflow.nxf_process
        proc_stdout, proc_stderr = cls.process.communicate()
        cls.returncode = cls.process.returncode
        cls.proc_stdout = proc_stdout
        cls.proc_stderr = proc_stderr

    @classmethod
    def tearDownClass(cls):
        """
        Clean up for Nextflow pipeline
        """
        os.remove(nextflow.NXF_LOG)
        shutil.rmtree(nextflow.NXF_WORK)
        shutil.rmtree(nextflow.NXF_OUTPUT)

    def test_true(self):
        self.assertTrue(True, 'Demo assertion')

    def test_returncode(self):
        self.assertTrue(self.returncode == 0, 'Non-zero exit code')
