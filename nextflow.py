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

NXF_OUTPUT = os.path.join('.', "output")

NXF_INPUT = os.path.join('.', "input")

# config = {
# 'NXF_DIR': NXF_DIR,
# 'NXF_SCRIPT': NXF_SCRIPT,
# 'NXF_LOG': NXF_LOG,
# 'NXF_OUTPUT': NXF_OUTPUT
# }

# env variables
NXF_ANSI_LOG = 'false'

env = {
'NXF_ANSI_LOG': NXF_ANSI_LOG
}

# CLI command to run
nxf_command = [
'nextflow',
'-log', NXF_LOG,
'run', NXF_SCRIPT,
'--outputDir', NXF_OUTPUT,
'--inputDir', NXF_INPUT
]

# Python subprocess to run the CLI command
nxf_process = subprocess.Popen(nxf_command,
    env = dict(os.environ, NXF_ANSI_LOG = env['NXF_ANSI_LOG']),
    universal_newlines = True,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE)

def main():
    """
    Example of how to run Nextflow from Python script
    """
    proc_stdout, proc_stderr = nxf_process.communicate()
    print(nxf_process.returncode)
    print(proc_stdout)
    print(proc_stderr)

if __name__ == '__main__':
    main()
