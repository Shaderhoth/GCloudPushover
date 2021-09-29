import os
import http.client, urllib
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
app = Flask(__name__)

bot_token = str(os.getenv('BOT_TOKEN'))
usr_token = str(os.environ.get('USR_TOKEN'))
flask_secret = str(os.environ.get('FLASK_SECRET'))

class MsgForm(FlaskForm):
    msg = StringField('Enter custom msg (not required): ')
    submit = SubmitField('Send')
    
app.config['SECRET_KEY'] = flask_secret
Bootstrap(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    form = MsgForm()
    title = str(request.args.get('title'))
    
    message = ""
    if form.validate_on_submit():
        msg = str(form.msg.data)
        
        ctx = request.headers.get('User-Agent')
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
          urllib.parse.urlencode({
            "token": bot_token,
            "user": usr_token,
            "message": str(title) + " \n" + str(msg) + " \n" + str(ctx),
          }), { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()
        message = "Message sent"
    return render_template('index.html', form=form, message=message)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
