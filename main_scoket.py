import socket
import click
import time

# 使用nc -ul port 可以监听到

class ScoketFile(object):

    def __init__(self,ip,port):
        self.ip = str(ip)
        self.port = int(port)

    def build(self):
        return self.start(),self

    def start(self):
        return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def close(self):
        self.socket.close()


def read_file(path):
    return open(path,mode="r").readlines()

def run(ip,port,path,sleep):
    sock ,self_= ScoketFile(ip,port).build() # 返回的自定义类的实列 
    lines = read_file(path)
    for line in lines:
        line_ = line.replace('\n','')
        click.echo(click.style('发送数据 :\t'+str(line_), fg='green'))
        sock.sendto(line.encode(), (self_.ip,self_.port)) #发送数据
        time.sleep(sleep)
    sock.close()
        


@click.command()
@click.option('--ip',type=str,default='localhost',help='默认是本机ip，通过--ip参数指定')
@click.option('--port',type=int,default=12345,help='默认是12345端口，通过--port参数指定')
@click.option('--sleep',type=int,default=1,help='默认睡眠1秒，通过--sleep指定睡眠时间')
@click.option('--path',type=str,help='通过--path指定需要发送的文件路径,注意路径中的空格')
def main(ip,port,path,sleep):
    if path is None:
        click.echo('请指定path参数，通过--help查看使用方法')
    else:
        try:
            click.echo('>==\t LiusNew开发 \t==<')
            click.echo(click.style(f'>\t指定传送ip为{ip}\n>\t指定接收数据端口为{port}\n>\t指定每次传送时间间隔为{sleep}\n>\t指定传送文件为 ({path})\n',fg='blue'))
            run(ip,port,path,sleep)
            click.echo(click.style('\n>\t发送完毕',fg='red'))
        except Exception as e:
            click.echo(click.style('--help查看说明，或者阅读错误信息 --> \t'+str(e), fg='red'))


if __name__ == "__main__":
    main()

