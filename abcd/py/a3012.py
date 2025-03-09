import logging
import os

# 确保日志目录存在
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)  

# 设置日志文件路径
log_file = os.path.join(log_dir, "a3012.log")

# 配置日志
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,  # 记录 INFO 级别及以上的日志
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# 测试日志
logging.info("Scr中午跟ted.")
logging.warning("This is a test warning.")
logging.error("This is a test error.")
