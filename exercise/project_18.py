#处理二进制文件，例：处理.wav音频文件（一种二进制文件）
#.wav文件包含头部信息，包括声道数、采样频率、编码位宽等，以及音频采样数据
#读取wav文件，以二进制形式打开
file_path = 'D:\\python\\vs python work\\exercise\\'
filename = 'music.wav'
music_file = open(file_path + filename,'rb')
#读取头部信息（0至44字节）
title_info = music_file.read(44)  #对于二进制文件，44代表读入44个字节
print(type(title_info))
#检查通道数（22至24字节），利用struct解析
import struct
#unpack(解析类型,需解析对象)，其中解析类型可以是：'i':int(4b) 'h':short(2b)
print(struct.unpack('h',title_info[22:24]))
#采样频率（24至28字节）
print(struct.unpack('i',title_info[24:28]))

#以上直接切片的坐标不一定准确，下面寻找所需ChunkID的确切位置
def Find_subchunk(Binfile,ChunkId):
    Binfile.seek(12)  #第一个子Chunk一定再12字节处，故将从头开始的指针指向12处
    while True:
        chunk_name = Binfile.read(4)
        #unpack解析后有个','，变量名后面加逗号使得变量为一个数字
        chunk_size, = struct.unpack('i', Binfile.read(4))
        if chunk_name == ChunkId:
            return Binfile.tell(),chunk_size  #.tell返回当前指针
        else:
            Binfile.seek(chunk_size,1)  #1代表从当前指针位置开始，读取chunk_size个字节

file_path = 'D:\\python\\vs python work\\exercise\\'
filename = 'music.wav'
music_file = open(file_path + filename,'rb')
music_file.seek(0)
pinloc,chunk_size = Find_subchunk(music_file,b'data')
print(pinloc)
print(chunk_size)

#对文件进行处理
import numpy as np
buf = np.zeros(chunk_size//2,dtype=np.short)
music_file.readinto(buf)
#将buf里的数据进行衰减
buf //= 8
#写入另一个文件中
output_file = open(file_path + 'output.wav','wb')
info = music_file.read(pinloc)
output_file.write(info)  #头部信息不变
buf.tofile(output_file)
output_file.close()