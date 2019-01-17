# AutoGTF
功能：根据配置文件自动生成对应的文件到指定的目录

说明：
1.配置config.ini
2.运行run.exe

注意：
1.会根据sql语句查询的文件路径列表，自动在file目录下生成对应数量的文件，自动重命名复制到文件路径目录
2.若相对路径的值不是以\\开头，需要在查询语句上加上。e.g.：select top 10 '\\'+FileRelativePath from DocumentInService
3.file目录不可删除
