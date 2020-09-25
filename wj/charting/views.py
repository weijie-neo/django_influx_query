from datetime import datetime
import time
import json
from django.shortcuts import render
from influxdb import InfluxDBClient
from requests.exceptions import ConnectionError
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):

	return render(request,'home.html',)

@login_required
def project_details(request):
	try:
		client = InfluxDBClient(host='localhost' , port =8086 , database ='test1')
		results = client.query('SELECT time,value from counter ' )
		points = results.get_points()
		data = list()
		
		for point in points:
			entry = list()
			t = time.mktime(datetime.strptime(point['time'], "%Y-%m-%dT%H:%M:%S.%fZ").timetuple())	
			entry.append(int(t)*1000)
			entry.append(point['value'])
			data.append(entry)

		context = {
		'data' : json.dumps(data)
		}

		return render(request,'charts.html',context)

	except Exception as e:    
   		print(type(e))   		

@login_required
def project_details1(request):
	try:
		client = InfluxDBClient(host='localhost' , port =8086 , database ='test1')
		results = client.query('SELECT time,value from wave ' )
		points = results.get_points()
		data = list()
		
		for point in points:
			entry = list()
			t = time.mktime(datetime.strptime(point['time'], "%Y-%m-%dT%H:%M:%S.%fZ").timetuple())	
			entry.append(int(t)*1000)
			entry.append(point['value'])
			data.append(entry)

		context = {
		'data' : json.dumps(data)
		}

		return render(request,'charts1.html',context)

	except Exception as e:    
   		print(type(e))   		