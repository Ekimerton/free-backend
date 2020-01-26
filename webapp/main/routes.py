from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import io
import os

from google.cloud import vision
from google.cloud.vision import types

main = Blueprint('main', __name__)

# Endpoint for getting user info
@main.route("/")
@main.route("/user", methods=["GET"])
def user():
    return jsonify(
        username="Ekimmy",
        score="0"
    )

# endpoint for taking in picture
@main.route("/submit_pic", methods=['post'])
def submit_pic():
    image_file = request.files.get('imagefile', '').read()
    client = vision.ImageAnnotatorClient()
    image = types.Image(content=image_file)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    # Code for getting primary colours of an image, not used
    """
    colour_response = client.image_properties(image=image)
    props = colour_response.image_properties_annotation
    for color in props.dominant_colors.colors:
        print('fraction: {}'.format(color.pixel_fraction))
        print('\tr: {}'.format(color.color.red))
        print('\tg: {}'.format(color.color.green))
        print('\tb: {}'.format(color.color.blue))
        print('\ta: {}'.format(color.color.alpha))
    """

    target = "plastic"
    found = False
    for label in labels:
        if target in label.description.lower():
            found = True
            break
    return jsonify(
        validated=found
    )

