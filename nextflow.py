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

config = {
'NXF_DIR': NXF_DIR,
'NXF_SCRIPT': NXF_SCRIPT,
'NXF_LOG': NXF_LOG
}

# env variables
NXF_ANSI_LOG = 'false'

env = {
'NXF_ANSI_LOG': NXF_ANSI_LOG
}

def main():
    nxf_command = [
    'nextflow',
    '-log',
    config['NXF_LOG'],
    'run',
    config['NXF_SCRIPT'],
    ]

    process = subprocess.Popen(nxf_command, env = dict(os.environ, NXF_ANSI_LOG = env['NXF_ANSI_LOG']), universal_newlines = True)
    proc_stdout, proc_stderr = process.communicate()
    print(proc_stdout)
    print(proc_stderr)

if __name__ == '__main__':
    main()
