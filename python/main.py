import pandas as pd

df = pd.read_csv('./yape_ready_12_11.csv')
df['content_join'] = df['content_join'].astype(str).fillna('')
text = list(df['content_join'])
with open('reviews.txt', 'w', encoding='utf-8') as file:
    for i in range(len(text)):
        file.write(f'{text[i]}\n')
