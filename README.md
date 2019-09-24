## Install

1. Open page of repository of the script https://github.com/vladiscripts/detail1688 (this page). 
(If shown `page 404` it's perhaps this repository is *private*, then ask me add you to contributor.) 

2. In top-right corner there is a green button `Clone or download`. 

    You can download the ZIP with script... 

    But better clone it for ability to get my updates. It's also better for installation on a hosting server.
    
    #### To clone:
    
    a. Install Git, if not already installed: https://git-scm.com/downloads. Usualy on hostings it already made. 
    
    b. Press this green button and copy the HTTPS link to this repository.
    
    c. Open a command prompt in folder where you want to download the script folder.
        (In Windows, to open a command prompt window in any folder, in File Explorer simply hold down the **Shift** key and **right click** on the folder. In the context menu, you will see the option **PowerShell** or **Open command window here**. Click on it, will open a CMD window.
        https://www.thewindowsclub.com/how-to-open-command-prompt-from-right-click-menu)
        
    d. Download the scripts by print there:
    
    `git clone <url from green button>`
    
    c. Go to new created folder with name of the repo:
    
    `cd <folder name>`

3. Perhaps, you want to create a python environment, or not:

    `python3 -m venv /path/to/new/virtual/env`

4. Install python dependencies of the script:

    `pip install -U -r requirements.txt`

# Run
For run on Windows you can use the files `.cmd`. 

To run this script on your PC (personal computer) in CMD print and run `python manage.py runserver` in the script's folder.
(Or run `start_local_server.cmd`)

It will run a local server, now in a browser you can open interface on url http://127.0.0.1:8000.

## Run a server and deploy
The script use "Django" - Python's framework to creating sites. 

On differ web hostings can be differ way to run server.
To better see help for this hosting on its site or in internet. https://www.google.com/search?q=django%20deploy

Also, need to switch value of variable `DEBUG = True` to `False`. 
It located in path `detail/detail/setting.py`. Edit it by text editor.

The following are a some links to Help about *How to deploy Django* on the largest half-free hosting services:

_pythonanywhere_ (on Free plan have not ability to scrape other sites, paid plans begins $5/mo)
* https://tutorial.djangogirls.org/en/deploy/
* https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/

_heroku_ (can be difficult)
* https://devcenter.heroku.com/articles/deploying-python

Also there are: AWS (Amazon, 1st year is free), Google Clouds (same). Digitalocean, etc.
