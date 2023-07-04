import requests
import os
from datetime import datetime
import pytz

# Definición de la clase WeatherClient
class WeatherClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self):
        # Limpia la consola
        os.system("clear")

        # Lista de algunas ciudades que puedes consultar con la API OPenWeather
        cities = ["London", "Paris", "Tokyo", "New York", "Berlin", "Rome", "Sydney", "Moscow", "Dubai", "Toronto",
          "Madrid", "Seoul", "Cairo", "Mumbai", "Rio de Janeiro", "Buenos Aires", "Cape Town", "Amsterdam",
          "Bangkok", "Stockholm", "Athens", "Lima", "Havana", "Beijing", "Riyadh", "Prague", "Vienna", "Lisbon",
          "Budapest", "Kuala Lumpur", "Mexico City", "Oslo", "Warsaw", "Helsinki", "Johannesburg", "Copenhagen",
          "Dublin", "Wellington", "Brussels", "Brasilia", "Singapore", "Jakarta", "Hanoi", "Santiago", "Nairobi",
          "Manila", "Reykjavik", "Helsinki", "Montreal", "Managua"]
        
        # Imprime la lista de ciudades 
        print("\n \t \t Algunas de las ciudades que puedes consultar en nuestra API con OpenWeather")
        print("========================================================================================================================")
        for i, city in enumerate(cities):
            print(f"{i+1:2}. {city:<15}", end="\t" if (i+1) % 5 != 0 else "\n")

        print("\n")
        
        # Solicita al usuario ingresar el nombre de la ciudad
        location = input("~> Ingrese el nombre de la ciudad: ")
        
        # Construye la URL de la API para obtener el clima de la ciudad especificada
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}"

        try:
            # Realiza la solicitud GET a la API para extraer los datos en formato json
            response = requests.get(url)
            
            # Obtiene los datos de clima en formato JSON
            weather_data = response.json()
            
            # Verifica si la respuesta fue exitosa (código de estado 200) y los datos de clima tienen código 200
            if response.status_code == 200 and weather_data.get('cod') == 200:
                # Extrae la temperatura en grados Celsius
                temperature_celsius = weather_data['main']['temp'] - 273.15
                
                # Convierte las horas de amanecer y atardecer a la zona horaria de América/Managua
                sunrise_utc = datetime.utcfromtimestamp(weather_data['sys']['sunrise'])
                sunset_utc = datetime.utcfromtimestamp(weather_data['sys']['sunset'])
                tz = pytz.timezone('America/Managua')
                sunrise_local = sunrise_utc.replace(tzinfo=pytz.utc).astimezone(tz)
                sunset_local = sunset_utc.replace(tzinfo=pytz.utc).astimezone(tz)
                
                # Extrae el país y la descripción del clima
                country = weather_data['sys']['country']
                description = weather_data['weather'][0]['description']
                
                # Imprime los datos del clima de la ciudad
                print(f"\n \nDatos del tiempo de la ciudad de {location}:")
                print("================================================")
                print(f"Zona horaria: {weather_data['timezone']}")
                print(f"ID de la ciudad: {weather_data['id']}")
                print(f"Nombre de la ciudad: {weather_data['name']}")
                print(f"País: {country}")
                print(f"Descripción del clima: {description}")
                print(f"Temperatura: {temperature_celsius:.2f} °C")
                print(f"Humedad: {weather_data['main']['humidity']} %")
                print(f"Presión: {weather_data['main']['pressure']} hPa")
                print(f"Visibilidad: {weather_data['visibility']} meters")
                print(f"Velocidad del viento: {weather_data['wind']['speed']} m/s")
                print(f"Cobertura de nubes: {weather_data['clouds']['all']} %")
                print(f"Amanecer: {sunrise_local.strftime('%Y-%m-%d %H:%M:%S')} horario local")
                print(f"Atardecer: {sunset_local.strftime('%Y-%m-%d %H:%M:%S')} horario local")
                
                # Devuelve los datos del clima
                return weather_data

        # Captura excepciones relacionadas con la solicitud o datos faltantes
        except (requests.exceptions.RequestException, KeyError):
            pass

        # Imprime un mensaje indicando que la ciudad no existe
        print("La ciudad no existe")
