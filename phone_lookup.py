from flask import Flask, render_template, request
import json 
import urllib.request

app = Flask(__name__)

@app.route('/phone', methods = ['POST', 'GET'])
def iplook():
	error = None
	if request.method == 'POST':
		numberDetails = request.form
		phone_num = numberDetails['phone_number']
		country_code = numberDetails['country_code']


		api_key = 'API_KEY'
		source = urllib.request.urlopen(f'http://apilayer.net/api/validate?access_key={api_key}&number={phone_num}&country_code={country_code.upper()}&format=1')
		# converting JSON data to a DICT
		list_of_data = json.load(source)

		# data for variable list_of_data
		data = {
			"phone_num": phone_num,
			"valid": list_of_data['valid'],
			"number": list_of_data['number'],
			"country_name": list_of_data['country_name'],
			"country_code": list_of_data['country_code'],
			"location": list_of_data['location'],
			"carrier": list_of_data['carrier'],
			"line_type": list_of_data["line_type"],
			"country_prefix": list_of_data["country_prefix"],
			"international_format": list_of_data["international_format"]
		}
		if data['valid'] != "true":
			error = "Invalid Phone Number. Please try again."
		else:
			return render_template('number.html', data=data, error=error)
	else:
		data = {
			"phone_num": "N/A",
			"valid": "N/A",
			"number": "N/A",
			"country_name": "N/A",
			"country_code": "N/A",
			"location": "N/A",
			"carrier": "N/A",
			"line_type": "N/A",
			"country_prefix": "N/A",
			"international_format": "N/A"
		}
		return render_template("number.html", data=data, title = 'Phone Number Lookup')

if __name__ == '__main__':
	app.run()
