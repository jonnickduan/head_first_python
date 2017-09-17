from suds.client import Client
import json

CRM_URL = "http://114.255.45.138:8896/JinYuanCRMInterface/CRMService?wsdl"  # CRM系统Services地址


def call_RegisterMember(url, ws_name, data):
    """
    :param url: wsdl地址
    :param ws_name: 方法名，做保存结果的文件名
    :param data: 方法的传入参数
    :return:
    """
    client = Client(url)  # 创建一个webservice接口对象
    client.service.RegisterMember(data)  # 调用这个接口下的getMobileCodeInfo方法，并传入参数
    req = str(client.last_sent())  # 保存请求报文，因为返回的是一个实例，所以要转换成str
    response = str(client.last_received())  # 保存返回报文，返回的也是一个实例
    print(response)  # 打印返回报文
    write_res(ws_name, req, response, data)  # 调用写入结果函数，把方法名、请求报文、返回报文、和入参传进去


def write_res(ws_name, req, response, data):
    """
    :param ws_name: 接口的方法名
    :param req: 请求报文
    :param response: 返回报文
    :param data: 传入的数据
    """
    res = response.find(data)  # 从返回结果里面找data，如果找到的话返回data的下标，也就是索引，找不到的话返回-1
    fw_flag = open('/tmp/WsTestRes/WsTestRes.txt', 'a')  # 以追加模式打开写入结果文件
    if res > 0:
        fw_flag.write('%s  pass' % ws_name)  # 如果在返回报文中找到data的话，就写pass,否则就写fail
    else:
        fw_flag.write('%s  fail' % ws_name)
        fw_flag.close()  # 关闭结果文件
        fw_result = open('/tmp/WsTestRes/%s_result.txt' % ws_name, 'w')  # 打开以接口方法命名的文件
        fw_result.write(req + '\n' * 3 + response)  # 保存请求报文和返回报文，\n*3的意思是换行三次
        fw_result.close()  # 关闭结果文件
    if __name__ == '__main__':
        call_RegisterMember(CRM_URL, 'RegisterMember', '110')