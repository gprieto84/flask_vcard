from flask import render_template, flash, send_file
from app import app
from app.forms import Generadorqr
from app.models import User
from segno import helpers
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import os

@app.route('/', methods=['GET', 'POST'])
def index():
    form = Generadorqr()
    if form.validate_on_submit():
        user = User.query.filter_by(correo=form.email.data).first()
        if user is None:
            flash('Usuario no existe')
        else:
            qr = helpers.make_vcard(name=((user.nombres)+' '+(user.apellidos)),
                        displayname=((user.nombres)+' '+(user.apellidos)),
                        title=(user.puesto+" -"+user.area), 
                        org=(user.empresa),
                        city=(user.ciudad),
                        zipcode=('20001'),
                        country=('Colombia'),
                        phone=[user.celular,user.extension], 
                        email=(user.correo), 
                        url= (user.pagina_web))
            qr.save('qr.png', scale=3, border=0)

            qr_code = Image.open('qr.png')
            base = Image.open('base.PNG')
            background = base.copy()
            background.paste(qr_code, (86, 248))
            background.save('qr_code.png', quality=100)

            im = Image.new("RGB", (500, 25), (255, 255, 255))
            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype('tahomabd.ttf', 20)
            draw.multiline_text((0, 0), user.nombres, fill=(0, 41, 130), font=font)
            im.save('nombres.png',quality=100)

            im = Image.new("RGB", (500, 25), (255, 255, 255))
            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype('tahoma.ttf', 20)
            draw.multiline_text((0, 0), user.apellidos, fill=(0, 41, 130), font=font)
            im.save('apellidos.png',quality=100)

            im = Image.new("RGB", (353, 18), (255, 255, 255))
            draw = ImageDraw.Draw(im)
            font = ImageFont.truetype('tahoma.ttf', 12)
            w, h = draw.textsize(user.puesto)
            draw.text(((353-w)/2,(18-h)/2), user.puesto, fill=(0, 41, 130), font=font)
            im.save('puesto.png',quality=100)

            background = Image.open('qr_code.png')
            nombres = Image.open('nombres.png')
            apellidos = Image.open('apellidos.png')
            puesto = Image.open('puesto.png')
            background.paste(nombres, (53, 131))
            background.paste(apellidos, (53, 158))
            background.paste(puesto, (0, 199))
            background.save('qr_code.png', quality=100)
            return send_file('../qr_code.png', mimetype='image/jpeg', attachment_filename=user.correo.split('@')[0]+'.png', as_attachment=True)
       
    return render_template('index.html', form= form)
