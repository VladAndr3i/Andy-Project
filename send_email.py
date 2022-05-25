import yagmail

yag = yagmail.SMTP("roberto.judet@gmail.com", "")

receiver = "roberto.judet@itschool.ro"
subject = "financial data"
body = "This is a message!"
attach = yagmail.inline("../my_finance/stock/diagram/diagram_nr_2866.png")

yag.send(to=receiver, subject=subject, contents=[body, attach])