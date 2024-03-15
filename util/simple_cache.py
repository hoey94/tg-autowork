import json

from core.settings import Settings


class SimpleCache:
    def __init__(self, storage_file=Settings.TEMP_TG_MSG_FILE):
        self.cache = {}
        self.storage_file = storage_file
        self.load_cache_from_file()

    def put(self, key, value):
        self.cache[key] = value
        self.save_cache_to_file()

    def get(self, key):
        return self.cache.get(key, None)

    def load_cache_from_file(self):
        try:
            with open(self.storage_file, 'r') as file:
                self.cache = json.load(file)
        except FileNotFoundError:
            pass

    def save_cache_to_file(self):
        with open(self.storage_file, 'w') as file:
            json.dump(self.cache, file)

    def __str__(self):
        return str(self.cache)

if __name__ == '__main__':

    # 示例用法：
    cache = SimpleCache()

    # 添加数据到缓存
    cache.put('key1', 53213)
    # cache.put('key2', 30211)

    # 从缓存获取数据
    print(cache.get('key1'))
    print(cache.get('key2'))

    # 输出当前缓存内容
    print(cache)

    # 程序结束时自动保存缓存到文件
