import sys
import json
import time

def handle_command(command, args):
    """
    根据接收到的命令和参数执行相应的逻辑，并返回响应数据。
    """
    if command == "PING":
        # 简单的心跳/测试命令
        return {"status": "PONG", "time": time.time()}

    elif command == "GET_INFO":
        # 返回一些程序信息
        return {
            "name": "My_Stdio_MCP_Server",
            "version": "1.0.0",
            "capabilities": ["PING", "GET_INFO", "TASK"]
        }

    elif command == "TASK":
        # 执行一个耗时任务的模拟
        try:
            task_name = args[0]
            if task_name == "setup":
                # 实际执行任务...
                return {"status": "SUCCESS", "message": f"Task '{task_name}' completed."}
            else:
                return {"status": "ERROR", "message": f"Unknown task: {task_name}"}
        except IndexError:
            return {"status": "ERROR", "message": "TASK command requires an argument."}

    else:
        return {"status": "ERROR", "message": f"Unknown command: {command}"}

def mcp_stdio_loop():
    print("MCP Stdio Server Started.") # 启动信息，可能被工具忽略

    # 持续从标准输入读取
    while True:
        try:
            # 读取一行命令
            line = sys.stdin.readline()
            if not line:
                # EOF，通常表示MCP工具已关闭连接
                break

            # 清理和解析命令
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            command = parts[0].upper()
            args = parts[1:]

            if command == "QUIT":
                print("BYE")
                break

            # 处理命令
            response_data = handle_command(command, args)

            # --- 响应输出 ---
            # 1. 打印JSON格式的响应数据
            print(json.dumps(response_data))
            # 2. 打印一个状态行或分隔符，告诉工具一个响应结束了
            #    （具体分隔符取决于你的目标MCP工具要求，例如可能是单个 "OK" 行）
            print("OK")

            # 刷新输出缓冲区，确保数据立即发送给MCP工具
            sys.stdout.flush()

        except Exception as e:
            # 发生异常，报告错误并刷新
            print(json.dumps({"status": "FATAL_ERROR", "message": str(e)}))
            print("ERROR")
            sys.stdout.flush()
            # 严重错误可能需要退出
            # break

if __name__ == "__main__":
    mcp_stdio_loop()