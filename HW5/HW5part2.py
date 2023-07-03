from flask import Flask
from webargs import fields, validate
from webargs.flaskparser import use_args

from database_handler import execute_query

app = Flask(__name__)

@app.route("/genrefinder")
@use_args(
    {
        "genre": fields.Str(
            required=True
        )
    },
    location="query"
)
def music_genre(genre):
    query = "SELECT g.Name AS Genre, c.City AS City, " \
            "COUNT (*) AS Listens FROM tracks t " \
            "JOIN genres g ON t.GenreId = g.GenreId " \
            "JOIN albums a ON t.AlbumId = a.AlbumId " \
            "JOIN artists ar ON a.ArtistId = ar.ArtistId " \
            "JOIN customers cu ON cu.CustomerId = ar.ArtistId " \
            "JOIN invoices i ON i.CustomerId = cu.CustomerId " \
            "JOIN invoice_items ii ON ii.InvoiceId = i.InvoiceId " \
            "JOIN customers c ON c.CustomerId = i.CustomerId "
    query += " WHERE g.Name = '" + str(genre['genre']) + "' " \
             "GROUP BY Genre, c.City " \
             "ORDER BY Listens DESC " \
             "LIMIT 1;"
    records = execute_query(query=query)
    return records
if __name__ == "__main__":
    app.run(debug=True)