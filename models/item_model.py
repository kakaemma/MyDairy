import datetime


class ItemModel(object):

    description = []

    def __init__(self, diary_id, desc):
        """
        This constructor creates an ItemModel object
        :param diary_id: 
        :param description: 
        """
        self.item_id = len(ItemModel.description)+1
        self.diary_id = diary_id
        self.desc = desc
        self.date_created = datetime.datetime.utcnow()
        self.date_modified = None

    def create_description(self):
        ItemModel.description.append(self)
        return self.item_id

    @staticmethod
    def modify_description(diary_id, item_id, desc):
        for this_item in ItemModel.description:
            if this_item.diary_id == diary_id and \
                            this_item.item_id == item_id:
                if this_item.desc == desc
                    return None

                this_item.desc = desc
                this_item.date_modified = datetime.datetime.utcnow()
                return this_item.item_id
