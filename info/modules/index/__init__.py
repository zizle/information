# _*_ coding:utf-8 _*_

from flask import Blueprint

index_blue = Blueprint('index', __name__)

from . import views
