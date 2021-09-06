# fyy-app-autotesting
Automation Testing of Mobile App

## UI自动化
> Case 待补充

## 埋点事件验证
### 使用方法
1. cmd执行
```zsh
mitmdump -p 8889 -s fyy-app-autotesting/catchevents/check_events.py
```
```python
# check_events.py
ST.all_events = ['filto_launch', ]  #填写需要验证是否存在的全部事件
```
2. 结果
- /report/now_event.txt 为已检测到的事件

- /report/lost_event.txt 为缺少的事件
