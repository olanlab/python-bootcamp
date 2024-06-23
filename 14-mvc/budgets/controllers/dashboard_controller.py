from views.dashboard_view import DashboardView

from utils.window import getCenterPosition
from utils.database import DatabaseUtil


class DashboardController:

    width = 1200
    height = 600

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.view = DashboardView(self, app)
        self.budgets = None
        self.show_budgets()

        print(self.app.user)

    def add_budget(self, formValues):
        db = DatabaseUtil.getInstance()
        db.execute_query("INSERT INTO budgets (created_date, title, type, amount) VALUES (%s, %s, %s, %s)", formValues)
        self.show_budgets()

    def delete_budget(self, id):
        db = DatabaseUtil.getInstance()
        db.execute_query("DELETE FROM budgets WHERE id = %s", (id,))
        self.show_budgets()

    def search_budgets(self, formValues):
        db = DatabaseUtil.getInstance()
        sql = "SELECT * FROM budgets WHERE year(created_date) =  %s and month(created_date) = %s "
        if (formValues[2] != 'All') : 
            sql += "and type = %s"
        else: 
            formValues = (formValues[0], formValues[1])
            
        self.budgets = db.fetch_data(sql, formValues)
        self.view.set_budgets(self.budgets)

    def show_budgets(self):
        db = DatabaseUtil.getInstance()
        self.budgets = db.fetch_data("SELECT * FROM budgets")
        self.view.set_budgets(self.budgets)


    def show(self):
        self.view.pack(padx=10, pady=10)
        x , y = getCenterPosition(self.app, width=self.width, height=self.height)
        self.app.geometry(f"{self.width}x{self.height}+{x}+{y}")
        self.view.pack(padx=10, pady=10)

    def hide(self):
        self.view.pack_forget()
    