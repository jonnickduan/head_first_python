class ReqRegisterMember:
    """
    定义会员注册接口(新)的入参
    """
    MemberName = None   # 会员姓名
    MobilPhone = None   # 会员手机号码
    MobilPhone1 = None  # 推荐人手机号
    CardID = None       # 身份证号
    Password = None     # 密码
    WeChat = None       # 微信号
    QQ = None           # QQ号
    Gender = None       # 性别
    Birthday = None     # 生日
    Email = None        # Email
    Channel = None      # 注册渠道 0:app 1:网站 2:微信 3:WIFI 5:收款机 6:CRM后台
    Source = None       # 会员来源
    Interest = None     # 会员爱好
    Address = None      # 邮寄地址
    Question = None     # 问题
    Answer = None       # 问题答案
    Type = None         # 注册类型 renren,tel,manual,web,sina,qq
    Avatarsurl = None   # 头像
    storeId = None      # 门店Id
