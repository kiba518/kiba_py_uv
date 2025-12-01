## Milvus
官网有在desktop上安装的步骤。
官网：https://milvus.io/docs/zh/install_standalone-windows.md
在powershell里执行命令
```
Invoke-WebRequest https://raw.githubusercontent.com/milvus-io/milvus/refs/heads/master/scripts/standalone_embed.bat -OutFile standalone.bat
.\standalone.bat start
```
运行安装脚本后

名为Milvus-standalone的 docker 容器已在19530 端口启动。

嵌入式 etcd 与 Milvus 安装在同一个容器中，服务端口为2379。其配置文件被映射到当前文件夹中的embedEtcd.yaml。

Milvus 数据卷映射到当前文件夹中的volumes/milvus。

可以使用以下命令管理 Milvus 容器和存储的数据。

```
.\standalone.bat stop
Stop successfully.

.\standalone.bat delete
Delete Milvus container successfully. # Container has been removed.
Delete successfully. # Data has been removed.
```

## 安装并启动 Milvus Insight（GUI 可视化工具）
```angular2html
docker pull milvusdb/milvus-insight:latest

docker run -d -p 8181:3000 --name insight milvusdb/milvus-insight:latest

```
然后在浏览器能使用可视化工具了。
```
http://localhost:8181
```

界面如下：

![1764320257708](C:\GitHub\kiba_py_uv\README-Milvus.assets\1764320257708.png)

但这个工具，我连接不上milvus。

## milvus测试非常不稳定，不知道原因，同一个代码，创建集合，在A项目就异常，在B项目就正常。

后来找到了解决方案，就是修改启动配置文件

![1764589429302](C:\GitHub\kiba_py_uv\README-Milvus.assets\1764589429302.png)

因为项目跟uv项目是放一起了，所以默认使用了uv的环境下的python.exe。但为什么不好使，不知道，因为uv下也安装了pymilvus。