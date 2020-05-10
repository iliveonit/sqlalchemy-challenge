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

PRCP_rows = engine.execute('SELECT * FROM Measurement').fetchall()
STN_rows = engine.execute('SELECT * FROM Station').fetchall()

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
    )

# #############################################################################
# `/api/v1.0/precipitation`
# #############################################################################

@app.route("/api/v1.0/Precipitations")
def Precipitations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a dictionary with `date` as the key and `prcp` from the dataset"""
    # Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
    PRCP_results = session.query(Measurement.date, Measurement.prcp).all()
    
    session.close()

    # Results
    all_Precipitations = list(np.ravel(PRCP_results))

    return jsonify(all_Precipitations)

# #############################################################################
#  `/api/v1.0/stations`
# #############################################################################

@app.route("/api/v1.0/Stations")
def Stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

     """Return a list of stations from the dataset"""
    # Return a JSON list of stations from the dataset.
    STN_results = session.query(Stations.station, Stations.name, Stations.latitude, Stations.longitude, Stations.elevation).all()

    session.close()

    # Resu;ts
     all_Stations = list(np.ravel(STN_results))

    return jsonify(all_Stations)


# #############################################################################
# `/api/v1.0/tobs`
# #############################################################################

    
    @app.route("/api/v1.0/Stations")
def TOBS():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #Query the dates and temperature observations of the most active station for the last year of data.
    Active_STN = session.query(Measurement.station, Measurement.dates, Measurement.tobs FROM Measurement).all()

    
    
        
        
    # Return a JSON list of temperature observations (TOBS) for the previous year.
    TOBS_LastYear = session.query(Measurement.station, Measurement.dates, Measurement.tobs FROM Measurement WHERE date >= '2016-01-01').all()
    
    session.close()

    # Results
     all_TOBS = list(np.ravel(Active_STN))
     all_TOBS = list(np.ravel(TOBS_LastYear))

    return jsonify(all_Stations)
  

# ############################################################################# 

if __name__ == '__main__':
    app.run(debug=True)
