#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module to run a Nextflow pipeline and get output
"""
import os
import subprocess

ABSDIR = os.path.realpath(".")

# location for execution of pipeline
NXF_DIR = os.path.join(ABSDIR, "nxf")

# nextflow script to execute
NXF_SCRIPT = os.path.join(ABSDIR, "main.nf")

# main pipeline output log file
NXF_LOG = os.path.join(NXF_DIR, ".nextflow.log")

NXF_WORK = os.path.join(NXF_DIR, "work")

NXF_OUTPUT = os.path.join(ABSDIR, "output")

NXF_INPUT = os.path.join(ABSDIR, "input")

# env variables
NXF_ANSI_LOG = 'false'

env = {
'NXF_ANSI_LOG': NXF_ANSI_LOG,
'NXF_WORK': NXF_WORK,
}

config = {
'NXF_DIR': NXF_DIR,
'NXF_SCRIPT': NXF_SCRIPT,
'NXF_LOG': NXF_LOG,
'NXF_OUTPUT': NXF_OUTPUT,
'NXF_INPUT': NXF_INPUT
}

class Nextflow(object):
    """
    Object class to configure and run a Nextflow pipeline
    """
    def __init__(self, config, env = env):
        self.config = config
        self.env = env

    def set_command(self):
        """
        CLI command to run
        """
        nxf_command = [
        'nextflow',
        '-log', self.config['NXF_LOG'],
        'run', self.config['NXF_SCRIPT'],
        '--outputDir', self.config['NXF_OUTPUT'],
        '--inputDir', self.config['NXF_INPUT']
        ]
        self.command = nxf_command

    def get_process(self, command):
        """
        Create Python subprocess object to run the CLI command
        """
        process = subprocess.Popen(command,
            env = dict(os.environ,
                NXF_ANSI_LOG = self.env['NXF_ANSI_LOG'],
                NXF_WORK = self.env['NXF_WORK']
                ), 
            universal_newlines = True,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE)
        return(process)

    def run(self):
        """
        Generate CLI command based on config and run it in Python subprocess
        """
        self.set_command()
        process = self.get_process(self.command)
        proc_stdout, proc_stderr = process.communicate()
        self.returncode = process.returncode
        self.stdout = proc_stdout
        self.stderr = proc_stderr

def main():
    """
    Example of how to run Nextflow from Python script
    """
    n = Nextflow(config = config)
    n.run()
    print(n.returncode)
    print(n.stdout)
    print(n.stderr)

if __name__ == '__main__':
    main()
