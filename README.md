# weather_forecast

A python script which displays weather data of the location given by the user as a desktop notification

## Libraries used

- `requests`
- `notify-py`

## Prerequisites

Make an account on <a href = "https://openweathermap.org/">OpenWeather</a> for the weather API and KEY

## Read documentations about

<a href = "https://requests.readthedocs.io/en/latest/">requests</a>

<a href = "https://pypi.org/project/notify-py/">notify-py</a>

<a href = "https://openweathermap.org/current">open weather API</a>

## Run locally

You will need to install python on you system, head over to this link: https://www.python.org/downloads/ for download python

(Dont forget to tick Add Python to PATH while installing python)

Once you have downloaded Python on your system, run the following command inside your terminal (only if your system is git enabled, otherwise download the zip file and extract it)

```bash
  git clone https://github.com/milan-sony/weather_forecast.git
```

Then go to the project folder

```bash
  cd weather_forecast
```

(This is optional, but strongly recommended) Make a virtual environment

```bash
  python -m venv venv
```

Then activate the virtual environment

```bash
  venv/Scripts/activate
```

If error occurs when activating virtual environment, run the following command

```bash
  Set-ExecutionPolicy Unrestricted
```

or

```bash
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

Install the dependencies needed for this project

```bash
  pip install -r requirements.txt
```

Now paste your OpenWeather API KEY inside the `secret.py` file

Then run the script

```bash
  python main.py
```

## Working

When you run the script it will ask your location (Please try to give a major city name as your location), then it will check whether that given location is available on not on OpenWeather

It the location is found, it will make a popup windows notification for each 15 min showing the current weather details of the location you have given 

<img src="screenshots/Screenshot 1.png">

<img src="screenshots/Screenshot 2.png">

<img src="screenshots/Screenshot 3.png">

## Points to be noted

You can change the notification details, Weather API and all as per your need

There may be some faults while running the program (If any error occurs exit the code `ctrl + c` and run again `python main.py`)

## Future updates

- Add weather alerts 
- Make the program run on background
- WebApp
