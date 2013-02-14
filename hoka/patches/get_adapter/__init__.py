from OFS.SimpleItem import Item
from zope.component import getAdapter as getComponentAdapter

def get_adapter(self,name):
    return getComponentAdapter(self,name=name)

Item.get_adapter=get_adapter