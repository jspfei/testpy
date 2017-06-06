#!/usr/bin/python
# -*- coding: utf-8 -*-

def showStringChar():
    var1 = 'hello world!'
    var2 = 'python runoob'

    print "var1[0]" ,var1[0]
    print "var2[1:5]",var2[1:5]

def changeString():
    var1 = 'test jspfei'

    print "更新",var1[0:4]+" jsss"

def shtringOperator():
    a = "海贼王"
    b = "D"

    print a+b
    print a * 2
    print a[1]
    print a[1:2]
    print "海" in a
    print "非" not in a
    print r'\n'

def stringFormatPrint():
    print "海贼王是%s的作品并且畅销了%d年。" % ("优秀",10)

def stringTripleQuotes():
    errHTML = '''
    <HTML><HEAD><TITLE>
    Friends CGI Demo</TITLE></HEAD>
    <BODY><H3>ERROR</H3>
    <B>%s</B><P>
    <FORM><INPUT TYPE=button VALUE=Back
    ONCLICK="window.history.back()"></FORM>
    </BODY></HTML>
    '''
    print errHTML

def stringFunction():
    test = "agaongfu"

    print test.capitalize()
    print test.center(10)
    print  test.count('g',0,len(test))
    print test.decode()
    print  test.endswith('fu',0,len(test))
    print  test.find('gf',0,len(test))
    print test.find('jj',0,len(test))
    print test.format()
  #  print test.index('f',0,len(test))
    print test.join("ssssssfu sfafusss")#以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
    print test.partition('g')#有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.
    print test.replace('g','k',1) #把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
    print test.split("o")
    print test.strip('o')
