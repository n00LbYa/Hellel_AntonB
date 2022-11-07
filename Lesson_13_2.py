# Прочитать сохранённый json-файл из задания №17 и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.
import csv
import json

first_field = ["Person1", "Person2", "Person3", "Person4", "Person5", "Person6"]
telephones = [980978998, 5345345, 3453445, 435345, 53453454, 3453453]
with open('our_task_1.json') as f:
    input_data = json.load(f)

print(input_data)

with open('our_task_2.csv', "w", encoding= "utf-8") as f:
    our_writer_file = csv.writer(f)
    for item in (first_field, input_data, telephones):
        our_writer_file.writerow(item)

print(our_writer_file)




#     for item in file_reader:
#         print(f'{item[0]}   |    {item[1]}   |    {item[2]}    |      {item[3]} |      {item[4]}|      '
#               f'{item[5]}|      {item[6]}|      {item[7]}|      {item[8]} |      {item[9]}|      {item[10]}|      '
#               f'{item[11]}')
#
# with open('our_task_2.csv', "w") as f:
#     file_writer = csv.writer(f, "our_task_1.json")