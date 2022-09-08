from collections.abc import Iterable,Iterator
import requests
'''
class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities
    def __iter__(self):
        for city in self.cities:
            city_info = self.get_weather_temp(city)
            yield city_info
    def get_weather_temp(self,city):
        url =  'http://wthrcdn.etouch.cn//weather_mini?city=' + city
        response = requests.get(url)
        temp_data = response.json()['data']['forecast'][0]
        return (city,temp_data['high'],temp_data['low'])

city_list = [
        '北京',
        '上海',
        '广州',
        '深圳',
        '杭州',
        '南京',
        '西安',
        '武汉',
        '沈阳',
        '成都',
    ]
response_cities = WeatherIterable(city_list)
for response_city in response_cities:
    print(response_city)'''
import numpy as np
wire_ns_x = [343.42023183206777, 651.2202318320678, 1044.5404636641356, 1352.3404636641358, 
            1745.6606954962035, 2053.4606954962037, -118.27976816793222]
x = 0
conform_x = np.array([x_ele for x_ele in wire_ns_x if x_ele<x])
corres_x = -np.min(x-conform_x)+x
print(corres_x)