## 使用 ruyi 为 milkv duo 安装镜像、编译器等开发环境

### PC上安装 ruyi

1. 可从RuyiSDK仓库下载最新版本 [https://mirror.iscas.ac.cn/ruyisdk/ruyi/releases/](https://gitee.com/link?target=https%3A%2F%2Fmirror.iscas.ac.cn%2Fruyisdk%2Fruyi%2Freleases%2F)

   ```
   wget https://mirror.iscas.ac.cn/ruyisdk/ruyi/releases/0.24.0/ruyi.amd64  #从软件源下载ruyi本体
   chmod +x ruyi.amd64  #给ruyi添加执行权限
   sudo cp ruyi.amd64 /usr/local/bin/ruyi #将ruyi本体改名为ruyi，并放入PATH
   ruyi version 
   ruyi update  #更新软件包索引
   ```
2. 安装 gnu-milkv-milkv-duo-musl 编译器

   ```
   #查看软件源的资源
   #ruyi list

   #安装指定的工具链
   ruyi install gnu-milkv-milkv-duo-bin
   #从返回信息中可以查看安装的路径，如 ~/.local/share/ruyi/binaries/x86_64/gnu-milkv-milkv-duo-bin-0.20240731.0+git.67688c7335e7
   ```
3. 创建和使用Duo编译环境

   ```
   #查看ruyi预配置环境
   #ruyi list profiles

   #创建一个虚拟环境（自定义命名milkv-venv）：工具链为gnu-milkv-milkv-duo-musl-bin
   #ruyi venv -t gnu-milkv-milkv-duo-musl-bin milkv-duo ./venv-milkvduo
   ruyi venv -t gnu-milkv-milkv-duo-musl-bin generic ./venv-milkvduo-generic

   #激活虚拟环境
   source venv-milkvduo-generic/bin/ruyi-activate
   ```
4. 下载 duo-example 源码并使用 gnu-milkv-milkv-duo-musl 工具链进行交叉编译

   > 当 ruyisdk 还未集成并提供开发板对应的 example 时，可自己下载或者导入想要编译的源码。
   >

   ```
   #下载duo-example
   mkdir milkv-duo-examples 
   cd milkv-duo-examples
   ruyi extract milkv-duo-examples   #资源名可通过ruyi list查询
   ```
5. 编译源码

   ```
   cd hello-world
   ls -al

   #执行编译
   riscv64-unknown-linux-musl-gcc -g -o helloworld helloworld.c  

   riscv64-unknown-linux-musl-gcc -march=rv64imafdcv0p7xthead -mabi=lp64d -O3 -g -o helloworld helloworld.c  

   riscv64-unknown-linux-musl-gcc -mcpu=c906fdv -march=rv64imafdcv0p7xthead -mcmodel=medany -mabi=lp64d -O3 -DNDEBUG -g -o helloworld helloworld.c  -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64

   # venv-milkvduo-generic虚拟环境下，上述3个命令都能编译成功。但是venv-milkvduo下，会报错：https://github.com/ruyisdk/ruyi/issues/255

   #查看
   ls -al
   file helloworld
   #helloworld: ELF 64-bit LSB executable, UCB RISC-V, RVC, double-float ABI, version 1 (SYSV), dynamically linked, interpreter /lib/ld-musl-riscv64v0p7_xthead.so.1, with debug_info, not stripped

   #退出虚拟环境
   ruyi-deactivate 
   ```

   至此，编译就完成了。目前生成了RISC-V目标程序。在当前PC端是无法运行的，需要拷贝到 milkv duo 开发板上运行。

   接下来就再介绍如何使用ruyisdk系统安装工具给 RISC-V 设备安装镜像，并运行上述的目标程序。

### RV设备端：烧录镜像

1. 【建议，但非必须，可以避免烧录过程出问题】格式化SD卡，准备烧录镜像

   ```bash
   #准备：sd卡插入读卡器，读卡器插入PC。先格式化并删除已有的分区
   #查看sd卡设备节点（我环境下一般是/dev/sdb）
   sudo df -h

   #umount：（按实际情况修改设备节点）
   sudo umount /dev/sdb1
   sudo umount /dev/sdb2

   # 删除sd卡所有分区（/dev/sdb1 和 /dev/sdb2）
   sudo wipefs --all /dev/sdb

   #格式化：
   sudo mkfs.ext4 /dev/sdb
   ```
2. 烧录系统到sd卡

   ```bash
   #烧录镜像
   ruyi device peovision
   #后续按照提示一步步执行，选择 milkv duo 设备对应的相关参数和选项，按照提示执行即可。

   # 烧录完成后，请将sd卡插入到 milkv duo sd卡卡槽中，将 milkv duo 设备通过 usb-typec 线通电，通电后将自动启动，启动成功后执行如下操作连接 milkv duo 设备进行远程操作
   ssh root@192.168.42.1  
   root 密码: milkv
   ```

### 执行目标程序

1. PC：执行scp拷贝命令将目标程序传输到目标设备
   ```
   $ scp helloworld root@192.168.42.1:/root/
   ```

2. 执行目标程序
   发送成功后，在 ssh 或者串口登陆的终端中运行 `./helloworld`，会打印 `Hello, World!`

   ```bash
   #连接远程设备
   ssh root@192.168.42.1
   root 密码: milkv

   [root@milkv]~# ./helloworld
   Hello, World!
   ```
