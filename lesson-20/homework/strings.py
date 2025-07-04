import sqlite3
import pandas as pd

# Подключаемся к базе данных chinook
conn = sqlite3.connect("task/chinook.db")

query = """
SELECT 
    Customer.CustomerId,
    Customer.FirstName || ' ' || Customer.LastName AS FullName,
    SUM(Invoice.Total) AS TotalSpent
FROM Invoice
JOIN Customer ON Invoice.CustomerId = Customer.CustomerId
GROUP BY Customer.CustomerId
"""
customer_spending = pd.read_sql_query(query, conn)

top_5_customers = customer_spending.sort_values(by='TotalSpent', ascending=False).head(5)
print(top_5_customers[['CustomerId', 'FullName', 'TotalSpent']])
# 1. Получаем все покупки клиентов (InvoiceLine содержит треки)
purchases = pd.read_sql_query("""
    SELECT 
        il.InvoiceId,
        i.CustomerId,
        t.TrackId,
        t.AlbumId
    FROM InvoiceLine il
    JOIN Invoice i ON il.InvoiceId = i.InvoiceId
    JOIN Track t ON il.TrackId = t.TrackId
""", conn)

# 2. Узнаём, сколько треков всего в каждом альбоме
album_track_counts = pd.read_sql_query("""
    SELECT AlbumId, COUNT(TrackId) as TotalTracks
    FROM Track
    GROUP BY AlbumId
""", conn)

# 3. Считаем, сколько треков из каждого альбома купил каждый клиент
client_album_purchases = purchases.groupby(['CustomerId', 'AlbumId']).agg(
    PurchasedTracks=('TrackId', 'nunique')
).reset_index()

# 4. Объединяем с общим количеством треков в альбоме
client_album_merged = client_album_purchases.merge(album_track_counts, on='AlbumId')

# 5. Отмечаем, купил ли клиент весь альбом
client_album_merged['BoughtFullAlbum'] = client_album_merged['PurchasedTracks'] == client_album_merged['TotalTracks']

# 6. Считаем клиентов, купивших ХОТЯ БЫ ОДИН полный альбом
customers_full_album = client_album_merged.groupby('CustomerId')['BoughtFullAlbum'].any().reset_index()
customers_full_album['Preference'] = customers_full_album['BoughtFullAlbum'].apply(
    lambda x: 'Albums' if x else 'Tracks'
)
summary = customers_full_album['Preference'].value_counts(normalize=True) * 100
print(summary)
print("🏆 Топ-5 клиентов по сумме покупок:")
print(top_5_customers[['CustomerId', 'FullName', 'TotalSpent']])

print("\n📊 Предпочтения клиентов:")
print(summary)
print("🏆 Топ-5 клиентов по сумме покупок:")
print(top_5_customers[['CustomerId', 'FullName', 'TotalSpent']])

print("\n📊 Предпочтения клиентов:")
print(summary)
