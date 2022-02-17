import json

import requests


class TestCase:
    """

    """

    def setup_class(self):
        self.base_url = "http://127.0.0.1:5000/testcase"

    def test_post(self):
        """
        新增测试用例
        :return:
        """
        data = {"id":4, "nodeid": ["node1", "node2"], "remark": "remark333"}
        r = requests.post(self.base_url, json=data)
        assert r.status_code == 200

    def test_delete(self):
        """
        删除测试用例
        :return:
        """
        r = requests.delete(self.base_url)
        print(r.json())
        assert  r.json()["error"] == 40001
        assert r.status_code == 200
        r2 = requests.delete(self.base_url, params={"id":2})
        print(r2.json())
        assert r2.status_code == 200

    def test_get(self):
        """
        查询测试用例
        :return:
        """
        # r = requests.get(self.base_url, params={"id":2})
        r = requests.get(self.base_url)
        print(json.dumps(r.json(), indent=2,ensure_ascii=False))
        assert r.status_code == 200

    def test_put(self):
        """
        修改测试用例
        :return:
        """
        data = {"id": 3, "nodeid": "nodeid123", "remark": "remark123"}
        r = requests.put(self.base_url, json=data)
        assert r.status_code == 200
