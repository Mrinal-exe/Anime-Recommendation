import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = TfidfVectorizer()

anime_data = pd.read_csv("Sample data/anime.csv")

list_of_all_animes = anime_data['name'].tolist()

selected_columns = ['name', 'genre', 'type']

for columns in selected_columns:
    anime_data[columns] = anime_data[columns].fillna('')

combined_columns = anime_data['name']+' '+anime_data['genre']+' '+anime_data['type']

columns_vector = vectorizer.fit_transform(combined_columns)

similarity = cosine_similarity(columns_vector)

user_input = input('Enter your favourite Anime : ')

find_close_match = difflib.get_close_matches(user_input, list_of_all_animes)

close_match = find_close_match[0]

anime_index = anime_data[anime_data['name'] == close_match].index[0]

similarity_score = list(enumerate(similarity[anime_index]))

sorted_similar_animes = sorted(similarity_score, key = lambda x:x[1], reverse = True)

print('Animes suggested for you :  \n')
i=1
for anime in sorted_similar_animes:
    index = anime[0]
    title_from_index = anime_data[anime_data.index==index]['name'].values[0]
    if (i<31):
        print(i, '.',title_from_index)
        i+=1




