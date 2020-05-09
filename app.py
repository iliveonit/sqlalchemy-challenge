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
        f"/api/v1.0/Stations"
    )


@app.route("/api/v1.0/names")
def Precipitations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    # Insert your <<< query ???? 

    session.close()

    # Convert list of tuples into normal list
    all_Precipitations = list(np.ravel(results))

    return jsonify(all_Precipitations)


@app.route("/api/v1.0/Stations")
def Stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

     """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    # Insert your <<< query ???? 
    results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_Stations = []
    for name, age, sex in results:
        passenger_dict = {}
        passenger_dict["name"] = name
        passenger_dict["age"] = age
        passenger_dict["sex"] = sex
        all_Stations.append(stations_dict)

    return jsonify(all_Stations)


if __name__ == '__main__':
    app.run(debug=True)
