from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# api实例化
api = Api(app)

username = "root"
password = "123456"
ip = "47.98.61.20"
port = "3306"
database = "test_platform"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{ip}:{port}/{database}?charset=utf8'
# 数据库关联flask
db = SQLAlchemy(app)


class TestCase(db.Model):
    __tablename__ = "testcase"
    id = db.Column(db.Integer, primary_key=True)
    nodeid = db.Column(db.String(80), nullable=False)
    remark = db.Column(db.String(120))


# 类代表是哪个接口资源，每个方法，代表对此资源的操作，比如 get post等
# 在类服务中集成resource，表示使用flask-restful
class TestCaseService(Resource):
    """
    测试用例服务
    """
    # 方法名对应app.route 中的methods
    def get(self):
        """
        查询接口，查询用例数据信息
        :return:
        """
        case_id = request.args.get("id")
        if case_id:
            # 查询单条数据信息
            case_data = TestCase.query.filter_by(id=case_id).first()
            app.logger.info(f"[TestCaseService][get]根据id={case_id}获取测试用例：{case_data}")
            data = [{"id": case_data.id, "nodeid": case_data.nodeid, "remark": case_data.remark}]
        else:
            # 查询所有用例信息
            case_data = TestCase.query.all()
            app.logger.info(f"[TestCaseService][get]获取所有测试用例：{case_data}")
            data = [{"id": i.id, "nodeid": i.nodeid, "remark": i.remark} for i in case_data]
        return {"error": 0, "msg": {"data": data}}

    def post(self):
        # 增加一條用例
        case_data = request.json
        app.logger.info(f"[TestCaseService][post]新增测试用例{case_data}")
        # 从接口中拿到的字典数据进行解包，使用关键字传惨，传入Testcase
        testcase = TestCase(**case_data)
        db.session.add(testcase)
        db.session.commit()
        return {"error": 0, "msg": "post success"}

    def put(self):
        """
        修改接口信息
        :return:
        """
        # 获取被修改的接口信息
        case_id = request.json.get("id")
        result = TestCase.query.filter_by(id=case_id).update(request.json)
        app.logger.info(f"[TestCaseService]数据已修改，id为{case_id}被修改为{request.json}")
        db.session.commit()
        # 找到被修改的信息然后做修改操作
        return {"error": 0, "msg": {"id": result}}

    def delete(self):
        """
        删除用例
        :return:
        """

        return {"error": 0, "msg": "delete success"}


if __name__ == '__main__':
    # db.create_all()
    # 把服务添加到app flask中
    # 第一个参数是添加的接口服务，第二个参数是指定对应接口服务使用的路由
    api.add_resource(TestCaseService, "/testcase")
    app.run(debug=True)
