from models.user import User
import mailtrap as mt
import smtplib
import jinja2

from config.config import Settings


from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader("./templates"),
    autoescape=select_autoescape(["html", "xml"]),
)


async def send_account_verification_email(user: User):
    sender = "ivan8tana@gmail.com"
    receiver = user.email

    template = env.get_template("user/account-verification.html")

    html_content = template.render(
        name=user.full_name,
        activate_url="https://example.com/activate",
        app_name="LearnWise",
    )

    mail = mt.Mail(
        sender=mt.Address(
            email="mailtrap@demomailtrap.com", name="Account  Verification"
        ),
        to=[mt.Address(email="ivan8tana@gmail.com")],
        subject="Account Varification!",
        html=html_content,
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
