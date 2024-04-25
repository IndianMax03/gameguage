import json
import random

def transform_json(input_json):
    output_data = []
    for item in input_json:
        word = item["word"]
        if len(word) > 1:
            index = random.randint(0, len(word) - 1)
            main_text = word[:index] + "_" + word[index + 1:]
            missed_text = word[index]
            output_data.append({"main_text": main_text, "missed_text": missed_text})
    return output_data

with open("words.json", "r") as f:
    input_data = json.load(f)

output_data = transform_json(input_data)

with open("fill_words.json", "w") as f:
    json.dump(output_data, f, indent=4)
