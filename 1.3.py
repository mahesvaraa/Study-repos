a = '''<cube color="blue">
    <cube color="red">
        <cube color="green">
            <cube color="green">
                <cube color="green">
                    <cube color="blue">
                    </cube>
                    <cube color="green">
                    </cube>
                    <cube color="red">
                    </cube>
                </cube>
            </cube>
        </cube>
    </cube>
    <cube color="red">
        <cube color="blue">
        </cube>
    </cube>
</cube>'''

from lxml import etree

root = etree.fromstring(a)
dic = {'red': 0, 'green': 0, 'blue': 0}
tree = etree.ElementTree(root)
for e in root.iter():
    dic[e.attrib['color']] += tree.getpath(e).count('/')
for i in dic.values():
    print(i, end=' ')
