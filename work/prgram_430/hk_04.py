import pandas as pd
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, 3, 9, 20, 20, 7, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# # 4 - a
# df = pd.DataFrame(exam_data)
# print(df)

# 4 - b
# df = pd.DataFrame(exam_data)
# max_score = df.max(axis=0).score
# print(df[df['score'] == max_score])

# # 4 - c
# df = pd.DataFrame(exam_data)
# max_score = df.max(axis=0).score
# min_attempts = df.min(axis=0).attempts
# print( df[(df['score'] == max_score) & (df['attempts'] == min_attempts)])
#
# # 4 - d
# avg = df[['score']].mean(axis=0)
# print(avg)
#
#
# # 4 - e
# avg =df[['score']].mean(axis=0).score
# print(df[df['score'] > avg])
