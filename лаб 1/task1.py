class Book:
    """
    Represents a book with its title, author, and number of pages.
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        pages (int): The number of pages in the book. Must be a positive integer.
    """

    def __init__(self, title: str, author: str, pages: int):
        """
        Initializes a Book object.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            pages (int): The number of pages in the book.
        Raises:
            TypeError: If any argument has an incorrect type.
            ValueError: If the number of pages is not a positive integer.
        """
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")

        if not isinstance(author, str):
            raise TypeError("Author must be a string.")

        if not isinstance(pages, int):
            raise TypeError("Pages must be an integer.")

        if pages <= 0:
            raise ValueError("Number of pages must be a positive integer.")

        self.title = title
        self.author = author
        self.pages = pages

    def get_details(self) -> str:
        """
        Returns a string containing the book's details.
        Returns:
            str: A string containing the title, author, and number of pages.
        >>> book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1178)
        >>> book.get_details()
        'Title: The Lord of the Rings, Author: J.R.R. Tolkien, Pages: 1178'
        """
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def read_chapter(self, chapter_number: int, chapter_length: int = 10) -> str:
        """
        Simulates reading a chapter of the book.
        Args:
            chapter_number (int): The chapter number to read. Must be a positive integer.
            chapter_length (int, optional): Approximate length of the chapter in pages. Defaults to 10.
        Returns:
            str: A message indicating which chapter was read.
        Raises:
            TypeError: If chapter_number or chapter_length are not integers.
            ValueError: If chapter_number or chapter_length are not positive.
        >>> book = Book("The Hobbit", "J.R.R. Tolkien", 310)
        >>> book.read_chapter(1)
        'Reading chapter 1...'
        """
        if not isinstance(chapter_number, int):
            raise TypeError("Chapter number must be an integer.")

        if not isinstance(chapter_length, int):
            raise TypeError("Chapter length must be an integer.")

        if chapter_number <= 0:
            raise ValueError("Chapter number must be a positive integer.")

        if chapter_length <= 0:
            raise ValueError("Chapter length must be a positive integer.")

        return f"Reading chapter {chapter_number}..."


class BankAccount:
    """
    Represents a bank account with a balance and account number.
    Attributes:
        account_number (str): The account number.
        balance (float): The current balance in the account. Must be non-negative.
    """

    def __init__(self, account_number: str, balance: float = 0.0):
        """
        Initializes a BankAccount object.
        Args:
            account_number (str): The account number.
            balance (float, optional): The initial balance. Defaults to 0.0.
        Raises:
            TypeError: If the balance is not a float.
            ValueError: If the balance is negative.
        """
        self.account_number = account_number
        if not isinstance(balance, float):
            raise TypeError("Balance must be a float.")
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.balance = balance

    def deposit(self, amount: float) -> float:
        """
        Deposits money into the account.
        Args:
            amount (float): The amount to deposit. Must be positive.
        Returns:
            float: The new balance after the deposit.
        Raises:
            TypeError: If the amount is not a float.
            ValueError: If the amount is not positive.
        >>> account = BankAccount("12345", 100.0)
        >>> account.deposit(50.0)
        150.0
        """
        if not isinstance(amount, float):
            raise TypeError("Amount must be a float.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Withdraws money from the account.
        Args:
            amount (float): The amount to withdraw. Must be positive and not exceed the balance.
        Returns:
            float: The new balance after the withdrawal.
        Raises:
            TypeError: If the amount is not a float.
            ValueError: If the amount is not positive or exceeds the balance.
        >>> account = BankAccount("67890", 200.0)
        >>> account.withdraw(100.0)
        100.0
        """
        if not isinstance(amount, float):
            raise TypeError("Amount must be a float.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance


class SocialNetwork:
    """Represents a social network with a name and number of users."""

    def __init__(self, name: str, num_users: int):
        """Initializes a SocialNetwork object."""
        self.name = name
        if not isinstance(num_users, int):
            raise TypeError("Number of users must be an integer.")
        if num_users < 0:
            raise ValueError("Number of users must be a non-negative integer.")
        self.num_users = num_users

    def add_users(self, num_new_users: int) -> int:
        """Adds new users to the social network.
        Args:
            num_new_users (int): The number of new users to add. Must be non-negative.
        Returns:
            int: The updated number of users.
        Raises:
            TypeError: if num_new_users is not an integer.
            ValueError: if num_new_users is negative.
        >>> sn = SocialNetwork("ExampleNet", 1000)
        >>> sn.add_users(500)
        1500
        """
        if not isinstance(num_new_users, int):
            raise TypeError("Number of new users must be an integer.")
        if num_new_users < 0:
            raise ValueError("Number of new users cannot be negative.")
        self.num_users += num_new_users
        return self.num_users

    def get_user_count(self) -> int:
        """Returns the current number of users."""
        return self.num_users
