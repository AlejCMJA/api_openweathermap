import pytest
from weather_client import WeatherClient

# Definición de la función de prueba "test_get_weather"
def test_get_weather():
    # Clave de la API para acceder a OpenWeatherMap
    api_key = "Poner tu API KEY AQUI"
    
    # Creación de una instancia del cliente WeatherClient
    client = WeatherClient(api_key)
    
    # Llamada al método get_weather para obtener los datos de clima
    weather_data = client.get_weather()
