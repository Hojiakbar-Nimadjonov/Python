import pandas as pd
import matplotlib.pyplot as plt
data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}
df1 = pd.DataFrame(data1)

# Упражнение 1: Средняя оценка каждого ученика
df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)

# Упражнение 2: Ученик с самой высокой средней оценкой
top_student = df1.loc[df1['Average'].idxmax()]

# Упражнение 3: Новый столбец "Всего"
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)

# Упражнение 4: Визуализация средних оценок по предметам
subject_means = df1[['Math', 'English', 'Science']].mean()
subject_means.plot(kind='bar', title='Average Score per Subject', ylabel='Average Score', color=['skyblue', 'salmon', 'lightgreen'])
plt.tight_layout()
plt.show()
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}
df2 = pd.DataFrame(data2)

# Упражнение 1: Общий объем продаж каждого продукта
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()

# Упражнение 2: Дата с наибольшим общим объемом продаж
df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
max_sales_date = df2.loc[df2['Total_Sales'].idxmax(), 'Date']

# Упражнение 3: Процентное изменение продаж по сравнению с предыдущим днём
percentage_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100

# Упражнение 4: Линейный график тренда продаж
plt.figure(figsize=(10, 5))
for product in ['Product_A', 'Product_B', 'Product_C']:
    plt.plot(df2['Date'], df2[product], label=product)
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}
df3 = pd.DataFrame(data3)

# Упражнение 1: Средняя зарплата по отделам
avg_salary_by_dept = df3.groupby('Department')['Salary'].mean()

# Упражнение 2: Сотрудник с наибольшим опытом
most_experienced = df3.loc[df3['Experience (Years)'].idxmax()]

# Упражнение 3: Увеличение зарплаты от минимальной
min_salary = df3['Salary'].min()
df3['Salary Increase %'] = ((df3['Salary'] - min_salary) / min_salary) * 100

# Упражнение 4: Распределение сотрудников по отделам
dept_counts = df3['Department'].value_counts()
dept_counts.plot(kind='bar', title='Employees per Department', ylabel='Count', color='orchid')
plt.tight_layout()
plt.show()
data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}
df4 = pd.DataFrame(data4)

# Упражнение 1: Общий доход
total_revenue = df4['Total_Price'].sum()

# Упражнение 2: Наиболее заказываемый товар
most_ordered = df4.groupby('Product')['Quantity'].sum().idxmax()

# Упражнение 3: Среднее количество заказанных товаров
avg_quantity = df4['Quantity'].mean()

# Упражнение 4: Круговая диаграмма распределения продаж по продуктам
product_sales = df4.groupby('Product')['Total_Price'].sum()
product_sales.plot(kind='pie', autopct='%1.1f%%', title='Sales by Product', startangle=90)
plt.ylabel('')
plt.tight_layout()
plt.show()

