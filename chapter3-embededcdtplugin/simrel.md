## Eclipse SimRel

### 参考

* **https://projects.eclipse.org/projects/technology.simrel**

  * https://projects.eclipse.org/proposals/eclipse-simrel
* **https://github.com/orgs/eclipse-simrel/**

  * Eclipse IDE 同时发布版：https://github.com/eclipse-simrel/.github/blob/main/wiki/Simultaneous_Release.md
  * Eclipse IDE 规划委员会：https://github.com/eclipse-simrel/.github/blob/main/wiki/Planning_Council.md
* [Overview of the Simultaneous Release Process](https://github.com/eclipse-simrel/.github/blob/main/wiki/SimRel/Overview.md) for projects
* [同步发布概述](https://github.com/eclipse-simrel/.github/blob/main/wiki/SimRel/Overview.md)
* [项目流程](https://github.com/eclipse-simrel/.github/blob/main/wiki/SimRel/Overview.md)
* https://wiki.eclipse.org/SimRel/Overview ？？



### 简介

Eclipse SimRel（Simultaneous Release）是Eclipse基金会的一个项目，它聚集了多个开源项目，以实现同时发布。这些项目涵盖了从云和边缘应用程序、物联网（IoT）、人工智能（AI）、汽车、系统工程、开放处理器设计等多个领域。Eclipse基金会是Eclipse IDE、Jakarta EE以及数百个开源项目的家园，这些项目包括运行时、工具、规范和框架等。

具体包含哪些项目，可以参考Eclipse基金会的官方网站，那里列出了所有参与SimRel的项目。由于项目列表经常更新，建议直接访问Eclipse基金会的官方网站或相关文档页面，以获取最新和最准确的信息。您可以通过Eclipsepedia的SimRel/Overview页面找到更多详细信息和历史数据。

请注意，由于项目数量众多且涉及多个领域，建议根据您的具体兴趣或需求来筛选和查看相关的项目。

Eclipse SimRel（Simultaneous Release）的发布周期是每年一次。从Eclipse基金会的官方网站和相关博客中可以了解到，Eclipse的版本发布经历了一次调整，由原来的一年发布三次调整为一年发布四次，这意味着每年会有一个主要版本和三个升级版本。每个季度（大约每三个月）会发布一次版本升级。

这种发布节奏有助于保持项目的活跃和更新，同时也确保了参与SimRel的各个项目能够保持同步和兼容。由于Eclipsepedia的SimRel/Simultaneous Release Cycle FAQ页面目前处于只读状态，建议访问Eclipse基金会的官方网站或相关GitHub页面以获取最新的发布信息和细节。

在软件发布过程中，特别是对于开源项目，“SimRel"通常指的是"Simultaneous Release”，这是Eclipse基金会采用的一种发布方式。Eclipse的Simultaneous Release允许多个项目同时发布，确保它们之间的兼容性。以下是关于“Clone SimRel”步骤的一般解释：

1. **什么是SimRel？**
   * SimRel是Eclipse社区用于协调多个项目同时发布的一个术语。它确保所有参与的项目在相同的版本号下工作，这样可以减少兼容性问题，并允许用户更容易地采用新版本。
2. **为什么要在准备发布之前克隆SimRel？**
   * 克隆SimRel通常是为了确保你的项目与Eclipse的当前发布版本兼容。这涉及到以下几个步骤：
     * **同步更新** ：通过克隆SimRel，你可以确保你的项目与Eclipse的最新版本保持同步，包括依赖项和API。
     * **兼容性测试** ：在发布前，确保你的插件或项目与Eclipse的SimRel版本兼容是非常重要的。这有助于避免在最终用户那里出现兼容性问题。
     * **文档和元数据** ：克隆SimRel还允许你访问相关的文档和元数据，这些对于正确地打包和发布你的项目是必要的。
3. **整体逻辑：**
   * 准备发布软件时，确保你的产品与它所依赖的平台或框架兼容是非常重要的。在Eclipse生态系统中，这意味着要与SimRel保持一致。克隆SimRel是确保这种兼容性的第一步，之后通常还会有构建、测试和文档更新等步骤。

在 https://github.com/eclipse-embed-cdt/eclipse-plugins/blob/develop/README-MAINTAINER.md 中，准备发布的工作流程中指出需要 Clone SimRel 。


### 过程

Eclipse Simultaneous Release 过程的工作原理如下：

* [simrel.aggr](https://github.com/eclipse-simrel/simrel.build/blob/main/simrel.aggr) 模型精确地指定要聚合的内容。
* [simrel.build change-requests](https://ci.eclipse.org/simrel/job/simrel.build/view/change-requests/) 作业在将更改提交到主分支之前验证对 simrel.aggr 模型的每个拉取请求。
* [simrel.build 主](https://ci.eclipse.org/simrel/job/simrel.build/)作业将当前 simrel.aggr 模型在 main 分支上的每个成功聚合构建提升到适当的当前[暂存](https://download.eclipse.org/staging/)子目录，以生成 SimRel p2 暂存存储库。
* [Eclipse Packaging Product 的 CI 作业](https://ci.eclipse.org/packaging/)使用 SimRel p2 Repository 作为输入生成 [EPP p2 Repository](https://download.eclipse.org/technology/epp/staging/repository/) 和相应的 [EPP 产品](https://download.eclipse.org/technology/epp/staging/)。
* 各种 [Releng 作业](https://ci.eclipse.org/simrel/view/Releng%20jobs/)会定期将暂存存储库提升到更永久的位置。
