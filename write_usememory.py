import psutil
import logging
import time

# ログファイルのフォーマットを定義します。
LOG_FORMAT = '%(asctime)s [%(levelname)s] %(message)s'
# ログファイルの出力先とファイル名を指定します。
logging.basicConfig(filename='memory_usage.log', level=logging.INFO, format=LOG_FORMAT)

def record_memory_usage():
    # 1分ごとにメモリ使用量を取得してログに記録します。
    while True:
        # 現在時刻を取得します。
        current_time = time.strftime('%Y/%m/%d %H:%M:%S')
        # メモリ使用量を取得します。
        memory_usage = round(psutil.virtual_memory().used / 1024 / 1024 / 1024, 1)
        # ログに記録します。
        logging.info(f'{current_time} Memory usage: {memory_usage}')
        # 1分待ちます。
        time.sleep(10)

if __name__ == '__main__':
    record_memory_usage()
