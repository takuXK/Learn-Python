#17.2
#利用pygal对api返回数据进行可视化
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#api响应及检测
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)
print("Status code:",response.status_code)
#存储api响应内容
response_dict = response.json()
#存储api响应内容中的项目信息
repo_dicts = response_dict['items']
#统计绘图数据
names,plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict ={
        'value':repo_dict['stargazers_count'],
        'label':repo_dict['description'],
        'xlink':repo_dict['html_url'],  #pygal会将'xlink'键相关联的值转化为链接
        }  #利用该形式能在图表中加上更多信息提示
    plot_dicts.append(plot_dict)
#可视化
my_style = LS('#333366',base_style=LCS)  #定义样式
#以下为my_config的属性
my_config = pygal.Config()  #创建Config实例，其中包含绘图所需的各项属性
my_config.x_label_rotation = 45  #x标签旋转45°
my_config.show_legend = False  #不显示图例
my_config.title_font_size = 24  #设置标题字符大小24
my_config.label_font_size = 14  #设置副标签字符大小（x轴和y轴上除5000的倍数的字符）14
my_config.major_label_font_size = 18  #设置主标签字符大小（y轴上5000的倍数的字符）18
my_config.truncate_label = 15  #truncate_label将较长的项目名缩减为15个字符
my_config.show_y_guides = False  #隐藏y轴基准线（水平线）
my_config.width = 1000  #定义柱状图的宽度为1000

chart = pygal.Bar(my_config,style=my_style)
chart._title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('',plot_dicts)
chart.render_to_file('python_repos4.svg')