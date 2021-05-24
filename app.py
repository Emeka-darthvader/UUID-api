from flask import Flask,jsonify, request
from datetime import datetime

import uuid

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False #prevent default sorting by flask jsonify

''' Function to generate the UUID'''
def generate_UUID():
    print("generating UUID...")
    generated_UUID = uuid.uuid4().hex
    result_announcer_helper(generated_UUID,1)
    generated_UUID = str(generated_UUID)
    return generated_UUID

''' Function to generate timestamps '''
def generate_timestamps():
    print("generating timestamps...")
    current_time = datetime.now()
    current_timestamp = current_time.strftime("%Y-%m-%d,%H:%M:%s")
    result_announcer_helper(current_timestamp,2)
    return current_timestamp

''' Helper function to output result, type 1 is for UUID while 2 is for timestamp.'''
def result_announcer_helper(value_got,alert_type):
    if (alert_type == 1):
        print("*"*10)
        print("Generated UUID is ",value_got) ##Could use python formatting like f'' or {} .format()
        print("*"*10)
    elif (alert_type == 2):
        print("*"*10)
        print("Generated Timestamp is ",value_got) ##Could use python formatting like f'' or {} .format()
        print("*"*10)

''' dicts are declared outside function as globals. This would enable retaining values'''
timestamp_UUID_pair = {} #dict to return values
timestamp_UUID_pair_temp = {} #temp dict to store value before reverse sorting

''' This route only accepts GET requests'''
@app.route('/generate',methods=['GET','POST'])
def generate_timestamp_UUID_pairs():
    if (request.method == 'POST'):
        payload_sent = request.get_json()
        return jsonify({'status':'wrong request type','payload':payload_sent}),405
    elif (request.method == 'GET'):
        
        generated_UUID = generate_UUID() #generating uuid
        generated_timestamp = generate_timestamps() #generating timestampa

        timestamp_UUID_pair_temp[generated_timestamp] = generated_UUID #assigning to the temp dict with timestamp as index/key
        timestamp_UUID_pair = dict(reversed(list(sorted(timestamp_UUID_pair_temp.items())))) # sorting then reversing the dict
        
        # print(timestamp_UUID_pair)
        return jsonify(timestamp_UUID_pair)


if __name__ == '__main__':
    # app.run(debug=True) #for debug only
    app.run()