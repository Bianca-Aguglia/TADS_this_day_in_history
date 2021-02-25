from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'wikipedia_tdih.db'

app.config['DEBUG'] = True

@app.route('/', methods = ['GET'])
def api_index():
    pass

@app.route('/today', methods = ['GET'])
def get_current_day_events():
    pass

@app.route('/<str:date>', methods = ['GET'])
def get_date_events_type_all(date):
    pass

@app.route('/<str:date>/<str:event_type>', methods = ['GET'])
def get_date_events_of_event_type(date):
    pass




# links on '/api'
    # overview
    # endpoints
    # contact (maybe just on header?)
    # support (?)
    # back to website
    
# endpoints
                                
# choice between
# 1
# api/January_1/all_types  (or api/January_1/all)
# api/January_1/events
# api/January_1/birthdays

# 2
# api/all_types/January_1
# api/events/January_1
# api/birthdays/January_1
           
           
           
           
           