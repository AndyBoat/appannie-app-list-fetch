# README
## 简介
抓取APP-ANNIE  IOS APP榜单。小程序模拟用户登录，模拟AJAX调用接口获取后台数据。
模拟用户登录、模拟AJAX调用后台的思路来自github。
## 文件目录
主程序`fetch.py`
配置文件`ini.config` ：设置app-annie用户名和密码
`item_array.py`,`countery.json`和`category.json`：AJAX相关参考信息
## 功能
支持按时间、地区、类别抓取APP-ANNIE IOS APP 榜单 前500APP的名字，保存到程序目录下的EXCEL文件中。
## 使用方法
1.  在`ini.config`中设置相关用户信息
2.  在`console`中使用命令行运行程序

 ```powershell
 python fetch.py [TIME] [COUNTRY] [CATEGORY]
 ```
[TIME]  `可选` 榜单的时间，精确到日，格式为`YYYY-MM-DD`，如 `2017-4-10` 。 如未提供，默认为当天时间。

[COUNTRY] `可选` 榜单对应的地区。 可以选择的地区代码见后文。 如未提供，默认为'CN' 中国

[CATEGORT] `可选` 榜单对应的类别。 可选择的类别代码见后文。 如未提供，则默认为爬取所有共25种类别。

## 结果
![结果示意图](http://i4.buimg.com/567571/5b98d8b3a8c97311.jpg)

## 注意事项
由于APP-ANNIE的反爬虫机制，在短时间内连续两次大规模爬取（如爬取所有25种类别的榜单）时会触发验证码，此时无法成功调用接口。
目前的解决方案是可以在网页端登录appannie人工输入验证码解除。
后续尝试使用代理IP解决该问题。
## todo
1. 代理IP
2. 更多可供选择的爬取内容：如制作公司等

## 地区代码
详见`country.json`


## 类别代码

| 类别      	|代码 |
| :-------- |:--------| 
|所有类别|overall|
|图书|books|
|商业|business|
|教育|education|
|娱乐|entertainment|
|财务|finance|
|美食佳饮|food-and-drink|
|游戏|games|
|健康健美|health-and-fitness|
|儿童|kids|
|生活|lifestyle|
|报刊杂志|magazines-and-newspaper|
|医疗|medical|
|音乐|music|
|导航|navigation|
|新闻|news|
|摄影与录像|photo-and-video|
|效率|productivity|
|参考|reference|
|购物|shopping|
|社交|social-networking|
|体育|sports|
|旅行|travel|
|工具|utilities|
|天气|weather|
