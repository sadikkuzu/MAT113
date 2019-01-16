from lxml import html
import requests


def sondegisiklik():
    page = requests.get('http://mat.msgsu.edu.tr/~dpierce/Dersler/113/2018/')
    tree = html.fromstring(page.content)
    son_deg = tree.xpath('/html/body/p[4]/em/text()')
    return son_deg[0]


print sondegisiklik()