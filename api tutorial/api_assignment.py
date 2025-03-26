import requests
import pandas as pd

url = "https://premier-league18.p.rapidapi.com/players/topAssisters"

headers = {
	"x-rapidapi-key": "f082045560mshef7eba822486d96p12b590jsn8b70b6a0b449",
	"x-rapidapi-host": "premier-league18.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

if response.status_code == 200: 
    data = response.json()
    df = pd.DataFrame(data)  
    print(df) 
else:
    print(f"Error {response.status_code}: {response.text}")

