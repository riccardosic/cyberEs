# ES - (SSE)Security Software Engineering

TEAM:
- *Aliprandi Federico*: `Programmer`
- *Benedetti Pietro*: `Jolly`
- *Erbisti Filippo*: `Scientist`
- *Sicchieri Riccardo*: `Engineer`

## Statement

[Link guide](https://edu.v-research.it/security_engineering_2021/)

- - -
• Creation Login System *without* password
- - -

Primarily for the correct operation you need to open Whatsapp Web on browser and login

## Installation

1. Run `git clone git@github.com:v-research/securityengineering.git`

2. Check if Python is installed:
   - Enter in `/project` directory
   - Enter in `/cyberES` directory
   - Run `python --version` and `which python` to check versione and installation directory

3. Install packages from **requirements.txt**:
```
pip install -r requirements.txt 
```

(Probably it required package flask, in that case install it ```pip install flask```)

## Start Project

1. Create virtual environment with:
```
python -m venv venv
```

2. Activate the virtual environment:

**For Windows**
```
venv/Scripts/activate
```

**For Unix**
```
source venv/bin/activate
```

To close Project use in terminal: ```deactivate```


## Run Project

In the `/follow-project` split the terminal and run:

```
python server.py
```

If server start correctly, run:

```
python client.py
```

In terminal, it ask for a cell number, enter a correct phone number and send.
This automatically open another Whatsapp Web Tab's and generate a randomic hash 20 characters, 
after a few seconds you can see the start of the chat and send the password.
`
Then enter the password received. If all is correct it prints 'connessione sicura', else 'connessione non riuscita' and close connection. 
