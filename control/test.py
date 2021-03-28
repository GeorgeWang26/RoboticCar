import json
import ast

if __name__ == '__main__':
    print('hi')
a = [1]
b = list(bytes(a))
print(b)







# json_string = """
# {
#     "researcher": {
#         "name": "Ford Prefect",
#         "species": 1,
#         "relatives": [
#             {
#                 "name": "Zaphod Beeblebrox",
#                 "species": "Betelgeusian"
#             }
#         ]
#     }
# }
# """
# data = json.loads(json_string)

# print(type(data["researcher"]["species"]))