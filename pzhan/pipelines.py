# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import MySQLdb,re
from scrapy.utils.python import to_bytes
from scrapy.http import Request
import hashlib

from scrapy.pipelines.images import ImagesPipeline

class PzhanPipeline(object):
    def process_item(self, item, spider):
        return item
class PzhanImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
           yield Request(image_url,meta={'item':item})

    # def get_media_requests(self, item, info):
    #     return [Request(x) for x in item.get(self.images_urls_field, [])]
    def file_path(self, request, response=None, info=None):
        ## start of deprecation warning block (can be removed in the future)
        item = request.meta['item']

        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('ImagesPipeline.image_key(url) and file_key(url) methods are deprecated, '
                          'please use file_path(request, response=None, info=None) instead',
                          category=ScrapyDeprecationWarning, stacklevel=1)

        # check if called from image_key or file_key with url as first argument
        if not isinstance(request, Request):
            _warn()
            url = request
        else:
            url = request.url

        # detect if file_key() or image_key() methods have been overridden
        if not hasattr(self.file_key, '_base'):
            _warn()
            return self.file_key(url)
        elif not hasattr(self.image_key, '_base'):
            _warn()
            return self.image_key(url)
        ## end of deprecation warning block
        #重写图片下载地址
        # image_guid = hashlib.sha1(to_bytes(url)).hexdigest()  # change to request.url after deprecation
        # return 'full/%s.jpg' % (image_guid)
        image_guid = item['date']['day'] + "---" + url[-15:-7]
        return 'full/%s/%s/%s.jpg' % (item['date']['year'],item['date']['month'],image_guid)





class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for ok, value in results:
            image_file_path = value['path']
        item['front_image_path'] = image_file_path
        return item
class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('article.json','w',encoding="utf-8")
    def process_item(self, item, spider):
        lines = json.dumps(dict(item),ensure_ascii=False)
        self.file.write(lines)
        return item
    def spider_closed(self,spider):
        self.file.close()

class MysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('localhost','root','root','spiders',charset='utf8')
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        insert_sql="""
            insert into article( title,url,create_date,fav_nums)
            values (%s,%s,%s,%s)                
        """
        self.cursor.execute(insert_sql,(item["title"],item["url"],item["create_date"],item["fav_nums"]))
        self.conn.commit();


