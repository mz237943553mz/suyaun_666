# 天气
# import requests
# url="https://v0.yiketianqi.com/api?appid=78778619&appsecret=y3UvmynJ&version=v61"
# data={"appid":"78778619","appsecret":"y3UvmynJ","version":"v61"}
# r=requests.get(url,data=data)
# print(r.json())
#登录
import unittest
from requests_toolbelt.multipart import MultipartEncoder
import requests
class suyuan(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        url="http://123.57.140.190/manage/index.php?act=adminlogin"
        data={"Username":"admin","Password":"admin999","Submit":"管理登录"}
        headers={"Content-Type":"application/x-www-form-urlencoded"}
        r=requests.post(url=url,data=data,headers=headers)
        print(r.text)
        cookie="PHPSESSID"+"="+r.cookies["PHPSESSID"]
        return cookie

    def test_add(self):
        a=self.setUpClass()
        url1 = "http://123.57.140.190/manage/add_cp.php?act=save_cp"
        data=MultipartEncoder({"pro_name":"大放厥词",
                               "cpbh":"154152",
                               "cptxm":"tfgew15465415",
                               "cpms":"车号虐范围"})
        headers1 = {"Content-Type":data.content_type,
                   "Cookie":a}
        r1=requests.post(url=url1,data=data,headers=headers1)
        print(r1.text)


if __name__ == '__main__':
 unittest.main()


