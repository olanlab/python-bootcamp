from utils.database import DatabaseUtil

class Model:

    def __init__(self):
        self.db = DatabaseUtil.getInstance()

    