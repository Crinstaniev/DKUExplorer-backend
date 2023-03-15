from datetime import datetime

from flask import Blueprint, Flask, jsonify, request, current_app
from flask_sqlalchemy import SQLAlchemy
from core.models import ImageSample, db
from core.utils.helper_functions import hex_to_byte
from flask_cors import cross_origin

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return "Hello, this is DKUAR Backend!"

@bp.route('/health')
@cross_origin()
def health():
    return jsonify({
        'status': 'OK',
        'message': 'Backend is running.',
        'time': f'{datetime.now()}'
    })


@bp.route('/image_samples', methods=['POST'])
@cross_origin()
def create_image_sample():
    # Create new image sample
    data = request.get_json()
    new_image_sample = ImageSample(
        image_content=data['image_content'],
        bbox_x=data['bbox_x'],
        bbox_y=data['bbox_y'],
        bbox_width=data['bbox_width'],
        bbox_height=data['bbox_height'],
        label=data['label']
    )
    db.session.add(new_image_sample)
    db.session.commit()
    return jsonify({'message': 'New image sample created.'})


@bp.route('/image_samples', methods=['GET'])
def get_all_image_samples():
    # Get all image samples
    image_samples = ImageSample.query.all()
    output = []
    for image_sample in image_samples:
        image_sample_data = {}
        image_sample_data['id'] = image_sample.id
        image_sample_data['upload_time'] = image_sample.upload_time
        image_sample_data['bbox_x'] = image_sample.bbox_x
        image_sample_data['bbox_y'] = image_sample.bbox_y
        image_sample_data['bbox_width'] = image_sample.bbox_width
        image_sample_data['bbox_height'] = image_sample.bbox_height
        image_sample_data['label'] = image_sample.label
        output.append(image_sample_data)
    return jsonify({'image_samples': output})


@bp.route('/image_samples/<id>', methods=['GET'])
def get_image_sample(id):
    # Get single image sample
    image_sample = ImageSample.query.get_or_404(id)
    image_sample_data = {}
    image_sample_data['id'] = image_sample.id
    image_sample_data['upload_time'] = image_sample.upload_time
    image_sample_data['bbox_x'] = image_sample.bbox_x
    image_sample_data['bbox_y'] = image_sample.bbox_y
    image_sample_data['bbox_width'] = image_sample.bbox_width
    image_sample_data['bbox_height'] = image_sample.bbox_height
    image_sample_data['label'] = image_sample.label
    return jsonify({'image_sample': image_sample_data})


@bp.route('/image_samples/<id>', methods=['PUT'])
def update_image_sample(id):
    # Update image sample
    image_sample = ImageSample.query.get_or_404(id)
    data = request.get_json()
    image_sample.image_content = data['image_content']
    image_sample.bbox_x = data['bbox_x']
    image_sample.bbox_y = data['bbox_y']
    image_sample.bbox_width = data['bbox_width']
    image_sample.bbox_height = data['bbox_height']
    image_sample.label = data['label']
    db.session.commit()
    return jsonify({'message': 'Image sample updated.'})
