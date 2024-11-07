import pandas as pd
from datetime import datetime

excel_path = 'C:/Users/55199/Desktop/EXERCICES/UNISIM/excel/dados.xlsx'
df = pd.read_excel(excel_path)

output_path = 'C:/Users/55199/Desktop/EXERCICES/UNISIM/excel/dados_formatados.txt'
# abrindo o arquivo de saída para escrita
with open(output_path, 'w') as file:
    # iterando sobre cada linha
    for _, row in df.iterrows():
        date = pd.to_datetime(row['DATE']).date()
        file.write(f"DATE {date.year} {date.month} {date.day}.00000\n")
        # iterando sobre cada coluna de produtor, ignorando a coluna DATE 
        for producer, value in row.items():
            if producer != 'DATE' and pd.notna(value):  
                producer_name = producer.strip("'")  
                file.write(f"PRODUCER '{producer_name}'\n")
                file.write(f"OPERATE  MAX  STO  {value}  CONT\n")
                file.write(f"OPERATE  MIN  BHP  36.0  CONT\n")

print(f"Le fichier a été généré avec succès: {output_path}")
