from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_mapping(SQLALCHEMY_DATABASE_URI='postgresql://postgres:admin@localhost:5432/admin')
db = SQLAlchemy(app)



class Advertisement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    header = db.Column(db.String(100), nullable=False)
    definition = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.now)

    def __str__(self):
        return '<Advertisement {}>'.format(self.username)

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            "header": self.header,
            'definition': self.definition,
            'created_on': self.created_on
        }




@app.route('/api/get/<int:advertisement_id>', methods=['GET', ])
def get_adv(advertisement_id):
    advertisement = Advertisement.query.get(advertisement_id)
    return jsonify(advertisement.to_dict())



@app.route('/api/post', methods=['POST', ])
def post_adv():
    advertisement = Advertisement(**request.json)
    try:
        db.session.add(advertisement)
        db.session.commit()
        return jsonify(advertisement.to_dict())
    except:
        return 'Ошибка'


@app.route('/api/delete/<int:advertisement_id>', methods=['DELETE', ])
def delete_adv(advertisement_id):
    advertisement = Advertisement.query.get(advertisement_id)
    try:
        db.session.delete(advertisement)
        db.session.commit()
        return jsonify(advertisement.to_dict())
    except:
        return 'Ошибка'


@app.route('/api/put/<int:advertisement_id>', methods=['PUT', ])
def put_adv(advertisement_id):
    advertisement = Advertisement.query.get(advertisement_id)
    db.session.delete(advertisement)
    advertisement = Advertisement(**request.json)
    db.session.add(advertisement)
    db.session.commit()
    return jsonify(advertisement.to_dict())




if __name__ == '__main__':
    app.run()