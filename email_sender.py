# -*- coding: utf-8 -*-
"""
邮件发送模块
支持发送HTML格式的价格报告
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime


class EmailSender:
    """邮件发送器"""

    def __init__(self, smtp_server=None, smtp_port=None, username=None, password=None):
        self.smtp_server = smtp_server or os.getenv('SMTP_SERVER', 'smtp.qq.com')
        self.smtp_port = smtp_port or int(os.getenv('SMTP_PORT', '587'))
        self.username = username or os.getenv('EMAIL_USERNAME')
        self.password = password or os.getenv('EMAIL_PASSWORD')

        if not self.username or not self.password:
            raise ValueError("请提供邮箱账号和密码，或设置环境变量 EMAIL_USERNAME 和 EMAIL_PASSWORD")

    def send_price_report(self, to_email, html_content, attachments=None):
        """发送价格报告邮件"""
        try:
            today = datetime.now().strftime('%Y年%m月%d日')
            msg = MIMEMultipart('related')
            msg['Subject'] = f'建筑材料价格日报 - {today}'
            msg['From'] = self.username
            msg['To'] = to_email
            msg.attach(MIMEText(html_content, 'html', 'utf-8'))

            if attachments:
                for filepath in attachments:
                    if os.path.exists(filepath):
                        self._attach_file(msg, filepath)

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(msg)

            print(f"邮件已成功发送至 {to_email}")
            return True
        except Exception as e:
            print(f"发送邮件失败: {e}")
            return False

    def _attach_file(self, msg, filepath):
        """添加附件到邮件"""
        import os
        filename = os.path.basename(filepath)
        with open(filepath, 'rb') as f:
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(f.read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', f'attachment; filename="{filename}"')
        msg.attach(attachment)
