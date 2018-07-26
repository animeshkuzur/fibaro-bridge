# fibaro_data_extractor
A simple python script to map the Fibaro room schematic and collect all the event log onto a .csv file. The temperature logs and electricity consumption logs are still in development.

#### Prerequisite
* Python == ^3.5.*
* Requests == ^2.18.*
* Git

#### Setup Instructions
* First check the Python version installed on your machine `python --verison` if the python version is >= `3.5.5` then you're good to go!
* Install all the required python modules `pip install -r requirements.txt`
* After successful installation, clone this repository `git clone https://github.com/animeshkuzur/fibaro_data_extractor.git`
* Copy and rename the `config.json.example` file to `config.json`
* Change the following values inside the file: `fibaro_ip`,`username` and `password`
```json
{
	"app":{
		"fibaro_ip":"127.0.0.1",
		"base_url":"http://localhost/api/",
		"username":"username",
		"password":"password",
		"env":"local",
		"debug":"true"
	},
	"mysql":{
		"host":"localhost",
		"user":"root",
		"password":"password",
		"database":"database"
	},
	"data":{
		"filename":"./data/data.csv"
	}
}
```

#### Execute Instructions
* To execute the program, `cd` into the project directory and run `python run.py`

> The data is collected under the `data` directory of the project folder.