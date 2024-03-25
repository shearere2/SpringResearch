from flask import Flask, redirect, url_for, render_template
from SpringResearch.walksheds_folder.find_elevation import summarize_journey
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
def home():
    render_template('index.html')

# @app.route('/elevation/<tuple:start_stop>')
# # ‘/elevation’ URL is bound with elev_app() function.
# def elev_app(start_stop:tuple):
#     return f"<p>{summarize_journey((start_stop[0][0],start_stop[0][1]),
                                #    (start_stop[1][0],start_stop[1][1]))}</p>"
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()

    """NOTE: On my laptop, takes ~50 seconds per linear mile to run the website.
    Would like to make it more efficient!"""