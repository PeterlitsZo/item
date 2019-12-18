如何配置自己的配置文件
===========================

配置文件
---------------------------
`item`使用简单的`yaml`文件格式作为数据结构表示。

和应用程序处在同一个文件夹的`yaml`是第一个加载的文件，同时优先度也最低，容易被局部的配置给覆盖住。

比如使用`help`后输出的数据`help_text`如下表示：
``` yaml
help_text: |
  ---------------------------------------------------------------------
  this is item help!

  init: add dirs like 'src', 'bin', 'include', add 'build' and so on.
  make: from src dir's file use gcc or else to build execable file.
  run : run the execable file.

  exit: exit the app_bot.
  quit: exit the qpp_bot.

  help: show this doc.
  ---------------------------------------------------------------------
```

而配置`cpp`的编译运行如下（暂未实现）：
``` yaml
lang_config:
    ...

    cpp:
        make:
        - gcc
        - ${item_root}/src/${file_name}
        - -o
        - ${item_root}/bin/${file_name_without_suffix}
        run:
        - ${item_root}/bin/${file_name}

    ...
```

（未完）