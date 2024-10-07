import requests
api_key = 'b5d27bc0587944bba5753736240610'  
city = input('Enter city name: ')
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()  
    temp = data['current']['temp_c'] 
    desc = data['current']['condition']['text']  
    print(f'Temperature: {temp} °C')  
    print(f'Description: {desc}')  
else:
    print('Error fetching weather data:', response.status_code) 

