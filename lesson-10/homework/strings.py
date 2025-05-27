# Домашнее задание 1: Приложение для списка дел

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.title} ({status}) - Due: {self.due_date}\nDescription: {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def list_all_tasks(self):
        return self.tasks

    def list_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

# CLI

def todo_cli():
    todo = ToDoList()
    while True:
        print("\n1. Add Task\n2. Mark Task Done\n3. List All Tasks\n4. List Pending Tasks\n5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due Date: ")
            todo.add_task(Task(title, desc, due))
        elif choice == '2':
            index = int(input("Task Index to mark done: "))
            todo.mark_task_done(index)
        elif choice == '3':
            for i, task in enumerate(todo.list_all_tasks()):
                print(f"{i}. {task}")
        elif choice == '4':
            for task in todo.list_pending_tasks():
                print(task)
        elif choice == '5':
            break

# Домашнее задание 2: Простая система блогов

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}\n{self.content}"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        return self.posts

    def posts_by_author(self, author):
        return [post for post in self.posts if post.author == author]

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            self.posts.pop(index)

    def edit_post(self, index, new_title, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].title = new_title
            self.posts[index].content = new_content

# Домашнее задание 3: Простая банковская система

class Account:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"{self.owner} - Account {self.account_number}: ${self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_balance(self, account_number):
        account = self.accounts.get(account_number)
        return account.balance if account else None

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            return self.accounts[account_number].withdraw(amount)
        return False

    def transfer(self, from_acc, to_acc, amount):
        if self.withdraw(from_acc, amount):
            self.deposit(to_acc, amount)
            return True
        return False
