# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
reload(sys)
sys.setdefaultencoding('utf8')

class ReadData:
    
    def _open_excel(self,filename):
        try:
            data = xlrd.open_workbook(filename)
            return data
        except Exception,e:
            print str(e)
    #根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引

    def Read_By_SheetId(self,filename,index=0,row=0,col=0):
        """
        通过sheet的id读取每个单元格的内容
        
        filename:execl表格文件名
        
        index：sheet的id
        
        row：行号（第一行为0）
        
        col：列号（第一列为0）
"""
        try:
            i=int(index)
            c=int(col)
            r=int(row)
            data=self._open_excel(filename)
            table = data.sheet_by_index(i)
            cell=table.cell(r,c).value
            return cell
        except Exception,e:
            print str(e)

    def Read_By_SheetName(self,filename,sname='Sheet1',row=0,col=0):
        """
        通过sheet的名称读取每个单元格的内容
        
        filename:execl表格文件名
        
        sname：sheet的名称
        
        row：行号（第一行为0）
        
        col：列号（第一列为0）
"""
        try:
            c=int(col)
            r=int(row)
            data=self._open_excel(filename)
            table = data.sheet_by_name(sname)
            cell=table.cell(r,c).value
            return cell
        except Exception,e:
            print str(e)

    def Excel_Table_Byrow(self,filename,by_index=0,rowindex=0):
        """
        通过行号获取一行数据
        
        filename:execl表格文件名
        
        by_index：sheet的id
        
        rowindex：行号（第一行为0）
"""
        try:
            r=int(rowindex)
            i=int(by_index)
            data = self._open_excel(filename)
            table = data.sheets()[i]
            nrows = table.nrows #行数
            ncols = table.ncols #列数
            rowdata =  table.row_values(r) #某一行数据
            return rowdata
        except Exception,e:
            print str(e)

    def Excel_Table_Bycol(self,filename,by_index=0,colindex=0):
        """
        通过列号获取一行数据
        
        filename:execl表格文件名
        
        by_index：sheet的id
        
        colindex：列号（第一列为0）
"""
        try:
            c=int(colindex)
            i=int(by_index)
            data = self._open_excel(filename)
            table = data.sheets()[i]
            nrows = table.nrows #行数
            ncols = table.ncols #列数
            coldata =  table.col_values(c) #某一列数据
            return coldata
        except Exception,e:
            print str(e)

    def Get_Col_length(self,filename,by_index=0):
        """
        获取总列数，返回整数
"""
        i=int(by_index)
        data = self._open_excel(filename)
        table = data.sheets()[i]
        nrows = table.nrows #行数
        rows=int(nrows)
        return rows
    
    def Get_Row_length(self,filename,by_index=0):
        """
        获取总行数，返回整数
"""
        i=int(by_index)
        data = self._open_excel(filename)
        table = data.sheets()[i]
        ncols = table.ncols #列数
        cols=int(ncols)
        return cols
    
    def Get_Col_Value(self,filename,by_index=0,colindex=0,startrow=0,number=0):
        """
        从某一行开始，获取某一列中的指定个数数据，返回数组列表
        
        filename:execl表格文件名
        
        by_index:sheet的id
        
        colindex:列号（第一列为0）
        
        startrow:开始的行号
        
        number:获取的数据的个数"""
        i=int(by_index)
        col=int(colindex)
        start=int(startrow)
        num=int(number)
        data = self._open_excel(filename)
        table = data.sheets()[i]
        nrows = table.nrows #行数
        ncols = table.ncols #列数
        celllist=[]
        time=nrows-start
        if num>time:
            num=int(time)
        for j in range(num):
            celllist.append(table.cell(start,col).value)
            start+=1
        return celllist    
              
    def Get_Row_Value(self,filename,by_index=0,rowindex=1,startcol=0,number=0):
        """
        从某一列开始，获取某一行中的指定个数数据，返回数组列表
        
        filename:execl表格文件名
        
        by_index:sheet的id
        
        rowindex:列号（第一行为0）
        
        startcol:开始的列号
        
        number:获取的数据的个数"""
        i=int(by_index)
        row=int(rowindex)
        start=int(startcol)
        num=int(number)
        data = self._open_excel(filename)
        table = data.sheets()[i]
        nrows = table.nrows #行数
        ncols = table.ncols #列数
        celllist=[]
        time=ncols-start
        if num>time:
            num=int(time)
        for j in range(num):
            celllist.append(table.cell(row,start).value)
            start+=1
        return celllist
        
            
    
