import json

def add(s):
    d = json.loads(s)
    db.append([d,s])
    return

def get(s):
    d0 = json.loads(s)
    for d in db:
        if find(d0, d[0]): print(d[1])
    
def delete(s):
    d0 = json.loads(s)
    return [d for d in db if not find(d0,d[0])]
    
def find(d0, d1):
    for k,v in d0.items():
        if k in d1 and has(v, d1[k]):
            continue
        else:
            return False
    return True
        
def has(v0, v1):
    if type(v0)!=type(v1): return False
    elif isinstance(v0, list):
        if not all(v in v1 for v in v0): return False 
    elif isinstance(v0, dict):
        for k,v in v0.items():
            if k in v1 and has(v, v1[k]):
                continue
            else:
                return False
    else:
        if v0!=v1: return False
    return True

db = []

add("{\"id\":1,\"last\":\"Doe\",\"first\":\"John\",\"location\":{\"city\":\"Oakland\",\"state\":\"CA\",\"postalCode\":\"94607\"},\"active\":true}")
add("{\"id\":2,\"last\":\"Doe\",\"first\":\"Jane\",\"location\":{\"city\":\"San Francisco\",\"state\":\"CA\",\"postalCode\":\"94105\"},\"active\":true}")
add("{\"id\":3,\"last\":\"Black\",\"first\":\"Jim\",\"location\":{\"city\":\"Spokane\",\"state\":\"WA\",\"postalCode\":\"99207\"},\"active\":true}")
add("{\"id\":4,\"last\":\"Frost\",\"first\":\"Jack\",\"location\":{\"city\":\"Seattle\",\"state\":\"WA\",\"postalCode\":\"98204\"},\"active\":false}")
get("{\"location\":{\"state\":\"WA\"},\"active\":true}")
get("{\"id\":1}")
db = delete("{\"id\":1}")

add("{\"type\":\"list\",\"list\":[1,2,3,4]}")
add("{\"type\":\"list\",\"list\":[2,3,4,5]}")
add("{\"type\":\"list\",\"list\":[3,4,5,6]}")
add("{\"type\":\"list\",\"list\":[4,5,6,7]}")
add("{\"type\":\"list\",\"list\":[5,6,7,8]}")
add("{\"type\":\"list\",\"list\":[6,7,8,9]}")
get("{\"type\":\"list\",\"list\":[1]}")
get("{\"type\":\"list\",\"list\":[3,4]}")
