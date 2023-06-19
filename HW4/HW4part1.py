

from flask import Flask
from webargs import fields, validate
from webargs.flaskparser import use_args

from database_handler import execute_query

app = Flask(__name__)

@app.route("/order-price")
@use_args(
    {
        "Country": fields.Str(
        )
    },
    location="query"
)
def order_price(Country):
    query = "SELECT SUM(Sales) AS Sales_by_Country, BillingCountry FROM (SELECT invoice_items.UnitPrice * invoice_items.Quantity AS Sales, BillingCountry FROM invoice_items JOIN invoices i on invoice_items.InvoiceId = i.InvoiceId) GROUP BY BillingCountry "

    fields = {}

    if Country:
        fields['BillingCountry'] = Country

    if fields:
        query += "HAVING BillingCountry ='" + str(fields['BillingCountry']['Country']) +"'"

    records = execute_query(query=query)
    return records


@app.route("/get-info")
@use_args(
    {
        "Idshka": fields.Int(
            missing=1,
            validate = validate.Range(min = 1, max= 500)
        )
    },
    location="query"
)
def get_all_info_about_track(Idshka):
    query ="SELECT * FROM (SELECT tracks.TrackId, tracks.Name, Composer, Milliseconds, Bytes, UnitPrice Title, a2.Name AS Artist, g.Name AS Genre, mt.Name AS media_type, p.Name AS Playlist  FROM tracks left join albums a on a.AlbumId = tracks.AlbumId LEFT JOIN artists a2 on a2.ArtistId = a.ArtistId LEFT JOIN genres g on g.GenreId = tracks.GenreId LEFT JOIN media_types mt on mt.MediaTypeId = tracks.MediaTypeId LEFT JOIN playlist_track pt on tracks.TrackId = pt.TrackId LEFT JOIN playlists p on pt.PlaylistId = p.PlaylistId)"

    fields = {}

    if Idshka:
        fields['TrackId'] = Idshka

    if fields:
        query += "WHERE TrackId ='" + str(fields['TrackId']['Idshka']) + "'"

    records = execute_query(query=query)
    return records


@app.route("/get-info-time")
@use_args(
    {
        "AlId": fields.Int(
        )
    },
    location="query"
)
def get_all_info_about_track_time(AlId):
    query ="SELECT AlbumId, SUM(Milliseconds/60000) AS Sum_in_minutes FROM tracks GROUP BY AlbumId"
    fields = {}

    if AlId:
        fields['AlbumId'] = AlId

    if fields:
        query += " HAVING AlbumId ='" + str(fields['AlbumId']['AlId']) + "'"
        records = execute_query(query=query)
        return f'The time in minutes of album with AlbumId {AlId["AlId"]} is {records[0][1]} minutes'
    records = execute_query(query=query)
    return records

if __name__ == "__main__":
    app.run(debug=True)
