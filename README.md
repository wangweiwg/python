# Python练习
**坚持每天学习Python，先把[廖雪峰官网](https://www.liaoxuefeng.com/wiki/1016959663602400 "廖雪峰官网")的教程学习一遍**
![热爱学习每一天](https://img.tuguaishou.com/ips_templ_preview/18/c1/00/lg_1925210_1556529276_5cc6c07c08037.jpg!w1024_w?auth_key=2196469202-0-0-42c24eaea075eca15fc60e9aea9af21c "我要敲代码")
<img src="https://img.tuguaishou.com/ips_templ_preview/18/c1/00/lg_1925210_1556529276_5cc6c07c08037.jpg!w1024_w?auth_key=2196469202-0-0-42c24eaea075eca15fc60e9aea9af21c" alt="我要敲代码" width="30%">

1、使用PyCharm的时候会在目录自动添加.idea文件，团队开发的时候为了保持代码统一，
可是在git中提交代码的时候忽略掉这个文件。创建.gitignore文件，把需要忽略的文件
添加到里面，如果已经提交了，执行git rm --cached -r .idea/ 然后再重新提交即可。

2、由于公司git账户和本人github账号不一致，导致前几天git每天的提交记录在Contribution activity没有显示，
执行 git config -l, 查看配置文件，发现user.email使用的是公司的，git config user.email youEmailAddress@XX.com修改github使用的email, 然后再次提交，就可以看到了



    