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
    ./configure --prefix=$HOME/.local -enable-pythoninterp
    ```
    其中，```–enable-pythoninterp```表示打开对python编写的插件的支持，YouCompleteMe插件需要；```--prefix=$HOME/.local```表示安装vim到一个自定义目录，默认装到```/usr/bin/local/```目录中。
    
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
./install.py --clang-complete
```

