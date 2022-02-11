- Filippo Erbisti : Scientist
- Riccardo Sicchieri : Engineer
- Federico Aliprandi : Programmer
- Pietro Benedetti : Jolly

Primarily for the correct operation you need to open Whatsapp Web on browser and login

# Start the Project

1. Create virtual environment with:
```
python -m venv v_env_x1
```

2. `cd v_env_x1`

3. Activate the virtual environment:

**For Windows**
```
. Scripts/activate
```

**For IOS**
```
. bin/activate
```

4. Enter into `/follow-project`

5. Install packages from **requirements.txt**:
```
pip install -r ../requirements.txt 
```

(Probably it required package flask, in that case install it ```pip install flask```)

To close Project use in terminal: ```deactivate```


# Run Project

In the `/follow-project` split the terminal and run:

```
python server.py
```

It start server, if all is correct run:

```
python client.py
```

It ask for a cell number, enter a correct phone number and send.
This automatically open another Whatsapp Web Tab's and generate a randomic hash 20 characters, 
after a few seconds you can see the start of the chat and send the password.