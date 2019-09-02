from pprint import pprint

def delete_in_dict(d, fields):
    data = d
    for i, f in enumerate(fields):
        if i==len(fields)-1:
            del data[fields[i]]
        else:
            data = data[fields[i]]



d = {
    "1": {
        "11": {
            "111": 111,
            "112": [1121, 1122]
        }
    },
    "2": {
        "21": {
            "211": 211,
            "212": [2121, 2122]
        }
    }
}
pprint(d)

delete_in_dict(d, ["1", "11", "112"])

pprint(d)