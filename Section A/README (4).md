SECTION B - (Task 2): Java

See solution link after the questions.

Question :
Create a class called Account that contains:
• An int data field named id that stores the accounts unique identification number.
• A double data field named balance that stores the current balance of the account.
• A Date data field named dateCreated that stores the date on which the account was
created.
• A constructor that creates an account with the specified id and initial balance.
• Methods that return the values of all data fields.
• Methods that set the values of the id and balance data fields.
• A method named withdraw that withdraws a specified amount from the Account.
• A method named deposit that deposits a specified amount into the account.
Create two subclasses of the Account class; one for a checking account and one for a
savings account. A checking account has an overdraft limit and a savings account can
earn interest. Call these subclasses SavingsAccount and CheckingAccount.
The SavingsAccount class should contain:
• A double data field named annualInterestRate that stores the current annual interest
rate.
• A method named getMonthlyInterestRate() that returns the monthly interest rate.
Monthly Interest Rate is calculated using annualInterestRate / 12. Note that
annualInterestRate is a percentage so you need to divide it by 100.
• A method named getMonthlyInterest() that returns the monthly interest. Monthly
interest is calculated using balance * monthlyInterestRate.
The CheckingAccount class should contain:
• A double data field named overdraft that stores the overdraft limit.
• A method that returns the value of the overdraft data field.
Now use these classes to simulate an ATM:
• Create five savings accounts and five checking accounts and store them in a list.
• The system should prompt the user to enter an id. If the id is entered incorrectly, it
should ask the user to enter a correct id.
• Once an id is accepted, the main menu should be displayed as follows:
Main menu
1. check balance
2. withdraw
3. deposit
4. exit
• The user should be able to enter 1 to view the current balance, 2 to withdraw money, 3 to
deposit money, and 4 to exit the main menu. Once you exit, the system should prompt
the user for an id again. Thus, once the system starts, it will not stop.

## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

  
## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

  
## Appendix

Any additional information goes here

  
## Authors

- [@EnochAy](https://github.com/EnochAy)
  