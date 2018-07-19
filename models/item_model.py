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
                if this_item.desc == desc:
                    return None

                this_item.desc = desc
                this_item.date_modified = datetime.datetime.utcnow()
                return this_item.item_id

    @staticmethod
    def get_descriptions(diary_id):
        response = []
        for this_diary in ItemModel.description:
            if this_diary.diary_id == diary_id:
                response.append({
                    'item id': this_diary.item_id,
                    'Description': this_diary.desc,
                    'Date created': this_diary.date_created,
                    'Date modified': this_diary.date_modified
                })
        return response

    @staticmethod
    def check_for_items():
        """ This checks whether there are any diary entries"""
        if len(ItemModel.description) >=1:
            return (len(ItemModel.description))

    @staticmethod
    def check_item(item_id):
        for item in ItemModel.description:
            if item.item_id == item_id:
                return item_id