"""
This microservice receives a city name and returns a JSON object of weather data
associated with that city. The JSON object can then be manipulated in the 
client program. This microservice requires a private API key for the openweathermap
API. A key is provided but it is requested that the user of this service not exceed 
100,000 API requests per day in order to not incur cost. 

This microservice uses the ZeroMQ library as a communication pipeline to the 
main program, and the requests library as a communication pipeline to the 
openweathermap API. 
"""



import requests 
import zmq


api_key = "34ca324945ebeca01725d6efefc7be43"
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://localhost:5555")

def main():
    while True:
        message = socket.recv_string()
        data = getWeatherInfo(message)

        print("Responding...")
        socket.send_pyobj(data)

def getWeatherInfo(city):
    """
    This function queries the openweathermap API for weather information. 

    : param: city - a string received from the client requesting this microservice
                and used to query the API

    : return : JSON object containing weather data for the requested location. 
    """
    city = city
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'imperial'
    }
    response = requests.get(base_url, params=params)
    return response.json()


if __name__ == "__main__":
    main()