![git header sales goal python](https://user-images.githubusercontent.com/54152996/129388901-22bf8432-865d-4c86-8dbe-3a0390819015.png)

> Status: Finished ✅

Software designed to read sales tables, check if it has reached the sales target, identify the salesperson who hit the sales target and send a SMS notifying that it has reached the target.

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
    if (sales_table['Sales'] > 55000).any():
        seller = sales_table.loc[sales_table['Sales']
                                > 55000, "Seller"].values[0]
        sales = sales_table.loc[sales_table['Sales']
                                > 55000, "Sales"].values[0]
    ```
6. Update the sales target value in code;
    ```
    # Your phone number
    to='Y',
    ```    
7. Run.

## SMS Template:

* The software identifies and shows through SMS the salesperson who reached the goal and also how much he made in sales

![git twilio message sales goal](https://user-images.githubusercontent.com/54152996/129395626-f3c77b74-cac6-444c-99d4-ffc46d5573ef.jpeg)

