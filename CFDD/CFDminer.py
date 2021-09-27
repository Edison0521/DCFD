'''
    def __init__(self,mapid : int):

        :param mapid:将不同的属性过滤之后重新编码
        :param mapattr: 列取属性

        self.id = mapid

    def add_node(self,nodeattr:str) -> int:
        self.nodelist = []
        self.nodeattrs = []
        self.nodenum = self.nodenum + 1
        node_id = self.nodenum
        node = Node(node_id,nodeattr)
        self.nodelist.append(node)
        self.nodeattr.append(nodeattr)
        return node_id
    def findnode(self,id:int):
        return self.nodes[id - 1]


    def __repr__(self):
        return "%s %s"%(self.id,self.attr)
        '''
class string2int(object):
    def __init__(self):
        self.attlist = []
    def s2v(self,attrs : list) -> list:
        i = 0
        attr = attrs
        for i in range(len(attrs)):
            k = i
        return k








class Gcgrowth(object):
    def __init__(self):
        self.dater = []
        self.sater = []
    def gcgrowth(self,dater : list,sater : list) -> list :
        '''

        :param dater:属性集
        :param sater: 属性
        :return: 返回一个由整型组成的二维数组
        dater和sater都是由属性构成的集合，但是由于gcgrowth仅仅支持整型变量，所以这个地方
        先建立一个每个属性和对应整型之间的映射
        先遍历整个列表，由出现的先后顺序构建映射
        '''
        Domattrs = dater
        Subattrs = sater
        temp = []
        '''
        for i in range(len(Subattrs[7])):
            if Subattrs[7][i] not in temp:
                temp.append(Subattrs[7][i])
        '''
        for i in range(len(Subattrs)):
            for j in range(len(Subattrs[i])):
                if Subattrs[i][j] not in temp:
                    temp.append(Subattrs[i][j])
        return temp
    '''
class mapping(object):
    def __init__(self):
        self.id = []
        self.attr = []
    def maps(self,attrs : list) -> dict:

        for i in range(len(attrs)):
            n = Node(i)
            n.add_node(attrs)
'''




