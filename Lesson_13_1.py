# Создать словарь в качестве ключа которого будет 6-ти значное число, а в качестве значений
# кортеж состоящий из 2-х элементов – имя(str), возраст(int). Сделать около 5-6 элементов словаря.
# Записать данный словарь на диск в json-файл.

import json

our_dictionary = [
    {
        123467: (
            {
                "Last_name": "Luka",
                "Age" :39
            }
        ),
        456457: (
            {
                "Last_name": "Karim",
                "Age": 38
            }
        ),
        624652: (
            {
                "Last_name": "Gareth",
                "Age": 40
            }
        ),
        452356: (
            {
                "Last_name": "Tibo",
                "Age": 35}
        ),
        976896: (
            {
                "Last_name": "Lucas",
                "Age": 35
            }
        ),
        123650: (
            {
                "Last_name": "Toni",
                "Age": 37
            }
        )
    }
]

with open("our_task_1.json", 'w') as f:
    json.dump(our_dictionary, f)
