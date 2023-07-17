############################ ZKCF API ############################
'''
Desc: 获取查分系统状态
Method: GET

Response Example:
// Always success
{
    "code": 0,
    "data": {
        "enableStatus": 1, // 查分是否开始
        "endTime": "2023-08-31 17:00:00",  // 查分结束时间
        "startTime": "2023-07-01 09:00:00" // 查分开始时间 (与公布的时间提前了1小时)
    },
    "msg":"success"
}
'''
ZKCF_PREQUERY_URL = "https://zkcf.whzkb.cn/api/preQuery"

'''
Response Example:
// Success
{
    "code": 0,
    "data": {
        "admissionCode": "准考证号",
        "highScore": false, // 高分保护
        "infos": [],        // 不知道用来干嘛
        "scoreList": [
            {
                "score": 79.0,
                "scoreName": "语文"
            },
            {
                "score": 103.0,
                "scoreName": "数学"
            },
            {
                "score": 114.0,
                "scoreName": "外语"
            },
            {
                "score": 112.0,
                "scoreName": "物理化学"
            },
            {
                "score": 109.0,
                "scoreName": "道德与法治、历史"
            },
            {
                "score": 50.0,
                "scoreName": "体育与健康"
            },
            {
                "score": 30.0,
                "scoreName": "理化生实验操作"
            }
        ],
        "scoreSum": 597.0,
        "signCode": "报名号",
        "studentName": "姓名"
    },
    "msg":"success"
}
'''
ZKCF_QUERY_URL = "https://zkcf.whzkb.cn/api/query"

############################ WWW API ############################

'''
Desc: 获取录取结果系统状态
Method: GET

Response Example:
{
    "code": 0,
    "data": {
        "companyName": "武汉市招生考试办公室",
        "enableStatus": 1,
        "endTime": "2023-08-31 17:00:00",
        "startTime": "2023-07-13 14:00:00"
    },
    "msg":"success"
}
'''

'''
Desc: 获取录取结果
Method: GET
Query:
  - signCode
  - admissionCode
  - stuName

Response Example:
// Success
{
    "code": 0,
    "data": {
        "admissionCode": "准考证号",
        "schoolName": "录取学校",
        "signCode": "报名号",
        "studentName": "姓名"
    },
    "msg":"success"
}
// Failed
// 由于一二三批录取时间各不相同, 在第X批录取时出现此情况只能说明第X批掉档
{
    "code": 2,
    "data": null,
    "msg": "未查询到该考生数据，请检查输入信息是否有误"
}
'''
WWW_QUERYRESULT_URL = "https://www.whzkb.cn/api/queryResult"

############################ ZKZZ API ############################
# 说明
# - JSESSIONID 来源
#     不带Cookie的初次访问 https://zkzz.whzkb.cn/stu
#     服务器会在响应头中 Set-Cookie: JSESSIONID=[A UUID]; Path=/; HttpOnly; SameSite=lax
#     后续请求都需要附带这个Cookie
#
# - 登录逻辑
#     获取到JSESSIONID后 带上
#     GET 请求 /captcha/captchaImage?type=char 获取验证码图片
#     POST请求 /stu  username=报名号&password=密码&validateCode=验证码
#     

'''
Desc: 登录
Method: GET(获取SID)/POST(登录)
Header:
  - (POST) Cookie: JSESSIONID
'''
ZKZZ_LOGIN_URL = "https://zkzz.whzkb.cn/stu"

'''
Desc: 获取验证码图片
Method: GET
Query:
  - type=char

Response: JPEG Image
'''
ZKZZ_CAPTCHA_IMAGE_URL = "https://zkzz.whzkb.cn/captcha/captchaImage"

'''
Desc: 获取志愿信息(HTML)
Note: 由于考生志愿至关重要, 本项目不会提供任何涉及修改志愿的接口
Method: GET
Header:
  - Cookie: JSESSIONID
'''
ZKZZ_WISH_SHOW_URL = "https://zkzz.whzkb.cn/wish/wish/show"

'''
Desc: 获取考务信息
Method: GET
Header:
  - Cookie: JSESSIONID

Response Example(Main Part):
<div class="wrapper wrapper-content animated fadeInRight">
    <form class="form-horizontal m" id="form-stu-edit">
        <div class="ibox-content m-b-sm border-bottom">
            <h4 class="form-header h4">考务信息</h4>
            <div class="row">
                <div class="col-sm-12">
                    <table class="layui-table" lay-size="sm">
                        <colgroup>
                            <col width="30">
                            <col width="30">
                            <col width="30">
                            <col width="30">
                            <col width="30">
                            <col width="30">
                        </colgroup>
                        <tbody>
                        <tr align="center">
                            <td>报名号</td>
                            <td>姓名</td>
                            <td>学籍号</td>
                            <td>性别</td>
                            <td>出生日期</td>
                            <td>生源学校</td>
                        </tr>
                        <tr align="center">
                            <td>${报名号}</td>
                            <td>${姓名}</td>
                            <td>${学籍号}</td>
                            <td>${性别}</td>
                            <td>${出生日期}</td>
                            <td>${毕业学校}</td>
                        </tr>
                        </tbody>
                    </table>
                    <table class="layui-table" lay-size="sm">
                        <colgroup>
                            <col width="100">
                            <col width="100">
                            <col width="100">
                        </colgroup>
                        <tbody>
                        <tr align="center">
                            <td>考点代码</td>
                            <td>考点名称</td>
                            <td>考点地址</td>
                        </tr>
                        <tr align="center">
                            <td>${考点代码}</td>
                            <td>${考点名称}</td>
                            <td>${考点地址}</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </form>
</div>
'''
ZKZZ_AFFAIR_SHOW_URL = "https://zkzz.whzkb.cn/affair/makeup/show"

'''
Desc: 退出登录
Method: GET
Headers:
  - Cookie: JSESSIONID
'''
ZKZZ_LOGOUT_URL = "https://zkzz.whzkb.cn/logout"
