# contig_taxonomy
Pipeline for taxonomic assignment of contigs using mmseq2 taxonomy 

## Installation ##
Dowload the pipeline using the command:
        
        git clone https://github.com/lfdelzam/contig_taxonomy.git

The pipeline uses the programs:

[snakemake](https://snakemake.github.io) 6.4.1

[mmseqs2](https://github.com/soedinglab/MMseqs2/releases/tag/13-45111) v13-45111


## Create conda environment ##

conda create -n MMSEQS2 -c conda-forge -c bioconda mmseqs2=13.45111 snakemake=6.4.1

## GTDB ###

To download GTDB use the following commands::


        cd contig_taxonomy
        mkdir GTDB_aa_db
        cd GTDB_aa_db/
        wget https://data.gtdb.ecogenomic.org/releases/latest/genomic_files_reps/gtdb_proteins_aa_reps.tar.gz
        wget -A _taxonomy.tsv -r -l 1 -nd https://data.gtdb.ecogenomic.org/releases/latest/
        cd ..

## Usage ##

set pipeline parameters in contigs_taxonomy_config.json using the command:

    nano contigs_taxonomy_config.json
  
and modify the parameters and save changes by taping `ctrl x` and tape `y`:

          "workdir": "/abs/path/to/contig_taxonomy",
          "threads": 20,
          "GTDB_dir": "/abs/path/to/contig_taxonomy/GTDB_aa_db/protein_faa_reps", -- required if GTDB used --
          "bact_tsv": "/abs/path/to/contig_taxonomy/GTDB_aa_db/bac120_taxonomy.tsv", -- required if GTDB used --
          "arch_tsv": "/abs/path/to/contig_taxonomy/GTDB_aa_db/ar122_taxonomy.tsv", -- required if GTDB used --
          "database": "/root/contig_taxonomy/<your option>", -- name of the file containing the GTDB database converted to mmseqs2 format --
          "DB_type": "your option", -- options "gtdb", "uniprot" --
          "uniprot_db_type": "your option", -- Uniprot DB to be used, e.g., "UniProtKB/Swiss-Prot" --
          "database_uniprot_name": "your option name", -- name of file, e.g, swissprot
          "DB_uniprot_option_name": "your selection", -- used when a subset of uniprot DB is used, e.g., "only_Virus", "Only_Euka"
          "DB_uniprot_option_parameter": "your selection", -- used when a subset of uniprot DB is used, e.g., "--taxon-list 2759" when using only Eukaryotic sequences
          "contigs": "/abs/path/to/contigs.fna",
          "mmseqs_taxonomy_params": "your options", e.g, "--orf-filter 0 --tax-lineage 1" when using Uniprot, or "--blacklist '' --orf-filter 0 --tax-lineage 1 --tax-lineage 1" when using GTDB, 
          "easy_taxo":"False",
          "temporary_directory": "/abs/path/to/<your option>",
          "params_tax_report_html": "--report-mode 1",
          "output_dir": "abs/path/to/your_option"

 
 Activate environemnt and run the pipeline with the commands:
        
                conda activate MMSEQS2
                snakemake -s snakefile_contigs_taxonomy --cores <your option>
        
