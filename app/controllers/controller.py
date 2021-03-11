from flask import render_template, request, redirect
from app import app
from app.modules.event_list import events_list, create_new_event
from app.modules.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Events', events=events_list)

@app.route('/events', methods=['POST'])
def create_event():
    eventName = request.form['event_name']
    eventDate = request.form['date']
    eventDesc = request.form['description']
    eventGuests = request.form['number_of_guests']
    eventRoom = request.form['room_location']
    eventRecurring = request.form['recurring']
    newEvent = Event(eventDate, eventName, eventGuests, eventRoom, eventDesc,eventRecurring)
    create_new_event(newEvent) 
    return redirect('/events')
    
