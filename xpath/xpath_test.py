
from lxml import etree

url = "https://www.baidu.com"


html = etree.HTML(wb_data)
html_data = html.xpath('/html/body/div/ul/li/a')
print(html)
for i in html_data:
    print(i.text)