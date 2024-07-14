import pandas as pd
data = {
    'Name': ['Sudeepa', 'Madhu', 'Niharika'],
    'Age': [28, 22, 25],
    'City': ['Chirala', 'Vizag', 'Pune']
}
df = pd.DataFrame(data)
city = df['City']
print(city)
