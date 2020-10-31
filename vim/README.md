## 本人使用vim的个性化配置，参考：

- [k-vim](https://github.com/wklken/k-vim)
- [vim-plug](https://github.com/junegunn/vim-plug)
- [YouCompleteMe](https://github.com/Valloric/YouCompleteMe)


## Vim 8.1编译安装：

- 下载Vim 8.1
    ```
    wget https://github.com/vim/vim/archive/v8.1.2135.tar.gz
    tar -zxvf v8.1.2135.tar.gz
    ```
- 编译Vim 8.1
    ```
    cd vim-8.1.2135
    ./configure --prefix=$HOME/.local --enable-python3interp
    make -j && make install
    ```
    其中，```--enable-python3interp```表示打开对python3编写的插件的支持，YouCompleteMe插件需要；```--prefix=$HOME/.local```表示安装vim到一个自定义目录，默认装到```/usr/local/bin/```目录中。
    
- 利用alias将vim指令定向到刚刚安装的vim8，同时修改.bashrc确保之后一直能生效
    ```
    alias vim='~/.local/bin/vim'
    echo "alias vim='~/.local/bin/vim'" >> ~/.bashrc
    ```

## Troubleshooting

### 问题一：

使用vim-plug安装YCM后，打开vim有如下问题：
```
The ycmd server SHUT DOWN (restart with ':YcmRestartServer'). YCM core library not detected; you need to compile YCM before
using it. Follow the instructions in the documentation.
```
解决办法：

```
cd ~/.vim/bundle/YouCompleteMe
python3 install.py --clangd-completer
```
### 问题二
使用vim-plug插件安装YouCompleteMe时间较长，如果失败，可以手动安装(由于YCM插件更新较快，依赖的组件较多，建议手动安装)
```
cd ~/.vim/bundle
git clone https://github.com/ycm-core/YouCompleteMe.git
cd YouCompleteMe
git submodule update --init --recursive
python3 install.py --go-completer --clangd-completer
```

如果YouCompleteMe安装成功，启动vim后，会启动一个**ycmd**进程，可以在```/tmp/```目录下看到**ycmd**进程的日志，注意观察日志查看进程是否正常启动

### 问题三
安装YouCompleteMe的go语言插件时，如果用的go版本较低，会出现如下问题，升级到最新的go版本即可
```
main.go:15:2: use of internal package not allowed
main.go:16:2: use of internal package not allowed
```

### 问题四
升级YouCompleteMe到最新版本(fa8c985)，YCM到跳转功能不能使用，**ycmd**进程日志出现如下错误：
```
- ERROR - The language server communication channel closed unexpectedly. Issue a RestartServer command to recover
```
同时在/tmp目录下可以看到clangd的error日志（clangd_stderrjq0zhzbe.log）如下：
```
/root/.vim/bundle/YouCompleteMe/third_party/ycmd/third_party/clangd/output/bin/clangd: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.20' not found (required by /root/.vim/bundle/YouCompleteMe/third_party/ycmd/third_party/clangd/output/bin/clangd)
/root/.vim/bundle/YouCompleteMe/third_party/ycmd/third_party/clangd/output/bin/clangd: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.21' not found (required by /root/.vim/bundle/YouCompleteMe/third_party/ycmd/third_party/clangd/output/bin/clangd)
/root/.vim/bundle/YouCompleteMe/third_party/ycmd/third_party/clangd/output/bin/clangd: /lib64/libstdc++.so.6: version `CXXABI_1.3.9' not found (required by /root/.vim/bundle/YouCompleteMe/third_party/ycmd/third_party/clangd/output/bin/clangd)
```
这是因为YCM使用默认的clangd程序，运行该程序缺少对应的glibc库导致的

解决办法：下载9.0.0以上版本的clangd，同时在vimrc配置文件指定clangd进程的路径

安装clangd：
```
wget https://github.com/clangd/clangd/releases/download/10.0.0/clangd-linux-10.0.0.zip
unzip clangd-linux-10.0.0.zip
cd clangd_10.0.0/bin/
./clangd --version
```
需要注意的是clangd 10.0.0依赖glibc-2.18,如果```./clangd --version```命令执行失败，那么要安装对应的glibc库，使用```strings /lib64/libc.so.6 |grep GLIBC_```可以查看系统支持的glibc库版本，安装glibc-2.18的放入如下：
```
wget http://mirrors.ustc.edu.cn/gnu/libc/glibc-2.18.tar.gz
tar -zxvf glibc-2.18.tar.gz
mkdir build
cd build
../configure --prefix=/usr
make -j4
sudo make install
```

在vimrc中指定clangd进程路径：
```
let g:ycm_clangd_binary_path = "/path/to/clangd"
```



