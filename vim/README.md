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
    其中，```--enable-python3interp```表示打开对python3编写的插件的支持，YouCompleteMe插件需要；```--prefix=$HOME/.local```表示安装vim到一个自定义目录，默认装到```/usr/bin/local/```目录中。
    
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
./install.py --clangd-completer
```
### 问题二
使用vim-plug插件安装YouCompleteMe时间较长，如果失败，可以手动安装(由于YCM插件更新较快，依赖的组件较多，建议手动安装)
```
cd ~/.vim/bundle
git clone https://github.com/ycm-core/YouCompleteMe.git
cd YouCompleteMe
git submodule update --init --recursive
./install.py --go-completer --clangd-completer
```

如果YouCompleteMe安装成功，启动vim后，会启动一个**ycmd**进程，可以在```/tmp/```目录下看到**ycmd**进程的日志，注意观察日志查看进程是否正常启动

### 问题三
安装YouCompleteMe的go语言插件时，如果用的go版本较低，会出现如下问题，升级到最新的go版本即可
```
main.go:15:2: use of internal package not allowed
main.go:16:2: use of internal package not allowed
```
