from flask import render_template, url_for
from app import app




@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/sports')
def sports_page():

    athletes = [{
        'name': 'Troy Aikman',
        'image': url_for('static', filename='troyaikman.jpg') 
    },{
        'name': 'Michael Jordan',
        'image': url_for('static', filename='Jordan.jpg')
    },{
        'name': 'Alex Morgan',
        'image': url_for('static', filename='alexmorgan.jpg')
     },{ 
        'name': 'David Beckham',
        'image':  url_for('static', filename='daveb.jpg')
    },{
        'name': 'Gabriella Reece',
        'image': url_for('static', filename='gabriellareece.jpg') 
                                
    }]

    return render_template('sports.html', athletes=athletes)