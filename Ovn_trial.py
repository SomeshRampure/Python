
import win32com.client

try:
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.To = "recipient@example.com"
    mail.Subject = "Test Email from Python"
    mail.Body = "This is a test email sent using Outlook automation."
    mail.Send()
    print("✅ Email sent successfully.")
except Exception as e:
    print(f"❌ Failed to send email: {e}")
