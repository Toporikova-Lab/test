from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import Required, DataRequired
from flask_bootstrap import Bootstrap
import pixels
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap(app)

filename = ''

class ImageUploadForm(Form):
    image = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])

#Allow user to upload image, save image to images folder
@app.route('/', methods = ['GET', 'POST'])
def starter():
    form = ImageUploadForm()
    if form.validate_on_submit():
        image_dir = os.path.join(os.path.dirname(app.instance_path), 'images')
        f = form.image.data
        global filename
        filename = secure_filename(f.filename)
        f.save(os.path.join(image_dir, filename))
        print(filename)
        flash("Image saved successfully.")
        return redirect(url_for("display_pixels"))
    return render_template('image_upload.html', form=form)

#Calculate number of pixels in image
@app.route('/pixels', methods = ['GET', 'POST'])
def display_pixels():
    #pixels.pixelcount()
    global filename
    pixelnum = pixels.pixel_count(filename)
    return render_template("pixelnum.html", pixelnum=pixelnum)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
