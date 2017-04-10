# -*- coding:utf-8 -*-
import sys  
import requests
import re
import json
import time
import ConfigParser






def loginWeb(url):

    referer = "https://www.appannie.com/account/login/?_ref=header"
    user_agent = ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0")
    headers = {"User-Agent":user_agent,
                "Referer":referer,
                "Host":"www.appannie.com",
                'Connection':'keep-alive',
                'Accept':'application/json, text/plain,*/*',
                'Accept-Encoding':'gzip, deflate, sdch',
                'Accept-Language':'zh-CN,zh;q=0.8',
                'X-NewRelic-ID':'VwcPUFJXGwEBUlJSDgc=',
                'X-Requested-With':'XMLHttpRequest',
                }

    urlogin = "https://www.appannie.com/account/login/"
    s  = requests.Session()
    s.get(urlogin,headers=headers)
    csrftoken = s.cookies['csrftoken']
    postdata = {
            'csrfmiddlewaretoken':csrftoken,
            'next':'/dashboard/home/',
            'username':cf_username,
            'password':cf_password,
            }
    
    s.headers=headers
    login_response = s.post(url=urlogin,data=postdata)
    if not 200 <= login_response.status_code < 300:
        raise Exception("Error while logging in, code: %d" % (response. status_code))
    else:
        print "login success..."
    headers["X-CSRFToken"] = csrftoken
    r = s.get(url=url,headers=headers)
    if not 200 <= r.status_code < 300:
        raise Exception("Error while download website, code:%d" % (r.status_code))
    else:
        return r.content

def matchRe(content,item):

    # print content
    # return 0

    decodejson = json.loads(content)
    rowslist = decodejson["table"]["rows"]
    # item = "books"
    # item = u'图书'
    app_name = []
    # version = []
    # rate = []
    # title = []
    # author = []
    # text = []
    # tanslate = ""
    # date = []
    # country = []

    for each in rowslist:
        # version.append(each["version"])
        # rate.append(each["rating"])
        # title.append(each["title"])
        # author.append(each["author"])
        # text.append(each["content"])
        # date.append(each["date"])
        # country.append(each["country"]["code"])
        app_name.append(each[1][0]["name"])
        # app_paid.append(each[2][0]["name"])

    print app_name


    # print "tmp hold"
    # return 0
    arrayDict = dict(item=item,app_array=app_name)
    print "create Dict done..."
    return arrayDict

def saveToExcel(appData,dateTime):
    # print "tmp hold"
    # return 0
    table_name,app_array= (appData["item"],appData["app_array"])

    import xlwt

    efile = xlwt.Workbook()
    table = efile.add_sheet('Sheet1')

    table.write(0,0,u'分类')
    table.write(0,1,table_name)
    table.write(0,2,u'时间')
    table.write(0,3,dateTime)

    for num,each in enumerate(app_array):
        index = num +1
        table.write(index,0,index)
        table.write(index,1,app_array[num])

    efile.save('App Annie'+ '_' + contry +'_' +table_name + '_' +dateTime+'.xls')

def savefile(content):
    f = open('index.html','wb')
    f.write(content)
    f.close()

if __name__ == '__main__':
    cf = ConfigParser.ConfigParser()
    cf.read('ini.config')
    cf_username = cf.get('user','username');
    cf_password = cf.get('user','password');

    dateTime =  sys.argv[1] if(len(sys.argv) > 1) else time.strftime('%Y-%m-%d',time.localtime(time.time()))
    contry 	 =  sys.argv[2] if(len(sys.argv) > 2) else 'CN'
    indexUrl = "https://www.appannie.com"
    #commentUrl="https://www.appannie.com/apps/ios/app/hi-words-a-new-word-search-puzzle-game/reviews/table/?date=2015-10-12~2016-01-02&orderby=&desc=t&page=1&limit=10"
    #commentUrl="https://www.appannie.com/apps/ios/app/wordfall-most-addictive-words/reviews/table/?date=2015-01-29~2015-12-21&orderby=&desc=t&page=1&limit=200"
    #commentUrl="https://www.appannie.com/apps/ios/app/word-jungle-challenging-word/reviews/table/?date=2015-02-01~2016-01-03&orderby=&desc=t&page=1&limit=200"
    # commentUrl="https://www.appannie.com/apps/ios/app/word-island-new-challenging/reviews/table/?date=2015-01-10~2015-10-18&orderby=&desc=t&page=1&limit=200"

    # chartUrl="https://www.appannie.com/apps/ios/top-chart/united-states/overall/?device=iphone&date=2017-03-12&feed=All&rank_sorting_type=rank&page_number=0&page_size=100&desc=t&order_by=sort_order"
    # 只能获得静态页面的数据 没有卵用

    #所有类目和类别
    # chartUrl ="https://www.appannie.com/ajax/top-chart/table/?market=ios&country_code=CN&category=overall&date=2017-03-12&rank_sorting_type=rank&page_size=100&order_by=sort_order&order_type=desc&device=iphone"
    item_array = item_array = [
        {
        "c_name":u"所有类别",
        "e_name":"overall"
        },
        {
        "c_name":u"图书",
        "e_name":"books"
        },
        {
        "c_name":u"商业",
        "e_name":"business"
        },
        {
        "c_name":u"教育",
        "e_name":"education"
        },
        {
        "c_name":u"娱乐",
        "e_name":"entertainment"
        },
        {
        "c_name":u"财务",
        "e_name":"finance"
        },
        {
        "c_name":u"美食佳饮",
        "e_name":"food-and-drink"
        },
        {
        "c_name":u"游戏",
        "e_name":"games"
        },
        {
        "c_name":u"健康健美",
        "e_name":"health-and-fitness"
        },
        {
        "c_name":u"儿童",
        "e_name":"kids"
        },
        {
        "c_name":u"生活",
        "e_name":"lifestyle"
        },
        {
        "c_name":u"报刊杂志",
        "e_name":"magazines-and-newspapers"
        },
        {
        "c_name":u"医疗",
        "e_name":"medical"
        },
        {
        "c_name":u"音乐",
        "e_name":"music"
        },
        {
        "c_name":u"导航",
        "e_name":"navigation"
        },
        {
        "c_name":u"新闻",
        "e_name":"news"
        },
        {
        "c_name":u"摄影与录像",
        "e_name":"photo-and-video"
        },
        {
        "c_name":u"效率",
        "e_name":"productivity"
        },
        {
        "c_name":u"参考",
        "e_name":"reference"
        },
        {
        "c_name":u"购物",
        "e_name":"shopping"
        },
        {
        "c_name":u"社交",
        "e_name":"social-networking"
        },
        {
        "c_name":u"体育",
        "e_name":"sports"
        },
        {
        "c_name":u"旅行",
        "e_name":"travel"
        },
        {
        "c_name":u"工具",
        "e_name":"utilities"
        },
        {
        "c_name":u"天气",
        "e_name":"weather"
        }

    ]

    if (len(sys.argv) > 3):
        chartUrl = "https://www.appannie.com/ajax/top-chart/table/?market=ios&country_code="+contry+"&category="+sys.argv[3]+"&date="+ dateTime+"&rank_sorting_type=rank&page_size=500&order_by=sort_order&order_type=desc&feed=Free&device=iphone"
        print "chartUrl="+chartUrl
        success = False
        attempt = 0

        # 5次尝试次数
        while not success and attempt < 5:
            try:
                print "第 %d 次尝试登陆" % (attempt+1)
                content = loginWeb(chartUrl)
                success = True
            except requests.exceptions.SSLError:
                attempt += 1
                if attempt==5:
                    print  "网络异常，已中断本次爬取：%s" % e.reason
                    exit()

        # 寻找类目的中文名
        ## 默认与英文名相同
        c_name = sys.argv[3]
        for item in item_array:
            if (item["e_name"] == sys.argv[3]):
                c_name= item["c_name"]

        appData = matchRe(content,c_name)
        saveToExcel(appData,dateTime)
        print sys.argv[3] + "xls is finised"

    else:
        for each_item in item_array:
            chartUrl = "https://www.appannie.com/ajax/top-chart/table/?market=ios&country_code="+contry+"&category="+each_item["e_name"]+"&date="+ dateTime+"&rank_sorting_type=rank&page_size=500&order_by=sort_order&order_type=desc&feed=Free&device=iphone"
            print "chartUrl="+chartUrl
            success = False
            attempt = 0

            # 5次尝试次数
            while not success and attempt < 5:
                try:
                    print "第 %d 次尝试登陆" % (attempt+1)
                    content = loginWeb(chartUrl)
                    success = True
                except requests.exceptions.SSLError:
                    attempt += 1
                    if attempt==5:
                        print  "网络异常，已中断本次爬取：%s" % e.reason
                        exit()

            appData = matchRe(content,each_item["c_name"])
            saveToExcel(appData,dateTime)
            print each_item["c_name"] + "xls is finised"

    # item = "books"
    # chartUrl = "https://www.appannie.com/ajax/top-chart/table/?market=ios&country_code=CN&category="+item+"&date="+ dateTime+"&rank_sorting_type=rank&page_size=500&order_by=sort_order&order_type=desc&feed=Free&device=iphone"

    # content = loginWeb(chartUrl)
    # appData = matchRe(content,item)
    # saveToExcel(appData,dateTime)
    #savefile(content)
