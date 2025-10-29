from datetime import datetime, timedelta

data_atual = datetime.now()

data_nova = data_atual - timedelta(days=90)

print(data_atual)

print(data_nova)