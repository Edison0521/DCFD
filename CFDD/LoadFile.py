import pandas as pd

class LoadFile:

    def __init__(self,filename:str) -> list:
        self.fname = filename
        self.Dom_attrs = []#读取文件的第一行作为属性的集合
        self.Sub_attrs = []#将具体的某个属性的值放入集合中

    def add_CSV(self,filename: str) -> list:
        attrs = pd.read_csv(filename)
        df = pd.DataFrame(attrs)
        Dom_attrs = df.columns.tolist()
        Sub_attr = []#保存某个特定列的属性
        Sub_attrs = []#使用二维数组来表示
        for i in range(len(Dom_attrs)):
            Sub_attr.append(df[Dom_attrs[i]].tolist())
        for i in range(len(Sub_attr)):
            Sub_attrs.append(Sub_attr[i])
        return self.Dom_attrs,self.Sub_attrs
    def __repr__(self):
        return self.Dom_attrs,self.Sub_attrs
