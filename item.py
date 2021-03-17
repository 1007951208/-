class Item():

    def __init__(self,name):
        self.name = name
        self.type = "item"
        
    def item_work(self):
        print("物品生效了")

    def set_type(self, item_type):
        """ 设置物品类型，item_typr : str """
        set_type = item_type

        