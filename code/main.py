import os
import time
import math
import subprocess
import matplotlib.pyplot as plt
from tkinter import*
from tkinter import simpledialog

number_of_hops=0
os.system("pwd > path1.txt")
f = open("path1.txt", "r")
path1=str(f.read())[:-1]
path=path1+"/new"
def log1(num):
    x=1
    y=0
    while x<num:
        x=x*2
        y=y+1
    return y

# Various MPI Algorithms
def allgather_ring(s,i,g,top):
    fol_name=0
    while True:
        global path
        if not os.path.exists(path+str(fol_name)):
            os.mkdir(path+str(fol_name),0o755)
            break
        fol_name=fol_name+1
    os.system("chmod +x "+path+str(fol_name))
    count=0
    for i in range(1,s-1):
        for k in range(1,s):
            a = ((i + k - 1)%s)
            if(a==0):
                a+=s
            b = ((i + k)%s)
            if(b==0):
                b+=s
            if(top=="Torus"):
                graph_torus(s,a,b,str(count)+" "+str(a)+":"+str(b),path+str(fol_name))
            if(top=="Fat-Tree"):
                graph(s,a,b,str(count)+" "+str(a)+":"+str(b),path+str(fol_name))
            if(top=="DragonFly"):
                dragonfly_graph(s,g,a-1,b-1,str(count)+" "+str(a)+":"+str(b),path+str(fol_name))
            count=count+1
    i = "*.png"
    o = "output.gif"
    subprocess.call("convert -delay 100 -loop 5 " + i + " " + o, shell=True)
    os.system("start output.gif")
    os.system("gthumb "+path+str(fol_name))

def recursive_doubling(s,i,g,top):
    i=i-1
    fol_name=0
    while True:
        global path
        if not os.path.exists(path+str(fol_name)):
            os.mkdir(path+str(fol_name),0o755)
            break
        fol_name=fol_name+1
    os.system("chmod +x "+path+str(fol_name))
    d=log1(int(s))
    node=[]
    node.append(i)
    count=0
    for k in range(0,d):
        count=0
        length=len(node)
        for x in range(0,length):
            if int(node[x])^int(2**(d-(k+1)))<int(s):
                node.append(int(node[x])^int(2**(d-(k+1))))
                val=str((int(node[x])^int(2**(d-(k+1))))+1)
                if(top=="DragonFly"):
                    dragonfly_graph(s,g,node[x],(int(node[x])^int(2**(d-(k+1)))),str(count)+" "+str(node[x]+1)+":"+str((int(node[x])^int(2**(d-(k+1))))+1),path+str(fol_name))
                if(top=="Fat-Tree"):
                    graph(s,node[x]+1,(int(node[x])^int(2**(d-(k+1))))+1,str(k)+" "+str(count)+"("+str(node[x]+1)+" to "+val+")",path+str(fol_name))
                count=count+1
    i = "*.png"
    o = "output.gif"
    subprocess.call("convert -delay 100 -loop 5 " + i + " " + o, shell=True)
    os.system("start output.gif")
    os.system("gthumb "+path+str(fol_name))

def naive(s,i,g,top):
    fol_name=0
    count=0
    while True:
        global path
        if not os.path.exists(path+str(fol_name)):
            os.mkdir(path+str(fol_name),0o755)
            break
        fol_name=fol_name+1
    os.system("chmod +x "+path+str(fol_name))
    for j in range(1,int(s)+1):
        if int(i)!=int(j):
            if(top=="Torus"):
                graph_torus(s,i,j,str(count)+" "+str(i)+":"+str(j),path+str(fol_name))
            if(top=="Fat-Tree"):
                graph(s,i,j,str(count)+" "+str(i)+":"+str(j),path+str(fol_name))
            if(top=="DragonFly"):
                dragonfly_graph(s,g,i-1,j-1,str(count)+" "+str(i)+":"+str(j),path+str(fol_name))
        count=count+1 
    time.sleep(2)
    i = "*.png"
    o = "output.gif"
    subprocess.call("convert -delay 100 -loop 5 " + i + " " + o, shell=True)
    os.system("start output.gif")
    os.system("gthumb "+path+str(fol_name))

def send(s,i,x,g,top):
    fol_name=0
    while True:
        global path
        if not os.path.exists(path+str(fol_name)):
            os.mkdir(path+str(fol_name),0o755)
            break
        fol_name=fol_name+1
    os.system("chmod +x "+path+str(fol_name))
    if(top=="Torus"):
        graph_torus(s,i,x,str(i)+":"+str(x),path+str(fol_name))
    if(top=="Fat-Tree"):
        graph(s,i,x,str(i)+":"+str(x),path+str(fol_name))
    if(top=="DragonFly"):
        dragonfly_graph(s,g,i-1,x-1,str(i)+":"+str(x),path+str(fol_name))
    os.system("gthumb "+path+str(fol_name))

def torus_recursive_doubling(s,i):
    i=i-1
    fol_name=0
    while True:
        global path
        if not os.path.exists(path+str(fol_name)):
            os.mkdir(path+str(fol_name),0o755)
            break
        fol_name=fol_name+1
    os.system("chmod +x "+path+str(fol_name))
    d=log1(int(s))
    node=[]
    node.append(i)
    count=0
    for k in range(0,d):
        count=0
        length=len(node)
        for x in range(0,length):
            if int(node[x])^int(2**(d-(k+1)))<int(s):
                node.append(int(node[x])^int(2**(d-(k+1))))
                val=str((int(node[x])^int(2**(d-(k+1))))+1)
                graph_torus(s,node[x]+1,(int(node[x])^int(2**(d-(k+1))))+1,str(k)+" "+str(count)+"("+str(node[x]+1)+" to "+val+")",path+str(fol_name))
                count=count+1
    i = "*.png"
    o = "output.gif"
    subprocess.call("convert -delay 100 -loop 5 " + i + " " + o, shell=True)
    os.system("start output.gif")
    os.system("gthumb "+path+str(fol_name))	

def allgather_rec(s,i,g,top):
    fol_name=0
    while True:
        global path
        if not os.path.exists(path+str(fol_name)):
            os.mkdir(path+str(fol_name),0o755)
            break
        fol_name=fol_name+1
    os.system("chmod +x "+path+str(fol_name))
    count=0
    arr = []
    for i in range(0,s+1):
        arr.append(0)
    for i in range(1,int(math.log(s,2))+1):
        count=count+1
        for k in range(1,s+1):
            a = 0  
            if(arr[((i + k - 1)%s)]==0 and arr[ (( (i + k - 1) % s ) + 2**(i-1) ) %s] ==0 ):
                a = (i + k - 1)%s
                if(a==0):
                    a+=s
            else:
                continue
            b = ((a + 2**(i-1))%s)
            if(b==0):
                b+=s
            arr[a] = 1
            arr[b] = 1
            if(top=="Torus"):
                graph_torus(s,a,b,str(count)+" "+str(a)+":"+str(b),path+str(fol_name))
            if(top=="Fat-Tree"):
                graph(s,a,b,str(count)+" "+str(a)+":"+str(b),path+str(fol_name))
            if(top=="DragonFly"):
                dragonfly_graph(s,g,a-1,b-1,str(a)+":"+str(b),path+str(fol_name))
        for i in range(0,s+1):
            arr[i] = 0
    i = "*.png"
    o = "output.gif"
    subprocess.call("convert -delay 100 -loop 5 " + i + " " + o, shell=True)
    os.system("start output.gif")
    os.system("gthumb "+path+str(fol_name))

def reduce_reb(s,i,g,top):
    fol_name=0
    while True:
        global path
        if not os.path.exists(path+str(fol_name)):
            os.mkdir(path+str(fol_name),0o755)
            break
        fol_name=fol_name+1
    os.system("chmod +x "+path+str(fol_name))
    count=0
    arr = []
    for i in range(0,s+1):
        arr.append(0)
    for i in range(1,int(math.log(s,2))+1):
        count=count+1
        for k in range(1,s+1):
            a = 0  
            if(arr[((i + k - 1)%s)]==0 and arr[ (( (i + k - 1) % s ) + 2**(i-1) ) %s] ==0 ):
                a = (i + k - 1)%s
                if(a==0):
                    a+=s
            else:
                continue
            b = ((a + 2**(i-1))%s)
            if(b==0):
                b+=s
            arr[a] = 1
            arr[b] = 1
            if(top=="Torus"):
                graph_torus(s,a,b,str(count)+" "+str(a)+":"+str(b),path+str(fol_name))
            if(top=="Fat-Tree"):
                graph(s,a,b,str(count)+" "+str(a)+":"+str(b),path+str(fol_name))
            if(top=="DragonFly"):
                dragonfly_graph(s,g,a-1,b-1,str(a)+":"+str(b),path+str(fol_name))
        for i in range(0,s+1):
            arr[i] = 0
    gather_rec1(s,i,g,top,path+str(fol_name))
    i = "*.png"
    o = "output.gif"
    subprocess.call("convert -delay 100 -loop 5 " + i + " " + o, shell=True)
    os.system("start output.gif")
    os.system("gthumb "+path+str(fol_name))

def allreduce_reb(s,i,g,top):
    fol_name=0
    while True:
        global path
        if not os.path.exists(path+str(fol_name)):
            os.mkdir(path+str(fol_name),0o755)
            break
        fol_name=fol_name+1
    arr = []
    for i in range(0,s+1):
        arr.append(0)
    for i in range(1,int(math.log(s,2))+1):
        for k in range(1,s+1):
            a = 0  
            if(arr[((i + k - 1)%s)]==0 and arr[ (( (i + k - 1) % s ) + 2**(i-1) ) %s] ==0 ):
                a = (i + k - 1)%s
                if(a==0):
                    a+=s
            else:
                continue
            b = ((a + 2**(i-1))%s)
            if(b==0):
                b+=s
            arr[a] = 1
            arr[b] = 1
            if(top=="Torus"):
                graph_torus(s,a,b,str(count)+" "+str(a)+":"+str(b),path+str(fol_name))
            if(top=="Fat-Tree"):
                graph(s,a,b,str(count)+" "+str(a)+":"+str(b),path+str(fol_name))
            if(top=="DragonFly"):
                dragonfly_graph(s,g,a-1,b-1,str(a)+":"+str(b),path+str(fol_name))
        for i in range(0,s+1):
            arr[i] = 0
    allgather_rec1(s,i,g,top,path+str(fol_name))
    i = "*.png"
    o = "output.gif"
    subprocess.call("convert -delay 100 -loop 5 " + i + " " + o, shell=True)
    os.system("start output.gif")
    os.system("gthumb "+path+str(fol_name))

def allgather_rec1(s,i,g,top,fol_name):
    count=0
    arr = []
    for i in range(0,s+1):
        arr.append(0)
    for i in range(1,int(math.log(s,2))+1):
        for k in range(1,s+1):
            a = 0  
            if(arr[((i + k - 1)%s)]==0 and arr[ (( (i + k - 1) % s ) + 2**(i-1) ) %s] ==0 ):
                a = (i + k - 1)%s
                if(a==0):
                    a+=s
            else:
                continue
            b = ((a + 2**(i-1))%s)
            if(b==0):
                b+=s
            arr[a] = 1
            arr[b] = 1
            if(top=="Torus"):
                graph_torus(s,a,b,str(count)+" "+str(a)+":"+str(b),str(fol_name))
            if(top=="Fat-Tree"):
                graph(s,a,b,str(count)+" "+str(a)+":"+str(b),str(fol_name))
            if(top=="DragonFly"):
                dragonfly_graph(s,g,a-1,b-1,str(a)+":"+str(b),str(fol_name))
            count=count+1
        for i in range(0,s+1):
            arr[i] = 0

def gather_rec1(s,i,g,top,fol_name):
    count=0
    i=i-1
    d=int(math.log(s,2))
    node=[]
    x_list=[]
    y_list=[]
    node.append(i)
    for k in range(0,d):
        length=len(node)
        for x in range(0,length):
            if int(node[x])^int(2**(d-(k+1)))<int(s):
                node.append(int(node[x])^int(2**(d-(k+1))))
                val=str((int(node[x])^int(2**(d-(k+1))))+1)
                y_list.insert(0,node[x]+1)
                x_list.insert(0,(int(node[x])^int(2**(d-(k+1))))+1)    
    k=int(len(x_list)/2)+1    
    c=0
    for i in range(0,len(x_list)):
        c+=1
        if(top=="Torus"):
            graph_torus(s,x_list[i],y_list[i],str(count)+" "+str(x_list[i])+":"+str(y_list[i]),str(fol_name))
        if(top=="Fat-Tree"):
            graph(s,x_list[i],y_list[i],str(count)+" "+str(x_list[i])+":"+str(y_list[i]),str(fol_name))
        if(top=="DragonFly"):
            dragonfly_graph(s,g,x_list[i]-1,y_list[i]-1,str(x_list[i])+":"+str(y_list[i]),str(fol_name))
        if(c==k):
            c=0
            k/=2
        count=count+1       

def gather_rec(s,i,g,top):
    fol_name=0
    while True:
        global path
        if not os.path.exists(path+str(fol_name)):
            os.mkdir(path+str(fol_name),0o755)
            break
        fol_name=fol_name+1
    os.system("chmod +x "+path+str(fol_name))
    count=0
    i=i-1
    d=int(math.log(s,2))
    node=[]
    x_list=[]
    y_list=[]
    node.append(i)
    for k in range(0,d):
        length=len(node)
        for x in range(0,length):
            if int(node[x])^int(2**(d-(k+1)))<int(s):
                node.append(int(node[x])^int(2**(d-(k+1))))
                val=str((int(node[x])^int(2**(d-(k+1))))+1)
                y_list.insert(0,node[x]+1)
                x_list.insert(0,(int(node[x])^int(2**(d-(k+1))))+1)    
    k=int(len(x_list)/2)+1    
    c=0
    for i in range(0,len(x_list)):
        c+=1
        if(top=="Torus"):
            graph_torus(s,x_list[i],y_list[i],str(count)+" "+str(x_list[i])+":"+str(y_list[i]),path+str(fol_name))
        if(top=="Fat-Tree"):
            graph(s,x_list[i],y_list[i],str(count)+" "+str(x_list[i])+":"+str(y_list[i]),path+str(fol_name))
        if(top=="DragonFly"):
            dragonfly_graph(s,g,x_list[i]-1,y_list[i]-1,str(count)+" "+str(x_list[i])+":"+str(y_list[i]),path+str(fol_name))
        if(c==k):
            c=0
            k/=2
        count=count+1   
    i = "*.png"
    o = "output.gif"
    subprocess.call("convert -delay 100 -loop 5 " + i + " " + o, shell=True)
    os.system("start output.gif")
    os.system("gthumb "+path+str(fol_name))   

def graph_torus(num_nodes,a,b,title,path):
    global number_of_hops
    levels=0
    hops=0
    x=[]
    y=[]
    point_num=[]
    side = int(math.sqrt(num_nodes))
    for i in range(1,side+1):
        for j in range(1,side+1):
            y.append(i)
            x.append(j)
    for i in range(0,len(x)):
        plt.annotate(str(i+1),xy=(x[i]+.1,y[i]+.1))
    for i in range(1,side+1):
        plt.plot([0.5,side+0.5], [i,i],'k-',color='y',linewidth=2)
        plt.plot([i,i], [0.5,side+0.5],'k-',color='y',linewidth=2)
    plt.scatter(x, y)
    if(abs(x[a-1]-x[b-1])<(side/2)):
        plt.plot([x[a-1],x[b-1]], [y[a-1],y[a-1]],'k-',color='r')
        number_of_hops=number_of_hops+abs(x[a-1]-x[b-1])
        hops=hops+abs(x[a-1]-x[b-1])
    else:
        if(x[a-1]<x[b-1]):
            plt.plot([x[a-1],0.5], [y[a-1],y[a-1]],'k-',color='r')
            plt.plot([x[b-1],side+0.5], [y[a-1],y[a-1]],'k-',color='r')
            number_of_hops=number_of_hops+abs(side-x[b-1]+x[a-1])
            hops=hops+abs(side-x[b-1]+x[a-1])
        else:
            plt.plot([x[b-1],0.5], [y[a-1],y[a-1]],'k-',color='r')
            plt.plot([x[a-1],side+0.5], [y[a-1],y[a-1]],'k-',color='r')
            number_of_hops=number_of_hops+abs(x[b-1])
            hops=hops+abs(x[b-1])
    if(abs(y[a-1]-y[b-1])<(side/2)):
        plt.plot([x[b-1],x[b-1]], [y[a-1],y[b-1]],'k-',color='r')
        number_of_hops=number_of_hops+abs(y[a-1]-y[b-1])
        hops=hops+abs(y[a-1]-y[b-1])
    else:
        if(y[a-1]<y[b-1]):
            plt.plot([x[b-1],x[b-1]], [y[a-1],0.5],'k-',color='r')
            plt.plot([x[b-1],x[b-1]], [side+0.5,y[b-1]],'k-',color='r')
            number_of_hops=number_of_hops+abs(side-y[b-1]+y[a-1])
            hops=hops+abs(side-y[b-1]+y[a-1])
        else:
            plt.plot([x[b-1],x[b-1]], [y[b-1],0.5],'k-',color='r')
            plt.plot([x[b-1],x[b-1]], [side+0.5,y[a-1]],'k-',color='r')
            number_of_hops=number_of_hops+abs(x[b-1])
            hops=hops+abs(x[b-1])
    k5entry.delete(0, END) #deletes the current value
    k5entry.insert(0, number_of_hops)
    os.chdir(path)
    plt.title("Time Stamp :"+title+" hops ="+str(hops))
    plt.xticks([])
    plt.yticks([])
    plt.savefig(title+".png")
    plt.clf()

def graph(s,x1,y1,title,path):
    hops=0
    global number_of_hops
    levels=0
    x=[]
    y=[]
    point_num=[]
    num_nodes=int(s)
    if num_nodes==1:
        levels=1
    if num_nodes==2:
        levels=2
    else:   
        for i in range(1,num_nodes):
            if ((2**i)-1)>=num_nodes:
                levels=i
                break
    ans=0
    for i in range(0,levels-1):
        ans+=2**i
    leaves_last_level=num_nodes-ans
    for i in range(0,levels):
        for j in range(0,2**(levels-i-1)):
            if i==0 and j==leaves_last_level:
                break
            x.append((2**i)+(2**(i+1)*j))
            y.append(i)
    plt.scatter(x, y)
    i=0
    num=0
    while i<len(y)-1:
        num=0
        plt.annotate(str(2**(levels-y[i]-1)+num),xy=(x[i]+.5,y[i]))
        point_num.append(2**(levels-y[i]-1)+num)
        i=i+1
        num=num+1
        while y[i-1]==y[i] and i<len(y):
            plt.annotate(str(2**(levels-y[i]-1)+num),xy=(x[i]+.5,y[i]))
            point_num.append(2**(levels-y[i]-1)+num)
            i=i+1
            num=num+1
    plt.annotate(str(2**(levels-y[len(y)-1]-1)),xy=(x[len(y)-1]+.5,y[len(y)-1]))
    point_num.append(2**(levels-y[len(y)-1]-1))
    i=0
    j=1
    while i<len(y):
        while j<len(y):
            if y[j]>y[i]:
                plt.plot([x[j],x[i]], [y[j],y[i]],'k-',linewidth=y[j],color="y")
                i=i+1
            if y[j]>y[i]:
                plt.plot([x[j],x[i]], [y[j],y[i]],'k-',linewidth=y[j],color="y")
                i=i+1
            j=j+1
        i=i+1
    global path1
    os.chdir(path1)
    os.system('./a.out '+str(x1)+' '+str(y1)+' > path.txt')
    data = []
    with open("path.txt", "r") as f:
        lines = f.readlines() 
        data = (lines[0].split())
    pj=0
    pj1=1
    i=0
    while i<len(data)-1:
        pj=point_num.index(int(data[i]))
        pj1=point_num.index(int(data[i+1]))
        plt.plot([x[int(pj)],x[int(pj1)]],[y[int(pj)],y[int(pj1)]],color="r")
        number_of_hops=number_of_hops+1
        hops=hops+1
        i=i+1
    k5entry.delete(0, END)
    k5entry.insert(0, number_of_hops)
    plt.title("Time Stamp :"+title+" hops ="+str(hops))
    hops=0
    os.chdir(path)
    plt.xticks([])
    plt.yticks([])
    plt.savefig(title+".png")
    plt.clf()
		
def dragonfly_graph(total,group,a,b,title,path):
    group_size=total/group
    extra=1
    rank_in_group_a=a%group_size
    rank_in_group_b=b%group_size
    inter_group_connection_per_node=int((group-1)/group_size)
    group_number_a=2
    total_number_groups=9
    X=2
    if(int(a/group_size)!=int(b/group_size)):
        group_number_b=int(b/group_size)
        group_number_a=int(a/group_size)
        for i in range(0,int(group_size)):
            for j in range(1,inter_group_connection_per_node+1):
                pj=int(a/group_size)+i*(-inter_group_connection_per_node)-j-1
                if pj<0:
                    if((group+pj+1)==group_number_b):
                        if(i==rank_in_group_a):
                            dragonfly_graph1(total,group,a,int(group_size*(group+pj+1)+i),title+" "+str(extra)+" ",path)
                            extra+=1
                            if(group_size*(group+pj+1)+i!=b):
                                dragonfly_graph1(total,group,int(group_size*(group+pj+1)+i),b,title+" "+str(extra)+" ",path)
                                extra+=1
                            break
                        else:
                            dragonfly_graph1(total,group,a,int(a-rank_in_group_a+i),title+" "+str(extra)+" ",path)
                            extra+=1
                            dragonfly_graph1(total,group,int(a-rank_in_group_a+i),int(group_size*(group+pj+1)+i),title+" "+str(extra)+" ",path)
                            extra+=1
                            if(group_size*(group+pj+1)+i!=b):
                                dragonfly_graph1(total,group,int(group_size*(group+pj+1)+i),b,title+" "+str(extra)+" ",path)
                                extra+=1
                            break
    else:
        dragonfly_graph1(total,group,a,b,title,path)
        extra+=1

def dragonfly_graph1(total,group,a,b,title,path):
    global number_of_hops
    hops=0
    numberpergroup = total/group
    x=[]
    y=[]
    angle = 2*math.pi/total
    colorarr=[]
    c=0
    col='red'
    for i in range(0,total):
        c+=1
        colorarr.append(col)
        if(c==numberpergroup):
            if(col=='red'):
                col='blue'
                c=0
            else:
                col='red'
                c=0
    for i in range(0,total):
        x.append(10*math.cos(i*angle))
        y.append(10*math.sin(i*angle))
    for i in range(0,total):
        plt.annotate(str(i+1),xy=(x[i]+.1,y[i]+.1))
        plt.plot([x[i],12*math.cos(i*angle)],[y[i],12*math.sin(i*angle)],'k-',color='y')
    plt.scatter(x, y,color=colorarr)
    g1 = int(a/numberpergroup)
    g2 = int(b/numberpergroup)
    if(g1==g2):
        hops=hops+1
        number_of_hops=number_of_hops+1
        plt.plot([12*math.cos(a*angle),12*math.cos(b*angle)],[12*math.sin(a*angle),12*math.sin(b*angle)],'k-',color='g')
    else:
        hops=hops+1
        number_of_hops=number_of_hops+1
        plt.plot([x[a],x[b]],[y[a],y[b]],'k-',color='g')
    k5entry.delete(0, END) 
    k5entry.insert(0, number_of_hops)
    os.chdir(path)
    plt.title("Time Stamp :"+title + "hops= "+str(hops))
    hops=0
    plt.xticks([])
    plt.yticks([])    
    plt.savefig(title+".png")
    plt.clf()

# User Interface
def get_me():
    global number_of_hops
    top=variable1.get()
    algo=variable2.get()
    s=k1.get()
    a=k2.get()
    b=k3.get()
    g=k4.get()
    if(algo=='Gather_Rec'):
        if int(a)<=int(s):
            gather_rec(int(s),int(a),int(g),top)
            number_of_hops=0
    if(algo=='All Reduce_Reb'):
        if int(a)<=int(s):
            allreduce_reb(int(s),int(a),g,top)
            number_of_hops=0
    if(algo=='Reduce_Reb'):
        if int(a)<=int(s):
            reduce_reb(int(s),int(a),g,top)
            number_of_hops=0
    if(algo=='Allgather_Ring'):
        if int(a)<=int(s):
            allgather_ring(int(s),int(a),g,top)
            number_of_hops=0
    if(algo=='Allgather_Rec'):
        if int(a)<=int(s):
            allgather_rec(int(s),int(a),g,top)
            number_of_hops=0
    if(algo=='Broadcast(naive)'):
        if int(a)<=int(s):
            naive(int(s),int(a),g,top)
            number_of_hops=0
    if((top=='Fat-Tree' or top=='DragonFly') and algo=='Broadcast(recursive-doubling)'):
        if int(a)<=int(s):
            recursive_doubling(int(s),int(a),g,top)
            number_of_hops=0
    if(top=='Torus' and algo=='Broadcast(recursive-doubling)'):
        if int(a)<=int(s):
            torus_recursive_doubling(int(s),int(a))
            number_of_hops=0
    if(algo=='Send'):	
        if int(a)<=int(s) and int(b)<=int(s):
            send(int(s),int(a),int(b),g,top)
            number_of_hops=0
    global path1
    os.chdir(path1)

master = Tk()
Topology=["Fat-Tree","Torus","DragonFly"]
MPI_call=["Broadcast(naive)","Broadcast(recursive-doubling)","Gather_Rec","Allgather_Ring","Allgather_Rec","Reduce_Reb","All Reduce_Reb","Send"]
variable1 = StringVar(master)
variable1.set(Topology[0]) 
variable2 = StringVar(master)
variable2.set(MPI_call[0]) 
l1 = Label(master, text="Topology")
l1.configure(font=('Impact', 25))
l1.pack(padx=4, pady=10)
w1 = OptionMenu(master, variable1, *Topology)
w1.configure(font=('Impact', 25))
w1.pack(padx=5, pady=10)
l2 = Label(master, text="MPI Call")
l2.configure(font=('Impact', 25))
l2.pack(padx=4, pady=10)
w2 = OptionMenu(master, variable2, *MPI_call)
w2.configure(font=('Impact', 25))
w2.pack(padx=5, pady=10)
menu = w1.nametowidget(w1.menuname)
menu.configure(font=('Impact', 25))
menu = w2.nametowidget(w2.menuname)
menu.configure(font=('Impact', 25))
l3 = Label(master, text="Number of nodes")
l3.configure(font=('Impact', 25))
l3.pack(padx=4, pady=10)
k1 = IntVar()
k1entry = Entry(textvariable=k1)
k1entry.configure(font=('Impact', 25))
k1entry.pack()
l4 = Label(master, text="Starting node")
l4.configure(font=('Impact', 25))
l4.pack(padx=4, pady=10)
k2 = IntVar()
k2entry = Entry(textvariable=k2)
k2entry.configure(font=('Impact', 25))
k2entry.pack()
l5 = Label(master, text="Ending node(for send)")
l5.configure(font=('Impact', 25))
l5.pack(padx=4, pady=10)
k3 = IntVar()
k3entry = Entry(textvariable=k3)
k3entry.configure(font=('Impact', 25))
k3entry.pack()
l6 = Label(master, text="Number of groups(Dragon Fly)")
l6.configure(font=('Impact', 25))
l6.pack(padx=4, pady=10)
k4 = IntVar()
k4entry = Entry(textvariable=k4)
k4entry.configure(font=('Impact', 25))
k4entry.pack()
l7 = Label(master, text="Number of hops")
l7.configure(font=('Impact', 25))
l7.pack(padx=4, pady=10)
k5 = IntVar()
k5entry = Entry(textvariable=k5)
k5entry.configure(font=('Impact', 25))
k5entry.pack()
button = Button(master, text="OK", command=get_me)
button.configure(font=('Impact', 25))
button.pack(padx=5, pady=10,side=BOTTOM)
master.geometry("600x900")
mainloop()