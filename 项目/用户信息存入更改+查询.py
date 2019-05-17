from flask import Flask,request
#import 项目.xianshiing as xianshiing
from 项目.xianshiing import xs
class YX(object):
    def __init__(self,name,xuehao):
        self.name = name
        self.xuehao = xuehao
yx=Flask(__name__)
xinxi = {}
@yx.route('/cunru',methods=['POST'])
def cunru():
    if not request.is_json:
        return"未选择JSON模式"
    name = request.args.get('name',None)
    xuehao = request.args.get('xuehao',None)
    if (not name) or (not xuehao):
        return"请输入新用户信息"
    if not name:
        return"请输入新用户名字"
    if not xuehao:
        return"请输入新用户学号"
    gainame = xinxi.get(name,None)
    if (name in xinxi) and (xuehao == gainame.xuehao ):
        return"该用户信息已保存过"
    if (name in xinxi) and (xuehao != gainame.xuehao ):
        gainame.xuehao = xuehao
        return"该用户信息已更改并保存;现用户信息为："+"用户"+gainame.name+"的学号为："+gainame.xuehao
    xinxi[name]=YX(name,xuehao)
    return"已保存新用户信息"
@yx.route('/chaxun',methods=['POST'])
def chaxun():
    if not request.is_json:
        return"未选择JSON模式"
    name = request.args.get('name',None)
    xuehao = request.args.get('xuehao',None)
    if not name:
        return"请输入用户姓名"
    if name not in xinxi:
        return"未存入该用户信息"
    youname = xinxi.get(name,None)
    if name in xinxi:

        return youname.name+"的学号为"+youname.xuehao
#yx.register_blueprint(xianshiing.xianshi)
yx.register_blueprint(xs,b='/xianshi')

if __name__=='__main__':
    yx.run(debug=True,port=5011)
