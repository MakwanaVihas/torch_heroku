_**Info about required files:**_

**The requirements.txt file**:<br />
 &nbsp; &nbsp;  This contains information about libraries/packages heroku needs to install for running the app.<br />

**Procfile**:<br />
   &nbsp;&nbsp;  This tells heroku which command to run to start your app.<br />
   &nbsp;&nbsp;  In this app it is:<br />
   &nbsp;&nbsp;  web: gunicorn example.wsgi --log-file -<br />
**runtime.txt file**:<br />
   &nbsp;&nbsp;  It tells which version of python is needed for runtime:<br />
   &nbsp;&nbsp;  python-3.7.6 (for this app)<br />

**app.json**:<br />
   &nbsp;&nbsp;  This contains info about your app name, app description, repo link, keywords etc.<br />

_**DEPLOYING THE APP:**_<br />

**Heroku CLI**:<br />
   &nbsp;&nbsp;  install heroku CLI according to https://devcenter.heroku.com/articles/getting-started-with-python#set-up <br />
   &nbsp;&nbsp;  login to your heroku account by typing:<br />
   &nbsp;&nbsp;   `$ heroku login`<br />

**Cloning this repository**:<br />
   &nbsp;&nbsp;  go to cmd and type: <br />
   &nbsp;&nbsp; `$ git clone https://github.com/MakwanaVihas/torch_heroku.git`<br />
   &nbsp;&nbsp; `$ cd torch_heroku`<br />

**Create heroku app**:<br />
  &nbsp;&nbsp;  go to terminal and type:<br />
  &nbsp;&nbsp;  `$ heroku create`<br />
  &nbsp;&nbsp;  Heroku generates a random name for your app, or you can pass a parameter to specify your own app name.<br />
   
  &nbsp;&nbsp;  Or:<br />
  &nbsp;&nbsp;  `$ heroku create app-name`<br />
  
  &nbsp;&nbsp;  To rename your app afterwards run:<br />
  &nbsp;&nbsp;  `$ heroku apps:rename the-new-name`<br />

**Deploying your code**:<br />
  &nbsp;&nbsp;  `$ git push heroku master`<br />

**Open the app**:<br />

  &nbsp;&nbsp;  We can now tell Heroku to start this web process:<br />
  &nbsp;&nbsp;  `$ heroku ps:scale web=1`<br />
  
  &nbsp;&nbsp;  `$ heroku open`<br />
  &nbsp;&nbsp;  this opens the app in your default browser<br />
