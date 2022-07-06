long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""
cell=long_text.split('\n');     #对long_text进行分片存入cell
#print(cell);
name=cell[1];    #第一行是空
lei=name[2];
sum1=long_text.count('.');   #数一下“.”出现的次数，看看有几个title
head=long_text.find('.');   #找到第一个title开头的位置索引
tile=long_text.find('UND');  #找到第一个title结束的位置索引
sum2=long_text.count('LU');   #数一下“LU”出现的次数，看看有几个isin
start=long_text.find('LU');   #找到第一个“LU”开头的位置索引

title=[]
head1=head
tile1=tile
for i in range(0,sum1):
    title.append(i)
    title[i]=long_text[head1+1:tile]
    head1=long_text.find('.',head1+1)   #找到下一个title开头的位置索引
    tile1=long_text.find('UND',tile1+1)   #找到下一个title结束的位置索引

isin=[]
LU=[]
head1=head
for i in range(0,sum1):
    head=long_text.find('.',head1+1)
    tile1=long_text.find('UND',head1,head)
    sum3=long_text.count('LU',tile1,head)   #查看 第i个isin有几个元素
    start=long_text.find('LU',tile1,head)
    for j in range(0,sum3):
        LU.append(j)
        LU[j]=long_text[start:start+12]
        start=long_text.find('LU',start+1,head)
    isin.append(i)
    isin.append(LU)
    LU=[]  #初始化
    head1=head  #初始化
#print(isin)
sub_find1=[]
for i in range(0,len(isin)):
    if type(isin[i])==int:
        sub_find1.append(i)
    else:
        continue
#print(sub_find1)

sub_find=[]
sub_find2=[]
for i in range(0,sum1):
    sub_find.append(i)
    sub_find2.append(i)
    n=sub_find1[i]
    sub_find2[i]=["title: ",title[i],'\n',"isin: ",isin[n+1]]
    #print(sub_find2)
    sub_find.append({"title":title[i],"isin":isin[n+1]})

h=[]
for i in range(0,len(sub_find)):
    if type(sub_find[i])==int:
        h.append(i)
    else:
        continue
print(h)
sub_find=[sub_find[i] for i in range(len(sub_find)) if(i not in h)]
output={'name':name,
        'lei':lei,
        'sub_fund':sub_find  #到这发现前面的fund都敲成find了
        }
print(output)

