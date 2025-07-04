import pandas as pd
df = pd.read_csv('task\\stackoverflow_qa.csv')

# 1. Вопросы, созданные до 2014 года
df_before_2014 = df[pd.to_datetime(df['датасоздания']) < '2014-01-01']

# 2. Вопросы с оценкой более 50
df_score_above_50 = df[df['счет'] > 50]

# 3. Вопросы с оценкой от 50 до 100
df_score_50_100 = df[(df['счет'] >= 50) & (df['счет'] <= 100)]

# 4. Ответы от Скотта Бостона
df_scott_boston = df[df['ans_name'] == 'Скотт Бостон']

# 5. Ответы от 5 конкретных пользователей
users = ['Unutbu', 'Скотт Бостон', 'Майк Пеннингтон', 'Дуг', 'Демитрий']
df_top5_users = df[df['ans_name'].isin(users)]

# 6. Вопросы с марта по октябрь 2014, ответил Unutbu, и оценка < 5
df_march_oct_unutbu = df[
    (pd.to_datetime(df['датасоздания']) >= '2014-03-01') &
    (pd.to_datetime(df['датасоздания']) <= '2014-10-31') &
    (df['ans_name'] == 'Unutbu') &
    (df['счет'] < 5)
]

# 7. Вопросы с оценкой от 5 до 10 или просмотрами более 10 000
df_score_or_views = df[(df['счет'].between(5, 10)) | (df['просмотры'] > 10000)]

# 8. Вопросы, на которые НЕ ответил Скотт Бостон
df_not_scott = df[df['ans_name'] != 'Скотт Бостон']

titanic_df = pd.read_csv("task\\titanic.csv")

# 1. Женщины в 1 классе, возраст 20–30 лет
df_women_1st_20_30 = titanic_df[
    (titanic_df['секс'] == 'женский') &
    (titanic_df['Pкласс'] == 1) &
    (titanic_df['Возраст'].between(20, 30))
]

# 2. Пассажиры, заплатившие > 100$
df_fare_over_100 = titanic_df[titanic_df['Тариф'] > 100]

# 3. Выжившие и путешествовавшие одни
df_survived_alone = titanic_df[
    (titanic_df['Выжил'] == 1) &
    (titanic_df['СибСп'] == 0) &
    (titanic_df['Парч'] == 0)
]

# 4. Сошли в порту "C" и заплатили > 50$
df_port_c_fare_50 = titanic_df[
    (titanic_df['Встал'] == 'С') &
    (titanic_df['Тариф'] > 50)
]

# 5. Пассажиры с братьями/сёстрами/супругами и родителями/детьми
df_family_onboard = titanic_df[
    (titanic_df['СибСп'] > 0) & (titanic_df['Парч'] > 0)
]

# 6. Возраст ≤ 15 лет и не выжили
df_kids_not_survived = titanic_df[
    (titanic_df['Возраст'] <= 15) &
    (titanic_df['Выжил'] == 0)
]

# 7. Есть каюта и стоимость > 200$
df_cabin_and_fare = titanic_df[
    (titanic_df['Кабина'].notna()) &
    (titanic_df['Тариф'] > 200)
]

# 8. Нечётные PassengerId
df_odd_ids = titanic_df[titanic_df['ПассажирскийId'] % 2 == 1]

# 9. Уникальные номера билетов
df_unique_tickets = titanic_df[titanic_df.duplicated('Билет') == False]

# 10. Имя содержит "мисс", класс 1, пол женский
df_miss_class1 = titanic_df[
    (titanic_df['Имя'].str.contains('мисс', case=False, na=False)) &
    (titanic_df['Pкласс'] == 1) &
    (titanic_df['секс'] == 'женский')
]
