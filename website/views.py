from flask import Blueprint, render_template, request,flash,jsonify
from flask_login import login_required,current_user
from .models import Note, User
from . import db
import json


views = Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')

    return render_template("home.html", user=current_user)

@views.route('/profile',methods=['GET','PUT','POST'])
@login_required
def profile():

    if request.method == 'POST':
        user = User.query.get(current_user.id)
        user.first_name = request.form.get('first_name')

        # Add check if email is unique
        user.email = request.form.get('email')
        db.session.commit()


    return render_template("profile.html", user=current_user)



@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/edit-note', methods=['POST'])
def edit_note():

    data = request.form.get('edit_note')
    #print(data)
    data = request.form.get('note')
    #print(data)

    request_data = request.data
    print(request_data)

    noteJSON = json.loads(request.data)
    noteId = noteJSON['noteId']
    note = Note.query.get(noteId)

    if note:
        if note.user_id == current_user.id:
            
            noteData = noteJSON['noteData']
            print(noteData)
            note.data = noteData
            db.session.commit()

    return jsonify({})