import json
import pandas as pd
import sys

if('win' in sys.platform):
    ROOT_PATH = "D:\\KnowledgeGraph\\Academic-Family-Knowledge-Graph/"
    DATA_PATH = "D:\\KnowledgeGraph\\Academic-Family-Knowledge-Graph/data/"
    STATIC_DATA_PATH = "D:\\KnowledgeGraph\\Academic-Family-Knowledge-Graph/static/"
else:
    ROOT_PATH = "/home/liuxk/KG/Academic-Family-Knowledge-Graph/"
    DATA_PATH = "/home/liuxk/KG/Academic-Family-Knowledge-Graph/data/"
    STATIC_DATA_PATH = "/home/liuxk/KG/Academic-Family-Knowledge-Graph/static/"


data = pd.read_csv(DATA_PATH+'AKG.csv')

#%% process the Node
node_set = set()
link_set = set()

for i in range(len(data)):
    node_set.add(data.iloc[i, 0].strip())
    node_set.add(data.iloc[i, 1].strip())

print(node_set)
node_list = list(node_set)
node_list = sorted(list(node_set), key=lambda i: i[0])

node_dict = dict()
node_dict_rev = dict()

for i in range(len(node_list)):
    node_dict.update({node_list[i]:i})
    node_dict_rev.update({i: node_list[i]})

print(node_dict)

rel_list = []

for i in range(len(data)):
    e_1 = data.iloc[i, 0].strip()
    e_2 = data.iloc[i, 1].strip()

    e_1_idx = node_dict.get(e_1)
    e_2_idx = node_dict.get(e_2)
    rel = data.iloc[i, 2].strip()
    rel_list.append({'source': e_1_idx, 'target': e_2_idx, 'value': rel})

# print(rel_list)

output_node_list = []
for i in range(len(node_dict)):
    output_node_list.append({'id': i, 'name': node_dict_rev.get(i)})

output_node = {"data": output_node_list, "links": rel_list}

output_node_jsonStr=json.dumps(output_node)
print(output_node_jsonStr)

with open(STATIC_DATA_PATH+'data-aka.json', 'wt') as f:
    print(output_node_jsonStr, file=f)
