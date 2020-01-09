import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def event_calender():
	finalList = []
	finalDict = {'date': '', 'event': []}

	eventList = []
	nested_dict = {'name': '', 'value':'', 'color':''}
	
	nested_dict['name'] = 'appointment'
	nested_dict['value'] = '132'
	nested_dict['color'] = 'green'
	
	eventList.append(dict(nested_dict))

	nested_dict['name'] = 'confirmed'
	nested_dict['value'] = '13'
	nested_dict['color'] = 'brown'
	
	eventList.append(dict(nested_dict))

	finalDict['date'] = '2020-01-01'
	finalDict['event'] = eventList

	finalList.append(dict(finalDict))

	finalDict['date'] = '2020-01-02'
	finalDict['event'] = eventList

	finalList.append(dict(finalDict))

	return jsonify(finalList)

if __name__ == "__main__":
    app.run(debug=True)
