from flask import Flask, render_template
import secrets
import os
from PIL import Image
from indisnacks import app
from .forms import SearchForm
import json
from ibm_watson import VisualRecognitionV3
from .keys import apikey, ver

visual_recognition = VisualRecognitionV3(
    ver,
    iam_apikey=apikey)

@app.route("/")
def home():
    return render_template('index.html')

def save_picture(form_picture, token):
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = token + f_ext
    picture_path = os.path.join(app.root_path, 'static/temp_img', picture_fn)
    list_pic = ['temp_pic', picture_fn]
    s = "/"
    s = s.join(list_pic)

    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return s

@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.image_file.data:
        f_name, f_ext = os.path.splitext(form.image_file.data.filename)
        token = secrets.token_urlsafe(4)
        save_picture(form.image_file.data, token)
        path = os.path.join(app.root_path, 'static/temp_img', token + f_ext)
        with open(path , 'rb') as images_file:
            classes = visual_recognition.classify(
            images_file,
            threshold='0.6',
            owners=["me"]).get_result()
            print(json.dumps(classes, indent=2))
            return render_template('res.html', classes = classes)
    return render_template('search.html', form = form)