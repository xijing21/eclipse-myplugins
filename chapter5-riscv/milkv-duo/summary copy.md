### RuyiSDK IDE中编译运行demo

1. 下载 RuyiSDK IDE v0.0.1 ：https://mirror.iscas.ac.cn/ruyisdk/ide/0.0.1/ruyisdk-0.0.1-linux.gtk.x86_64.tar.gz
2. 解压并启动 IDE

   - 工作空间：ews-milkvduo-v001
3. 导入 milkv duo的示例 hello-world
4. 

## RuyiSDK

### ruyisdk下的upstream SDK资源

理想情况：

当前现状：

### ruyi搭建安装环境

### IDE中使用

# 结论

1. plct-gnu 暂时不支持 musl 库，milkv duo 目前还需要使用硬件厂商提供的 工具链版本。plct-gnu后续有支持 musl 计划。
2. qemu：qemu 目前无法运行 musl 工具链编译的目标程序。（可能需要适配运行环境？）
3. milkv duo 的 demo仓库：目前似乎在目录组织方便还有改进的空间。工具链、头文件、库文件都集合在这个文件夹中。ruyisdk如果想要在ide中按照统一模版集成不同开发板的demo，则需要建立统一的demo目录标准。

总的来说，milkv duo 虽然已经能够使用 ruyi 包管理器安装和使用，也能够在 ide 中配置使用，但是 核心的 plct-gnu 和 milkvduo ruyisdk（这里特指 demo/template+头文件+库文件+运行环境sysroot等）并未形成一整套有一定标准的开发环境。



而且目前只针对 milkv duo helloworld这种最简单的demo进行了验证，更多demo需要进一步验证和集成打包到ruyisdk
更多的开发板型号也需要进一步的验证。

至少在ide中，demo/template + 头文件+库文件+sysroot等链接所需的环境都必须打包到 ruyisdk中。这样的sdk才能算是一整套的开发sdk；

