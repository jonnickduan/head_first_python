import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_RegisterMember(self):
        pass

    def test_it(self):
        pass


def write_res(ws_name, req, response, data):
    fw_flag = None
    fw_result = None
    res = response.find(data)
    try:
        fw_flag = open('/ws_test_res.txt', 'a')
        if res > 0:
            fw_flag.write('%s  pass' % ws_name)
        else:
            fw_flag.write('%s  fail' % ws_name)
            fw_result = open('/tmp/WsTestRes/%s_result.txt' % ws_name, 'w')
            fw_result.write(req + '\n' * 3 + response)  # 保存请求报文和返回报文，\n*3的意思是换行三次
    except Exception as err:
        print(err)
    finally:
        fw_flag.close()
        fw_result.close()

if __name__ == '__main__':
    unittest.main()
