# -*- coding: utf-8 -*-
import os
import sys
class EasyWay:
    def Judge_Type(self,inputType):
        if isinstance(inputType,float):
            return 'float'
        elif isinstance(inputType,int):
            return 'int'
        else:
            return 'str'

    def Change_Type(self,changeType,inputType):
        try:
             if changeType=='int':
                 output=int(inputType)
                 return output
                
             elif changeType=='float':
                 output=float(inputType)
                 return output
                
             elif changeType=='string':
                 output=str(inputType)
                 return output
             else:
                 print 'tpye is error'
                 
        except Exception,e:
            print str(e)
            
    def Change_Type_No(self,changeType,inputType):
        try:
             if changeType=='int':
                 output=int(inputType)
                 inputType=output
                
             elif changeType=='float':
                 output=float(inputType)
                 inputType=output
                
             elif changeType=='string':
                 output=str(inputType)
                 inputType=output
             else:
                 print 'tpye is error'
                 
        except Exception,e:
            print str(e)


    def Open_Bit_File(self,filename):
        try:
            f=open(filename, 'rb')
            return f
                 
        except Exception,e:
            print str(e)

    def Open_Bit_File_Data(self,filename):
        try:
            fdata=open(filename, 'rb').read()
            return fdata
                 
        except Exception,e:
            print str(e)

    def Get_File_Size(self,filename):
        size=os.path.getsize(filename)
        return size

    def In_String(self,str1,str2):
        if str1 in str2:
            return "true"
        else:
            return "false"


    

