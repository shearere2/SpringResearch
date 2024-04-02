from flask import Flask, render_template, url_for, request, Response
import geoplot.crs as gcrs
from datetime import datetime
import geopandas as gpd
import geoplot
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from elev_tools import summarize_journey
from SpringResearch.walksheds_folder import bus_routes

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the web application."

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "index.html",
        name=name,
        date=datetime.now()
    )

@app.route("/journey/")
@app.route("/journey/<coords>")
def journey(coords:str=None):
    if coords is None:
        return render_template("input.html")
    coords = coords.split('_')
    start = (coords[0],coords[1])
    end = (coords[2],coords[3])
    info = summarize_journey(start,end)
    return render_template(
        "input.html",
        up = '{0:.2f}'.format(info['Cumulative Uphill Travel']),
        down = '{0:.2f}'.format(info['Cumulative Downhill Travel']),
        alt = '{0:.2f}'.format(info['Total Altitude Change']),
        dist = '{0:.2f}'.format(info['Total Distance']),
        coords = coords
    )

@app.route('/input')
def my_form():
    return render_template('my-form.html')

@app.route('/input', methods=['POST'])
def my_form_post():
    slat = request.form['start_lat']
    slon = request.form['start_lon']
    elat = request.form['end_lat']
    elon = request.form['end_lon']
    start = tuple((slat,slon))
    end = tuple((elat,elon))
    coords = [start,end]
    info = summarize_journey(start,end)
    up = info['Cumulative Uphill Travel']
    down = info['Cumulative Downhill Travel']
    alt = info['Total Altitude Change']
    dist = info['Total Distance']
    return render_template(
        "input.html",
        up = '{0:.2f}'.format(info['Cumulative Uphill Travel']),
        down = '{0:.2f}'.format(info['Cumulative Downhill Travel']),
        alt = '{0:.2f}'.format(info['Total Altitude Change']),
        dist = '{0:.2f}'.format(info['Total Distance']),
        coords = coords
    )


@app.route('/prt')
def prt_form():
    return render_template('prt_form.html')

@app.route('/prt',methods=['POST'])
def prt():
    route = request.form['route']
    df = bus_routes.bus_route(route)
    return str(df['Latitude'][0]) + "," + str(df['Longitude'][0])

@app.route('/test')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    df = gpd.read_file('data/pittsburgh_outline.shp')
    stops = bus_routes.bus_route(14)
    burgh = geoplot.polyplot(df,projection=gcrs.AlbersEqualArea(),figsize = (60,45))
    burgh_stops = geoplot.pointplot(stops['Latitude','Longitude'], ax=burgh).figure
    return burgh_stops



if __name__ == "__main__":
    app.run()