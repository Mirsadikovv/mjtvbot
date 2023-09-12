from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili


DP_USER = env.str("DP_USER")
DP_PASS = env.str("DP_PASS")
DP_NAME = env.str("DP_NAME")
DP_HOST = env.str("DP_HOST")