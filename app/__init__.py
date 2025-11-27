# api/__init__.py
print("api package loaded")
import logging

# 1. 配置 Logger
# 设置 level=logging.DEBUG 将 Logger 和默认的 Handler 都设置为 DEBUG 级别
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# 获取一个 logger 实例
logger = logging.getLogger(__name__)

# 2. 输出 DEBUG 日志
logger.debug("这是一个 DEBUG 级别的消息，通常用于详细的流程跟踪。")
logger.info("这是一个 INFO 级别的消息。")
logger.warning("这是一个 WARNING 级别的消息。")