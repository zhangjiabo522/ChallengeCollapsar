import requests
import time
import concurrent.futures
import json
import urllib.parse

def get_user_input():
    """
    获取用户输入的目标 URL、端口（可选）、请求次数、并发数和请求间隔。
    """
    url = input("请输入目标 URL（例如 https://www.example.com）： ").strip()
    port_input = input("请输入端口号（如果不需要，请按 Enter）： ").strip()
    times = input("请输入请求次数： ").strip()
    max_workers = input("请输入并发数（默认为10）： ").strip() or "10"
    interval = input("请输入请求间隔（秒，默认为0）： ").strip() or "0"
    
    # 处理端口号
    if port_input:
        try:
            port = int(port_input)
            parsed_url = urllib.parse.urlparse(url)
            if parsed_url.port is None:
                netloc = f"{parsed_url.hostname}:{port}"
                if parsed_url.scheme == 'https':
                    new_url = f"https://{netloc}{parsed_url.path}"
                else:
                    new_url = f"http://{netloc}{parsed_url.path}"
                url = new_url
        except ValueError:
            print("端口号必须是整数。")
            return None, None, None, None, None
    else:
        port = None
    
    try:
        request_times = int(times)
        if request_times <= 0:
            print("请求次数必须是正整数。")
            return None, None, None, None, None
    except ValueError:
        print("请求次数必须是整数。")
        return None, None, None, None, None
    
    try:
        max_workers = int(max_workers)
        if max_workers <= 0:
            print("并发数必须是正整数。")
            return None, None, None, None, None
    except ValueError:
        print("并发数必须是整数。")
        return None, None, None, None, None
    
    try:
        interval = float(interval)
        if interval < 0:
            print("请求间隔必须是非负数。")
            return None, None, None, None, None
    except ValueError:
        print("请求间隔必须是数字。")
        return None, None, None, None, None
    
    return url, request_times, max_workers, interval

def send_request(url, interval):
    """
    发送单个请求并返回结果。
    """
    try:
        start = time.time()
        response = requests.get(url, timeout=10)  # 设置超时时间为10秒
        end = time.time()
        elapsed = end - start
        return {
            "status_code": response.status_code,
            "elapsed": elapsed,
            "success": response.status_code == 200
        }
    except requests.exceptions.RequestException as e:
        return {
            "status_code": None,
            "elapsed": None,
            "success": False,
            "error": str(e)
        }
    finally:
        time.sleep(interval)

def stress_test(url, request_times, max_workers, interval):
    """
    对指定的 URL 进行压力测试，支持并发请求和请求间隔。
    """
    successes = 0
    failures = 0
    response_times = []
    error_messages = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(send_request, url, interval) for _ in range(request_times)]
        for idx, future in enumerate(concurrent.futures.as_completed(futures), start=1):
            result = future.result()
            if result["success"]:
                successes += 1
                response_times.append(result["elapsed"])
                print(f"请求 {idx} 成功，响应时间：{result['elapsed']:.2f} 秒")
            else:
                failures += 1
                if "error" in result:
                    error_messages.append(result["error"])
                print(f"请求 {idx} 失败，错误信息：{result.get('error', '未知错误')}")
    
    total_time = sum(response_times)
    average_time = total_time / len(response_times) if response_times else 0
    max_time = max(response_times) if response_times else 0
    min_time = min(response_times) if response_times else 0
    
    print("\n压力测试结果：")
    print(f"总请求次数：{request_times}")
    print(f"成功次数：{successes}")
    print(f"失败次数：{failures}")
    print(f"总耗时：{total_time:.2f} 秒")
    print(f"平均每次请求耗时：{average_time:.2f} 秒")
    print(f"最大响应时间：{max_time:.2f} 秒")
    print(f"最小响应时间：{min_time:.2f} 秒")
    print(f"错误信息：{error_messages}")
    
    # 生成测试报告
    report = {
        "total_requests": request_times,
        "successes": successes,
        "failures": failures,
        "total_time": total_time,
        "average_time": average_time,
        "max_time": max_time,
        "min_time": min_time,
        "error_messages": error_messages
    }
    
    with open("stress_test_report.json", "w") as f:
        json.dump(report, f, indent=4)

def main():
    url, request_times, max_workers, interval = get_user_input()
    if url is None:
        return
    
    print(f"\n开始对 {url} 进行压力测试，共 {request_times} 次请求，{max_workers} 并发，间隔 {interval} 秒。")
    stress_test(url, request_times, max_workers, interval)

if __name__ == "__main__":
    main()
