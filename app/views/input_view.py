import os
from flask import Flask, render_template, request, url_for, redirect, Blueprint
from app.models.Inputs import Inputs
from app import app, db

input_blueprint = Blueprint("input", __name__, url_prefix="/input")

@input_blueprint.route('/')
def index():
    inputs = Inputs.query.all()
    return render_template('index.html', inputs=inputs)

@input_blueprint.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        ipaddress = request.form['ipaddress']
        dispatcher = request.form['dispatcher']
        ipversion = request.form['ipversion']
        note = request.form['note']
        inputs = Inputs(ipaddress=ipaddress,
                          dispatcher=dispatcher,
                          ipversion=ipversion,
                          note=note)
        db.session.add(inputs)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('create.html')


@input_blueprint.route('/<int:input_id>/edit/', methods=('GET', 'POST'))
def edit(input_id):
    input = Inputs.query.get_or_404(input_id)

    if request.method == 'POST':
        ipaddress = request.form['ipaddress']
        dispatcher = request.form['dispatcher']
        ipversion = request.form['ipversion']
        note = request.form['note']

        input.ipaddress=ipaddress
        input.dispatcher=dispatcher
        input.ipversion=ipversion
        input.note=note

        db.session.add(input)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', input=input)


@input_blueprint.post('/<int:input_id>/delete/')
def delete(input_id):
    input = Inputs.query.get_or_404(input_id)
    db.session.delete(input)
    db.session.commit()
    return redirect(url_for('index'))
