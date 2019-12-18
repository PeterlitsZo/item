item
===========================
item 是用来快速管理，运行，开发结构化程序的命令行小程序。

命令列表
---------------------------
- init: 在当前目录下新建`src`（存放源文件），`build`（存放构建信息），`include`（存放外部库或文件），`bin`（存放可执行二进制文件）
- make: 把`src`目录下的源文件通过`gcc`编译到`bin`文件夹下。
- run: 执行二进制文件。
- help: 显示帮助。

依赖项
---------------------------
使用`pip install the-package-you-want-to-install`来安装相关的包。
- colored: 用来给输出染色，没有该包输出会全变为默认颜色。
- pyyaml: 用来读取配置文件。

配置文件
---------------------------
使用简单的`yaml`文件格式作为数据结构表示。

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

todo
---------------------------
- 通过读取yaml配置文件，来改变`item`的行为。如：使用的编辑器，`init`后构建的模板结构，使用什么编译器，来生成文件。
- `yaml`应该有有全局和局部的区别。我们应该一开始就提供好简单易用的`yaml`配置文件，尽量不让大家在配置文件上浪费过多时间。
- `init` 命令应该可以通过不同的模板来初始化，比如提供给`init`的参数是`cpp`和是`python`后的结果应该不一样。可以体现在`./build/item_config.yaml`文件中。
- `help.txt`之后应该存储在全局的`yaml`文件下。
- 在doc文件夹下应该有一个`en.md`来提供英文`markdown`文档。
- 提供用`pyinstall`生成的二进制文件。
- `item._get_valid_file`中键入`?q`后退出的功能还没有实现。
- 打算做一个vscode的插件。
- 听说读取配置时`libyaml`会更快一点，之后争取搞上去。（脸红）
- 用`config`命令来修改变量。
- 实现tab补全和模糊搜索。
- UML图。
- 更好的`setup.py`文件。