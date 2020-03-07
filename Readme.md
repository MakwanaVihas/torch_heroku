_**Info about required files:**_

The requirements.txt file:
  This contains information about libraries/packages heroku needs to install for running the app.

Procfile:
  This tells heroku which command to run to start your app.
  In this app it is:
    web: gunicorn example.wsgi --log-file -
runtime.txt file:
  It tells which version of python is needed for runtime:
    python-3.7.6 (for this app)

app.json:
  This contains info about your app name, app description, repo link, keywords etc.

_**DEPLOYING THE APP:**_

**Heroku CLI**:
  install heroku CLI according to https://devcenter.heroku.com/articles/getting-started-with-python#set-up and 
  login to your heroku account by typing:
    $ heroku login

**Cloning this repository**:
  go to cmd and type: 
    $ git clone https://github.com/MakwanaVihas/torch_heroku.git
    $ cd torch_heroku

**Create heroku app**:
  go to terminal and type:
  $ heroku create
  Heroku generates a random name for your app, or you can pass a parameter to specify your own app name.
   
  Or:
  $ heroku create app-name
  
  To rename your app afterwards run:
  $ heroku apps:rename the-new-name

**Deploying your code**:
  $ git push heroku master

**Open the app**:

  We can now tell Heroku to start this web process:
  $ heroku ps:scale web=1
  
  $ heroku open
  this opens the app in your default browser
