#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import os
import shutil
import nextflow
import unittest
import subprocess
import tempfile
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
        # get the base config and env from the module
        cls.config = nextflow.config
        cls.env = nextflow.env
        # create temporary directory to run the pipeline in
        tmp_output_dir = tempfile.mkdtemp()
        # update the configs to use the new temp dir for output items
        cls.config['NXF_OUTPUT'] = os.path.join(tmp_output_dir, "output")
        cls.config['NXF_LOG'] = os.path.join(tmp_output_dir, ".nextflow.log")
        cls.env['NXF_WORK'] = os.path.join(tmp_output_dir, 'work')
        cls.demo_output1 = os.path.join(cls.config['NXF_OUTPUT'], 'Sample1.bam.txt')
        cls.demo_output2 = os.path.join(cls.config['NXF_OUTPUT'], 'Sample2.bam.txt')
        cls.pipeline = nextflow.Nextflow(config = cls.config, env = cls.env)
        cls.pipeline.run()
        # print to console to show log and completion during testing
        print(cls.pipeline.stdout)
        print(cls.pipeline.stderr)

    @classmethod
    def tearDownClass(cls):
        """
        Clean up for Nextflow pipeline
        """
        os.remove(cls.config['NXF_LOG'])
        shutil.rmtree(cls.env['NXF_WORK'])
        shutil.rmtree(cls.config['NXF_OUTPUT'])

    def test_true(self):
        self.assertTrue(True, 'Demo assertion')

    def test_returncode(self):
        """
        Test that the pipeline finished with exit status of 0 (success)
        """
        self.assertTrue(self.pipeline.returncode == 0, 'Non-zero exit code')

    def test_pipeline_output(self):
        """
        Test that the expected output items exist after pipeline completion
        """
        self.assertTrue(os.path.exists(self.config['NXF_OUTPUT']), 'Nextflow output directory does not exist')
        self.assertTrue(os.path.exists(self.demo_output1))
        self.assertTrue(os.path.exists(self.demo_output2))

    def test_sample1_vals(self):
        """
        Test that the values of analysis for sample 1 match expected values
        """
        f = flagstat.Flagstat(txt = self.demo_output1)
        self.assertTrue(f.vals['TotalMappedReads'] == 6922, 'Total mapped reads do not match expected value')
        self.assertTrue(f.vals['SequencedPairedReads'] == 6906, 'Number of Sequenced Paired Reads do not match expected value')
        self.assertTrue(f.vals['ProperlyPairedReads'] == 6896, 'Number of Properly Paired Reads do not match expected value')
        self.assertTrue(f.vals['ProperlyPairedPcnt'] == 0.9985519837822183, 'Properly Paired Reads Percent do not match expected value')
