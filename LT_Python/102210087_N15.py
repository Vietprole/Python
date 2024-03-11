import json
import logging
import pandas as pd

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load the JSON data
with open('LT_Python/Vietnamese_dataset.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Initialize a counter for non-empty "question" fields
non_empty_contexts = 0
non_empty_questions = 0
non_empty_answers = 0

# Prepare a list to store the data
data_list = []

# Iterate over the data
for item in data['data']:
    for paragraph in item['paragraphs']:
        context = paragraph['context']
        if paragraph['context']:
            non_empty_contexts += 1
        for qa in paragraph['qas']:
            question = qa['question']
            is_impossible = qa['is_impossible']
            # If the "question" field is not empty, increment the counter
            if qa['question']:
                non_empty_questions += 1
            if qa['answers']:
                non_empty_answers += 1
                answer = qa['answers'][0]['text']
            else :
                answer = 'None'
            # Append the data to the list
            data_list.append([context, question, answer, is_impossible])

# Convert the list to a DataFrame
df = pd.DataFrame(data_list, columns=['Context', 'Question', 'Answer', 'Is_impossible'])

# Log the count of non-empty "question" fields
logging.info(f'Số context là: {non_empty_questions}')
logging.info(f'Số question là: {non_empty_questions}')
logging.info(f'Số answers là: {non_empty_answers}')

with open('output.csv', 'wb') as f:
    f.write(df.to_csv(sep='\t', index=False).encode())
# print(df)
# # Save the DataFrame to a CSV file
# df.to_csv('output.csv', sep='\t', index=False)