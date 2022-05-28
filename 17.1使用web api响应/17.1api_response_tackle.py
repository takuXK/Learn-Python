#17.1
#调用Web API使网站返回特定格式（json,csv等）的信息
import requests
#api需调用的url
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)  #get方法进行调用，将响应对象存储在变量r中
print("Status code:",r.status_code)  #r包含一个称为status_code的属性，用以核实调用是否成功（200为成功）
response_dict = r.json()  #以字典形式存储信息
#访问total_count属性，返回GitHub共包含多少python项目
print("Total repositories:",response_dict['total_count'])
#items属性是一个列表，包含很多字典，每个字典包含一个python项目的信息
repo_dicts = response_dict['items']
print("Repositories returned:",len(repo_dicts))
#打印各项目的信息
for repo_dict in repo_dicts:
    print("\nSelected imformation about first repository:")
    print('Name:',repo_dict['name'])
    print('Owner:',repo_dict['owner']['login'])
    print('Stars:',repo_dict['stargazers_count'])
    print('Repository:',repo_dict['html_url'])
    print('Created:',repo_dict['created_at'])
    print('Updated:',repo_dict['updated_at'])
    print('Description:',repo_dict['description'])

#监视api限制的速率限制
url1 = 'http://api.github.com/rate_limit'
info = requests.get(url1)
info_dict = info.json()
print("Search limit:",info_dict['resources']['search']['limit'])