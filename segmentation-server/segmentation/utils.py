import random

def get_segments(image_id):
    data = []
    points_num = random.randrange(3, 4)
    polygons_num = random.randrange(1, 2)
    for index, type in enumerate(('a', 'b', 'c')):
        data.append({'polygons': [], 'type': type, 'image': image_id})
        for i in range(polygons_num):
            data[index]['polygons'].append({'points': []})
            for j in range(points_num):
                x = random.randrange(10000, 60000)
                y = random.randrange(10000, 90000)
                data[index]['polygons'][i]['points'].append({'x': x, 'y': y})
    return data


# Объект request POST запроса, тут я формирую такой же, чтобы в сериализатор засунуть
# data = [
#     {'polygons': [{'points': [{'x': 0, 'y': 0}, {'x': 1, 'y': 1}]}], 'type': 'c'}, 
#     {'polygons': [{'points': [{'x': 2, 'y': 3}, {'x': 6, 'y': 8}]}], 'type': 'a'}
# ]