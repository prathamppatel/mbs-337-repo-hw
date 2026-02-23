FROM python:3.12
RUN pip3 install biopython pydantic
COPY fasta_filter.py /code/fasta_filter.py
COPY fasta_stats.py /code/fasta_stats.py
COPY fastq_filter.py /code/fastq_filter.py
COPY mmcif_summary.py /code/mmcif_summary.py

COPY immune_proteins.fasta /code/immune_proteins.fasta
COPY sample1_rawReads.fastq /code/sample1_rawReads.fastq
COPY 4HHB.cif /code/4HHB.cif

RUN chmod ugo+x /code/fasta_stats.py
RUN chmod ugo+x /code/fastq_filter.py
RUN chmod ugo+x /code/fasta_filter.py
RUN chmod ugo+x /code/mmcif_summary.py

ENV PATH="/code:$PATH"