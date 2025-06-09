from pycocotools import COCO

class CocoDataSet:

  def __init__(self, captions, instance):
    self.instance = COCO(instance)
    self.captions = COCO(captions)
