from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

text = "error 403"
key = 0
caesarCi = False
reflectCi = False
reverseCi = False
decryptCi = False

@app.route("/decrypt", methods=["GET", "POST"])
def decrypt():
    """Decrypt already encrypted plaintext"""
    if request.method == "POST":
        global decryptCi
        global caesarCi
        global reflectCi
        global reverseCi
        decryptCi = True
        state = request.form.get("dropdown")
        if state == "initial":
            return redirect("/decrypt")
        if state == "caesar":
            caesarCi = True
            global key
            key = int(request.form.get("number"))
        elif state == "reflect":
            reflectCi = True
        elif state == "reverse":
            reverseCi = True
        return redirect("/text")
    return render_template("decrypt.html")

@app.route("/", methods=["GET", "POST"])
def index():
    """Allow choice of cipher algorithm"""
    if request.method == "POST":
        global caesarCi
        global reflectCi
        global reverseCi
        global decryptCi
        state = request.form.get("dropdown")
        if state == "initial":
            return redirect("/")
        if state == "caesar":
            caesarCi = True
            global key
            key = int(request.form.get("number"))
        elif state == "reflect":
            reflectCi = True
        elif state == "reverse":
            reverseCi = True
        return redirect("/text")
    decryptCi = False
    caesarCi = False
    reflectCi = False
    reverseCi = False
    return render_template("index.html")

@app.route("/text", methods=["GET", "POST"])
def plaintext():
    """Submit text"""
    if request.method == "POST":
        global text
        text = request.form.get("plaintext")
        return redirect("/result")
    return render_template("plaintext.html")

@app.route("/result", methods=["GET", "POST"])
def result():
    """Result of cipher"""
    if request.method == "POST":
        return redirect("/")
    global decryptCi
    global text
    global key
    global caesarCi
    global reflectCi
    global reverseCi
    if decryptCi:
        if caesarCi:
            result = decaesar(text, key)
            caesarCi = False
        if reflectCi:
            result = reflect(text)
            reflectCi = False
        if reverseCi:
            result = reverse(text)
            reverseCi = False
        return render_template("result.html", text=result)
    if caesarCi:
        result = caesar(text, key)
        caesarCi = False
    if reflectCi:
        result = reflect(text)
        reflectCi = False
    if reverseCi:
        result = reverse(text)
        reverseCi = False
    return render_template("result.html", text=result)

def caesar(plaintext, key):
    cipher = ""
    for char in plaintext:
        if char.isalpha():
            num = ord(char)
            num = num + key
            if char.isupper():
                if num > ord('Z'):
                    num = num - 26
                elif num < ord('A'):
                    num = num + 26
            elif char.islower():
                if num > ord('z'):
                    num = num - 26
                elif num < ord('a'):
                    num = num + 26
            cipher = cipher + chr(num)
        else:
            cipher = cipher + char
    return cipher

def reflect(plaintext):
    cipher = ""
    for char in plaintext:
        if char.isalpha():
            num = ord(char)
            if char.isupper():
                if num >= ord('N'):
                    num = num - 13
                else:
                    num = num + 13
            elif char.islower():
                if num >= ord('n'):
                    num = num - 13
                else:
                    num = num + 13
            cipher = cipher + chr(num)
        else:
            cipher = cipher + char
    return cipher

def reverse(plaintext):
    cipher = ""
    i = len(plaintext) - 1
    while i >= 0:
       cipher = cipher + plaintext[i]
       i = i - 1
    return cipher

def decaesar(plaintext, key):
    cipher = ""
    for char in plaintext:
        if char.isalpha():
            num = ord(char)
            num = num - key
            if char.isupper():
                if num > ord('Z'):
                    num = num - 26
                elif num < ord('A'):
                    num = num + 26
            elif char.islower():
                if num > ord('z'):
                    num = num - 26
                elif num < ord('a'):
                    num = num + 26
            cipher = cipher + chr(num)
        else:
            cipher = cipher + char
    return cipher