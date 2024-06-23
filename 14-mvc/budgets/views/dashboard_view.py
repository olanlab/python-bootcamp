from tkinter import ttk
from views.components.forms.budget_form import BudgetForm
from views.components.frames.budget_summary import BudgetSummaryFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from datetime import datetime

class DashboardView(ttk.Frame):
    def __init__(self, controller, app):
        super().__init__(app)
        self.controller = controller

        years = list(range(datetime.now().year + 1, datetime.now().year - 50, -1))
        # years.insert(0, 'All')
        months = list(range(1, 12))
        # months.insert(0, 'All')

        self.main_frame = ttk.Frame(self)
        self.year_combobox = ttk.Combobox(self.main_frame, values=years)
        self.year_combobox.set(datetime.now().year)
        self.year_combobox.grid(row=0, column=0, columnspan=1, padx=10, pady=0, sticky="nsew")
        self.year_combobox.bind("<<ComboboxSelected>>", lambda event: self.search_budgets())
        
        self.month_combobox = ttk.Combobox(self.main_frame, values=months)
        self.month_combobox.set(datetime.now().month)
        self.month_combobox.grid(row=0, column=1, columnspan=1, padx=10, pady=0, sticky="nsew")
        self.month_combobox.bind("<<ComboboxSelected>>", lambda event: self.search_budgets())

        self.type_combobox = ttk.Combobox(self.main_frame, values=["All", "Income", "Expense"])
        self.type_combobox.set("All")
        self.type_combobox.grid(row=0, column=2, columnspan=1, padx=10, pady=0, sticky="nsew")
        self.type_combobox.bind("<<ComboboxSelected>>", lambda event: self.search_budgets())


        self.clear_button = ttk.Button(self.main_frame, text="Clear", command=self.clear_budget)
        self.clear_button.grid(row=1, column=0, padx=10, pady=0, sticky="nsew")
        self.delete_button = ttk.Button(self.main_frame, text="Delete", command=self.delete_budget)
        self.delete_button.grid(row=1, column=2, padx=10, pady=0, sticky="nsew")

        self.main_frame.pack(side="left", fill="both", expand=True)

        # Budgets
        self.treeview = ttk.Treeview(self.main_frame, columns=("ID", "Created Date", "Title", "Type", "Amount"), show="headings")
        self.treeview.heading("ID", text="ID" , command=lambda: self.sort_column("ID", False))
        self.treeview.heading("Created Date", text="Created Date", command=lambda: self.sort_column("Created Date", False))
        self.treeview.heading("Title", text="Title", command=lambda: self.sort_column("Title", True))
        self.treeview.heading("Type", text="Type", command=lambda: self.sort_column("Type", False))
        self.treeview.heading("Amount", text="Amount", command=lambda: self.sort_column("Amount", False))
        self.treeview.column("ID", width=40, )
        self.treeview.column("Type", width=100)
        self.treeview.grid(row=2, column=0, sticky="nsew", columnspan=4 ,padx=0, pady=10)
        
        self.form_frame = ttk.Frame(self)
        self.budget_form = BudgetForm(self.controller, self.form_frame)
        self.budget_form.pack(side="top",fill="both", expand=True, padx=20, pady=0)
        self.form_frame.pack(side="left", fill="both", expand=True)

        self.budget_summary = BudgetSummaryFrame(self.controller, self.main_frame)
        self.budget_summary.grid(row=3, column=2, sticky="nsew", padx=50, pady=25)
        
    def search_budgets(self):
        type = ('r' if self.type_combobox.get() == 'Income' else 'All' if self.type_combobox.get() == 'All' else 'e' )
        formValues = (self.year_combobox.get(), self.month_combobox.get(), type)
        self.controller.search_budgets(formValues)

    def delete_budget(self):
        selected_item = self.treeview.focus()
        if selected_item:
            values = self.treeview.item(selected_item)["values"] 
            self.controller.delete_budget(values[0])

    def clear_budget(self):
        self.controller.show_budgets()


    def set_budgets(self, budgets):
        self.treeview.delete(*self.treeview.get_children())
        income = 0
        expense = 0

        for budget in budgets:
            (id, created_date, title, type, amount, user_id) = budget

            type_ = ('Income' if type == 'r' else 'Expense' )
            self.treeview.insert("", "end", values=(id, created_date, title, type_, "{:,.2f}".format(amount)))
            if type == 'r' : income += amount
            if type == 'e' : expense += amount
        self.budget_summary.setSummary(income, expense, income - expense)

         # Create a Matplotlib figure
        figure = Figure(figsize=(6, 4), dpi=70)
        subplot = figure.add_subplot(111)

        #  Bar data
        labels = ["Income", "Expense", "Remain"]
        values = [income, expense, income - expense]

        # Create a bar plot
        subplot.bar(labels, values)

        # Create a FigureCanvasTkAgg widget
        canvas = FigureCanvasTkAgg(figure, master=self.main_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, sticky="nsew", padx=0, pady=0)


    def sort_column(self, column, reverse):
        """Sort treeview by a column"""
        data = [(self.treeview.set(child, column), child) for child in self.treeview.get_children("")]
        data.sort(reverse=reverse)

        if reverse:
            self.treeview.heading(column, text=f"{column} ▼")
        else:
            self.treeview.heading(column, text=f"{column} ▲")

        for index, (value, child) in enumerate(data):
            self.treeview.move(child, "", index)

        self.treeview.heading(column, command=lambda: self.sort_column(column, not reverse))

