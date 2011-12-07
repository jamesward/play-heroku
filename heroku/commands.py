import os
import subprocess
import sys

# Here you can create play commands that are specific to the module, and extend existing commands

MODULE = 'heroku'

# Commands that are specific to your module

COMMANDS = ['heroku:deploy']

def execute(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")

    if command == "heroku:deploy":
        print "~ Deploying app to Heroku"
        java_cmd = app.java_cmd(args, None, "play.modules.heroku.Deploy")
        subprocess.call(java_cmd, env=os.environ)
        print "~ App Deployed"


# This will be executed before any command (new, run...)
def before(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")


# This will be executed after any command (new, run...)
def after(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")

    if command == "new":
        pass
