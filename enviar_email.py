import smtplib
from email.message import EmailMessage

def enviar_email():
    email = EmailMessage()
    email["Subject"] = "Relatório automático"
    email["From"] = "seuemail@gmail.com"
    email["To"] = "destinatario@gmail.com"

    email.set_content("Segue o relatório de vendas.")

    with open("relatorio/relatorio_final.csv", "rb") as f:
        email.add_attachment(
            f.read(),
            maintype="application",
            subtype="csv",
            filename="relatorio.csv"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("seuemail@gmail.com", "sua_senha")
        smtp.send_message(email)

    print("Email enviado!")