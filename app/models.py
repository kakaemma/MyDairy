import datetime


class UserModel(object):
    """ This class handles all model operations to the User"""
    user = []

    def __init__(self, first_name, last_name, email, password):
        """
        This constructor initialises all the parameters
        :param first_name: 
        :param last_name: 
        :param email: 
        :param password: 
        """
        self.user_id = len(UserModel.user) + 1
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def create_user(self):
        """
        Adds user model object to user list
        :return: 
        """
        UserModel.user.append(self)
        return self.user_id

    @staticmethod
    def check_if_email_exists(email):
        """
        This method checks if an email already exists
        :param email: 
        :return: 
        """
        for this_user in UserModel.user:
            if this_user.email == email:
                return this_user.email

    @staticmethod
    def check_if_user_is_valid(email, password):
        """
         This method checks if the email and 
         password exist in the system

        :param email: 
        :param password: 
        :return: 
        """
        for this_user in UserModel.user:
            if this_user.email == email and \
                            this_user.password == password:
                return this_user.user_id

    @staticmethod
    def reset_user_pass(email, new_password):
        for user in UserModel.user:
            if user.email == email:
                user.password = new_password
                response = user.user_id
                return response

    @staticmethod
    def get_user_by_id(user_id):
        for user in UserModel.user:
            if user.user_id == user_id:
                return user.user_id

    @staticmethod
    def check_user_return_pass(email):
        for user in UserModel.user:
            if user.email == email:
                response = user.password
                return response


class DiaryModel(object):
    diary = []

    def __init__(self, name):
        """
        This constructor initialises diary
        :param name: 
        """
        self.diary_id = len(DiaryModel.diary)+1
        self.name = name
        self.date_created = datetime.datetime.utcnow()
        self.date_modified = None

    def create_diary(self):
        """
        Adds diary object to list
        :return: 
        """
        DiaryModel.diary.append(self)
        return self.diary_id


    @staticmethod
    def check_for_diaries():
        """ This checks whether there are any diary entries"""
        if len(DiaryModel.diary) >=1:
            return (len(DiaryModel.diary))

    @classmethod
    def get_diaries(cls):
        all_diaries = []
        for this_diary in DiaryModel.diary:
            all_diaries.append({
                'id': this_diary.diary_id,
                'name': this_diary.name,
                'Date created': this_diary.date_created,
                'Date Modified': this_diary.date_modified

            })
        return all_diaries

    @staticmethod
    def check_diary_by_id(search_id):
        for this_diary in DiaryModel.diary:
            if this_diary.diary_id == search_id:
                print(this_diary.diary_id)
                return this_diary.diary_id

    @staticmethod
    def check_name(name):
        for this_diary in DiaryModel.diary:
            if this_diary.name == name:
                return this_diary.name

    @staticmethod
    def get_diary_by_id(search_id):
        response = []
        for this_diary in DiaryModel.diary:
            if this_diary.diary_id == search_id:
                response.append({
                    'id': this_diary.diary_id,
                    'name': this_diary.name,
                    'Date created': this_diary.date_created,
                    'Date Modified': this_diary.date_modified
                })
                return response

    @staticmethod
    def edit_diary(diary_id, diary_name):
        for this_diary in DiaryModel.diary:
            if this_diary.diary_id == diary_id:
                if this_diary.name == diary_name:
                    return None
                this_diary.name = diary_name
                this_diary.date_modified = datetime.datetime.utcnow()
                return this_diary.diary_id


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