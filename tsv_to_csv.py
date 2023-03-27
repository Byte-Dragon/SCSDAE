import pandas as pd
tsv_file='C:\\Users\\27170\\Desktop\\GCKT\\breast_dataset\\TCGA-BLCA.htseq_counts.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_file='C:\\Users\\27170\\Desktop\\GCKT\\breast_dataset\\TCGA-BLCA.htseq_counts.csv'
csv_table.to_csv(csv_file,index=False)