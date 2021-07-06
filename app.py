from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'
if ENV =='dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yourpasswordhere@localhost/MuseByte'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = '' 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db = SQLAlchemy(app)
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key= True)
    profession = db.Column(db.String(200))
    purpose = db.Column(db.String(200))
    usability_rating = db.Column(db.Integer)
    quickmemo_rating = db.Column(db.Integer)
    comments = db.Column(db.Text())
    ip_address = db.Column(db.String(100))

    def __init__(self,profession,purpose,usability_rating,quickmemo_rating,comments,ip_address):
        self.profession = profession
        self.purpose = purpose
        self.usability_rating = usability_rating
        self.quickmemo_rating = quickmemo_rating
        self.comments = comments
        self.ip_address = ip_address
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    if request.method =='POST':
        profession = request.form['profession']
        purpose = request.form['purpose']
        usability_rating = request.form['usability']
        quickmemo_rating = request.form['quickmemo']
        comments = request.form['comments']
        ip_address = request.remote_addr
        #print (comments,profession, ip_address)
        if profession == '' or purpose =='':
            return render_template('index.html', message='Please enter required fields')
        if db.session.query(Feedback).filter(Feedback.ip_address == ip_address).count()==0:
            data = Feedback(profession,purpose,usability_rating,quickmemo_rating,comments,ip_address)
            db.session.add(data)
            db.session.commit()
            return render_template('completed.html')

        if db.session.query(Feedback).filter(Feedback.ip_address == ip_address).count()==1:
            print (db.session.query(Feedback).filter(Feedback.ip_address == ip_address).count())
            db.session.query(Feedback).filter(Feedback.ip_address == ip_address).delete()
            print ('after', db.session.query(Feedback).filter(Feedback.ip_address == ip_address).count())
            data = Feedback(profession,purpose,usability_rating,quickmemo_rating,comments,ip_address)
            db.session.add(data)
            db.session.commit()    
            return render_template('completed.html')

if __name__ =='__main__':
    
    app.run() #to run server