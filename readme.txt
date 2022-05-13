Requires dependencies listed in requirements.txt
Can be run without any arguments:

> python app.py

A development server is started at runtime, and runs at http://127.0.0.1:5000
There is one endpoint, '/test'
'/test' returns a JSON object with a return string, based on an HTTP POST request made to http://127.0.0.1:5000/test that must include a JSON string with a 'string_to_cut' key
'Invalid request' is returned in the case that there is a 400 error