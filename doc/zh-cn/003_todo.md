TODO
===========================
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
- UML图。（使用`graphviz`和`Pyreverse`）
- 更好的`setup.py`文件。
- 把`run`和`make`做非特殊化处理。
- 编写`help command`的文档。