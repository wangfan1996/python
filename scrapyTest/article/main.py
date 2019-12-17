from scrapy.cmdline import execute
import sys
import os

# 当前项目根目录
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'book'])

