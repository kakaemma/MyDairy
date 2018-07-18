import datetime


class ItemModel(object):

    description = []

    def __init__(self, diary_id, description):
        """
        This constructor creates an ItemModel object
        :param diary_id: 
        :param description: 
        """
        self.item_id = len(ItemModel.description)+1
        self.diary_id = diary_id
        self.date_created = datetime.datetime.utcnow()
        self.date_modified = None

    def create_description(self):
        ItemModel.description.append(self)
        return self.item_id
