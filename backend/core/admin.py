from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from core.models import ImageSample, db

admin = Admin()


class ImageSampleView(ModelView):
    column_exclude_list = ['image_content']


admin.add_view(ImageSampleView(ImageSample, db.session))
