import networkx as nx
import matplotlib.pyplot as plt
#绘制无向图
#创建图框
G = nx.Graph()
H = nx.Graph()
#添加结点
G.add_node(1)  #添加单个结点，结点名任意，除了bool值
G.add_nodes_from([2,3])  #添加多个结点，参数可以是数组、字典、range
G.add_nodes_from(range(4,7))
H.add_node(7)
G.add_nodes_from(H)  #从H图中导入结点
#添加连接
G.add_edge(1,2)  #添加单个连接
G.add_edge(1,1)
G.add_edges_from([(2,3),(3,6),(4,6),(5,6)])  #添加多个连接，参数为[tuple]形式
H.add_edges_from([(4,7),(5,7),(6,7)])
G.add_edges_from(H.edges())  #将H中的连接导入G中
#作图
nx.draw_networkx(G)
plt.show()

#绘制有向图
#创建图框
G = nx.DiGraph()
#添加结点
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(range(4,6))
nx.add_path(G,[6,7,8])  #add_path将直接添加结点并依次连接
#添加有向连接
G.add_edge(1,2)
G.add_edges_from([(1,4),(4,5),(2,3),(3,6),(5,6)])
#其他参数
colors = list('rggggmmr')
labels = {
    1:'start',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'end'
}
size = [800,300,300,300,300,600,300,800]
nx.draw_networkx(G,node_color=colors,node_shape='D',
    with_labels=True,labels=labels,
    node_size = size
    )
plt.show()
G.to_directed()  #有向图转换为无向图
nx.draw_networkx(G)
plt.show()