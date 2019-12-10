import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element : %s" % collection.getAttribute("shelf"))

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

for movie in movies:
    print('*****Movie*****')
    if movie.hasAttribute('title'):
        print('Title:%s' % movie.getAttribute('title'))

    typeName = movie.getElementsByTagName('type')[0]
    print("Type: %s" % typeName.childNodes[0].data)
    formatName = movie.getElementsByTagName('format')[0]
    print("Format: %s" % formatName.childNodes[0].data)
    rating = movie.getElementsByTagName('rating')[0]
    print("Rating: %s" % rating.childNodes[0].data)
    description = movie.getElementsByTagName('description')[0]
    print("Description: %s" % description.childNodes[0].data)
    stars = movie.getElementsByTagName('description')[0]
    print("Stars: %s" % stars.childNodes[0].data)
    year = movie.getElementsByTagName('description')[0]
    print("Stars: %s" % year.childNodes[0].data)










