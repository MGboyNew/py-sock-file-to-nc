import click
import os

#  (echo 'hellsdfso'; sleep 1) | telnet localhost 12345
# os.system("""(echo 'hellsdfso'; sleep 1) | telnet localhost 12345""")

def read_file(path):
    return open(path,mode="r").readlines()

def run(ip,port,path,sleep):
    lines = read_file(path)
    for line in lines:
        line_ = line.replace('\n','')
        click.echo(click.style('发送数据 :\t'+str(line_), fg='green'))
        command = """(echo '{}'; sleep {}) | telnet {} {} >/dev/null 2>&1""".format(line_,sleep,ip,port)
        os.system(command)
        


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

