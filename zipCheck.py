import requests
import json

#python 3.6.7
#function for checking for a valid zipcode
def zipchecker(zipcode):

	resp = requests.get('http://postcodes.io/postcodes/' + zipcode + '/validate')

	#test for response from api
	if resp.status_code != 200:
		raise ApiError('GET /tasks/ {}'.format(resp.status_code))
	json_data = json.loads(resp.text)

	#determine if json_data result is boolean val true
	if json_data['result'] == True:
		return True
	else:
		return False

#function for retrieving country and region
def getCountry(zipcode):

	resp = requests.get('http://postcodes.io/postcodes/'+zipcode)

	if resp.status_code != 200:
		raise ApiError('GET /tasks/ {}'.format(resp.status_code))
	json_data = json.loads(resp.text)

	print('Country: '+json_data['result']['country'])
	print('Region: '+json_data['result']['region'])

#list nearest postcodes and country/region
def nearest(zipcode):

	resp = requests.get('http://postcodes.io/postcodes/' + zipcode + '/nearest')

	if resp.status_code != 200:
		raise ApiError('GET /tasks/ {}'.format(resp.status_code))
	json_data = json.loads(resp.text)

	print('Nearest:')

	#loop through nested json data to return only relative information
	for near in json_data['result']:
		print('   Country: '+near['country'])
		print('   Region: '+near['region'])
		print('   Postcode: '+near['outcode']+' '+near['incode'])
		print('')

def isBlank (zipcode):
	return not (zipcode and zipcode.strip())

def main():

	zipcode  = input('Enter post code:')

    #while valid zip perform other functions else call back main
	while zipchecker(zipcode) == True and isBlank(zipcode) == False :
		print('Valid Postcode')
		getCountry(zipcode)
		nearest(zipcode)
		main()
		break
	else:
		print('Invalid Postcode')
		main()

main()