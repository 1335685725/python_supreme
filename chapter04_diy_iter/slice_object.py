# from _collections_abc import *
import numbers

class Group:
    '''
    支持切片操作的group
    '''
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __getitem__(self, item):
        clz = type(self)
        if isinstance(item, slice):
            return clz(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return clz(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __reversed__(self):
        self.staffs.reverse()

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False

staffs = ["boo1", "boo2", "boo3"]
group = Group(company_name="imooc", group_name="user", staffs=staffs)
sub_group = group[:2]
sub_group = group[0]
pass