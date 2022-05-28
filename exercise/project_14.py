#生成器函数和生成可迭代对象
from collections.abc import Iterable,Iterator
#生成器函数
def generator_fun():
    print('first')
    yield 1
    print('second')
    yield 2
    print('third')
    yield 3     
#对于带有yield的函数，一开始不运行而得到一个生成器对象，直到生成器实例调用了next()函数，该生成器函数才运行
#调用一次next()函数，生成器函数将停在yield 1处，第二次调用，生成器函数将停在yield 2处...
generator = generator_fun()
print(isinstance(generator,Iterator))  #generator_fun()是一个迭代器对象，那么一定是一个可迭代对象
print(iter(generator) is generator)  #生成的迭代器对象是其自身
print(next(generator))
print('\n')

#利用生成器函数寻找素数
class PrimeNumber(Iterable):
    def __init__(self,min,max):
        self.min = min
        self.max = max
    def __iter__(self):  #生成器函数
        for k in range(self.min,self.max+1):
            if self.is_Prime(k):
                yield k
    def is_Prime(self,k):
        if k < 2:
            return 0
        else:
            #all函数要求所有的判断为真才返回True，也就是所有2至k-1的x都不能使k%x==0
            return all(map(lambda x: k%x,range(2,k)))

primeNum = PrimeNumber(1,30)
for n in primeNum:
    print(n)


#天气爬取生成器函数版本#
from collections.abc import Iterable,Iterator
import requests

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
    print(response_city)