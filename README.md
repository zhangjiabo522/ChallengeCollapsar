
# HTTP 压力测试工具(ceya.py)


## 简介/Introduction

本项目是一个用于对指定 URL 进行 HTTP 压力测试的 Python 脚本。它支持并发请求、请求间隔控制，并自动生成测试报告。

This project is a Python script for performing HTTP stress testing on a specified URL.It supports concurrent requests,request interval control,and automatic test report generation.


## 功能特点/Features


• 并发请求/Concurrent Requests：支持多线程并发访问，提高测试效率。

• 可配置参数/Configurable Parameters：允许用户自定义目标 URL、端口号、请求次数、并发数、请求间隔。

• 错误处理/Error Handling：记录失败请求的错误信息。

• 测试报告/Test Report：自动生成 JSON 格式的压力测试报告。


## 安装与运行/Installation&Usage


## 1.安装依赖/Install Dependencies

确保你的环境安装了`requests`库（Python 3 以上版本自带`concurrent.futures`）。如果未安装，请运行以下命令：


```bash
pip install requests
```



## 2.运行脚本/Run the Script

在终端或命令行输入以下命令：


```bash
python ceya.py
```



## 使用方法/Usage

运行脚本后，按提示输入以下参数：


• 目标 URL/Target URL（必填/Required）：需要进行压力测试的目标地址，例如[]()。

• 端口号/Port Number（可选/Optional）：若目标网站运行在特定端口（如 8080），可手动指定。

• 请求次数/Number of Requests（必填/Required）：需要执行的总请求数，必须是正整数。

• 并发数/Concurrency Level（可选/Optional）：同时执行的最大线程数，默认为 10。

• 请求间隔/Request Interval（可选/Optional）：每个请求之间的等待时间（秒），默认为 0。


## 示例输入/Example Input


```
请输入目标 URL（例如 [https://www.example.com](https://www.example.com)）：[https://www.test.com](https://www.test.com)
请输入端口号（如果不需要，请按 Enter）：8080
请输入请求次数：100
请输入并发数（默认为10）：20
请输入请求间隔（秒，默认为0）：0.5
```



## 示例输出/Example Output


```
开始对 [https://www.test.com:8080](https://www.test.com:8080) 进行压力测试，共 100 次请求，20 并发，间隔 0.5 秒。
请求 1 成功，响应时间：0.20 秒
请求 2 失败，错误信息：连接超时
...
压力测试结果：
总请求次数：100  
成功次数：85  
失败次数：15  
总耗时：21.5 秒  
平均每次请求耗时：0.25 秒  
最大响应时间：1.2 秒  
最小响应时间：0.05 秒  
错误信息：['连接超时', '服务器错误']
```



## 测试报告/Test Report

运行结束后，程序会在当前目录下生成`stress_test_report.json`，示例如下：


```json
{
    "total_requests": 100,
    "successes": 85,
    "failures": 15,
    "total_time": 21.5,
    "average_time": 0.25,
    "max_time": 1.2,
    "min_time": 0.05,
    "error_messages": ["连接超时", "服务器错误"]
}
```



## 适用场景/Use Cases


• 网站压力测试/Website stress testing

• 服务器性能测试/Server performance testing

• API 接口测试/API testing


## 注意事项/Notes


• 请勿在未经授权的情况下对他人网站进行压力测试，否则可能违反相关法规。

• 并发数过高可能会影响本机网络性能，请合理设置参数。

Do not perform stress testing on websites without proper authorization,as this may violate legal regulations.Setting too high a concurrency level may impact your local network performance,so adjust parameters accordingly.


## 许可证/License

本项目基于 MIT 许可证开源，欢迎自由使用与修改。

This project is open-source under the MIT License.Feel free to use and modify it.


