import os
from flask import Flask, render_template, request, url_for, redirect, Blueprint
from app.models.Inputs import Inputs
from app import app, db


@app.route('/')
def index():
    return redirect(url_for("input.index"))
