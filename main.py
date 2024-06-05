import os
from zipfile import ZipFile
from google import generativeai as gen_ai
from time import sleep


GOOGLE_API_KEY = 'API_KEY'
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')


def generate_output(prompt):
    output = model.generate_content(prompt)
    return output.text

def make_zip(file_path, count):
    with ZipFile(f'zipFile_{count}.zip', 'w') as zip_object:
        zip_object.write(file_path, os.path.basename(file_path))


count = 0
while True:

    prompts = input("Enter the Prompt: ")

    if prompts:

        output = generate_output(prompts)

        with open('output.txt', 'w') as f:
            f.write(output)

        if count < 20:
            make_zip('output.txt', count)
            count += 1
        else:
            print("Limit Has Been Crossed")


        sleep(2)
        os.remove('output.txt')
