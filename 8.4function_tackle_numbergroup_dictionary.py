#8.4
#函数的形参在实际输入时，可以是一个值也可以是一个数组
def print_models(unprinted_models,completed_models):
    while unprinted_models:
        current_model = unprinted_models.pop()
        print('printing model:' + current_model)
        completed_models.append(current_model)
        print('\nThe following models have been completed:')
        for model in completed_models:
            print(model)
        print('\n')
unprinted_models = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_models[:],completed_models)  #切片表示法[:]可保持一个列表不被修改
print(unprinted_models)