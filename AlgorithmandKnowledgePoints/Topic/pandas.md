# Pandas 时间处理函数选择题

## 单选

**1. 以下哪一个函数可以将字符串转换为 datetime 类型？**  
A. pd.to_date()  
B. pd.to_datetime()  
C. pd.date_parse()  
D. pd.datetime_convert()  

**2. 以下哪个参数可以指定 `to_datetime()` 中字符串的格式？**  
A. time_format  
B. pattern  
C. format  
D. datetime_format  

**3. 若要生成一个从 2022-01-01 开始的每小时时间序列，共 10 个，应该使用：**  
A. pd.date_range('2022-01-01', periods=10, freq='H')  
B. pd.datetime_range('2022-01-01', 10, 'H')  
C. pd.time_range(start='2022-01-01', end=10, freq='H')  
D. pd.hour_range('2022-01-01', 10)  

**4. `pd.to_timedelta("2 days 3 hours")` 的返回类型是：**  
A. DatetimeIndex  
B. Timedelta  
C. str  
D. Period  

**5. 想对时间列进行向下取整，可以使用哪个方法？**  
A. .round()  
B. .ceil()  
C. .floor()  
D. .clip()  

**6. 下面哪个表达式可以获取时间是月初的布尔值？**  
A. df['time'].is_month_begin  
B. df['time'].dt.is_month_start  
C. df['time'].dt.is_start_of_month  
D. df['time'].is_month_start  

**7. 获取一个 Timestamp 对象的“星期几”应使用：**  
A. .weekday  
B. .week  
C. .dayofweek  
D. A 或 C  

**8. 下列哪个函数可用于按天统计时间序列？**  
A. .groupby('day')  
B. .resample('D')  
C. .daily()  
D. .aggregate_by('D')  

**9. 将时间设置为当天的 00:00:00 应使用：**  
A. .normalize()  
B. .truncate()  
C. .zero_time()  
D. .set_hour(0)  

**10. `pd.date_range(start='2023-01-01', periods=3, freq='D')` 的返回类型是？**  
A. DatetimeIndex  
B. PeriodIndex  
C. list[str]  
D. Series  

**11. 使用 `.shift(periods=1, freq='D')` 可以实现什么功能？**  
A. 时间列加一天  
B. 时间列减一天  
C. 时间列按原顺序排序  
D. A 和 B 取决于 periods 正负  

**12. `df['time'].dt.strftime('%Y-%m-%d')` 返回的数据类型是：**  
A. datetime64  
B. Timestamp  
C. str  
D. Series[str]  

**13. 想将某列从 datetime 转为毫秒级差值，应该使用哪个函数？**  
A. .astype(int)  
B. .view('int64')  
C. pd.to_timedelta(...).total_seconds() \* 1000  
D. .timestamp()  

**14. 获取一个时间差对象的总秒数应使用：**  
A. .seconds  
B. .total_seconds()  
C. .seconds_total  
D. .time_seconds()  

**15. 以下哪个频率代码表示“每月最后一天”？**  
A. 'ME'  
B. 'M'  
C. 'BM'  
D. 'MEnd'  

**16. 若要对时间序列重新采样为每小时，应使用哪个频率？**  
A. 'H'  
B. 'h'  
C. '1hr'  
D. 'hour'  

**17. 使用 `pd.Timestamp('2023-06-01') + pd.DateOffset(months=1)` 的结果是？**  
A. 2023-06-30  
B. 2023-07-01  
C. 2023-06-02  
D. 报错  

**18. 如何用 Pandas 筛选每天 8:00 到 10:00 的数据？**  
A. df.between_time('8:00', '10:00')  
B. df.loc['08:00':'10:00']  
C. df['time'].between('8:00', '10:00')  
D. df.query('8 <= time <= 10')  

**19. 若希望创建一个每两小时的 timedelta 序列，应使用：**  
A. pd.timedelta_range(start='0s', periods=5, freq='2H')  
B. pd.to_timedelta(np.arange(0, 10, 2))  
C. pd.timedelta_range('2H', 5)  
D. pd.timedelta_seq(0, 10, 2, unit='H')  

**20. `df['time'].dt.round('5min')` 的含义是？**  
A. 向上取整到 5 分钟  
B. 向下取整到 5 分钟  
C. 四舍五入到 5 分钟  
D. 舍去分钟信息  

1.以下哪一个函数可以将字符串转换为 datetime 类型？
A、pd.to_date()
B、pd.to_datetime()
C、pd.date_parse()
D、pd.datetime_convert()
答案:B
解析:pd.to_datetime() 是 Pandas 中将对象转换为 datetime 类型的标准方法。

2.pd.to_timedelta("2 days 3 hours") 的返回类型是：
A、DatetimeIndex
B、Timedelta
C、str
D、Period
答案:B
解析:返回的是时间差对象 Timedelta。

3.df['time'].dt.strftime('%Y-%m-%d') 的结果类型是：
A、datetime64
B、Series[str]
C、int64
D、Timestamp
答案:B
解析:strftime 返回的是字符串序列。

4.设置时间为当天 00:00:00 应使用哪个方法？
A、.normalize()
B、.truncate()
C、.floor()
D、.reset_time()
答案:A
解析:.normalize() 将时间归一化到日期部分。

5.获取“是否月末”的布尔值应使用：
A、df.time.is_month_end
B、df.time.dt.is_month_end
C、df.time.dt.end_of_month
D、df.time.is_end
答案:B
解析:必须通过 .dt 才能访问时间属性。

6.pd.date_range('2024-01-01', periods=3, freq='D') 返回：
A、DatetimeIndex
B、list
C、Series
D、Timestamp
答案:A
解析:date_range 返回 DatetimeIndex 类型。

7.获取某时间是星期几用哪个属性？
A、.day
B、.week
C、.weekday
D、.hour
答案:C
解析:.weekday 或 .dayofweek 可表示星期几。

8.下列哪个频率代码表示“每小时”？
A、'M'
B、'H'
C、'T'
D、'D'
答案:B
解析:H 表示 hourly。

9..shift(periods=1, freq='D') 表示：
A、值不动，时间前移一天
B、时间不动，值前移一天
C、值和时间都前移一天
D、向前取样
答案:A
解析:带 freq 的 shift 作用于时间轴。

10.将时间四舍五入到 15 分钟应使用：
A、round(15)
B、.dt.round('15min')
C、.floor(15min)
D、.adjust('15')
答案:B
解析:.dt.round('15min') 表示按 15 分钟单位四舍五入。

## 多选

1.以下哪些可以提取时间字段？
A、.dt.year
B、.dt.month
C、.dt.weekday
D、.dt.string
答案:ABC
解析:前三个都是合法时间字段。

2.以下属于创建时间范围的函数有：
A、pd.date_range
B、pd.period_range
C、pd.timedelta_range
D、pd.time_range
答案:ABC
解析:A/B/C 是合法函数，D 不存在。

3.以下哪些是合法的时间频率单位？
A、'H'
B、'T'
C、'W'
D、'MS'
答案:ABCD
解析:H:小时；T:分钟；W:周；MS:月初。

4.以下哪些函数可以用于重采样？
A、.resample
B、.asfreq
C、.groupby
D、.merge
答案:ABC
解析:前三者都可以实现频率变换。

5.以下哪些可以创建时间差对象？
A、pd.Timedelta
B、pd.to_timedelta
C、pd.timedelta_range
D、pd.date_diff
答案:ABC
解析:pd.date_diff 并不存在。

6.以下哪些方法可用于向下取整时间？
A、.floor
B、.ceil
C、.round
D、.truncate
答案:ACD
解析:floor 向下，truncate 截断，round 四舍五入。

7.以下哪些表示季度频率？
A、'Q'
B、'Q-DEC'
C、'QS'
D、'QTR'
答案:ABC
解析:Q, Q-DEC, QS 均合法；QTR 不是标准频率。

8.使用 .between_time() 需要什么前提？
A、索引为 DatetimeIndex
B、时间字段为字符串
C、DataFrame 按时间排序
D、必须在索引中筛选
答案:AD
解析:该函数仅对 DatetimeIndex 使用。

9.以下哪些操作结果是 DatetimeIndex 类型？
A、pd.date_range
B、DatetimeIndex([...])
C、df.index
D、pd.to_datetime(list)
答案:ABCD
解析:都可以得到 DatetimeIndex。

10.以下哪些单位可用于 pd.to_timedelta()？
A、's'
B、'ms'
C、'min'
D、'day'
答案:ABCD
解析:这些单位都是合法的。

## 判断

1.pd.to_datetime() 可以将字符串、数值或 Series 转为时间类型。
答案:对
解析:它是 Pandas 中最常用的时间转换函数。

2..dt.year 可直接应用于字符串列。
答案:错
解析:必须是 datetime 类型列才能使用 .dt。

3.pd.date_range() 不能用于创建时间索引。
答案:错
解析:date_range 默认返回 DatetimeIndex。

4..resample() 方法仅适用于 Series。
答案:错
解析:DataFrame 和 Series 都可使用。

5.pd.Timedelta('2 days') 和 pd.to_timedelta('2 days') 作用相同。
答案:对
解析:两者都可生成时间差对象。

6.df['time'].dt.round('H') 可将时间按小时四舍五入。
答案:对
解析:round 可用于多种时间粒度。

7..dayofweek 的返回值是字符串格式。
答案:错
解析:返回整数（0~6）。

8.pd.PeriodIndex 表示一段时间区间。
答案:对
解析:Period 表示的是一个周期。

9..shift(freq='M') 将数据移动一个月的值。
答案:错
解析:它移动的是时间标签，不是值。

10.pd.date_range() 的结果不能作为 DataFrame 的索引。
答案:错
解析:它可以直接作为时间索引使用。

## 填空

1.pd.to_datetime() 函数可以将 ______ 和 ______ 转换为 Pandas 的 datetime 类型。
答案:字符串 数值
解析:主要支持字符串与整数格式的转换。

2..dt 访问器常用于 Series 中包含 ______ 类型的数据。
答案:datetime64
解析:只有 datetime 类型数据支持 .dt。

3.pd.date_range(start, periods, freq) 中 freq='D' 表示按 ______ 为间隔。
答案:天
解析:'D' 表示 day。

4.pd.Timedelta('1 hour 30 minutes') 的单位是 ______ 类型。
答案:Timedelta
解析:该类表示时间差。

5.若要提取时间列中的“月”，应使用 df['time'].dt.______。
答案:month
解析:month 是合法时间属性。

6.pd.timedelta_range(start='0s', periods=5, freq='2H') 表示每 ______ 小时一个间隔。
答案:2
解析:freq='2H' 表示每两个小时一个单位。

7.df['time'].dt.floor('T') 中 'T' 表示按 ______ 取整。
答案:分钟
解析:'T' 是 minute 的缩写。

8..between_time('09:00', '12:00') 用于筛选时间在 ______ 和 ______ 之间的数据。
答案:09:00 12:00
解析:按时间筛选必须是时间索引。

9..round('H') 是将时间数据按 ______ 粒度四舍五入。
答案:小时
解析:四舍五入到最近小时。

10.pd.Timestamp('2024-01-01') + pd.DateOffset(months=1) 的结果是 ______。
答案:2024-02-01
解析:时间偏移加一个月。

## 论述

1.[论述题]简述 Pandas 中 .resample() 方法的作用。
答案:用于对时间序列数据进行重采样，实现按指定频率聚合或填充等操作。
解析:无

2.[论述题]什么是 DatetimeIndex，它有何作用？
答案:DatetimeIndex 是表示时间序列索引的类型，用于时间对齐、切片、重采样等操作。
解析:无

3.[论述题]如何使用 pd.to_timedelta()？
答案:传入字符串、数值或序列即可转换为时间差对象，常用于时长计算。
解析:无

4.[论述题]Pandas 中如何创建从某日起每小时一次的时间序列？
答案:使用 pd.date_range(start=..., periods=..., freq='H') 即可。
解析:无

5.[论述题]如何从时间列中提取“年、月、日”？
答案:可使用 .dt.year、.dt.month、.dt.day 分别提取时间字段。
解析:无

6.[论述题]解释 .shift() 和 .tshift() 的区别。
答案:.shift() 移动数据；.tshift() 移动索引（已弃用）。
解析:无

7.[论述题]如何对时间序列向下取整、向上取整和四舍五入？
答案:使用 .floor()、.ceil()、.round() 方法，配合指定频率使用。
解析:无

8.[论述题]时间类型数据为何需转换为 datetime 格式？
答案:便于使用 Pandas 的时间处理功能，如切片、排序、重采样等。
解析:无

9.[论述题]时间序列索引的优点有哪些？
答案:支持高效筛选、对齐、分组、重采样等操作。
解析:无

10.[论述题]简述 pd.Timedelta 和 pd.DateOffset 的区别。
答案:Timedelta 表示精确的时间差（秒、分）；DateOffset 表示日历偏移量（如月底、季度）。
解析:无

## 简单时间函数

✅ 单选题
1.以下哪个属性可用于提取“年内的第几天”？
A、.dayofweek
B、.dayofyear
C、.is_month_start
D、.day
答案:B
解析:.dayofyear 表示一年中的第几天，返回整数。

2.若要将时间设置为当天 00:00:00，应该使用以下哪个方法？
A、.floor()
B、.round()
C、.normalize()
D、.ceil()
答案:C
解析:.normalize() 可将时间归一化为 00:00:00。

3.以下哪个方法可将时间向下取整？
A、.ceil()
B、.floor()
C、.normalize()
D、.round()
答案:B
解析:.floor() 表示向下取整到最近的时间粒度。

4.若要将 2024-07-15 11:23 向上取整为小时，应使用：
A、.round('H')
B、.floor('H')
C、.ceil('H')
D、.normalize()
答案:C
解析:.ceil() 会向上取整到指定频率。

5.以下哪个属性或方法返回值类型为 bool？
A、.month
B、.dayofweek
C、.is_month_end
D、.hour
答案:C
解析:.is_month_end 返回布尔类型，表示是否为月末。

✅ 多选题
1.以下哪些属性返回的结果是整数？
A、.year
B、.hour
C、.dayofweek
D、.is_month_start
答案:ABC
解析:前三者都返回 int；.is_month_start 返回 bool。

2.以下哪些方法可以接受 freq 参数？
A、.round()
B、.floor()
C、.ceil()
D、.normalize()
答案:ABC
解析:.normalize() 无 freq；其余三者支持时间单位频率参数。

3.以下哪些属性适用于 datetime64[ns] 类型的 Series？
A、.dt.day
B、.dt.is_month_end
C、.dt.floor('D')
D、.dt.normalize()
答案:AB
解析:.floor() 和 .normalize() 是方法，不是属性，不能加 .dt. 直接调用。

4.以下哪些方法的返回类型是 DatetimeIndex？
A、.normalize()
B、.floor('D')
C、.ceil('D')
D、.round('D')
答案:ABCD
解析:这些方法都返回 DatetimeIndex，用于批量处理时间数据。

5.以下哪些表示可用于提取“星期几”？
A、.dayofweek
B、.weekday
C、.dayofyear
D、.is_month_start
答案:AB
解析:.dayofweek 和 .weekday 都可提取星期几，返回 0（周一）~6（周日）。

✅ 判断题
1..is_month_end 返回值为布尔类型。
答案:对
解析:它用于判断当前时间是否为月末。

2..normalize() 会将所有时间归一化为 23:59:59。
答案:错
解析:normalize() 设置为当天的 00:00:00。

3..floor() 方法用于向上取整时间。
答案:错
解析:.floor() 是向下取整，.ceil() 才是向上。

4..round('H') 可以将时间四舍五入到小时。
答案:对
解析:round 方法用于按照给定粒度进行四舍五入。

5..month 和 .hour 方法的返回类型都是 int。
答案:对
解析:两者都表示数值型时间字段。

✅ 填空题
1..dayofweek 和 .weekday 返回值范围是 ______ 到 ______，其中 0 表示周一。
答案:0 6
解析:这两个属性返回星期几（0=周一，6=周日）。

2..dayofyear 表示一年中的第 ______ 天。
答案:int
解析:返回一个整数，表示从 1 月 1 日起到今天的天数。

3.若时间为 "2024-07-15 09:33:48"，使用 .normalize() 后时间变为 ______。
答案:2024-07-15 00:00:00
解析:normalize 会保留日期，时间归零。

4.要将时间取整到最近 10 分钟，应该使用方法是 ______，参数为 ______。
答案:.round '10min'
解析:round 是取整方法，'10min' 为频率单位。

5..is_month_start 属性的返回值类型是 ______，表示当前日期是否为每月的第 ______ 天。
答案:bool 1
解析:只有月初时该属性为 True。

✅ 论述题
1.[论述题]简述 .normalize() 方法的作用。
答案:将时间设置为当天 00:00:00，保留日期部分，清除小时分钟秒信息。
解析:用于清洗时间数据，只保留日期。

2.[论述题].floor(), .ceil(), .round() 三者的区别是什么？
答案:.floor() 向下取整，.ceil() 向上取整，.round() 四舍五入。都需指定频率。
解析:常用于对齐时间序列。

3.[论述题]说明 .is_month_start 和 .is_month_end 的作用。
答案:用于判断某个日期是否为当月第一天或最后一天，返回布尔值。
解析:适合用于边界日期判断。

4.[论述题]哪些常用的时间字段可以直接从 datetime 类型中提取？
答案:包括 year、month、day、hour、minute、second 等。
解析:便于拆分时间特征用于建模。

5.[论述题]如果需要按“天”重采样数据，为什么使用 .floor('D') 比 .normalize() 更通用？
答案:.floor('D') 支持更多频率粒度选择，而 normalize 只能归一化为 00:00。
解析:.floor 适用于多种时间单位。


# 数据预处理

1.以下哪个函数可用于填补缺失值？
A、fillna()
B、dropna()
C、isna()
D、notna()
答案:A
解析:fillna() 用于将缺失值填补为指定值。

2.以下哪个函数可用于删除存在缺失值的行？
A、drop()
B、dropna()
C、remove_na()
D、cleanna()
答案:B
解析:dropna() 用于丢弃包含 NaN 的行或列。

3.以下哪个方法可以替换 DataFrame 中的指定值？
A、map()
B、replace()
C、fillna()
D、drop()
答案:B
解析:replace() 可指定将某些值替换为其他值。

4.对某列数据进行标准化，常用哪个函数组合？
A、apply() + mean()
B、(x - x.mean()) / x.std()
C、normalize()
D、rescale()
答案:B
解析:标准化公式为 z = (x - μ) / σ。

5.若要对分类变量编码成数字，应该使用：
A、astype(int)
B、pd.get_dummies()
C、label_replace()
D、drop_duplicates()
答案:B
解析:get_dummies() 可将分类变量转换为 one-hot 编码。

1.以下哪些函数可用于检测缺失值？
A、isna()
B、isnull()
C、notna()
D、dropna()
答案:ABC
解析:isna()/isnull() 检测缺失，notna() 检测非缺失。

2.以下哪些函数可用于对重复值进行处理？
A、duplicated()
B、drop_duplicates()
C、unique()
D、dropna()
答案:AB
解析:duplicated 检测重复，drop_duplicates 删除重复。

3.以下哪些函数或方法支持自定义函数处理数据？
A、apply()
B、map()
C、groupby().agg()
D、drop()
答案:ABC
解析:前三者都可接受函数作为参数处理数据。

4.以下哪些方法可用于替换值？
A、replace()
B、fillna()
C、mask()
D、merge()
答案:ABC
解析:replace 替换指定值，fillna 用于 NaN 替换，mask 根据条件替换。

5.以下哪些操作会改变 DataFrame 的结构？
A、drop()
B、pivot()
C、melt()
D、fillna()
答案:ABC
解析:drop 删除列/行，pivot 重塑表结构，melt 拉平成长格式。

1.fillna() 函数可用于填充缺失值。
答案:对
解析:该函数可使用固定值、前向或后向填充等方式处理 NaN。

2.drop_duplicates() 可用于去除重复行。
答案:对
解析:默认会保留首次出现的记录。

3.isna() 函数会直接修改原数据。
答案:错
解析:isna() 返回布尔结果，不修改原数据。

4.replace() 只能用于替换字符串类型的值。
答案:错
解析:replace 支持多种类型的替换操作。

5.get_dummies() 可以用于将数值列变成分类变量。
答案:错
解析:get_dummies() 用于将分类变量转为 one-hot，不能直接作用于连续数值。

1.用来检查缺失值的函数包括 ______ 和 ______。
答案:isna isnull
解析:isna/isnull 作用完全一致。

2.删除重复行的函数是 ______。
答案:drop_duplicates
解析:默认保留第一次出现的重复行。

3.若要对每一列都减去均值，应使用函数 ______ 配合 ______。
答案:apply lambda
解析:apply 可按列执行匿名函数。

4.对列“col1”中的值为 0 的项替换为 NaN，应使用 df['col1'].______。
答案:replace(0, np.nan)
解析:replace 支持单值替换。

5.使用 get_dummies() 函数可将类别变量转换为 ______ 形式。
答案:one-hot
解析:每个类别变成一个独立列。

1.[论述题]如何使用 Pandas 检查并删除缺失数据？
答案:使用 isna()/isnull() 检查缺失项，使用 dropna() 删除包含缺失的行或列。
解析:无

2.[论述题]简述 apply() 函数的常见用途。
答案:apply() 可对 Series 或 DataFrame 的每行/列应用自定义函数，常用于标准化、分组处理等。
解析:无

3.[论述题]简述 get_dummies() 的作用和使用场景。
答案:将分类变量编码为 one-hot 形式，常用于机器学习前的数据预处理。
解析:无

4.[论述题]如何使用 replace() 批量替换 DataFrame 中的值？
答案:传入字典或列表，指定旧值和新值，即可对多个值进行替换操作。
解析:无

5.[论述题]简述 drop_duplicates() 函数的参数和作用。
答案:用于删除重复行，subset 指定检测列，keep 控制保留哪一个重复值。
解析:无