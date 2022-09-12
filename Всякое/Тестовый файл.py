class SoftList(list):

    def __getitem__(self, item):
        return super().__getitem__(item) if item in range(-len(self), len(self)) else False


sl = SoftList("python")
print(sl[0])  # 'p'
print(sl[-1])  # 'n'
print(sl[6])  # False
print(sl[-7])  # False
