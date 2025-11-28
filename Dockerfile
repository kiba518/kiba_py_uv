
FROM python:3.14

# 设置工作目录
WORKDIR /app

# 设置环境变量，保证 Python 输出实时显示
ENV PYTHONUNBUFFERED=1

# 复制依赖文件
# 如果 UV 项目没有 requirements.txt，可以先导出：
# uv export requirements > requirements.txt
COPY requirements.txt /app/

# 安装依赖
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# 复制整个项目
COPY . /app

# 暴露 FastAPI 默认端口
EXPOSE 5001

# 启动命令
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5001", "--reload"]
