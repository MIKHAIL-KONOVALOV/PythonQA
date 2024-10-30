# country = {key : value}
country = {'code': 'ru', 'name': 'Russian', 'population': 144}
for element in country:
    print(element, ' = ', country[element])
workers = {
    'worker_1' : {
        'firstName' : 'Bob',
        'secondName' : 'Marley',
        'age' : 29,
        'adress' : ['Piter', 'st. Bolshoy', 87],
        'grades' : {'math': 5, 'physics' : 4, 'biology' : 2}
    },
    'worker_2' : {
        'firstName' : 'Kith',
        'secondName' : 'Flint',
        'age' : 33,
        'adress' : ['Usa', 'st. Orpheus', 87],
        'grades' : {'math': 3, 'physics' : 2, 'biology' : 17}
    }
}

print(workers['worker_2'].get('grades').get('biology'))