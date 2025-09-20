# 所有可能涉及的编码点

## **算法编程题可能有模板**

实质是将所有算法进行对应的分类


## python

### 内置数据结构及其特点

| 数据结构 | 类型    | 可变性 | 是否有序 | 是否支持重复元素 | 常用方法/操作                             | 适用场景与特点                                       |
|----------|---------|--------|----------|------------------|------------------------------------------|------------------------------------------------------|
| list     | 列表    | ✅ 可变 | ✅ 有序   | ✅ 支持           | append(), extend(), pop(), sort(), etc. | 存储多个元素，顺序重要，常用于收集和处理数据         |
| tuple    | 元组    | ❌ 不可变 | ✅ 有序 | ✅ 支持           | count(), index()                         | 不可变、可以作为字典的键，提高安全性与性能          |
| dict     | 字典    | ✅ 可变 | ✅ 有序（3.7+） | ❌ 不支持（键） | get(), keys(), values(), items(), update() | 键值对结构，适用于查找/映射类型的数据               |
| set      | 集合    | ✅ 可变 | ❌ 无序   | ❌ 不支持         | add(), remove(), union(), intersection() | 去重、集合运算，快速查找                            |
| frozenset| 冻结集合| ❌ 不可变 | ❌ 无序 | ❌ 不支持         | 支持集合操作但不可修改                    | 用于需要不可变集合的场合，如字典的键                 |
| str      | 字符串  | ❌ 不可变 | ✅ 有序 | ✅ 支持（字符）   | split(), join(), replace(), format()     | 文本数据的存储和处理，支持切片操作                   |
| range    | 范围    | ❌ 不可变 | ✅ 有序 | ✅ 支持（生成）   | 可迭代、可索引                            | 生成数字序列，常用于循环                             |
| bytes    | 字节串  | ❌ 不可变 | ✅ 有序 | ✅                | decode(), hex(), etc.                    | 处理二进制数据或与文件/网络通信交互时使用            |
| bytearray| 字节数组| ✅ 可变 | ✅ 有序  | ✅                | 支持大部分 bytes 的方法                  | 需要修改二进制数据的场景                             |


### string 字符串

| 函数名                      | 功能说明              | 参数说明                           | 示例                                               |
| ------------------------ | ----------------- | ------------------------------ | ------------------------------------------------ |
| `str.lower()`            | 转换为小写             | 无                              | `'ABC'.lower()` → `'abc'`                        |
| `str.upper()`            | 转换为大写             | 无                              | `'abc'.upper()` → `'ABC'`                        |
| `str.strip()`            | 去除首尾空白字符          | `chars`：可选，指定要去除的字符            | `'  hello \n'.strip()` → `'hello'`               |
| `str.lstrip()`           | 去除左侧空白字符          | 同上                             | `'  hello'.lstrip()` → `'hello'`                 |
| `str.rstrip()`           | 去除右侧空白字符          | 同上                             | `'hello   '.rstrip()` → `'hello'`                |
| `str.replace(old, new)`  | 替换子串              | `old`：要替换的字符串<br>`new`：替换成的字符串 | `'a-b-c'.replace('-', '')` → `'abc'`             |
| `str.split(sep)`         | 拆分为列表             | `sep`：分隔符，默认为空格                | `'a,b,c'.split(',')` → `['a', 'b', 'c']`         |
| `str.join(iterable)`     | 将序列拼接成字符串         | `iterable`：如列表、元组等             | `'-'.join(['a','b','c'])` → `'a-b-c'`            |
| `str.startswith(prefix)` | 判断是否以某前缀开头        | `prefix`：前缀字符串                 | `'hello'.startswith('he')` → `True`              |
| `str.endswith(suffix)`   | 判断是否以某后缀结尾        | `suffix`：后缀字符串                 | `'world'.endswith('ld')` → `True`                |
| `str.find(sub)`          | 查找子串首次出现位置        | `sub`：要查找的子串                   | `'hello'.find('l')` → `2`                        |
| `str.rfind(sub)`         | 查找子串最后一次出现的位置     | 同上                             | `'hello'.rfind('l')` → `3`                       |
| `str.count(sub)`         | 统计子串出现次数          | `sub`：要统计的子串                   | `'banana'.count('a')` → `3`                      |
| `str.isdigit()`          | 判断是否全是数字          | 无                              | `'123'.isdigit()` → `True`                       |
| `str.isalpha()`          | 判断是否全是字母          | 无                              | `'abc'.isalpha()` → `True`                       |
| `str.isalnum()`          | 判断是否全是字母或数字       | 无                              | `'abc123'.isalnum()` → `True`                    |
| `str.isspace()`          | 判断是否全是空白字符        | 无                              | `'  \t\n'.isspace()` → `True`                    |
| `str.title()`            | 每个单词首字母大写         | 无                              | `'hello world'.title()` → `'Hello World'`        |
| `str.capitalize()`       | 首字母大写，其余小写        | 无                              | `'hello world'.capitalize()` → `'Hello world'`   |
| `str.zfill(width)`       | 左侧补零              | `width`：总长度                    | `'42'.zfill(5)` → `'00042'`                      |
| `str.format(...)`        | 格式化字符串            | 支持位置或关键字参数                     | `'{} + {} = {}'.format(1, 2, 3)` → `'1 + 2 = 3'` |
| `f"{...}"`               | 格式化字符串 (f-string) | 表达式直接嵌入                        | `name = 'Tom'; f"Hello {name}"` → `'Hello Tom'`  |




### tuple 元组

| 方法/函数           | 功能描述                                                      | 示例                             |
|---------------------|---------------------------------------------------------------|----------------------------------|
| `len(tuple)`        | 返回元组的长度（元素个数）                                   | `len((1, 2, 3))  # 输出: 3`      |
| `tuple.count(x)`    | 返回元素 `x` 在元组中出现的次数                               | `(1, 2, 2, 3).count(2)`          |
| `tuple.index(x)`    | 返回元素 `x` 第一次出现的索引                                 | `(1, 2, 3).index(2)`             |
| `tuple()`           | 将其他可迭代对象转换为元组                                   | `tuple([1, 2]) → (1, 2)`         |
| `in`, `not in`      | 成员运算符，判断元素是否在元组中                             | `'a' in ('a', 'b') → True`       |
| `max(tuple)`        | 返回元组中最大的元素（元素必须可比较）                       | `max((1, 5, 3)) → 5`             |
| `min(tuple)`        | 返回元组中最小的元素                                          | `min((1, 5, 3)) → 1`             |
| `sum(tuple)`        | 返回元组中所有数值元素的总和                                  | `sum((1, 2, 3)) → 6`             |
| `sorted(tuple)`     | 返回元组中元素的排序结果（结果是列表）                       | `sorted((3, 1, 2)) → [1, 2, 3]`  |
| `enumerate(tuple)`  | 返回枚举对象，用于遍历时获取索引和值                         | `for i, v in enumerate(t): ...` |
| `zip(tuple1, ...)`  | 将多个元组合并为一个个元组对                                 | `zip((1,2), ('a','b'))`          |


### dict 字典常用函数

| 方法名           | 功能描述                                                                 | 示例                                      |
|------------------|--------------------------------------------------------------------------|-------------------------------------------|
| `dict.get(key)`  | 获取指定键的值，不存在时返回 `None` 或指定默认值                        | `d.get('a', 0)`                            |
| `dict.keys()`    | 返回字典中所有键的视图                                                   | `d.keys()`                                |
| `dict.values()`  | 返回字典中所有值的视图                                                   | `d.values()`                              |
| `dict.items()`   | 返回包含键值对的视图对象（`(key, value)` 元组）                         | `d.items()`                               |
| `dict.update()`  | 更新字典，使用另一个字典或键值对序列                                    | `d.update({'b': 2})`                       |
| `dict.pop(key)`  | 删除指定键并返回对应的值                                                 | `d.pop('a')`                              |
| `dict.popitem()` | 删除并返回字典中最后插入的键值对（Python 3.7+保持插入顺序）             | `d.popitem()`                             |
| `dict.clear()`   | 清空字典                                                                 | `d.clear()`                               |
| `dict.copy()`    | 返回字典的浅拷贝                                                         | `new_d = d.copy()`                        |
| `dict.setdefault(key, default)` | 若 key 不存在，设置为默认值并返回该值，否则返回已有值       | `d.setdefault('a', 100)`                  |
| `fromkeys(seq, val)` | 使用序列中元素作为键创建新字典，值都设为 `val`                      | `dict.fromkeys(['x', 'y'], 0)`            |

### set 集合

| 方法名                   | 功能描述                                                                 | 示例                                        |
|--------------------------|--------------------------------------------------------------------------|---------------------------------------------|
| `add(elem)`              | 向集合添加元素，如果已存在则无效果                                     | `s.add(5)`                                  |
| `remove(elem)`           | 删除集合中的指定元素，不存在会抛出错误                                 | `s.remove(3)`                               |
| `discard(elem)`          | 删除集合中的指定元素，不存在不会抛出错误                               | `s.discard(10)`                             |
| `pop()`                  | 随机删除并返回一个元素                                                 | `s.pop()`                                   |
| `clear()`                | 清空集合                                                               | `s.clear()`                                 |
| `copy()`                 | 返回集合的浅拷贝                                                       | `new_set = s.copy()`                        |
| `union(*others)` 或 `|`  | 并集操作：返回包含所有集合元素的新集合                                | `s1.union(s2)` 或 `s1 | s2`                 |
| `intersection(*others)` 或 `&` | 交集操作：返回所有集合共有的元素                                | `s1 & s2`                                   |
| `difference(*others)` 或 `-`   | 差集操作：返回只在当前集合中的元素                               | `s1 - s2`                                   |
| `symmetric_difference(other)` 或 `^` | 对称差集：仅存在于一个集合中的元素                         | `s1 ^ s2`                                   |
| `update(*others)` 或 `|=`     | 原地并集更新当前集合                                               | `s1.update(s2)`                             |
| `intersection_update(*others)` | 原地交集更新                                                      | `s1.intersection_update(s2)`                |
| `difference_update(*others)`   | 原地差集更新                                                      | `s1.difference_update(s2)`                  |
| `symmetric_difference_update(other)` | 原地对称差集更新                                             | `s1.symmetric_difference_update(s2)`        |
| `issubset(other)`        | 判断当前集合是否是另一个集合的子集                                   | `s1.issubset(s2)`                           |
| `issuperset(other)`      | 判断当前集合是否是另一个集合的超集                                   | `s1.issuperset(s2)`                         |
| `isdisjoint(other)`      | 判断两个集合是否没有交集（是否不相交）                               | `s1.isdisjoint(s2)`                         |
#### set 集合的逻辑运算

| 运算符 | 方法名称                       | 功能描述                                     | 示例                          |
|--------|--------------------------------|----------------------------------------------|-------------------------------|
| `|`    | `union()`                      | 并集：返回两个集合的所有元素（去重）         | `A | B` 或 `A.union(B)`       |
| `&`    | `intersection()`               | 交集：返回两个集合的公共元素                 | `A & B` 或 `A.intersection(B)`|
| `-`    | `difference()`                 | 差集：返回只在 A 不在 B 中的元素             | `A - B` 或 `A.difference(B)`  |
| `^`    | `symmetric_difference()`       | 对称差集：返回只在一个集合中不在另一个集合中 | `A ^ B` 或 `A.symmetric_difference(B)` |
| `<=`   | `issubset()`                   | 子集判断：A 是否是 B 的子集                  | `A <= B`                      |
| `<`    |                                | 真子集判断：A 是 B 的子集且不等于 B          | `A < B`                       |
| `>=`   | `issuperset()`                 | 超集判断：A 是否是 B 的超集                  | `A >= B`                      |
| `>`    |                                | 真超集判断：A 是 B 的超集且不等于 B          | `A > B`                       |
| `==`   |                                | 判断两个集合是否相等                         | `A == B`                      |
| `!=`   |                                | 判断两个集合是否不相等                       | `A != B`                      |



### list 链表

| 方法名              | 功能描述                                                     | 示例代码                              |
|---------------------|--------------------------------------------------------------|----------------------------------------|
| `append(x)`         | 在列表末尾添加一个元素 x                                     | `lst.append(5)`                        |
| `extend(iterable)`  | 扩展列表，将可迭代对象中的所有元素添加到列表末尾            | `lst.extend([4, 5])`                   |
| `insert(i, x)`      | 在指定位置 i 插入元素 x                                      | `lst.insert(2, 10)`                    |
| `remove(x)`         | 删除列表中第一个出现的元素 x                                 | `lst.remove(3)`                        |
| `pop([i])`          | 删除并返回指定位置 i 的元素，默认删除最后一个元素           | `lst.pop()` 或 `lst.pop(1)`            |
| `clear()`           | 清空列表                                                     | `lst.clear()`                          |
| `index(x[, start[, end]])` | 返回元素 x 第一次出现的索引位置（可指定范围）       | `lst.index(2)`                         |
| `count(x)`          | 返回元素 x 在列表中出现的次数                                | `lst.count(3)`                         |
| `sort(key=None, reverse=False)` | 就地排序列表                                  | `lst.sort()` 或 `lst.sort(reverse=True)` |
| `reverse()`         | 就地反转列表                                                 | `lst.reverse()`                        |
| `copy()`            | 返回列表的浅拷贝                                             | `new_lst = lst.copy()`                 |
| `len(lst)`          | 返回列表中元素的个数                                         | `len(lst)`                             |
| `max(lst)`          | 返回列表中的最大值                                           | `max(lst)`                             |
| `min(lst)`          | 返回列表中的最小值                                           | `min(lst)`                             |
| `sum(lst)`          | 返回所有数值型元素的总和                                     | `sum([1, 2, 3])`                        |
| `sorted(lst)`       | 返回排序后的新列表（原列表不变）                            | `sorted(lst)`                          |
| `enumerate(lst)`    | 返回带索引的可枚举对象，可用于 `for i, v in enumerate(lst)` | `enumerate(lst)`                       |
| `zip(lst1, lst2)`   | 将多个列表组合成元组列表                                     | `zip([1,2], ['a','b'])`                |


### 文件读写函数

| 函数/方法         | 功能描述                                               | 示例代码                                      |
|------------------|--------------------------------------------------------|-----------------------------------------------|
| `open()`         | 打开文件并返回文件对象                                 | `f = open('file.txt', 'r')`                   |
| `read()`         | 读取整个文件内容（字符串形式）                         | `content = f.read()`                          |
| `readline()`     | 一次读取一行                                           | `line = f.readline()`                         |
| `readlines()`    | 一次读取所有行，返回列表                               | `lines = f.readlines()`                       |
| `write()`        | 向文件写入字符串                                       | `f.write("hello world\n")`                    |
| `writelines()`   | 向文件写入多个字符串（不自动换行）                    | `f.writelines(["line1\n", "line2\n"])`        |
| `close()`        | 关闭文件，释放资源                                     | `f.close()`                                   |
| `with open()`    | 上下文管理器，自动管理文件打开与关闭                  | `with open('file.txt', 'r') as f:`            |
| `seek(offset)`   | 移动文件指针到指定位置                                 | `f.seek(0)`                                   |
| `tell()`         | 返回当前文件指针位置                                   | `pos = f.tell()`                              |
| `flush()`        | 刷新写入缓冲区，立即写入磁盘                          | `f.flush()`                                   |
| `truncate(size)` | 截断文件到指定大小，默认截断到当前位置                | `f.truncate(10)`                              |
| `mode`           | 文件访问模式属性（只读、写入等）                      | `f.mode`                                      |
| `name`           | 返回文件名                                             | `f.name`                                      |
| `encoding`       | 返回文件的编码类型（如 UTF-8）                        | `f.encoding`                                  |


#### 文件打开模式说明

| 模式   | 含义                                       | 是否可读 | 是否可写 | 文件存在时行为                  | 文件不存在时行为               |
|--------|--------------------------------------------|----------|----------|-------------------------------|------------------------------|
| `'r'`  | 只读模式（默认）                            | ✅       | ❌       | 打开文件，从开头读取            | 报错（FileNotFoundError）    |
| `'w'`  | 只写模式                                    | ❌       | ✅       | 清空原文件内容                  | 创建新文件                   |
| `'a'`  | 追加模式                                    | ❌       | ✅       | 从文件末尾添加内容              | 创建新文件                   |
| `'r+'` | 可读写模式（读写文件）                      | ✅       | ✅       | 不清空原文件，从头开始读写      | 报错                         |
| `'w+'` | 可读写模式（先清空再写）                    | ✅       | ✅       | 清空原文件，从头开始读写        | 创建新文件                   |
| `'a+'` | 可读写模式（追加时写、可读）                | ✅       | ✅       | 从末尾追加，读不清空文件        | 创建新文件                   |
| `'rb'` | 以二进制模式读取                           | ✅       | ❌       | 读取二进制内容                  | 报错                         |
| `'wb'` | 以二进制模式写入（清空内容）               | ❌       | ✅       | 清空原文件内容写入二进制        | 创建新文件                   |
| `'ab'` | 以二进制模式追加写入                       | ❌       | ✅       | 向文件末尾追加二进制内容        | 创建新文件                   |
| `'rb+'`| 以二进制读写模式                           | ✅       | ✅       | 从头开始读写二进制内容          | 报错                         |
| `'wb+'`| 以二进制读写模式，清空内容写入             | ✅       | ✅       | 清空后读写二进制                | 创建新文件                   |
| `'ab+'`| 以二进制追加读写模式                       | ✅       | ✅       | 从末尾追加写，文件可读取二进制  | 创建新文件                   |

说明：
1. 文本模式（默认）：不加 b，如 'r', 'w'，处理字符串（如 "hello"）。
2. 二进制模式：加 b，如 'rb', 'wb'，处理字节数据（如 b"hello"）。
3. 所有模式中，加上 + 都代表同时支持读写。

### 异常

| 异常类型               | 含义说明                                                                 |
|------------------------|--------------------------------------------------------------------------|
|`BaseException`|所有异常的基类。|
|`SystemExit`|请求退出解释器。|
| `SyntaxError`          | 语法错误，例如拼写错误、缺少冒号、括号未闭合等                         |
| `IndentationError`     | 缩进错误，代码块未正确缩进                                               |
| `NameError`            | 使用了未定义的变量名                                                     |
| `TypeError`            | 数据类型不匹配，例如把字符串当作数字处理                                 |
| `ValueError`           | 值类型正确，但值本身不合法（如将字母转换为整数）                        |
| `IndexError`           | 索引越界，如访问不存在的列表元素                                         |
| `KeyError`             | 访问字典中不存在的键                                                     |
| `AttributeError`       | 访问对象中不存在的属性或方法                                             |
| `ZeroDivisionError`    | 除数为零导致错误                                                         |
| `FileNotFoundError`    | 文件或路径不存在时触发                                                   |
| `IOError`              | 输入/输出操作失败（如文件读写出错，Python3中多用`OSError`代替）          |
| `OSError`              | 操作系统相关错误（如文件不存在、权限不足）                              |
| `ImportError`          | 无法引入模块或模块中不存在的成员                                         |
| `ModuleNotFoundError`  | Python 无法找到指定模块（是 `ImportError` 的子类）                      |
| `RuntimeError`         | 程序运行中出现的常规错误，不属于其他具体类型                            |
| `RecursionError`       | 函数递归次数过多，超过最大递归深度限制                                   |
| `MemoryError`          | 内存溢出，程序申请的内存超出了系统可用内存                               |
| `StopIteration`        | 迭代器无更多内容时触发，通常用于 `for` 循环或 `next()` 中                 |
| `AssertionError`       | 断言失败，如使用 `assert` 表达式不满足时触发                            |
| `KeyboardInterrupt`    | 用户手动中断程序执行（如 Ctrl+C）                                        |
| `EOFError`             | `input()` 函数读取到输入结束（如 Ctrl+D）时触发                         |


### 函数参数

| 参数类型         | 语法示例                              | 说明                                                                 |
|------------------|----------------------------------------|----------------------------------------------------------------------|
| 位置参数         | `def func(a, b):`                      | 调用函数时，必须按顺序传入所有参数                                  |
| 默认参数         | `def func(a, b=10):`                   | 为参数设置默认值，调用时可以不传该参数                              |
| 可变位置参数     | `def func(*args):`                     | 将多个位置参数打包成一个元组                                        |
| 可变关键字参数   | `def func(**kwargs):`                  | 将多个关键字参数打包成一个字典                                      |
| 仅限关键字参数   | `def func(*, a, b):`                   | `a` 和 `b` 只能作为关键字参数传入                                   |
| 仅限位置参数     | `def func(a, b, /):`                   | `/` 之前的参数只能作为位置参数传入（Python 3.8+ 支持）             |
| 混合参数         | `def func(a, b=1, *args, c, **kwargs):`| 综合使用所有类型，顺序必须为：位置 → 默认 → *args → 仅限关键字 → **kwargs |


|知识点|函数名称|常用形式|参数说明|
|---|---|---|---|
|||zscore(a, axis=0, ddof=0, nan_policy='propagate', keepdims=False)||


### 数据处理pandas

| 函数名                                     | 功能说明          | 常用参数                                                                        | 示例（基于 `df`）                                               |
| --------------------------------------- | ------------- | --------------------------------------------------------------------------- | --------------------------------------------------------- |
| `df.drop_duplicates()`                  | 去除重复行         | `subset`: 指定列去重<br>`keep`: 保留方式（'first'/'last'/False）<br>`inplace`: 是否原地修改  | `df.drop_duplicates(subset=['A'], keep='first')`          |
| `df.drop()`                             | 删除指定行或列       | `labels`: 标签名<br>`axis`: 0=行，1=列<br>`inplace`: 是否原地修改                       | `df.drop(['col1'], axis=1)`<br>`df.drop([0, 2], axis=0)`  |
| `df.isnull()`                           | 判断是否为空        | 无                                                                           | `df['col1'].isnull()` → 返回布尔 Series                       |
| `df.notnull()`                          | 判断是否非空        | 无                                                                           | `df['col1'].notnull()`                                    |
| `df.dropna()`                           | 删除空值所在的行/列    | `axis`: 0=行，1=列<br>`how`: 'any' 或 'all'<br>`thresh`: 至少非空数<br>`subset`: 指定列 | `df.dropna(how='any')`<br>`df.dropna(thresh=2)`           |
| `df.fillna(value)`                      | 填充空值          | `value`: 单值或 dict<br>`method`: 'ffill' 或 'bfill'<br>`inplace`: 是否原地修改       | `df.fillna(0)`<br>`df.fillna({'A': 0, 'B': '未知'})`        |
| `df['col'].fillna(df['col'].mean())`    | 用均值填充         | 通常配合 `mean()` 使用                                                            | `df['A'].fillna(df['A'].mean())`                          |
| `df['col'].fillna(df['col'].median())`  | 用中位数填充        | 通常配合 `median()` 使用                                                          | `df['A'].fillna(df['A'].median())`                        |
| `df['col'].fillna(df['col'].mode()[0])` | 用众数填充         | `mode()` 返回 Series，要取 `[0]`                                                 | `df['A'].fillna(df['A'].mode()[0])`                       |
| `df.replace()`                          | 替换值           | `to_replace`: 原值<br>`value`: 替换后的值<br>`inplace`: 是否原地修改                     | `df.replace('未知', np.nan)`<br>`df.replace({0: '缺失'})`     |
| `df.replace(regex=...)`                 | 正则替换          | `regex`: 字符串或字典                                                             | `df.replace(regex={'A': r'\d+', 'B': r'foo'}, value='X')` |
| `df.mask(cond, value)`                  | 条件替换为某值       | `cond`: 条件<br>`value`: 替换值                                                  | `df['A'].mask(df['A'] < 0, 0)`                            |
| `df.where(cond, value)`                 | 条件为 False 时替换 | 与 `mask` 相反逻辑                                                               | `df['A'].where(df['A'] > 0, 0)`                           |
|`Series.map(arg)`| |arg一般是字典。用于将离散的字符串转化为数值。|`gender_map = {'male': 0, 'female': 1}`<br> `train['Sex_encoded'] = train['Sex'].map(gender_map)`|

- drop() 用于删除行或列，常与 axis 参数配合使用。
- dropna() 会直接丢弃有空值的行或列，fillna() 用于保留数据并进行填充。
- fillna()、replace() 等支持 inplace=True 进行原地修改。
- 使用 mode()（众数）时注意返回的是 Series，需加 [0] 取第一个值。

pandas的字符串处理函数：
`Series.str.contains()` 方法用于判断指定系列是否包含指定字符串。类似于 SQL 中的 like 函数，实现模糊匹配。str 将 Series 转换为类似于 String 。的结构。
`Series.str.isin()` isin 方法用于判断给定元素是否在给定的列表中，返回布尔序列。
`~Series.str.isin()` 不存在 isnotin 函数，直接在 isin 前面添加 ~ 即可。


在使用groupby()函数之后，会出现多层index的情况，这个时候可以将多层index理解为新增的列，只不过列中有重复的值。这些值是由于groupby造成的（这句话没有看到例子可能无法理解的）。

`countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])`在使用了groupby()之后的多层索引结构：
|||len|
|---|---|---|
|country	|province	||
|Argentina	|Mendoza Province|	3264|
||Other|	536|
|...	|...	|...|
|Uruguay	|San Jose|	3|
||Uruguay|	24|

```python
mi = countries_reviewed.index
type(mi)
```
查看多层索引的数据类型。
```log
pandas.core.indexes.multi.MultiIndex
```

重置多层索引`countries_reviewed.reset_index()`之后的数据结构：
|	|country	|province	|len|
|---|---|---|---|
|0	|Argentina	|Mendoza Province|	3264|
|1	|Argentina	|Other|	536|
|...	|...	|...	|...|
|423	|Uruguay	|San Jose	|3|
|424	|Uruguay	|Uruguay|	24|

### 数据统计pandas
| 函数名                 | 功能说明                           | 常用参数                                                | 示例（基于 `df`）                                     |
| ------------------- | ------------------------------ | --------------------------------------------------- | ----------------------------------------------- |
| `df.describe()`     | 快速统计摘要（计数、均值、标准差、最小值、四分位数、最大值） | `percentiles`: 指定分位点<br>`include/exclude`: 包含哪些数据类型 | `df.describe()`<br>`df.describe(include='all')` |
| `df.mean()`         | 计算平均值                          | `axis`: 0=列，1=行<br>`skipna`: 是否跳过 NaN               | `df.mean()`                                     |
| `df.median()`       | 中位数                            | 同上                                                  | `df.median()`                                   |
| `df.mode()`         | 众数（可能多个）                       | `axis`: 默认 0                                        | `df.mode()`                                     |
| `df.std()`          | 标准差                            | `ddof`: 自由度（默认 1）                                   | `df.std()`                                      |
| `df.var()`          | 方差                             | 同上                                                  | `df.var()`                                      |
| `df.min()`          | 最小值                            | 同上                                                  | `df.min()`                                      |
| `df.max()`          | 最大值                            | 同上                                                  | `df.max()`                                      |
| `df.count()`        | 非空值数量                          | `axis` 可选                                           | `df.count()`                                    |
| `df.sum()`          | 求和                             | 可选择 axis                                            | `df.sum()`                                      |
| `df.quantile(q)`    | 计算分位数                          | `q`: 0\~1 的 float 或列表                               | `df.quantile(0.75)`                             |
| `df.corr()`         | 计算相关系数（默认皮尔逊）                  | `method`: 'pearson'（默认）、'kendall'、'spearman'        | `df.corr(method='spearman')`                    |
| `df.cov()`          | 协方差矩阵                          | 无                                                   | `df.cov()`                                      |
| `df.value_counts()` | 统计频次（仅限 Series）                | `normalize`: 是否显示占比<br>`dropna`: 是否忽略 NaN           | `df['col'].value_counts()`                      |
| `df.nunique()`      | 统计唯一值数量                        | `dropna`: 是否忽略 NaN                                  | `df.nunique()`                                  |
| `df.duplicated()`   | 判断是否为重复行                       | `subset`: 指定列<br>`keep`: 'first'/'last'/False       | `df.duplicated()`                               |
| `df.idxmax()`       | 返回最大值对应的索引                     | `axis`: 默认 0<br>`skipna`: 是否跳过 NaN                  | `df.idxmax()`                                   |
| `df.idxmin()`       | 最小值对应的索引                       | 同上                                                  | `df.idxmin()`                                   |

`df['col_name'].unique()`

`df['col_name'].value_counts()`


| 函数                            | 功能说明                      | 示例                            |
| ----------------------------- | ------------------------- | ----------------------------- |
| `df.isnull()`                 | 返回与原数据等形状的布尔矩阵，空值为 `True` | `df.isnull()`                 |
| `df.isnull().sum()`           | 每列空值数量统计（最常用）             | `df.isnull().sum()`           |
| `df.isnull().sum().sum()`     | 所有空值的总数                   | `df.isnull().sum().sum()`     |
| `df.isna()`                   | 与 `isnull()` 完全等价         | `df.isna().sum()`             |
| `df.info()`                   | 快速查看每列非空数量和类型             | `df.info()`                   |
| `df[df.isnull().any(axis=1)]` | 筛选出含有空值的行                 | `df[df.isnull().any(axis=1)]` |


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, 3],
    'B': [4, 5, np.nan],
    'C': [7, 8, 9]
})

print(df.isnull())
# 显示布尔矩阵

print(df.isnull().sum())
# 输出每列中空值的个数：
# A    1
# B    1
# C    0

print(df.isnull().sum().sum())
# 输出整个 DataFrame 中空值总数：2

# 统计 每行的空值数量
df.isnull().sum(axis=1)
```

### pandas 时间处理

| 函数/属性                                           | 主要参数                              | 功能说明                                   |
| ----------------------------------------------- | --------------------------------- | -------------------------------------- |
| `pd.to_datetime(arg, ...)`                      | `arg`, `format`, `utc`, `errors`  | 将字符串、列表、Series 转换为 `datetime64[ns]` 类型 |
| `pd.to_timedelta(arg, ...)`                     | `arg`, `unit`, `errors`           | 将数字或字符串转换为时间差对象 `Timedelta`            |
| `pd.date_range(start, end, periods, freq)`      | `start`, `end`, `periods`, `freq` | 生成等间隔时间序列                              |
| `pd.timedelta_range(start, end, periods, freq)` | 同上                                | 生成时间差序列                                |
| `pd.period_range(start, end, periods, freq)`    | 同上                                | 生成 Period 序列（固定频率的时间段）                 |
| `pd.DatetimeIndex(...)`                         | `data`, `freq`, `tz`, ...         | 创建一个时间索引                               |
| `pd.PeriodIndex(...)`                           | `data`, `freq`, `tz`, ...         | 创建一个周期索引                               |


| 属性/方法                                                    | 返回值类型           | 功能说明             |
| -------------------------------------------------------- | --------------- | ---------------- |
| `.year`, `.month`, `.day`, `.hour`, `.minute`, `.second` | `int`           | 提取具体时间字段         |
| `.dayofweek`, `.weekday`                                 | `int` (0=周一)    | 返回星期几            |
| `.dayofyear`                                             | `int`           | 年内的第几天           |
| `.is_month_start`, `.is_month_end`                       | `bool`          | 是否月初 / 月末        |
| `.normalize()`                                           | `DatetimeIndex` | 设置时间为当天 00:00:00 |
| `.floor(freq)`                                           | `DatetimeIndex` | 向下取整（如：按天、小时）    |
| `.ceil(freq)`                                            | `DatetimeIndex` | 向上取整             |
| `.round(freq)`                                           | `DatetimeIndex` | 四舍五入到某个频率        |

| 函数/对象                                            | 参数                    | 功能说明                           |
| ------------------------------------------------ | --------------------- | ------------------------------ |
| `pd.Timedelta(value, unit)`                      | `value`, `unit`       | 构造时间差，如 `'1 day'`, `'2 hours'` |
| `Timedelta.days`, `.seconds`, `.total_seconds()` | -                     | 获取差值的组成部分                      |
| `pd.DateOffset(...)`                             | `days`, `months`, ... | 灵活构造偏移量                        |
| `pd.offsets.MonthEnd(n)`                         | `n`                   | 表示每月末偏移量                       |
| `.shift(periods, freq)`                          | `periods`, `freq`     | 对时间序列按频率平移                     |
| `.resample(rule)`                                | `rule`                | 重新采样（如按天、月汇总）                  |
| `.asfreq(freq)`                                  | `freq`                | 转换为指定频率的数据                     |

| 函数                          | 功能说明              |
| --------------------------- | ----------------- |
| `pd.Timestamp(...)`         | 创建单个时间戳对象         |
| `pd.Period(...)`            | 创建周期对象（如“2024Q1”） |
| `.strftime(fmt)`            | 将时间格式化为字符串（按格式）   |
| `.strptime(s, fmt)`         | 将字符串按格式解析为时间      |
| `.between_time(start, end)` | 选取特定时间段的行（仅时间部分）  |
| `.at_time(time)`            | 筛选指定时间的行          |



### 模型算法函数（scikit-learn）
| 算法名称                      | 所属模块           | 导入方式                                                  | 函数/类                       | 常用参数说明                                               |
| ------------------------- | -------------- | ----------------------------------------------------- | -------------------------- | ---------------------------------------------------- |
| 线性回归（Linear Regression）   | `linear_model` | `from sklearn.linear_model import LinearRegression`   | `LinearRegression()`       | `fit_intercept=True`, `normalize=False`（新版废弃）        |
| 逻辑回归（Logistic Regression） | `linear_model` | `from sklearn.linear_model import LogisticRegression` | `LogisticRegression()`     | `penalty='l2'`, `C=1.0`, `solver='lbfgs'`            |
| 决策树（Decision Tree）        | `tree`         | `from sklearn.tree import DecisionTreeClassifier`     | `DecisionTreeClassifier()` | `criterion='gini'`, `max_depth=None`                 |
| 支持向量机（SVM）                | `svm`          | `from sklearn.svm import SVC`                         | `SVC()`                    | `kernel='rbf'`, `C=1.0`, `gamma='scale'`             |
| K最近邻（KNN）                 | `neighbors`    | `from sklearn.neighbors import KNeighborsClassifier`  | `KNeighborsClassifier()`   | `n_neighbors=5`, `metric='minkowski'`                |
| K均值聚类（KMeans）             | `cluster`      | `from sklearn.cluster import KMeans`                  | `KMeans()`                 | `n_clusters=8`, `random_state=0`, `init='k-means++'` |


| 模型                         | 主要参数                | 参数作用                   | 常见调参范围（经验值）                                                  |
| -------------------------- | ------------------- | ---------------------- | ------------------------------------------------------------ |
| **LinearRegression**       | `fit_intercept`     | 是否计算截距                 | `True` / `False`                                             |
|                            | `normalize`（已弃用）    | 是否在回归前标准化特征            | 一般不使用，改用 `StandardScaler`                                    |
| **LogisticRegression**     | `penalty`           | 正则化方式                  | `l1`, `l2`, `elasticnet`, `none`                             |
|                            | `C`                 | 正则化强度（越小正则化越强）         | `0.001` \~ `100`（对数刻度搜索）                                     |
|                            | `solver`            | 优化算法选择                 | `liblinear`, `saga`, `lbfgs`（根据数据大小和正则化方式选择）                 |
|                            | `max_iter`          | 最大迭代次数                 | `100` \~ `1000`                                              |
| **DecisionTreeClassifier** | `criterion`         | 划分质量指标                 | `gini`, `entropy`, `log_loss`                                |
|                            | `max_depth`         | 树最大深度                  | `3` \~ `None`（`None`表示不限制）                                   |
|                            | `min_samples_split` | 内部分裂所需最小样本数            | `2` \~ `20`                                                  |
|                            | `min_samples_leaf`  | 叶子节点最少样本数              | `1` \~ `10`                                                  |
|                            | `max_features`      | 划分时考虑的特征数              | `None`, `sqrt`, `log2`, 或整数                                  |
| **DecisionTreeRegressor**  | `criterion`         | 划分质量指标                 | `squared_error`, `friedman_mse`, `absolute_error`, `poisson` |
|                            | `max_depth`         | 树最大深度                  | `3` \~ `None`                                                |
|                            | `min_samples_split` | 内部分裂所需最小样本数            | `2` \~ `20`                                                  |
|                            | `min_samples_leaf`  | 叶子节点最少样本数              | `1` \~ `10`                                                  |
|                            | `max_features`      | 划分时考虑的特征数              | `None`, `sqrt`, `log2`, 或整数                                  |
| **SVC**                    | `C`                 | 惩罚系数（越小正则化越强）          | `0.01` \~ `100`（对数刻度搜索）                                      |
|                            | `kernel`            | 核函数                    | `linear`, `poly`, `rbf`, `sigmoid`                           |
|                            | `gamma`             | RBF/poly/sigmoid 核函数系数 | `'scale'`, `'auto'`, 或 `1e-4` \~ `10`                        |
|                            | `degree`            | `poly` 核的多项式次数         | `2` \~ `5`                                                   |
| **SVR**                    | `C`                 | 惩罚系数                   | `0.01` \~ `100`                                              |
|                            | `kernel`            | 核函数                    | `linear`, `poly`, `rbf`, `sigmoid`                           |
|                            | `gamma`             | 核系数                    | `'scale'`, `'auto'`, 或 `1e-4` \~ `10`                        |
|                            | `epsilon`           | 允许误差范围（不惩罚的区域）         | `0.01` \~ `1`                                                |
| **KNeighborsClassifier**   | `n_neighbors`       | 邻居数                    | `3` \~ `20`                                                  |
|                            | `weights`           | 权重方式                   | `'uniform'`, `'distance'`                                    |
|                            | `metric`            | 距离度量方式                 | `'minkowski'`（默认 p=2），`'manhattan'`                          |
|                            | `p`                 | Minkowski 距离的 p 值      | `1`（曼哈顿）或 `2`（欧氏）                                            |
| **KMeans**                 | `n_clusters`        | 聚类数                    | `2` \~ `数据特征数`                                               |
|                            | `init`              | 初始质心方法                 | `'k-means++'`, `'random'`                                    |
|                            | `n_init`            | 重新初始化次数                | `10` \~ `50`                                                 |
|                            | `max_iter`          | 最大迭代次数                 | `100` \~ `1000`                                              |
|                            | `tol`               | 收敛容忍度                  | `1e-4` \~ `1e-6`                                             |
|                            | `random_state`      | 随机种子                   | 任意整数，保证结果可复现                                                 |




### 模型评估函数（scikit-learn）

#### 分类的评价指标

| 指标名称                   | 所属模块      | 导入方式                                              | 函数名                                   | 参数说明                               |
| ---------------------- | --------- | ------------------------------------------------- | ------------------------------------- | ---------------------------------- |
| 准确率（Accuracy）          | `metrics` | `from sklearn.metrics import accuracy_score`      | `accuracy_score(y_true, y_pred)`      | `normalize=True/False`             |
| 精确度（Precision）         | `metrics` | `from sklearn.metrics import precision_score`     | `precision_score(y_true, y_pred)`     | `average='binary'/‘macro’/‘micro’` |
| 召回率（Recall）            | `metrics` | `from sklearn.metrics import recall_score`        | `recall_score(y_true, y_pred)`        | `average=...`                      |
| F1 分数（F1-score）        | `metrics` | `from sklearn.metrics import f1_score`            | `f1_score(y_true, y_pred)`            | `average=...`                      |
| 混淆矩阵（Confusion Matrix） | `metrics` | `from sklearn.metrics import confusion_matrix`    | `confusion_matrix(y_true, y_pred)`    | -                                  |
| 均方误差（MSE）              | `metrics` | `from sklearn.metrics import mean_squared_error`  | `mean_squared_error(y_true, y_pred)`  | `squared=True/False`               |
| 平均绝对误差（MAE）            | `metrics` | `from sklearn.metrics import mean_absolute_error` | `mean_absolute_error(y_true, y_pred)` | -                                  |
| 交叉熵（log loss）          | `metrics` | `from sklearn.metrics import log_loss`            | `log_loss(y_true, y_prob)`            | 适用于概率输出                            |


#### 聚类算法的评价指标

| 指标名称                                   | 类型 | 取值范围     | 含义                                                  | 优劣势                          |
| -------------------------------------- | -- | -------- | --------------------------------------------------- | ---------------------------- |
| **Silhouette Coefficient（轮廓系数）**       | 内部 | \[-1, 1] | 衡量样本与同簇的紧密度与与最近簇的分离度。1 表示聚类效果好，0 表示簇间重叠，负值表示样本被分错簇。 | 直观易懂，适合簇形状较规则的情况，但对簇形状和分布敏感。 |
| **Calinski-Harabasz Index（CH 指数）**     | 内部 | \[0, +∞) | 簇间离散度 / 簇内离散度，值越大聚类效果越好。                            | 计算快，适合高维数据，但可能对簇大小差异敏感。      |
| **Davies-Bouldin Index（DB 指数）**        | 内部 | \[0, +∞) | 簇内相似度与簇间差异的比值，越小越好。                                 | 计算简单，适合自动选择簇数，但在噪声多时不稳定。     |
| **Dunn Index（Dunn 指数）**                | 内部 | \[0, +∞) | 最小簇间距离 / 最大簇内直径，越大越好。                               | 对小簇敏感，受噪声影响大，计算较慢。           |
| **Rand Index（RI）**                     | 外部 | \[0, 1]  | 衡量预测簇标签与真实标签的一致性。1 表示完全一致。                          | 简单直观，但对簇数量差异敏感。              |
| **Adjusted Rand Index（ARI）**           | 外部 | \[-1, 1] | 对 RI 进行调整，随机聚类的期望值为 0。越接近 1 越好。                     | 不受簇数量影响，适合不同簇规模比较。           |
| **Mutual Information (MI)**            | 外部 | \[0, +∞) | 聚类结果与真实标签的互信息，越大越好。                                 | 对簇规模不平衡敏感。                   |
| **Normalized Mutual Information（NMI）** | 外部 | \[0, 1]  | 对 MI 归一化，1 表示完全一致。                                  | 可比较不同数据集聚类效果，常用。             |
| **Homogeneity（同质性）**                   | 外部 | \[0, 1]  | 簇内样本是否属于同一真实类别，1 表示完全同质。                            | 适合类别数接近簇数的情况。                |
| **Completeness（完整性）**                  | 外部 | \[0, 1]  | 一个真实类别的样本是否全部在同一簇中，1 表示完全完整。                        | 与 Homogeneity 配合使用更有意义。      |
| **V-Measure**                          | 外部 | \[0, 1]  | Homogeneity 与 Completeness 的调和平均数，越大越好。             | 兼顾同质性与完整性，平衡评估效果。            |
| **Fowlkes-Mallows Index（FMI）**         | 外部 | \[0, 1]  | 聚类正确率与召回率的几何平均数，1 表示完全一致。                           | 适合簇数接近真实类别数的情况。              |


### 特征选择（scikit-learn）

| 方法/类名                                              | 主要参数                                                             | 作用简介                    |
| -------------------------------------------------- | ---------------------------------------------------------------- | ----------------------- |
| `sklearn.feature_selection.SelectKBest`            | `score_func`（评分函数，默认`f_classif`），`k`（选择的特征数量，默认10）               | 根据评分函数选择得分最高的k个特征       |
| `sklearn.feature_selection.SelectPercentile`       | `score_func`，`percentile`（选择的百分比特征数）                             | 选择得分最高的百分比特征            |
| `sklearn.feature_selection.VarianceThreshold`      | `threshold`（方差阈值，默认0）                                            | 移除低方差特征（方差低于阈值的特征）      |
| `sklearn.feature_selection.RFE` (递归特征消除)           | `estimator`（基础模型），`n_features_to_select`（选择特征数），`step`（每次消除的特征数） | 递归地训练模型并消除不重要特征         |
| `sklearn.feature_selection.RFECV` (带交叉验证的RFE)      | `estimator`，`step`，`cv`（交叉验证策略）                                  | 基于交叉验证自动选择最优特征数的递归特征消除  |
| `sklearn.feature_selection.SelectFromModel`        | `estimator`（已训练模型），`threshold`（阈值）                               | 根据模型权重或重要性自动选择特征        |
| `sklearn.feature_selection.chi2`                   | 无（输入X,y）                                                         | 卡方统计量，用于分类任务的特征选择评分函数   |
| `sklearn.feature_selection.f_classif`              | 无                                                                | 方差分析F值，用于分类任务的特征评分函数    |
| `sklearn.feature_selection.f_regression`           | 无                                                                | 线性回归相关的F值评分函数，用于回归任务    |
| `sklearn.feature_selection.mutual_info_classif`    | `discrete_features`，`n_neighbors`等                               | 互信息法，用于分类任务的非线性特征选择评分函数 |
| `sklearn.feature_selection.mutual_info_regression` | `discrete_features`，`n_neighbors`等                               | 用于回归任务的互信息评分函数          |

### 降维（scikit-learn）

| 方法名称            | 函数/类名                                                      | 是否监督 | 主要参数           | 参数说明                                               |
| --------------- | ---------------------------------------------------------- | ---- | -------------- | -------------------------------------------------- |
| **PCA**（主成分分析）  | `sklearn.decomposition.PCA`                                | 否    | `n_components` | 降维后的目标维度或保留的方差比例（如 0.95 表示保留 95% 信息）               |
|                 |                                                            |      | `svd_solver`   | SVD 求解方式：`auto`, `full`, `arpack`, `randomized`    |
|                 |                                                            |      | `whiten`       | 是否对每个主成分进行归一化处理（默认为 False）                         |
| **LDA**（线性判别分析） | `sklearn.discriminant_analysis.LinearDiscriminantAnalysis` | 是    | `n_components` | 降维后的维度（最多为类别数减1）                                   |
|                 |                                                            |      | `solver`       | 求解算法：`svd`, `lsqr`, `eigen`                        |
|                 |                                                            |      | `shrinkage`    | 收缩参数（仅用于 `lsqr` 或 `eigen`）用于稳定协方差矩阵估计              |
| **LLE**（局部线性嵌入） | `sklearn.manifold.LocallyLinearEmbedding`                  | 否    | `n_neighbors`  | 每个点的邻居数，用于构建局部结构                                   |
|                 |                                                            |      | `n_components` | 降维后的目标维度                                           |
|                 |                                                            |      | `method`       | 使用的LLE变体：`standard`, `modified`, `hessian`, `ltsa` |
|                 |                                                            |      | `eigen_solver` | 特征值求解器，如 `auto`, `dense`, `arpack`                 |
|                 |                                                            |      | `random_state` | 随机种子，影响求解初始值                                       |



### 处理时间pandas

| 函数 / 属性                             | 功能描述                 | 参数说明                              | 示例代码                                                  |
| ----------------------------------- | -------------------- | --------------------------------- | ----------------------------------------------------- |
| `pd.to_datetime()`                  | 字符串或列转换为 datetime 类型 | `format`, `errors`, `utc`, `unit` | `df['time'] = pd.to_datetime(df['time'])`             |
| `.dt.year`                          | 提取年份                 | 仅适用于 datetime 类型列                 | `df['year'] = df['time'].dt.year`                     |
| `.dt.month`                         | 提取月份                 | 同上                                | `df['month'] = df['time'].dt.month`                   |
| `.dt.day`                           | 提取日                  | 同上                                | `df['day'] = df['time'].dt.day`                       |
| `.dt.hour`                          | 提取小时                 | 同上                                | `df['hour'] = df['time'].dt.hour`                     |
| `.dt.minute`                        | 提取分钟                 | 同上                                | `df['minute'] = df['time'].dt.minute`                 |
| `.dt.second`                        | 提取秒                  | 同上                                | `df['second'] = df['time'].dt.second`                 |
| `.dt.date`                          | 只提取日期（date 类型）       | 无                                 | `df['only_date'] = df['time'].dt.date`                |
| `.dt.strftime()`                    | 时间格式化为字符串            | `format` 格式                       | `df['time_str'] = df['time'].dt.strftime('%Y-%m')`    |
| `df.resample()`                     | 按时间重采样（需设定时间为索引）     | `rule`, `on`, `agg()` 等           | `df.resample('D').sum()`                              |
| `(df['col1'] - df['col2']).dt.days` | 计算时间差（单位为天）          | `timedelta` 系列                    | `df['diff_days'] = (df['end'] - df['start']).dt.days` |
| `df['col'].dt.floor()`              | 向下取整到最近的时间单位         | 例如 'D', 'H', 'T'(分钟)              | `df['floor_day'] = df['time'].dt.floor('D')`          |


## SQL

### 处理时间

| 函数名                      | 功能描述            | 常见参数说明                   | 示例                                                      |
| ------------------------ | --------------- | ------------------------ | ------------------------------------------------------- |
| `NOW()`                  | 返回当前日期和时间       | 无                        | `SELECT NOW();`                                         |
| `CURDATE()`              | 返回当前日期（不含时间）    | 无                        | `SELECT CURDATE();`                                     |
| `CURTIME()`              | 返回当前时间（不含日期）    | 无                        | `SELECT CURTIME();`                                     |
| `DATE()`                 | 提取日期部分          | `datetime` 类型字段          | `SELECT DATE(order_time)`                               |
| `YEAR()`                 | 提取年份            | `datetime`               | `SELECT YEAR(order_time)`                               |
| `MONTH()`                | 提取月份            | `datetime`               | `SELECT MONTH(order_time)`                              |
| `DAY()` / `DAYOFMONTH()` | 提取日             | `datetime`               | `SELECT DAY(order_time)`                                |
| `HOUR()`                 | 提取小时            | `datetime`               | `SELECT HOUR(order_time)`                               |
| `MINUTE()`               | 提取分钟            | `datetime`               | `SELECT MINUTE(order_time)`                             |
| `SECOND()`               | 提取秒             | `datetime`               | `SELECT SECOND(order_time)`                             |
| `DATEDIFF()`             | 计算两个日期之间的天数     | `DATEDIFF(date1, date2)` | `SELECT DATEDIFF('2025-06-10', '2025-01-01')`           |
| `TIMESTAMPDIFF()`        | 计算两个时间之间的差（按单位） | `unit, date1, date2`     | `SELECT TIMESTAMPDIFF(DAY, '2025-01-01', '2025-06-10')` |
| `DATE_FORMAT()`          | 格式化日期输出         | `date, format_string`    | `SELECT DATE_FORMAT(order_time, '%Y-%m-%d')`            |
| `STR_TO_DATE()`          | 字符串转日期          | `string, format`         | `SELECT STR_TO_DATE('2025-01-01', '%Y-%m-%d')`          |


### SQL字符串函数

| 函数名               | 语法格式                                                              | 参数说明                                                                                   | 功能描述                                                                 |
|----------------------|-----------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `CHAR_LENGTH()`      | `CHAR_LENGTH(str)`                                                    | `str`: 要计算长度的字符串                                                                  | 返回字符串中的字符数（注意不是字节数）                                  |
| `LENGTH()`           | `LENGTH(str)`                                                         | `str`: 要计算字节长度的字符串                                                              | 返回字符串的字节长度（多字节字符长度大于1）                             |
| `CONCAT()`           | `CONCAT(str1, str2, ..., strN)`                                       | 多个字符串                                                                                 | 连接多个字符串为一个字符串                                               |
| `CONCAT_WS()`        | `CONCAT_WS(separator, str1, str2, ..., strN)`                         | `separator`: 分隔符；`strN`: 要连接的字符串                                                | 用指定分隔符连接多个字符串                                               |
| `SUBSTRING()`        | `SUBSTRING(str, pos [, len])`                                         | `pos`: 起始位置（从1开始）；`len`：可选长度                                                | 从字符串中截取子字符串                                                   |
| `SUBSTRING_INDEX()`  | `SUBSTRING_INDEX(str, delim, count)`                                  | `str`: 原始字符串；`delim`: 分隔符；`count`: 截取的段数（正数从左，负数从右）             | 根据分隔符提取子字符串                                                   |
| `LEFT()`             | `LEFT(str, len)`                                                      | `len`: 提取的字符数                                                                        | 从左边开始提取指定长度的子字符串                                         |
| `RIGHT()`            | `RIGHT(str, len)`                                                     | `len`: 提取的字符数                                                                        | 从右边开始提取指定长度的子字符串                                         |
| `INSTR()`            | `INSTR(str, substr)`                                                  | `substr`: 要查找的子字符串                                                                 | 返回子字符串在原字符串中首次出现的位置（没有返回0）                     |
| `LOCATE()`           | `LOCATE(substr, str [, start])`                                       | `start`: 可选起始位置                                                                      | 查找子字符串位置，支持起始位置                                           |
| `POSITION()`         | `POSITION(substr IN str)`                                             | 同 `LOCATE()`                                                                             | 同上，语法不同                                                           |
| `REPLACE()`          | `REPLACE(str, from_str, to_str)`                                      | 将 `from_str` 替换为 `to_str`                                                              | 替换指定的子字符串                                                       |
| `REVERSE()`          | `REVERSE(str)`                                                        | `str`: 输入字符串                                                                          | 反转字符串                                                               |
| `LTRIM()`            | `LTRIM(str)`                                                          | 去掉字符串左边的空格                                                                      |                                                                          |
| `RTRIM()`            | `RTRIM(str)`                                                          | 去掉字符串右边的空格                                                                      |                                                                          |
| `TRIM()`             | `TRIM([[LEADING | TRAILING | BOTH] remstr FROM] str)`                 | `remstr`: 要去除的字符，默认是空格                                                         | 去除字符串首尾的字符或空格                                               |
| `LPAD()`             | `LPAD(str, len, padstr)`                                              | 用 `padstr` 在左边填充字符串直到长度为 `len`                                               |                                                                          |
| `RPAD()`             | `RPAD(str, len, padstr)`                                              | 用 `padstr` 在右边填充字符串直到长度为 `len`                                               |                                                                          |
| `ELT()`              | `ELT(N, str1, str2, ...)`                                              | 根据索引 `N` 返回对应的字符串                                                              |                                                                          |
| `FIELD()`            | `FIELD(str, str1, str2, ...)`                                         | 返回 `str` 在列表中的索引（第几个）                                                       |                                                                          |
| `FIND_IN_SET()`      | `FIND_IN_SET(str, strlist)`                                           | 在以逗号分隔的字符串列表中查找某个值                                                      | 返回位置索引                                                             |
| `FORMAT()`           | `FORMAT(number, decimal_places)`                                      | 按照指定小数位数格式化数字（返回字符串）                                                  |                                                                          |
| `REGEXP_LIKE()`      | `REGEXP_LIKE(str, pattern)`                                           | 判断字符串是否匹配正则表达式                                                              | MySQL 8.0+ 支持                                                          |
| `REGEXP_REPLACE()`   | `REGEXP_REPLACE(str, pattern, replacement)`                           | 替换匹配正则表达式的部分                                                                  | MySQL 8.0+ 支持                                                          |
| `REGEXP_SUBSTR()`    | `REGEXP_SUBSTR(str, pattern)`                                         | 提取匹配正则表达式的子串                                                                  | MySQL 8.0+ 支持                                                          |


### SQL数学函数

|名称|函数形式|功能说明|
|---|---|---|
|绝对值函数|ABS(x) |返回 x 的绝对值。|
|圆周率|PI() |返回圆周率 π 的值。|
|平方根|SQRT(x) |返回 x 的平方根。|
|取余数|MOD(x, y) |返回 x 除以 y 的余数。|
|向上取整|CEIL(x) 或 CEILING(x) |返回大于或等于 x 的最小整数。|
|向下取整|FLOOR(x) |返回小于或等于 x 的最大整数。|
|随机数|RAND() |返回 0 到 1 之间的随机数。|
|四舍五入|ROUND(x, y) |返回 x 保留到小数点后 y 位的值。|
|截断|TRUNCATE(x, y) |返回 x 保留到小数点后 y 位的值（不四舍五入）。|
|符号函数|SIGN(x) |返回 x 的符号，负数、0、正数分别返回 -1、0、1。|
|幂函数|POW(x, y) |或 POWER(x, y) 返回 x 的 y 次方。|
|自然对数|LOG(x) |返回 x 的自然对数。|
|以 10 为底的对数|LOG10(x) |返回 x 的以 10 为底的对数。|
|角度转换为弧度|RADIANS(x) |将角度 x 转换为弧度。|
|弧度转换为角度|DEGREES(x) |将弧度 x 转换为角度。|
|正弦函数|SIN(x) |返回 x 的正弦值，x 是弧度。|
|余弦函数|COS(x) |返回 x 的余弦值，x 是弧度。|
|正切函数|TAN(x) |返回 x 的正切值，x 是弧度。|



## （空）sklearn