# Python练习
**坚持每天学习Python，先把[廖雪峰官网](https://www.liaoxuefeng.com/wiki/1016959663602400)的教程学习一遍**
![热爱学习每一天](http://image.so.com/view?q=%E7%A8%8B%E5%BA%8F%E5%91%98%E6%90%9E%E7%AC%91%E5%9B%BE%E7%89%87&src=srp&correct=%E7%A8%8B%E5%BA%8F%E5%91%98%E6%90%9E%E7%AC%91%E5%9B%BE%E7%89%87&ancestor=list&cmsid=be8bc7ac3ee2dd611ba5482acbf24b01&cmran=0&cmras=0&cn=0&gn=0&kn=50&fsn=130&adstar=0&clw=251#id=87b99d746dd267004f7ce385c5a47925&currsn=0&ps=99&pc=99)

1、使用PyCharm的时候会在目录自动添加.idea文件，团队开发的时候为了保持代码统一，
可是在git中提交代码的时候忽略掉这个文件。创建.gitignore文件，把需要忽略的文件
添加到里面，如果已经提交了，执行git rm --cached -r .idea/ 然后再重新提交即可。

2、由于公司git账户和本人github账号不一致，导致前几天git每天的提交记录在Contribution activity没有显示，
执行 git config -l, 查看配置文件，发现user.email使用的是公司的，git config user.email youEmailAddress@XX.com修改github使用的email, 然后再次提交，就可以看到了



    