import pandas as pd
import pandas_gbq


query = """
SELECT * FROM first-vigil-440513-q0.aulasql.paises
"""

df_paises = pandas_gbq.read_gbq(query, project_id='first-vigil-440513-q0')

df_paises_novos = pd.DataFrame({
    "id":[24,25,26],
    "nome":['Estados unidos', 'Groelandia', 'Canadá'],
    "populacao":[339996563,56367,38929902],
    "codigo": ['US', 'GO','CA']
})

df_final = pd.concat([df_paises,df_paises_novos], ignore_index=True)

#print(df_final)


pandas_gbq.to_gbq(df_final,'python_ETL.paises_novos_diego', project_id= 'first-vigil-440513-q0', if_exists= 'replace')

