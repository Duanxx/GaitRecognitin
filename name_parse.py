# -*- coding=utf-8 -*-
"""
@file ： name_parse.py
@author : duanxxnj@163.com
@time : 12/4/16 7:34 AM
"""

"""
    split avi file name to string list
    input: '001-bg-01-018.avi'
    output: ['001','bg','01','018','avi']
"""
def fileName_to_stringList(InputFileName):
    strList = InputFileName.split('-')
    strList.extend(strList[-1].split('.'))
    del strList[-3]
    return strList

"""
    assem string list into a image file name
    default image file format is *.jpg
    input: string list, image counter
    output: image file name
    Examples:
        input: ['001','bg','01','018'], 13
        output: '001-bg-01-018-013.jpg'
"""
def stringList_to_fileName():
    pass



if __name__ == '__main__':
    strList = fileName_to_stringList('001-bg-01-018.avi')
    print strList