from os import sep
from Bio.Blast.Applications import NcbiblastpCommandline
import pandas as pd
from Bio import SearchIO
from Bio import SeqIO
import numpy as np

comando = NcbiblastpCommandline(query = "Target.faa", subject = "DEG.faa", outfmt = 10, out = "out.csv", evalue = 0.000001)
stdout,stderr = comando()

abrir = pd.read_table("out.csv", sep = ",", names= ["IDs","b","c","d","e","f","g","h","i","j","coluna1","coluna2"])
dups1 = abrir.iloc[:,[0]]
dups2 = dups1.drop_duplicates(subset='IDs', keep="first")
dups2.to_csv('resultado.csv', header= None,
                  index = None)

import csv
csv_file = ('resultado.csv')
with open("DEGids.list", "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()
    



