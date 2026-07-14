def get_email_domain(email):
    return email.split("@", 1)[1]
    
mail = str(input("Write your email: "))
print(get_email_domain(mail))