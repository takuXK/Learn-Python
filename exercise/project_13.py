#实现可迭代对象和迭代器对象(Iterable&Iterator)
from collections.abc import Iterable,Iterator
#数组、字典、字符串均为可迭代对象，它们都拥有__iter__()方法
l = list(range(1,6))
print(isinstance(l,Iterable))
print(issubclass(list,Iterable))
print(issubclass(str,Iterable))
print(issubclass(dict,Iterable))
print(issubclass(int,Iterable))
#iter()函数将返回一个迭代器对象，其本质使用了__iter__()方法，注意每次生成的迭代器对象是不同的
it1 = iter(l)  #迭代器对象也是可迭代对象
it2 = l.__iter__()
print(isinstance(it1,Iterable))
print(it1)
print(it2)
print(next(it1))  #迭代器对象拥有next函数，可以逐一提取迭代器对象元素
print(it1.__next__())  #next函数实质使用了__next__()方法
print(list(it1))  #迭代器对象是一次性的，提取/使用以后元素便从迭代器对象里消失
print(list(it1))
print(list(it2))  #同一可迭代对象生成的迭代器对象是独立的

#依次访问读取城市信息并显示
import requests
city = '北京'
url = 'http://wthrcdn.etouch.cn//weather_mini?city=' + city
response = requests.get(url)  
response_dict = response.json()  #返回字典形式信息
print(response_dict)

#自建迭代器对象WeatherIterator和可迭代对象WeatherIterable
class WeatherIterator(Iterator):  #类产生可操作迭代器对象
    def __init__(self,cities):
        self.cities = cities
        self.index = 0  #便于__next__判断后续是否还存在城市可访问
    def get_weather_temp(self,city):
        url =  'http://wthrcdn.etouch.cn//weather_mini?city=' + city
        response = requests.get(url)
        temp_data = response.json()['data']['forecast'][0]
        return (city,temp_data['high'],temp_data['low'])
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration  #raise返回错误，后面不再执行
        else:
            self.cities[self.index]
            self.index += 1
            return self.get_weather_temp(city)

class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities
    def __iter__(self):
        return WeatherIterator(self.cities)  #创建迭代器对象

def show_cities_temp(cities_Iterator):
    for city_info in cities_Iterator:
        print(city_info)

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
for city in city_list:
    response_city = WeatherIterable(city)
    show_cities_temp(response_city)