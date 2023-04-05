from Dbase import DEncode, DDecode
from ast import literal_eval
data = {}

money = 12345
items = {
    'sword': {
        'amount': 1,
        'type': 'item'
    },
    'water': {
        'amount': 1,
        'type': 'item'
    },
    'testitem': {
        'amount': 1,
        'type': 'testitem'
    }
}

data["money"] = money
data["items"] = items

print(data)
print('-'*20)



def read(file):
    with open(file, 'r') as f:
        x = f.read()
    f.close()
    print(f'READ DATA: {x}')
    return x

def save(data):
    data = DEncode(data,20)
    print(f'Encoded data: {data}')
    with open('save.py', 'w') as f:
        f.write(f'{data}')
    f.close()
    print('Written to file')

save(data)

x = read('save.py')
x = DDecode(x)
print(x)
x = literal_eval(x)
print(x)
print('-'*20)
print(f'Passed money: {money}')
print(x['money'])
print(x['items']['sword']['amount'])