"""
You have been provided with a dataset containing mixed data types and nested structures.
Your task is to filter the data to remove null values and empty objects, considering nested structures,
and then output the cleaned dataset.
"""

all_data = [
    5,
    "apple",
    None,
    {"name": "John", "age": 25, "address": {}},
    {"phone": "123-456-7890", "email": ""},
    "",
    10.5,
    None,
    {"city": "New York", "zipcode": None},
    {
        "name": "Jane",
        "age": None,
        "address": {"city": "", "zipcode": 10001}
    },
    0
]


def recu_filter(data):
    if isinstance(data, list):
        return [recu_filter(i) for i in data if recu_filter(i)]
    elif isinstance(data, dict):
        return {key: recu_filter(val) for key, val in data.items() if recu_filter(val)}
    elif data is None or data == "" or data == {}:
        return None
    else:
        return data


print(recu_filter(all_data))
