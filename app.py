import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the 2 table: 
Measurement = Base.classes.measurement
Station = Base.classes.station


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available API Routes."""
    return (
        f"Available API Routes:<br/>"
        f"/api/v1.0/Precipitation<br/>"
        f"/api/v1.0/Stations<br/>"
        f"/api/v1.0/TOBS<br/>"
        f"/api/v1.0/BONUS"
    )

# #############################################################################
# `/api/v1.0/precipitation`
# #############################################################################

@app.route("/api/v1.0/Precipitations")
def Precipitations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
    PRCP_results = session.query(Stations.station, Stations.name, Stations.latitude, Stations.longitude, Stations.elevation).all()
    
    # Return the JSON representation of your dictionary.
   
    

    session.close()
    

    # Convert list of tuples into normal list
    all_Precipitations = list(np.ravel(PRCP_results))

    return jsonify(all_Precipitations)

# #############################################################################
#  `/api/v1.0/stations`
# #############################################################################

@app.route("/api/v1.0/Stations")
def Stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

     """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    # engine.execute('SELECT * FROM Station').fetchall()
    STN_results = session.query(Stations.station, Stations.name, Stations.latitude, Stations.longitude, Stations.elevation).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_Stations = []
    for  in STN_results:
        stations_dict = {}
        stations_dict["station"] = Station_ID
        stations_dict["name"] = Station_Name
        stations_dict["latitude"] = Latitude
        stations_dict["longitude"] = Longitude
        
        all_Stations.append(stations_dict)

    return jsonify(all_Stations)


# #############################################################################
# `/api/v1.0/tobs`
# #############################################################################

    
    @app.route("/api/v1.0/Stations")
def TOBS():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #Query the dates and temperature observations of the most active station for the last year of data.
    # engine.execute('SELECT * FROM Station').fetchall()
    
    STN_results = session.query(Stations.station, Stations.name, Stations.latitude, Stations.longitude, Stations.elevation).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_Stations = []
    for  in results:
        passenger_dict = {}
        passenger_dict["name"] = name
        passenger_dict["age"] = age
        passenger_dict["sex"] = sex
        all_Stations.append(stations_dict)

    return jsonify(all_Stations)
  
# Return a JSON list of temperature observations (TOBS) for the previous year.


    
    
# #############################################################################
# BONUS related
# ############################################################################# 

# ----------------------------------------------------
#  `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
# ----------------------------------------------------

# Return a JSON list of the minimum temperature, the average temperature, 
# and the max temperature for a given start or start-end range.

# When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` 
# for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates 
# between the start and end date inclusive.
    
    @app.route("/api/v1.0/Stations")
def TOBS():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #Query the dates and temperature observations of the most active station for the last year of data.
    # engine.execute('SELECT * FROM Station').fetchall()
    
    STN_results = session.query(Stations.station, Stations.name, Stations.latitude, Stations.longitude, Stations.elevation).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_BONUS = []
    for  in results:
        bonus_dict = {}
        bonus_dict["a1"] = name
        bonus_dict["a2"] = age
        bonus_dict["a3"] = sex
        all_BONUS.append(bonus_dict)

    return jsonify(all_BONUS)
  
# Return a JSON list of temperature observations (BONUS) for the previous year.

# ############################################################################# 

if __name__ == '__main__':
    app.run(debug=True)
