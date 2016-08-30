#!/usr/bin/python
# coding: UTF-8
"""
Created on 2013-1-15
@author: CaiKnife
"""

import re

text = """
和憧憬的空中小姐性交 春原未来<br/><img src="http://img60.qqqimg.com/201010/1363020130115151015.jpg" border="0"/><br/><img src="http://img60.qqqimg.com/201010/1067820130115151015.jpg" border="0"/><br/>本集电影迅雷下载地址：<br/>thunder://QUFodHRwOi8vdXMwMTYuZnJlZS1kdmQ1OC5jb20vob7Dv8jVuPzQwmZlZHZkLmNvbaG/NjU0LVVGRC0wMzAuYXZpWlo=<br/>LOVE FINAL 冈田真由香 <br/><img src="http://img60.qqqimg.com/201010/2846120130115151155.jpg" border="0"/><br/><img src="http://img60.qqqimg.com/201010/2637520130115151156.jpg" border="0"/><br/>本集电影迅雷下载地址：<br/>thunder://QUFodHRwOi8vdXMwMTYuZnJlZS1kdmQ1OC5jb20vob7Dv8jVuPzQwmZlZHZkLmNvbaG/ODc2eXRyLXRlazA0My5hdmlaWg==<br/>店长推荐(HEY-001) Sexy Flight Attendant CA 性感空姐  <br/><img src="http://img60.qqqimg.com/201010/2618720130115151314.jpg" border="0"/><br/><img src="http://img60.qqqimg.com/201010/1161620130115151314.jpg" border="0"/><br/>本集电影迅雷下载地址：<br/>thunder://QUFodHRwOi8vdXMwMTYuZnJlZS1kdmQ1OC5jb20vob7Dv8jVuPzQwmZlZHZkLmNvbaG/ODc2eWd2LV9IRVktMDAxLmF2aVpa<br/>最新avs-museum 100274 茉莉花 义母编 Part 1  <br/><img src="http://img60.ioioq.com/201010/2357520130115151439.jpg" border="0"/><br/><img src="http://img60.ioioq.com/201010/3817520130115151439.jpg" border="0"/><br/>本集电影迅雷下载地址：<br/>thunder://QUFodHRwOi8vdXMwMTYuZnJlZS1kdmQ1OC5jb20vob7Dv8jVuPzQwmZlZHZkLmNvbaG/MDk4aWp1LTEwMDI3NC1hbGwud212Wlo=<br/>最新avs-museum 100296 淫语中出SOP 彩名 Part 1  <br/><img src="http://img60.ioioq.com/201010/1101820130115151541.jpg" border="0"/><br/><img src="http://img60.ioioq.com/201010/3806720130115151541.jpg" border="0"/><br/>本集电影迅雷下载地址：<br/>thunder://QUFodHRwOi8vdXMwMTYuZnJlZS1kdmQ1OC5jb20vob7Dv8jVuPzQwmZlZHZkLmNvbaG/OTgwb2l1LTEwMDI5Ni1hbGwud212Wlo=<br/>Hustler - Teen Truth Or Dare <br/><img src="http://img60.ioioq.com/201010/1509620130115151649.jpg" border="0"/><br/><img src="http://img60.ioioq.com/201010/2376420130115151649.jpg" border="0"/><br/>本集电影迅雷下载地址：<br/>thunder://QUFodHRwOi8vdXMwMTYuZnJlZS1kdmQ1OC5jb20vob7Dv8jVuPzQwmZlZHZkLmNvbaG/ODc2dGZyLVRlZW4uVHJ1dGguT3IuRGFyZS5BLmF2aVpa<br/>thunder://QUFodHRwOi8vdXMwMTYuZnJlZS1kdmQ1OC5jb20vob7Dv8jVuPzQwmZlZHZkLmNvbaG/MDk4aWpuLVRlZW4uVHJ1dGguT3IuRGFyZS5CLmF2aVpa&#13;

"""

text2 = """
-中文字幕- 最喜欢美臀的H恶作剧<br/><img src="http://img60.qqqimg.com/201010/2080020130105160912.jpg" border="0"/><br/><img src="http://img60.qqqimg.com/201010/3623020130105160912.jpg" border="0"/><br/>本集电影迅雷下载地址：<br/>thunder://QUFodHRwOi8vdXMwMTMuZnJlZS1kdmQ1OC5jb20vob7Dv8jVuPzQwjY3OGR2ZC5jb22hv3VqdTc2dC1nZzA5NnIuYXZpWlo=<br/><br/> 人妻不伦温泉 16 北川美绪  <br/><img src="http://img60.qqqimg.com/201010/2014020130105161316.jpg" border="0"/><br/><img src="http://img60.qqqimg.com/201010/3557020130105161316.jpg" border="0"/><br/>本集电影迅雷下载地址：<br/>thunder://QUFodHRwOi8vdXMwMTMuZnJlZS1kdmQ1OC5jb20vob7Dv8jVuPzQwjY3OGR2ZC5jb22hvzlpdTd5NnQ1LWFieTAxNi5hdmlaWg==<br/><br/>最新一本道 111612_473「超级名模系列 田中志乃」  <br/><img src="http://img60.qqqimg.com/201010/3928520130105161532.jpg" border="0"/><br/><img src="http://img60.qqqimg.com/201010/3633420130105161532.jpg" border="0"/><br/><img src="http://img60.qqqimg.com/201010/2662020130105161532.jpg" border="0"/><br/><img src="http://img60.qqqimg.com/201010/1690620130105161532.jpg" border="0"/><br/><img src="http://img60.qqqimg.com/201010/2557320130105161532.jpg" border="0"/><br/><img src="http://img60.qqqimg.com/201010/1585920130105161532.jpg" border="0"/><br/><img src="http://img60.qqqimg.com/201010/3614620130105161532.jpg" border="0"/><br/>本集电影迅雷下载地址：<br/>thunder://QUFodHRwOi8vdXMwMTMuZnJlZS1kdmQ1OC5jb20vob7Dv8jVuPzQwjY3OGR2ZC5jb22hvzExMTYxMl80NzMtMXBvbi13aG9sZTFfaGQuYXZpWlo=<br/><br/>最新一本道102412_456 北川瞳「与瞳的SEX  <br/><img src="http://img60.ioioq.com/201010/1879320130105161731.jpg" border="0"/><br/><img src="http://img60.ioioq.com/201010/1584220130105161731.jpg" border="0"/><br/><img src="http://img60.ioioq.com/201010/1774720130105161731.jpg" border="0"/><br/><img src="http://img60.ioioq.com/201010/3803420130105161731.jpg" border="0"/><br/><img src="http://img60.ioioq.com/201010/1860620130105161731.jpg" border="0"/><br/>本集电影迅雷下载地址：<br/>thunder://QUFodHRwOi8vdXMwMTMuZnJlZS1kdmQ1OC5jb20vob7Dv8jVuPzQwjY3OGR2ZC5jb22hvzEwMjQxMl80NTYtMXBvbi13aG9sZTFfaGQuYXZpWlo=<br/><br/>120712_781 做爱瘦身想让自己变得更漂亮<br/><img src="http://img60.ioioq.com/201010/3030920130105161854.jpg" border="0"/><br/><img src="http://img60.ioioq.com/201010/3897720130105161854.jpg" border="0"/><br/>本集电影迅雷下载地址：<br/>thunder://QUFodHRwOi8vdXMwMTMuZnJlZS1kdmQ1OC5jb20vob7Dv8jVuPzQwjY3OGR2ZC5jb22hvzEyMDcxMl83ODEtbXVyYS13aG9sZTFfaGQud212Wlo=<br/><br/>Digital Playground - Unsexpected<br/><img src="http://img60.ioioq.com/201010/2357520130105162047.jpg" border="0"/><br/><img src="http://img60.ioioq.com/201010/3892620130105162047.jpg" border="0"/><br/>本集电影迅雷下载地址：<br/>thunder://QUFodHRwOi8vdXMwMTMuZnJlZS1kdmQ1OC5jb20vob7Dv8jVuPzQwjY3OGR2ZC5jb22hv2lrajc0LVVuU0VYcGVjdGVkLmF2aVpa&#13;
"""

pattern = re.compile(r"thunder://[\w/]+=*")
match = pattern.findall(text2)

if match:
    for m in match:
        print m
else:
    print "No match!"
