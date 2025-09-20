#Analyse


████████╗ ██████╗      ███████╗ ██████╗  ██████╗ 
╚══██╔══╝██╔═══██╗     ██╔════╝██╔═══██╗██╔═══██╗
   ██║   ██║   ██║     █████╗  ██║   ██║██║   ██║
   ██║   ██║   ██║     ██╔══╝  ██║   ██║██║   ██║
   ██║   ╚██████╔╝     ██║     ╚██████╔╝╚██████╔╝
   ╚═╝    ╚═════╝      ╚═╝      ╚═════╝  ╚═════╝





🧭 TG‑SEC Assistant — خلاصه معرفی
این ابزار یک دستیار امنیتی برای تلگرامه که روی Termux، Kali Linux، macOS و Windows Terminal اجرا می‌شه.  
کار اصلیش اینه که کدها و فایل‌های پروژه‌ت رو بررسی کنه و موارد حساس یا مشکوک رو پیدا کنه.  

✨ قابلیت‌ها
- 🔑 اسکن نشت کلیدها و توکن‌ها (مثل Bot Token، API ID/Hash، AWS Keys و …)  
- 🔗 شناسایی لینک‌های مشکوک و فیشینگ (دامنه‌های جعلی یا شبیه‌سازی‌شده)  
- 📡 مانیتور وبهوک‌ها (بررسی وضعیت HTTP و TLS)  
- 📊 گزارش‌دهی کامل: خروجی JSON و داشبورد HTML رنگی با ایموجی و استایل حرفه‌ای  

⚡ مزایا
- اجرا روی موبایل (Termux) و دسکتاپ بدون نیاز به هاست خارجی  
- سبک، سریع و قابل بازیابی از GitHub  
- داشبورد آنلاین از طریق GitHub Pages  

-

`markdown
<h1 align="center">🧭 TG‑SEC Assistant</h1>
<p align="center">
  <b>ابزار امنیت تلگرام · اجرا روی Termux/Kali · بدون نیاز به هاست خارجی</b><br>
  <i>اسکن کلیدها، بررسی لینک‌های مشکوک، مانیتور وبهوک‌ها و داشبورد رنگی روی GitHub Pages</i>
</p>

---


`
┌──────────────────────────────────────────┐
│  🧭 TG‑SEC · Termux/Kali · GitHub Actions │
└──────────────────────────────────────────┘
`

---

📊 زبان‌ها و تکنولوژی‌ها

<p align="center">
  <!-- زبان‌ها -->
  <img src="https://img.shields.io/badge/Python-90%25-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML-5%25-orange?logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS-3%25-blueviolet?logo=css3&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-2%25-yellow?logo=javascript&logoColor=black" />
</p>

<p align="center">
  <!-- تکنولوژی‌ها -->
  <img src="https://img.shields.io/badge/Termux-black?logo=linux&logoColor=white" />
  <img src="https://img.shields.io/badge/Kali%20Linux-blue?logo=kalilinux&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-gray?logo=githubactions&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub%20Pages-181717?logo=github&logoColor=white" />
</p>

---

⚡ قابلیت‌ها
- 🔑 اسکن نشت توکن‌ها و API Keyها (Telegram Bot Token, API ID/Hash, AWS Keys, JWT و …)  
- 🔗 بررسی لینک‌های مشکوک (دامنه‌های فیشینگ و lookalike)  
- 📡 مانیتور وبهوک بات‌ها (وضعیت HTTP, TLS, latency)  
- 📊 گزارش JSON + داشبورد HTML رنگی با ایموجی و استایل حرفه‌ای  

---

📥 نصب و راه‌اندازی

روی Termux
`bash
pkg update -y && pkg upgrade -y
pkg install -y git python
git clone https://github.com/MRAvarvokiranshare/Analyse.git
cd Analyse
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
`



اگر ارور دا با روش دوم اجرا کنید 

cd ~/Analyse
source .venv/bin/activate

# ساخت فایل تست با یک Bot Token الکی
echo "BOT_TOKEN = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'" > test.py

# اجرای اسکن روی کل پروژه + آپدیت داشبورد
python -m tgsec.cli scan-secrets --path . --dashboard

# ذخیره تغییرات و پوش به گیت‌هاب
git add .
git commit -m "تست ابزار TG-SEC با توکن الکی"
git push origin main

روی Kali Linux
`bash
sudo apt update && sudo apt install -y git python3 python3-venv
git clone https://github.com/MRAvarvokiranshare/Analyse.git
cd Analyse
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
`

روی macOS / Linux Terminal
`bash
git clone https://github.com/MRAvarvokiranshare/Analyse.git
cd Analyse
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
`

روی Windows (PowerShell)
`powershell
git clone https://github.com/MRAvarvokiranshare/Analyse.git
cd Analyse
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
`

---

🖥️ اجرای ابزار

اسکن نشت کلیدها
`bash
python -m tgsec.cli scan-secrets --path . --dashboard
`

بررسی لینک‌های مشکوک
`bash
python -m tgsec.cli links --file README.md --dashboard
`

مانیتور وبهوک‌ها
`bash
python -m tgsec.cli webhook https://example.com/hook --secret-preview TEST --dashboard
`

---

