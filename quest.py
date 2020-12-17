# import random
# from data_maps import data_maps, maps_description1, maps_description2, maps_description3, maps_description4, \
#     maps_description5, maps_description6, maps_description7
#
# client_data = []
# character = input("Добро пожаловать в Новогодний квест! Как вас зовут?: ")
# client_data.append(character)
# location = input("Откуда вы к нам?: ")
# client_data.append(location)
# print("-------------------------------------------------------------")
# input('Отличные новости, ' + client_data[0] + '! Двери нашей резиденции откроются совсем скоро. '
#                                                     'Хотите посмотреть карту?:')
#
# input("К сожалению, волшебные двери неконтролируемо открываются каждый раз в новом месте. Открывайте! "
#             "Просто напишите слово (открыть)")
#
# random_maps = random.choice(data_maps)
#
# print("Вы попали в интересное место: " + random_maps)
# if random_maps == data_maps[0]:
#     print(maps_description1)
# elif random_maps == data_maps[1]:
#     print(maps_description2)
# elif random_maps == data_maps[2]:
#     print(maps_description3)
# elif random_maps == data_maps[3]:
#     print(maps_description4)
# elif random_maps == data_maps[4]:
#     print(maps_description5)
# elif random_maps == data_maps[5]:
#     print(maps_description6)
# elif random_maps == data_maps[6]:
#     print(maps_description7)
import networkx as nx
import json

with open('data.json', 'r') as f:
    data = json.load(f)

data_maps = data['data_maps']
edges_list = data['edges_list']

map_graph = nx.Graph()
map_graph.add_nodes_from(data_maps)
map_graph.add_edges_from(edges_list)

location = "Снежная площадь"
while True:
    if location == 'Выход':
        break
    print(f'Вы находитесь в локации {location}.')
    print('Можно пойти в:')
    for door_in in map_graph[location].keys():
        print(door_in)
    print('Для выхода введите "Выход"')
    location = input('Куда отправимся? ')
