import json

import requests


class TestCase:
    """

    """

    def setup_class(self):
        self.base_url = "http://127.0.0.1:5000/testcase"

    def test_post(self):
        data = {"id": 2, "nodeid": "nodeid222", "remark": "remark222"}
        r = requests.post(self.base_url, json=data)
        assert r.status_code == 200

    def test_delete(self):
        r = requests.delete(self.base_url)

        assert r.status_code == 200

    def test_get(self):
        # r = requests.get(self.base_url, params={"id":2})
        r = requests.get(self.base_url)
        print(json.dumps(r.json(), indent=2,ensure_ascii=False))
        assert r.status_code == 200

    def test_put(self):
        data = {"id": 3, "nodeid": "nodeid11", "remark": "remark123"}
        r = requests.put(self.base_url, json=data)
        assert r.status_code == 200
