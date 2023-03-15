from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ImageSample(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    upload_time = db.Column(db.DateTime, default=datetime.utcnow())
    image_content = db.Column(db.String(1024 * 1024 * 10))
    bbox_x = db.Column(db.Float)
    bbox_y = db.Column(db.Float)
    bbox_width = db.Column(db.Float)
    bbox_height = db.Column(db.Float)
    label = db.Column(db.String(50))

    def __repr__(self) -> str:
        return f'<ImageSample {self.id}>'
