import json
import webbrowser
import requests
import csv

username = "ashwini95menon"

token = "0f10ca525a26da9ec86a8471b9473f4c7398c849"

sesn = requests.session()


def list_all_repos():
    googlerepo = ['name']
    url1 = "https://api.github.com/orgs/google/repos"
    authenticatn = sesn.get(url1, auth=(username, token))
    react_data = json.loads(authenticatn.text)
    # print(react_data)\
    for list_issues in authenticatn.json():
        googlerepo.append(list_issues['name'])

    googlerepos = list(zip(googlerepo))

    # print(googlerepo)
    return googlerepos

    ##with open('test_csv.csv', 'w') as file:

    ##    writer = csv.writer(file)
    ##    writer.writerows(googlerepos)


RepostList = list(list_all_repos())


# conert tuple to string
def convertTuple(tup):
    str = ''.join(tup)
    return str


## webpage from python
f = open('portal.html', 'w')

message = """<!DOCTYPE html>
<html>
<style>
body {

 font-style:Arvo;

}
/* The container */
.container {
  display: block;
  position: relative;
  padding-left: 35px;
  margin-bottom: 12px;
  cursor: pointer;
  font-size: 20px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
/* Hide the browser's default checkbox */
.container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}
/* Create a custom checkbox */
.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 20px;
  width: 20px;
  background-color: #eee;
}
/* On mouse-over, add a grey background color */
.container:hover input ~ .checkmark {
  background-color: #ccc;
}
/* When the checkbox is checked, add a blue background */
.container input:checked ~ .checkmark {
  background-color: white;
}
/* Create the checkmark/indicator (hidden when not checked) */
.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}
/* Show the checkmark when checked */
.container input:checked ~ .checkmark:after {
  display: block;
}
/* Style the checkmark/indicator */
.container .checkmark:after {
  left: 9px;
  top: 5px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}
.center {
  margin: auto;
  width: 50%;
  border: 3px solid green;
  padding: 10px;
}
.name{

  text-align: left;
    float:left;
}
.button {
  background-color: #008CBA;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
</style>
<body>
<center>
<h1 color="white"> GitHub Analytics </h1>
<div id="list">
<h3>Repositories</h3>
<div style="float:none; width:500px; height:200px; overflow:auto;"> 
<div class="name">
<ul>"""

# Creating List of repositories
for val in RepostList:
    message = message + "<li>" + convertTuple(val) + "</li>"

message = message + """</ul>
</div>
</div>
<button class="button" onclick="ShowCheckList()"><a href="uc1.htm">Create New View</a></button>
</div>
<!--Check Box Starts Here -->
<div id="disp_hide" style="display:none">
<h3>Please Select Repositories:</h3>
<div style="float:none; width:500px; height:200px; overflow:auto;"> 
<div class="name">"""

# creating checkbox repositories
for val in RepostList:
    message = message + """<label class="container">""" + convertTuple(val) + """<input type="checkbox" >
  <span class="checkmark"></span>
</label>"""
message = message + """</div>
</div>
<button class="button">Visualize</button>
</div>
</center>
<script>
function ShowCheckList() {
  var x = document.getElementById("disp_hide");
  if (x.style.display === "none") {
    x.style.display = "block";
  } 
  var y = document.getElementById("list");
  y.style.display = "none"
}
</script>
</body>
</html>"""

f.write(message)
f.close()
webbrowser.open_new_tab('portal.html')