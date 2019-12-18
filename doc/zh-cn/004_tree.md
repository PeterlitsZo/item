程序结构
===========================
从大的方面来看，程序结构包含了
``` yaml
- src:                    # 源文件目录
    - item:               # 包文件
      - __init__.py
      - color.py          # 提供着色方案
      - core.py           # 提供item类
      - get_Path.py       # 给定一个地址，输出该地址下的所有文件
      - item.py           # 入口程序，处理输入输出，调用item类
      - read_config.py    # 读取配置，返回字典
      # 配置文件
      - global_config.yaml
    - item.py             # 调用item包里面的item.main()函数
                          # 我还是不是很懂到底什么时相对引用
- include:                # 不知道干什么，用来包含外部库的，
      ''                  # 但是python可以自己管理包，就显得很没有用
- doc:                    # 用来包含各国语言的帮助文档
    - ...
    - readme.md           # 索引
- build:                  # 用来存放构建信息
    - item_config.yaml    # 同上
- bin:                    # 用来存储构建好的二进制文件
    ''
- readme.md               # README
- LICENSE
- setup.py                # 通过这个来安装库
- .gitignore
```

（未完）