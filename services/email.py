from models.user import User
import mailtrap as mt
import smtplib

from config.config import Settings


async def send_account_verification_email(user: User):
    sender = "ivan8tana@gmail.com"
    receiver = user.email

    mail = mt.Mail(
        sender=mt.Address(email="mailtrap@demomailtrap.com", name="Mailtrap Test"),
        to=[mt.Address(email="ivan8tana@gmail.com")],
        subject="You are awesome!",
        text="Congrats for sending test email with Mailtrap!",
        category="Integration Test",
    )

    client = mt.MailtrapClient(token=Settings().MAILTRAP_TOKEN)
    client.send(mail)


async def send_account_activation_confirmation_email(user: User):
    pass


async def send_password_reset_email(
    user: User,
):
    pass
