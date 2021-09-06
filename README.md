# fyy-app-autotesting
Automation Testing of Mobile App

## UI自动化
> Case 待补充

## 埋点事件验证
### 使用方法
1.  连接代理

- 手机代理网络到：ip:你的电脑ip, 端口:8889
- 下载证书：在手机浏览器中打开网址 mitm.it，选择对应的证书下载安装

2.  cmd执行
  ```zsh
  mitmdump -p 8889 -s fyy-app-autotesting/catchevents/check_events.py
  ```
  ```python
  # check_events.py
  ST.all_events = ['filto_launch', ]  #填写需要验证是否存在的全部事件
  ```
3.  操作业务，触发事件，shell中打印关键日志

  ![avatar]()

5.  结果
- /report/now_event.txt 为已检测到的事件

- /report/lost_event.txt 为缺少的事件
