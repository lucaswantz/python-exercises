# Erro
print('Chris' + 2)
# Correto
print('Chris' + str(2))


# O Python possui um método interno para formatação conveniente de strings.
sales_record = {
    'price': 3.24,
    'num_items': 4,
    'person': 'Chris'}

# Definição da string com placeholders
sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

# print com formatação de string e substituição dos itens a partir do dicionário
print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))
