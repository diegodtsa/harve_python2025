import pandas as pd
import pandas_gbq

query = """
SELECT * FROM first-vigil-440513-q0.aulasql.fifanova
WHERE potencial > 80
"""

df_jogadores = pandas_gbq.read_gbq(query, project_id='first-vigil-440513-q0')
print(df_jogadores.head())