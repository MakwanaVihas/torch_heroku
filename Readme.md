_**Info about required files:**_

The requirements.txt file:<br />
&nbspThis contains information about libraries/packages heroku needs to install for running the app.<br />

Procfile:<br />
  This tells heroku which command to run to start your app.<br />
  In this app it is:<br />
    web: gunicorn example.wsgi --log-file -<br />
runtime.txt file:<br />
  It tells which version of python is needed for runtime:<br />
    python-3.7.6 (for this app)<br />

app.json:<br />
  This contains info about your app name, app description, repo link, keywords etc.<br />

_**DEPLOYING THE APP:**_<br />

**Heroku CLI**:<br />
  install heroku CLI according to https://devcenter.heroku.com/articles/getting-started-with-python#set-up <br />
  login to your heroku account by typing:<br />
    $ heroku login<br />

**Cloning this repository**:<br />
  go to cmd and type: <br />
    $ git clone https://github.com/MakwanaVihas/torch_heroku.git<br />
    $ cd torch_heroku<br />

**Create heroku app**:<br />
  go to terminal and type:<br />
  $ heroku create<br />
  Heroku generates a random name for your app, or you can pass a parameter to specify your own app name.<br />
   
  Or:<br />
  $ heroku create app-name<br />
  
  To rename your app afterwards run:<br />
  $ heroku apps:rename the-new-name<br />

**Deploying your code**:<br />
  $ git push heroku master<br />

**Open the app**:<br />

  We can now tell Heroku to start this web process:<br />
  $ heroku ps:scale web=1<br />
  
  $ heroku open<br />
  this opens the app in your default browser<br />
