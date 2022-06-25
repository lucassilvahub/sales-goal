<h1 align="center">
<br>
  <img src="https://user-images.githubusercontent.com/54152996/147424802-379e6773-25f8-403a-83b6-e3fbbb9117c2.gif" alt="Sales Goal" width="200">
<br>
<br>
  Sales Goal
</h1>

> Status: Finished ✅

<p>Software designed to read sales tables, check if it has reached the sales goal, identify the salesperson who hit the goal and send a SMS notifying that it has reached the target.</p>

<br>

<p align="center">
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License MIT">
  </a>
</p>

## Technologies Used:

<table>
  <tr>
    <td>Technology</td>
    <td>Python</td>
    <td>Openpyxl</td>
    <td>Pandas</td>
    <td>Twilio</td>
  </tr>
  <tr>
    <td>Version</td>
    <td>3.9.6</td>
    <td>3.0.7</td>
    <td>1.2.4</td>
    <td>6.63.0</td>
  </tr>
</table>

## How to run the application:

1. Install all dependencies;
2. Add your sales sheets for each month;

    ![1](https://user-images.githubusercontent.com/54152996/129397022-28d29576-2695-40a7-9e8f-3fc5073fa48c.jpg)

3. Create a free [Twilio](https://www.twilio.com/try-twilio) account; 
 
4. Get your account_sid, auth_token and your trial phone number;

     ```
    # Your Account SID from twilio.com/console
    account_sid = "W"
    
    # Your Auth Token from twilio.com/console
    auth_token = "X"
    
    # Trial phone number
    from_="Z",
    ```    
    
5. add your phone number to receive the SMS;

    ```
    # Your phone number
    to='Y',
    ```    
    
6. Update the sales target value in code;

    ```
    if (sales_table['Sales'] > 55000).any():
        seller = sales_table.loc[sales_table['Sales'] > 55000, "Seller"].values[0]
        sales = sales_table.loc[sales_table['Sales'] > 55000, "Sales"].values[0]
    ```
    
7. Run.

## SMS Template:

* The software identifies and shows through SMS the salesperson who reached the goal and also how much he made in sales

![git twilio message sales goal](https://user-images.githubusercontent.com/54152996/129395626-f3c77b74-cac6-444c-99d4-ffc46d5573ef.jpeg)

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) page for details..

