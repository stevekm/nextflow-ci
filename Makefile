SHELL:=/bin/bash
export NXF_ANSI_LOG=false
export NXF_WORK=nxf/work
NXF_LOG:=nxf/.nextflow.log
ABSDIR:=$(shell python -c 'import os; print(os.path.realpath("."))')
UNAME:=$(shell uname)
export PATH:=$(CURDIR)/conda/bin:$(PATH)
unexport PYTHONPATH
unexport PYTHONHOME

ifeq ($(UNAME), Darwin)
CONDASH:=Miniconda3-4.5.4-MacOSX-x86_64.sh
endif

ifeq ($(UNAME), Linux)
CONDASH:=Miniconda3-4.5.4-Linux-x86_64.sh
endif

CONDAURL:=https://repo.continuum.io/miniconda/$(CONDASH)

conda:
	@echo ">>> Setting up conda..."
	wget "$(CONDAURL)" && \
	bash "$(CONDASH)" -b -p conda && \
	rm -f "$(CONDASH)"

conda-install: conda
	conda install -y -c bioconda \
	python=3.6.7 \
	conda=4.5.4 \
    samtools=1.9  \
	nextflow=19.07.0

run:
	python nextflow.py
# nextflow -log "$(NXF_LOG)" run main.nf

test:
	python test.py
# python -c 'import test_nextflow'

flagstat: output/Sample1.bam.txt
	python bin/flagstat.py output/Sample1.bam.txt

bash:
	bash
