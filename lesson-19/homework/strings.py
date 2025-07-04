import pandas as pd

sales_df = pd.read_csv('task\\sales_data.csv')

# 1. Группировка по категориям
grouped = sales_df.groupby('Category').agg(
    Total_Quantity=('Quantity', 'sum'),
    Avg_Price=('Price', 'mean'),
    Max_Quantity_Single_Transaction=('Quantity', 'max')
).reset_index()

# 2. Самый продаваемый продукт в каждой категории
top_products = sales_df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top_sellers = top_products.sort_values(['Category', 'Quantity'], ascending=[True, False]).drop_duplicates('Category')

# 3. Дата с наибольшим объёмом продаж
sales_df['TotalSale'] = sales_df['Quantity'] * sales_df['Price']
max_sales_date = sales_df.groupby('Date')['TotalSale'].sum().reset_index().sort_values('TotalSale', ascending=False).head(1)

orders_df = pd.read_csv('task\\customer_orders.csv')

# 1. Клиенты с менее чем 20 заказами
customer_order_counts = orders_df.groupby('CustomerID').size().reset_index(name='OrderCount')
customers_less_than_20 = customer_order_counts[customer_order_counts['OrderCount'] < 20]

# 2. Клиенты со средней ценой за единицу > $120
avg_price_by_customer = orders_df.groupby('CustomerID')['Price'].mean().reset_index()
high_avg_price_customers = avg_price_by_customer[avg_price_by_customer['Price'] > 120]

# 3. Количество и общая цена каждого товара, фильтрация товаров с количеством < 5
product_stats = orders_df.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Revenue=('Price', lambda x: (x * orders_df.loc[x.index, 'Quantity']).sum())
).reset_index()
filtered_products = product_stats[product_stats['Total_Quantity'] >= 5]

import sqlite3

# 1. Подключение к базе данных
conn = sqlite3.connect('task\\population.db')

# 2. Чтение таблицы
population_df = pd.read_sql_query("SELECT * FROM population", conn)

# 3. Загрузка Excel с категориями зарплат
salary_categories = pd.read_excel('task\\population salary analysis.xlsx')

# Предположим, в файле есть две колонки: 'Category', 'Min', 'Max'
# Добавим категорию каждому
def get_salary_category(salary):
    for _, row in salary_categories.iterrows():
        if row['Min'] <= salary <= row['Max']:
            return row['Category']
    return 'Unknown'

population_df['Salary_Category'] = population_df['Salary'].apply(get_salary_category)

# 4. Группировка по категориям
by_category = population_df.groupby('Salary_Category').agg(
    Population_Size=('Salary', 'count'),
    Avg_Salary=('Salary', 'mean')
).reset_index()

total_population = len(population_df)
by_category['Percent'] = 100 * by_category['Population_Size'] / total_population

# 5. Группировка по категориям и Штатам
by_state_category = population_df.groupby(['State', 'Salary_Category']).agg(
    Population_Size=('Salary', 'count'),
    Avg_Salary=('Salary', 'mean')
).reset_index()

# Добавим процент внутри каждого штата
state_totals = population_df.groupby('State').size().to_dict()
by_state_category['Percent'] = by_state_category.apply(
    lambda row: 100 * row['Population_Size'] / state_totals[row['State']],
    axis=1
)

# Примеры сохранения
grouped.to_csv('task\\category_summary.csv', index=False)
top_sellers.to_csv('task\\top_selling_products.csv', index=False)
max_sales_date.to_csv('task\\max_sales_date.csv', index=False)

customers_less_than_20.to_csv('task\\customers_less_20_orders.csv', index=False)
high_avg_price_customers.to_csv('task\\high_avg_price_customers.csv', index=False)
filtered_products.to_csv('task\\filtered_products.csv', index=False)

by_category.to_excel('task\\salary_analysis_by_category.xlsx', index=False)
by_state_category.to_excel('task\\salary_analysis_by_state.xlsx', index=False)
