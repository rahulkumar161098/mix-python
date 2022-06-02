def bubble_sort(element):
    for i in range(len(element)):
        for j in range( len(element)-i-1):
            # filter by transaction_amount 
            if element[j]['transaction_amount'] > element[j+1]['transaction_amount']:
                temp= element[j]
                element[j]= element[j+1]
                element[j+1]= temp




# element=[3,9,8,6,4,1,76,34,12]


element = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
bubble_sort(element)
print('Bubble sorting.........................')
print(element)