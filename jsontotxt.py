import json
with open("mtoutput.json", "r") as read_file:
    data = json.load(read_file)

translated = data["data"]["translations"][0]["translatedText"]

write_file = open("mtresult.txt", "w")
write_file.write(translated.encode('utf-8'))
write_file.close()