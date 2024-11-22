## 任务背景

### 目标

开始研究Eclipse的插件开发，考虑为RISC-V开发者（重点先考虑应用开发者）打造 RISC-V嵌入式开发IDE。

- 从操作的流程来说：

  * （1）RISC-V架构的编译—》连接到RISC-V开发板——》文件传输——》开发板上运行；
  * （2）RISC-V架构的编译—》模拟运行；
  * （3）调试；
- 从支持的编程语言类型来看：基本上都要支持；但是先只考虑C/C++；
- 从支持的RISC-V开发板来说：愿景是需要集成很多不同的开发板。

### 参考产品

市面上还是有不少类似的产品，从应用场景角度，可以参考嵌入式开发IDE（RISC-V/ARM Embeded IDE相关均可）。

基于Eclipse开发的产品：

- [Eclipse IDE for Embedded C/C++ Developers](https://www.eclipse.org/downloads/packages/release/2024-09/r/eclipse-ide-embedded-cc-developers) ：与嵌入式C/C++开发相关，且目前已经有了一些RISC-V交叉构建的插件和调试插件，比如 sifive hifive1。
- [Nuclei Studio IDE ](https://www.nucleisys.com/download.php)：芯来科技（专业RISC-V CPU IP及解决方案供应商）基于 Eclipse 开发的开源的 IDE 产品，主要集成了自研的 RISC-V芯片和SDK。
- ~~[SiFive Freedom Studio RISC-V IDE ](https://github.com/sifive/freedom-studio)：下载链接目前直接导向注册登陆，登陆后进入线上Core Designs。~~

其它场景类似的产品：

- PlatformIO ： 一个开源的物联网开发生态系统，支持多种架构，包括 RISC-V。
- IAR Embedded Workbench for RISC-V ：IAR 提供的专业级 IDE，支持 RISC-V 微控制器。商业软件，提供有限时间试用版。

### 预计任务

需要逐步的搞清楚如下的事情：

* 产品调研：[Eclipse IDE for Embedded C/C++ Developers](https://www.eclipse.org/downloads/packages/release/2024-09/r/eclipse-ide-embedded-cc-developers) 如何使用，如何开发实现的？源码（插件源码）是否开源？许可协议？是否可以二次开发且再开发的软件是否可以商用？
* 插件开发：

  * Eclipse插件是怎么开发的？选择什么Eclipse Package版本？
  * Eclipse都有哪些插件，达成项目目标需要哪些插件？有哪些开源插件可以复用？
* 目标插件开发：

  * 基于[Eclipse IDE for Embedded C/C++ Developers](https://www.eclipse.org/downloads/packages/release/2024-09/r/eclipse-ide-embedded-cc-developers) 进行二次开发，扩展增加一个RISC-V开发板的支持怎么做？
  * 嵌入式开发怎么开发的（不依赖IDE的开发流程）？如何将这个流程集成到 Eclipse中？
  * 编译、设备连接、远程发送运行指令在RISC-V上运行，这些功能是如何定义、实现和相互调用贯穿起来的？
  * 开发环境怎么搭建：

    * 作为目标插件开发的开发工具的Eclipse Version 及 Java 版本的选择；
    * CDT 插件及版本
    * Embedded 插件及版本
* Eclipse定制化打包：如何定制二次开发后的Eclipse IDE，自定义自己想要的LOGO、命令、启动过程、菜单、welcome页面等，并打包输出成自定义产品？（类似[Nuclei Studio IDE ](https://www.nucleisys.com/download.php)的产品化）
