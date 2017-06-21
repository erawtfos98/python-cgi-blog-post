#!/usr/bin/python
# -*- coding:utf8 -*-

# title=asdasdasd&date=2017-06-01&bg-color=bg-green&input=asdasdasd

import cgi
import cgitb
import json
import random

def post(post_id, title, date, bg_color, input_text):
    d = {}
    d[post_id] = {}
    d[post_id]['title'] = title
    d[post_id]['date'] = date
    d[post_id]['bg_color'] = bg_color
    d[post_id]['input_text'] = input_text
    return d

def toJSON(printfile):
        return json.dumps(printfile, indent=4)

def readFile():
    with open('database.json', 'r') as json_file:
        return json.load(json_file)

def wrap_data(data):
    old_data = readFile()
    old_data.update(data)
    return old_data

def writeFile(outfile):
    file = toJSON(wrap_data(outfile))
    f = open('database.json', 'wt', encoding='utf-8')
    f.write(file)

def get_new_id():
    return len(readFile())

def def_random_color():
    colors = [
    "bg-yellow",
    "bg-red",
    "bg-lightgrey",
    "bg-lightblue",
    "bg-green",
    "bg-winered",
    "bg-pink",
    "bg-purple",
    "bg-darkgreen",
    "bg-violet",
    "bg-navy",
    "bg-steelblue",
    "bg-turqoise",
    "bg-springgreen",
    "bg-honeydew",
    "bg-olivegreen",
    "bg-khaki",
    "bg-gold",
    "bg-orange",
    "bg-fire",
    "bg-salmon",
    "bg-black"
    ]
    d = readFile()
    old_color = d[str(int(get_new_id()) - 1)]['bg_color']
    new_color = random.choice(colors)
    if new_color is old_color:
      def_random_color()
    return new_color

def remove_post(post_id):
    if int(post_id) is not 0:
            d = readFile()
            a = d.pop(str(post_id), None)
            if a is not None:
                new_data = {}
                i = 0
                for key, value in d.items():
                    new_data[i] = value
                    i += 1
                f = open('database.json', 'wt', encoding='utf-8')
                f.write(toJSON(new_data))

def auth(user, pw):
    if user == "Franziska" and pw == "secure":
        return True
    return False

def write_session(state):
    f = open('session', 'wt', encoding='utf-8')
    f.write(str(state))

def read_session():
    with open('session', 'r') as myfile:
        data=myfile.read().replace('\n', '')
    return data

#-------------- website methods ----------------------------------------

def send_header():
    print("Content-Type: text/html")
    print("")
    print("""
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta name="description" content="A simple but fancy blog made with python/cgi for TH-Brandenburg Betriebssysteme/Webcomputing Sem. 2">
            <meta name="author" content="Franziska Schwarz">
            <link rel="icon" href="assets/ico/favicon.ico">
            <title>MyB10g</title>
            <link href="https://fonts.googleapis.com/css?family=Catamaran:100,200,300,400,500,600,700,800,900" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css?family=Muli" rel="stylesheet">
            <link href="css/bootstrap.min.css" rel="stylesheet">
            <link href="css/ie10-viewport-bug-workaround.css" rel="stylesheet">
            <link href="css/my.css" rel="stylesheet">
            <script src="js/ie-emulation-modes-warning.js"></script>
          </head>
          <body>
        """)
def send_index_nav():
    print("""
            <nav class="navbar navbar-inverse navbar-fixed-top">
              <div class="container">
                <div class="navbar-header">
                  <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                  </button>
                  <a class="navbar-brand">MyB10g</a>
                </div>
                <div id="navbar" class="navbar-collapse collapse">
                  <form class="navbar-form navbar-right" action="index.cgi?" method="Post">
                    <div class="form-group">
                      <input type="text" placeholder="Username" name="username" class="form-control">
                    </div>
                    <div class="form-group">
                      <input type="password" placeholder="Password" name="password" class="form-control">
                    </div> 
                    <button type="submit" class="btn btn-success">Sign in</button>
                  </form>
                </div>
              </div>
            </nav>
        """)
def jumbotron():
    print("""
            <div class="jumbotron">
              <div class="container">
                <h1>Hello, world!
                <br>
                This is a template for a simple marketing or informational website. It includes a large callout called a jumbotron and three supporting pieces of content. Use it as a starting point to create something more unique.</h1>
              </div>
            </div>
        """)
def blog_posts():
    print("""
    <div class="container-fluid">

      <div class="row bg-yellow">
        <div class="col-md-10 col-md-offset-1">
          <h2>Heading 2</h2>
          <p>30.05.2017</p>
          <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
        </div>
      </div>
      
    </div>
        """)
def footer():
    print("""
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="js/jquery.min.js"><\/script>')</script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
        """)

def editor_body():
    print("""
    <div class="container-fluid">
      <ul class="nav nav-tabs">
        <li role="presentation" class="active"><a href="index.cgi?editor=True">Editor</a></li>
        <li role="presentation"><a href="index.cgi?settings=True">Posts</a></li>
      </ul>
      <form action="index.cgi" method="GET" role="form">
        <div class="form-group">
          <div class="input-group">
            <span class="input-group-addon" id="basic-addon1">Titel:</span>
            <input type="text" class="form-control" aria-describedby="basic-addon1" name="title" value="" placeholder="Titel deines Beitrages" required>
            <span class="input-group-addon" id="basic-addon2">Datum:</span>
            <input type="date" class="form-control" aria-describedby="basic-addon2" name="date" value="" required>
            <span class="input-group-addon" id="basic-addon3">Hintergrundfarbe:</span>
            <select name="bg-color" class="form-control" aria-describedby="basic-addon3">
              <option value="random" selected> random </option>
              <option value="bg-yellow"> yellow </option>
              <option value="bg-red"> red </option>
              <option value="bg-lightgrey"> lightgrey </option>
              <option value="bg-lightblue"> lightblue </option>
              <option value="bg-green"> green </option>
              <option value="bg-winered"> winered </option>
              <option value="bg-pink"> pink </option>
              <option value="bg-purple"> purple </option>
              <option value="bg-darkgreen"> darkgreen </option>
              <option value="bg-violet"> violet </option>
              <option value="bg-navy"> navy </option>
              <option value="bg-steelblue"> steelblue </option>
              <option value="bg-turqoise"> turqoise </option>
              <option value="bg-springgreen"> springgreen </option>
              <option value="bg-honeydew"> honeydew </option>
              <option value="bg-olivegreen"> olivegreen </option>
              <option value="bg-khaki"> khaki </option>
              <option value="bg-gold"> gold </option>
              <option value="bg-orange"> orange </option>
              <option value="bg-fire"> fire </option>
              <option value="bg-salmon"> salmon </option>
              <option value="bg-black"> black </option>
            </select>
            <span class="input-group-btn">
              <button class="btn btn-success" type="submit">Submit!</button>
            </span>
          </div>
        </div>
        <div class="form-horizontal">
          <div class="form-group">
            <textarea class="form-control" rows="30" name="input" placeholder="And then..." required></textarea>
          </div>
        </div> 
      </form>
    </div>
        """)

def settings_body():
    print("""
<div class="container-fluid">
      <ul class="nav nav-tabs">
        <li role="presentation"><a href="index.cgi?editor=True">Editor</a></li>
        <li role="presentation" class="active"><a href="index.cgi?settings=True">Posts</a></li>
      </ul>
      
      <div class="container" id="settings">
        <h2>MyB10g Settings</h2>
        <p>This page is for editing or removing posts</p>            
        <table class="table table-hover">
          <thead>
            <tr>
              <th>Title</th>
              <th>Date</th>
              <th>Color</th>
              <th></th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Foo</td>
              <td>01.01.1990</td>
              <td>green</td>
              <td><a class="btn btn-primary" href="index.cgi?edit_id=id" role="button">Edit</a></td>
              <td><a class="btn btn-danger" href="index.cgi?remove_id=id" role="button">Delete</a></td>
            </tr>
          </tbody>
        </table>
      </div>

    </div>
        """)

def settings_and_editor_nav():
    print("""
<nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand">MyB10g</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <form class="navbar-form navbar-right">
            <a class="btn btn-danger" href="index.cgi?logout=True" role="button">Log Out</a>
          </form>
        </div>
      </div>
    </nav>
        """)

#----------------website calls ------------------------------------------

def frontpage():
    send_index_nav()
    jumbotron()
    blog_posts()

def text_editor():
    pass

def settings():
    pass

#------------- main -----------------------------------------------------

#jumbotron = post('0', 'jumbotron', '01-01-1990', 'no', """Hello World!""")
#jumbotron2 = post('1', 'jumbotron2', '01-01-1990', 'no', """Hello World!""")
#jumbotron3 = post('2', 'jumbotron3', '01-01-1990', 'no', """Hello World!""")
#jumbotron4 = post('{0}'.format(get_new_id()), 'jumbotron3', '01-01-1990', 'no', """Hello World!""")
#writeFile(jumbotron)
#writeFile(jumbotron2)
#writeFile(jumbotron3)

#database = readFile()

#print(type(database))
#print(len(database))
#print(toJSON(jumbotron4))
#writeFile(jumbotron4)
#print(def_random_color())

#for x in range(0,int(get_new_id())):
#  remove_post(x)

#remove_post(0)
# ------------------------- field storage and handling ---------------------------------------------
cgitb.enable()
logged_in = False
logout = False
session = read_session()

send_header()

form = cgi.FieldStorage(
    environ={'REQUEST_METHOD':'POST'})

if "password" and "username" in form:
    pw = form["password"].value
    user = form["username"].value
    logged_in = auth(user, pw)

if "editor" not in form:
    editor = False
elif "settings" not in form:
    settings = False
elif "logout" in form:
    logout = form["logout"].value
elif "title" not in form:
    title = "Undefined"
elif "date" not in form:
    date = "1990-01-01"
elif "bg-color" not in form:
    bg_color = "random"
elif "input" not in form:
    input = "And then..."
elif "edit_id" not in form:
    edit_id = -1
elif "remove_id" not in form:
    remove_id = -1
# --------------------------- site content logic ---------------------------------------------------

if not logged_in and not session:
    frontpage()
elif logout:
    write_session(False)
    frontpage()
elif logged_in:
    settings_and_editor_nav()
    editor_body()
elif logged_in and editor:
    write_session(True)
    settings_and_editor_nav()
    editor_body()
elif session and settings:
    settings_and_editor_nav()
    settings_body()
#else:
#    frontpage()

footer()

