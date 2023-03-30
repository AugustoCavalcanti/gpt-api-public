# ready json file
import json

import unicodedata

ready_file = open("dados_biblioteca.json", "r")
ready_json = json.load(ready_file)
ready_file.close()



def func(value):
    return ''.join(value.splitlines())

def remove_control_characters(s):
    return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")

#conventional way to convert a list of dictionaries to a string
def convert_to_string(data):
    converted = str()
    for key in data:
        if key == "Autores":
            converted += str(key) + ": ["
            for author in data[key]:
                converted += str(author["Tipo"]) + ": " + str(author["Nome"]) + ", "
            converted += "], "
        elif key == "Banca":
            converted += str(key) + ": ["
            for member in data[key]:
                converted += str(member['Tipo']) + ": " + str(member['Nome']) + ", "
            converted += "], "
        elif key == "PalavrasChave":
            converted += str(key) + ": ["
            for keyword in data[key]:
                converted += str(keyword['Termo']).replace('"', "") + ", "
            converted += "], "
        else:
            converted += str(key) + ": " + remove_control_characters(func(str(data[key])).replace('"', "")).replace('\\', "") + ", "
        # converted += str(key) + ": " + data[key] + ", "
    return converted

# use this to write a json file
with open("dados_biblioteca_fine_format.json", "w") as json_file:
    json_file.write("[")
    for data in ready_json:
        #convert dictionary to string
        converted_to_string = convert_to_string(data)
        json_file.write("{" + "\"prompt\": \"Quem é o orientador do trabalho " +
                        remove_control_characters(func(str(data["Titulo"])).replace('"', "")) + "? "+ converted_to_string +"\", \"completion\": \"O orientador do trabalho " + remove_control_characters(func(str(data["Titulo"])).replace('"', "")) + " é " + data["OrientadorNome"] + "\"},")
    json_file.write("]")
json_file.close()

# use this to write a csv file
with open("dados_biblioteca.csv", "w") as csv_file:
    csv_file.write("prompt,completion")
    for data in ready_json:
        #convert dictionary to string
        converted_to_string = convert_to_string(data)
        csv_file.write("Quem é o orientador do trabalho " +
                       remove_control_characters(func(str(data["Titulo"])).replace('"', "")) + "? " + converted_to_string + ",O orientado do trabalho" + remove_control_characters(func(str(data["Titulo"])).replace('"', "")) + " é " + data["OrientadorNome"])
csv_file.close()

# right now, we have a list of dictionaries, each dictionary has a key "text" and a key "label"
