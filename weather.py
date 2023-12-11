import streamlit as st
import requests

API_KEY = "KEY"

def get_weather(city):
    API = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    data = requests.get(API).json()

    try:
        lat, lon = data['coord']['lat'], data['coord']['lon']
        main = data['weather'][0]['main']
        temp = round(data['main']['temp'] - 273.15, 2)  # Convert temperature to Celsius
        return main, temp, lat, lon
    except KeyError:
        return None, None, None, None


def get_air_quality(lat, lon):
    API = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    data = requests.get(API).json()
    aqi = data['list'][0]['main']['aqi']

    quality = {
        1: 'Good',
        2: 'Fair',
        3: 'Moderate',
        4: 'Poor',
        5: 'Very Poor'
    }
    return quality[aqi]


def main():
    st.title('Weather Application')
    city = st.text_input('Enter City name:', 'Delhi')

    if st.button('Get Weather'):
        main, temp, lat, lon = get_weather(city)
        if main and temp and lat and lon:
            st.write(f'**City:** {city.capitalize()}')
            st.write(f'**Weather:** {main}')
            st.write(f'**Temperature:** {temp}°C')

            air_quality = get_air_quality(lat, lon)
            st.write(f'**Air Quality:** {air_quality}')
        else:
            st.error('City not found. Please enter a valid city name.')


if __name__ == "__main__":
    main()
