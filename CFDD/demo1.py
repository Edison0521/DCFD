class map(object):
    class mapp(object):
        def __init__(self,id:int,attr:str):
            self.id = id
            self.attr = attr
    def makemap(self,id,attr):
        return self.mapp(id,attr)
class Gcgrowth(object):
    def __init__(self):
        self.dater = []
        self.sater = []

    def gcgrowth(self, dater: list, sater: list) -> list:
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
        将Subattrs中的元素进行过滤，将重复出现的属性给清除，然后返回到temp列表当中
        '''
        for i in range(len(Subattrs)):
            for j in range(len(Subattrs[i])):
                if Subattrs[i][j] not in temp:
                    temp.append(Subattrs[i][j])
        '''
        对subattrs进行第二次遍历，然后在temp中寻找对应的元素以便进行下一步处理
        '''
        m = map()
        mapp = []
        for i in range(len(temp)):
            mapp.append(m.mapp(i,temp[i]))
        print(mapp[9].attr)

        return temp