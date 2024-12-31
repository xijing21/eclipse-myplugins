## 课程大纲：从零开始开发 Eclipse 插件与 RuyiSDK IDE插件

### 第一部分：Eclipse 基础

> 目标：
>
> 1. Eclispe 及插件的开源许可证是什么？是否允许基于已有插件进行二次开发。
> 2. 版本基线选择：Eclipse 及 CDT、embeded-cdt 等插件的版本及JVM版本。
> 3. Eclipse 及插件的安装使用。

1. [Eclipse IDE 概述](../chapter1/1.1-introduce.md)

   * Eclipse 简介：开源、许可证
   * Eclipse的下载与安装
   * Eclipse各种版本与适用场景
   * Eclipse的Java环境：兼容性及Java环境配置
2. [Eclipse 使用基础](../chapter1/1.2-basicUse.md)

   * 工作区、视图与编辑器的基本概念
   * 项目创建与管理
   * 文件导航与编辑
   * 程序的运行/调试
3. [Eclipse IDE 插件查询和安装](../chapter1/1.3-pluginBasics.md)

   * 插件查询
   * 插件安装
4. [Eclipse 社区与资源](../chapter1/1.4-resource.md)

   * 开源项目
   * 贡献代码
   * 技术论坛/问题讨论
   * 书籍、在线课程与教程

### 第二部分：Eclipse 插件开发

> 了解和掌握 Eclipse 插件开发的一些基础操作，什么是 Extension 和 Extention Point ？有哪些 Extension 和 Extention Point，它们是什么怎么用。如何利用它们实现需求？亦或者需要自己开发 Extension，如何实现。

5. Eclipse 插件项目创建和运行

   * 插件开发环境设置：安装 Plugin Development Environment (PDE)
   * 创建第一个插件项目 Hello,World
   * 插件的 Manifest 文件
   * 插件的 plugin.xml 文件
   * 插件的 build.properties 文件
   * 运行插件项目
6. Eclipse 插件架构

   * OSGi 的基本概念
   * 插件与扩展点的关系
   * Eclipse 运行时环境
7. 插件功能实现

   * 开发自定义视图与编辑器
   * 使用 Eclipse API 访问工作区资源
   * 实现菜单和工具栏的自定义功能
8. 调试与测试插件

   * 在 Eclipse 中调试插件
   * 单元测试与集成测试的基本方法

### 第三部分：Eclipse Embeded CDT

> 目前已知 Eclipse Embeded CDT 插件是非常接近目标需求的插件，甚至一些 RISC-V 插件已经有了，它们当前的效果如何，是如何实现的。

   * Eclipse Embeded CDT 源码分析
   * Eclipse Embeded CDT 本地构建

### 第四部分：Eclipse IDE构建打包以定制化
> Eclipse 官网的 Eclipse Embeded CDT 安装包是如何构建打包的？源码工程是哪个？如何构建？
> 如何基于 Eclipse Embeded CDT 源码改造和定制安装包？

9. Eclipse IDE 构建打包

   * 工程
   * 本地构建
  
10. Eclipse IDE 定制化

   * 定制化需求
   * 定制化开发

### 第五部分：RISC-V 开发相关背景
> RISC-V SDK 具体包含哪些内容？不同的开发板，开发环境要解决哪些问题？ IDE 要实现并解决哪些问题？

11. RISC-V 概述

   * RISC-V 发展背景
   * RISC-V 国内软硬件发展现状
   * RISC-V 开发工具现状

12. RISC-V 开发板及SDK调研

   * 厂商 SDK（文档、镜像、编译器等开发有关的资源）现状
   * 厂商 SDK 的改进/完善需求
   * RuyiSDK 建设

### 第六部分：RISC-V 插件功能改造/实现

> 基于 Eclipse RISC-V 开发相关插件的现状和问题，进行功能改进和插件的自定义实现，提高易用性。

13. 资源管理器的开发

   * 创建自定义视图以展示资源
   * 实现资源的增删改查功能

14. 编译器集成

   * 调用外部编译器进行代码编译
   * 处理编译错误与警告

15. 设备连接与通信

   * 通过串口/JTAG 连接 RISC-V 开发板
   * 实现数据的发送和接收

16. 指令发送与结果反馈

   * 在 IDE 中发送指令到开发板
   * 接收并显示运行结果
