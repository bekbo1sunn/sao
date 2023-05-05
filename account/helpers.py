from django.core.mail import send_mail
from account.models import User


def send_spam(new_user):
    users_email = [x.email for x in User.objects.all()]
    message = f'''
Ура!
Вы зарегистрировались!

'''
    send_mail(
        subject="Привет!", 
        message=message, 
        from_email="a@gmail.com", 
        recipient_list=users_email
    )
    