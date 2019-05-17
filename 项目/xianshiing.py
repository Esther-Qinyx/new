from flask import Blueprint
xs = Blueprint('xs',__name__)
@xs.route('/xianshi',methods=['POST'])
def xianshi():
    return "hello world"