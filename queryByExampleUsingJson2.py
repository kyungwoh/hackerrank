import json

def add(s):
    data.append([s,True])
    n = len(data)-1
    d = json.loads(s)
    addIndex(index, n, d, s)
    return

def addIndex(index, n, d, s):
    for k,v in d.items():
        if isinstance(v, dict):
            if not k in index: index[k] = {}
            addIndex(index[k], n, v, s)
        else:
            if not k in index: index[k] = []
            index[k].append([v,n])

def get(s):
    d = json.loads(s)
    rSet = find(index, d)
    ans = ""
    for i in rSet:
        if data[i][1]: ans += data[i][0]+"\n"
    return ans
    
def delete(s):
    d = json.loads(s)
    rSet = find(index, d)
    for i in rSet:
        if data[i][1]: data[i][1] = False
    
def find(index, d):
    rSet = set()
    for k,v in d.items():
        newSet = set()
        if k in index:
            if isinstance(v, dict): newSet = find(index[k], v)
            elif isinstance(v, list):
                for vi in index[k]:
                    if all(x in vi[0] for x in v): newSet.add(vi[1])
            else:
                for vi in index[k]:
                    if v==vi[0]: newSet.add(vi[1])
        if newSet:
            rSet = rSet.intersection(newSet) if rSet else newSet
    return rSet

data = []
index = {}

add("{\"id\":1,\"last\":\"Doe\",\"first\":\"John\",\"location\":{\"city\":\"Oakland\",\"state\":\"CA\",\"postalCode\":\"94607\"},\"active\":true}")
add("{\"id\":2,\"last\":\"Doe\",\"first\":\"Jane\",\"location\":{\"city\":\"San Francisco\",\"state\":\"CA\",\"postalCode\":\"94105\"},\"active\":true}")
add("{\"id\":3,\"last\":\"Black\",\"first\":\"Jim\",\"location\":{\"city\":\"Spokane\",\"state\":\"WA\",\"postalCode\":\"99207\"},\"active\":true}")
add("{\"id\":4,\"last\":\"Frost\",\"first\":\"Jack\",\"location\":{\"city\":\"Seattle\",\"state\":\"WA\",\"postalCode\":\"98204\"},\"active\":false}")
print(0,index)
print(1,get("{\"location\":{\"state\":\"WA\"},\"active\":true}"))
print(2,get("{\"id\":1}"))
delete("{\"id\":1}")
print(3,data)
add("{\"type\":\"list\",\"list\":[1,2,3,4]}")
add("{\"type\":\"list\",\"list\":[2,3,4,5]}")
add("{\"type\":\"list\",\"list\":[3,4,5,6]}")
add("{\"type\":\"list\",\"list\":[4,5,6,7]}")
add("{\"type\":\"list\",\"list\":[5,6,7,8]}")
add("{\"type\":\"list\",\"list\":[6,7,8,9]}")
print(4,get("{\"type\":\"list\",\"list\":[1]}"))
print(5,get("{\"type\":\"list\",\"list\":[3,4]}"))
