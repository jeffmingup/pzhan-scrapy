import scrapy,re
from pzhan.items import PzhanItem
class PzhanSpider(scrapy.Spider):
    name = "pzhan"
    allowed_domains = ["pixiv.net"]
    cookie ={'first_visit_datetime_pc': '2018-08-24+15%3A45%3A00', ' p_ab_id': '4', ' p_ab_id_2': '5', ' yuid': 'FxlliJc76', ' __utma': '235335808.1873689210.1535093030.1535093030.1535093030.1', ' __utmc': '235335808', ' __utmz': '235335808.1535093030.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)', ' __utmt': '1', ' tag_view_ranking': 'y8GNntYHsi~BU9SQkS-zU~ueeKYaEKwj~144zWY--zX~fafuO7KcEk~jl9Gy4v1Ny~ya2M5yc9BW~xZ6jtQjaj9', ' _ga': 'GA1.2.661695032.1534239892', ' _gid': 'GA1.2.324695742.1535093057', ' _gat': '1', ' login_bc': '1', ' PHPSESSID': '14704921_447e241ea4dd76dbf944f2e6cd8fe770', ' device_token': '37c73b90c5b7e513abff3af8c0e8aef1', ' privacy_policy_agreement': '1', ' c_type': '23', ' a_type': '0', ' b_type': '1', ' __utmv': '235335808.|2=login%20ever=no=1^3=plan=normal=1^5=gender=male=1^6=user_id=14704921=1^9=p_ab_id=4=1^10=p_ab_id_2=5=1^11=lang=zh=1', ' __utmb': '235335808.3.9.1535093033947'}
    zhannum=30000

    start_urls = [
        "https://www.pixiv.net/ranking_log.php?mode=daily&content=all&date=201808"
    ]

    # def parse(self, response):
    #     for sel in response.xpath('//td[@class="active"]/a/div/img'):
    #         item = PzhanItem()
    #         url =sel.xpath('@data-src').extract()
    #         url=str(url).replace('c/128x128/img-master','img-original')
    #         url=url[2:-17]
    #         imgext = ['.jpg', '.png']
    #         for ext in imgext:
    #             iurl = url + ext            
    #             item['image_urls'] = [iurl]
    #             print(item['image_urls'])
    #             yield item

    def parse(self, response):
        for sel in response.xpath('//td[@class="active"]/a/div/img'):
            
            url  = sel.xpath('@data-src').extract()
            urlid  = str(url)[-28:-20]
            url  = 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id=' + urlid
            yield scrapy.Request(url, callback=self.parse2,cookies=self.cookie)
    def parse2(self,response):
        html = response.body
        item = PzhanItem()
        # f = open('test.html', 'wb')
        # f.write(collect)
        # f.close()
        # exit()
        pattern = re.compile(r'bookmarkCount":(.*),"likeCount')
        pattern2 = re.compile(r'"original":"(.*)"},"tags":{"authorId"')
        num = pattern.findall(str(html))
        imgurl = pattern2.findall(str(html))
        imgurl = str(imgurl[0]).replace('\\','')
        if int(num[0]) > self.zhannum:
            print(num[0])
            print(imgurl)
            item['image_urls'] = [imgurl]
            yield item

            
        
        


