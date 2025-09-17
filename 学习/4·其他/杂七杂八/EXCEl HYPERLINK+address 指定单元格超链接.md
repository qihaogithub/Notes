---
column1:
  - 办公
---


Excel 的链接功能通常只链接到固定的sheet页的固定单元格,有时希望点击特定人物时可以链接到对应的单元格，这时候可以采用HYPERLINK+address的方式实现。

**HYPERLINK(link\_location，friendly\_name)：** 

*   link_location 为链接位置
*   friendly_name 为显示文本

**ADDRESS(row\_num,column\_num,abs\_num,A1,sheet\_text)**

*   row_num 在单元格引用中使用的行号
*   column_num 在单元格引用中使用的列标
*   abs_num 引用类型
*   A1 用以指定 A1 或 R1C1 引用样式的逻辑值。如果 A1 为 TRUE 或省略，函数 ADDRESS 返回 A1 样式的引用；如果 A1 为 FALSE，函数 ADDRESS 返回 R1C1样式的引用。
*   sheet\_text 为一文本，指定作为外部引用的工作表的名称，如果省略 sheet\_text，则不使用任何工作表名

建一张成绩表和班级表，并希望从班级表的姓名链接到成绩表的对应位置，  
![](https://img-blog.csdnimg.cn/20210528145013787.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzUwNDM1MTIz,size_16,color_FFFFFF,t_70)
  
![](https://img-blog.csdnimg.cn/20210528145021300.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzUwNDM1MTIz,size_16,color_FFFFFF,t_70)
  
步骤：

1.  通过MATCH(B2,成绩!A:A,0),1)函数可以获得对应同学的行数;
2.  通过ADDRESS(MATCH(B2,成绩!A:A,0),1)获得对应姓名的单元格位置如： 小明对应$A$2;
3.  通过HYPERLINK("#成绩!"&ADDRESS(MATCH(B2,成绩!A:A,0),1),B2)成功链接到成绩表的单元格位置 。  
    ![](https://img-blog.csdnimg.cn/20210528145644517.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzUwNDM1MTIz,size_16,color_FFFFFF,t_70)
      
    HYPERLINK同样可以链接到其他excel文件或者其他链接上，如：  
    =HYPERLINK(“工作簿1.xlsx#成绩!”&ADDRESS(MATCH(B2,\[工作簿1.xlsx\]成绩!A:A,0),1),B2)  
    ![](https://img-blog.csdnimg.cn/20210528150029848.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzUwNDM1MTIz,size_16,color_FFFFFF,t_70)
      
    这里只需要将其他excel的名称加到sheet表名字前就可以了。
    
    [EXCEl HYPERLINK+address 指定单元格超链接_m0_50435123的博客-CSDN博客_hyperlink和address函数用法](https://blog.csdn.net/m0_50435123/article/details/117361004) 
