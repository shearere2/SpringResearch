from flask import Flask
from SpringResearch.walksheds_folder.find_elevation import summarize_journey
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def elev_app():
    return f"<p>{summarize_journey((40.1125,-79.8899),(40.1223,-79.8793))}</p>"
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()

    """NOTE: On my laptop, takes ~50 seconds per linear mile to run the website.
    Would like to make it more efficient!"""