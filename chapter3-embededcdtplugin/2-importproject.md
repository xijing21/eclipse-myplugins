https://help.eclipse.org/latest/index.jsp?nav=%2F4_2_3

https://help.eclipse.org/latest/index.jsp?topic=%2Forg.eclipse.pde.doc.user%2Ftasks%2Fapi_tooling_baseline.htm&cp%3D4_2_3_1

API Baseline 向导：https://help.eclipse.org/latest/index.jsp?topic=%2Forg.eclipse.pde.doc.user%2Freference%2Fapi-tooling%2Fwizards%2Fref-api-baseline-wizard.htm

兼容性：https://marketplace.eclipse.org/content/eclipse-embedded-cc

方法：下载与RCP同版本的eclipse-embedded版本，在软件市场中搜索并查询 riscv，检索到eclipse-embedded 的插件版本为6.6.1，并查看更多的插件信息。

https://eclipse-embed-cdt.github.io/feed.xml

## 导入embeded-cdt-plugin工程和插件

### 导入工程

### 导入插件

### MAINFEST.MF

以下是对 `MANIFEST.MF`文件中各个头的详细解释：

- **Manifest-Version**: 1.0
  - 标准的JAR文件清单版本。
- **Bundle-ManifestVersion**: 2
  - 表示这个清单文件遵循的OSGi框架规范的版本号。
- **Bundle-Name**: %bundle.name
  - 插件的名称，`%bundle.name`是一个占位符，将在构建过程中替换为实际的插件名称。
- **Bundle-SymbolicName**: org.eclipse.embedcdt.core;singleton:=true
  - 插件的唯一标识符，格式通常是反向域名。`singleton:=true`表示这个插件在OSGi框架中只能有一个实例。
- **Bundle-Version**: 6.6.1.qualifier
  - 插件的版本号，`qualifier`是一个占位符，通常用于构建时的版本后缀。
- **Bundle-Activator**: org.eclipse.embedcdt.internal.core.Activator
  - 指定负责在插件启动和停止时执行特定代码的类。
- **Bundle-RequiredExecutionEnvironment**: JavaSE-11
  - 指定插件运行所需的Java执行环境版本。
- **Bundle-ActivationPolicy**: lazy
  - 指定插件的激活策略，`lazy`表示插件只有在需要时才会被激活。
- **Bundle-Vendor**: %bundle.vendor
  - 插件的供应商，`%bundle.vendor`是一个占位符，将在构建过程中替换为实际的供应商名称。
- **Bundle-Localization**: plugin
  - 指定插件本地化的策略，这里表示本地化属性文件位于插件的根目录。
- **Export-Package**: org.eclipse.embedcdt.core, org.eclipse.embedcdt.core.liqp;
  - 这定义了插件导出的包，其他插件可以通过导入这些包来使用它们。
- **x-friends**:="org.eclipse.embedcdt,... (此处省略若干行)
  - 这是一个自定义指令，它允许列出的插件访问导出的包，即使它们没有明确导入这些包。这对于插件之间的特殊依赖关系很有用。
- **Require-Bundle**: org.eclipse.cdt.core;bundle-version="7.0.0",...
  - 这指定了插件运行所依赖的其他插件列表，以及它们的最小版本号。这表示当前插件需要这些指定的插件才能正常工作。
- **Bundle-ClassPath**: lib/antlr-runtime-3.5.2.jar,...
  - 定义了插件类路径中的JAR文件和目录列表。这些资源将被包含在插件的类加载器中。
- **Automatic-Module-Name**: org.eclipse.embedcdt.core
  - 这是Java 9及以上版本引入的概念，用于为插件提供一个稳定的模块名称，以便在模块路径上使用。

以下是具体作用：

- **Export-Package**: 允许其他插件访问和依赖当前插件提供的公共API。这是插件间代码共享的关键机制。
- **x-friends**: 提供了一种方式，允许某些插件访问另一个插件导出的包，即使它们不是通过常规的导入机制声明依赖关系。
- **Require-Bundle**: 声明当前插件依赖的其他插件。这是确保插件在运行时可以找到并使用所需功能的方式。
- **Bundle-ClassPath**: 定义了插件运行时需要加载的类和资源。这包括插件自身的代码以及其他可能的外部JAR文件。
- **Automatic-Module-Name**: 对于在Java模块化环境中运行的插件，这提供了插件模块的稳定名称，以便其他模块可以明确地引用它。

### Errors

![1730104251977](image/1730104251977.png)

在这个页面中下载历史版本：https://github.com/eclipse-cdt/cdt/blob/main/Downloads.md

org.eclipse.cdt.core (7.0.0) ：

org.eclipse.cdt.debug.core (8.5.0)

org.eclipse.cdt.managedbuilder.core (9.0.0)

备份：

```
Require-Bundle: org.eclipse.cdt.core;bundle-version="7.0.0",
 org.eclipse.cdt.debug.core;bundle-version="8.5.0",
 org.eclipse.cdt.managedbuilder.core;bundle-version="9.0.0",
 org.eclipse.core.runtime;bundle-version="3.19.0",
 org.eclipse.core.variables;bundle-version="3.4.800",
 org.eclipse.debug.core;bundle-version="3.16.0",
 org.eclipse.core.expressions;bundle-version="3.7.0"
Bundle-ClassPath: lib/antlr-runtime-3.5.2.jar,
 lib/jackson-annotations-2.9.9.jar,
 lib/jackson-core-2.9.9.jar,
 lib/jackson-databind-2.9.9.3.jar,
 lib/ST4-4.0.8.jar,
 lib/json-simple-1.1.1.jar,
 lib/org.jsoup_1.7.2.v201411291515.jar,
 .
Automatic-Module-Name: org.eclipse.embedcdt.core
```

为什么cdt版本是9.2.1；这里的插件还依赖多个不同的版本？

1. 我是需要按照这个配置的描述版本准备对应的依赖包? 准备了包又如何配置使用呢？

   > - 可以通过Eclipse的 `Install New Software...`功能来安装特定版本的插件。
   > - 使用Maven或Tycho，你需要在 `pom.xml`或构建配置中指定正确的依赖版本，然后构建系统会自动下载并配置它们。
   >
2. 还是修改配置文件的版本为cdt的版本9.2.1 ?

在eclipse202409R+CDT9.2.1插件安装的基础上，导入embeded-plugin的工程后，依赖报错（版本不匹配）。通过详细比对，CDT9.2.1中的

org.eclipse.cdt.core (7.0.0) ：

org.eclipse.cdt.debug.core (8.5.0)

org.eclipse.cdt.managedbuilder.core (9.0.0)

版本对不上。为了弄清楚上述的这些依赖指定的版本具体在哪里，我下载了多个CDT版本，并逐一比对后发现CDT10.0.0下的版本与上述要求是匹配的。

通过Eclipse的 `Install New Software...`功能安装特定CDT10.0.0的插件（这里其实就意味着eclipse环境下有两个版本的CDT了？——》事后补充：事实上安装插件的时候根本不会按照版本安装，多次试验发现版本都被部分调整了），安装的时候注意修改选项：

![1730172121355](image/1730172121355.png)

![1730172078125](image/1730172078125.png)

![1730171813250](image/1730171813250.png)

![1730172226440](image/1730172226440.png)

![1730172295666](image/1730172295666.png)

![1730172374057](image/1730172374057.png)

重新选择eclipse的plugin文件夹，而不是cdt包；

![1730172425854](image/1730172425854.png)

设置后问题依然没解决，所谓不行，问题不在于这里。

回到eclipse的工具根目录，plugin目录下的包，没有按照我预期的希望安装之前报错的包版本：
这里不对。

![1730172782617](image/1730172782617.png)

![1730173097097](image/1730173097097.png)

![1730173152967](image/1730173152967.png)

![1730173195670](image/1730173195670.png)

org.eclipse.cdt.core;bundle-version="[6.2.0,7.0.0]",
 org.eclipse.cdt.debug.core;bundle-version="[8.1.0,8.5.0]",
 org.eclipse.cdt.managedbuilder.core;bundle-version="[8.4.0,9.0.0]",

![1730193810727](image/1730193810727.png)

https://archive.eclipse.org/tools/cdt/releases/10.0/

---

转换思路：插件单独搭建cdt10.0.0

1. 下载并解压eclipse202409R
2. 安装cdt 10.0.0:  https://download.eclipse.org/tools/cdt/releases/10.0

   ![1730256837455](image/1730256837455.png)

   输入url后发现默认安装的是10.0.1 ，检查包版本与依赖定义的版本是否一致：

   ![1730260747444](image/1730260747444.png)

   ![1730260800724](image/1730260800724.png)

   ![1730260849345](image/1730260849345.png)

为了保持版本一致，退回重新执行，p2 链接地址明确到10.0.0  : https://archive.eclipse.org/tools/cdt/releases/10.0/cdt-10.0.0/

![1730261096255](image/1730261096255.png)

![1730270611129](image/1730270611129.png)

比对了一下，似乎自动调整成了 10.0.1 版本。

还是直接指定下载到本地的10.0.0的本地cdt包文件夹进行安装。

![1730270857009](image/1730270857009.png)

![1730272144028](image/1730272144028.png)

我选的本地文件目录，为什么列表中依然会出现版本不对应的情况呢？  ——》本地目录最后安装的版本很新，疑似自动更新到最新版本。

Show only the latest versions ofavailable software
Group items by category

Show only software applicable to target environment
Contact all update sites during install to find required software

Hide items that are already installed

https://archive.eclipse.org/tools/cdt/releases/10.0/cdt-10.0.0/  + 去掉所有的复选框：依然是安装了cdt 11.6.1版本.

**改成先导入插件，然后再安装cdt依赖，这里选项这么设置的：**

![1730278296837](image/1730278296837.png)

后面弹出信任窗口的时候，全选——信任。（很多包的版本是11.6.x，但是cdt主要的还是10.0.）

安装重启后：

![1730298519112](image/1730298519112.png)

An API baseline has not been set for the current workspace.

这个问题是需要设置下 API baseline：https://help.eclipse.org/latest/index.jsp?topic=%2Forg.eclipse.pde.doc.user%2Ftasks%2Fapi_tooling_baseline.htm

设置方法：https://help.eclipse.org/latest/index.jsp?topic=%2Forg.eclipse.pde.doc.user%2Ftasks%2Fapi_tooling_baseline.htm

Location：API 基线的位置是 Eclipse SDK 安装的路径，通常是安装的“ *plugins* ”文件夹的路径。

建议的修复方法：https://help.eclipse.org/latest/index.jsp?topic=%2Forg.eclipse.pde.doc.user%2Ftasks%2Fapi_tooling_baseline.htm

> 用这种方式解决问题其实与直接**Windows** -> **Preferences** -> **Plug-in Development** -> **API Baselines**  一样![1730299088406](image/1730299088406.png)

这里设置为当前的eclipse根目录下的plugin（eclipse 202409R+cdt 10.0.0）；

![1730299255259](image/1730299255259.png)

值得高兴的是，所有的包依赖错误都没有了。但是还有一个错误：There is a possible API baseline mismatch since none of the workspace projects is in the baseline.

我已经很多次遇到这个问题了。不设置基线报错，设置完成后依然报不匹配。

![1730300117664](image/1730300117664.png)

仔细看了下，版本不对，比10.0.0的要高。改成下载下来的cdt10.0.0目录试试看：

![1730300234298](image/1730300234298.png)

project——》clean。完成后，错误依然不变：There is a possible API baseline mismatch since none of the workspace projects is in the baseline.

[这里](https://stackoverflow.com/questions/29473967/eclipse-gives-an-api-baseline-has-not-been-set-for-the-current-work-space-er)有人没有设置基线，忽略基线的错误。如果实在解决不了，我也只能这样了：

**Windows** -> **Preferences** -> **Plug-in Development** -> **API Baselines**

Under **Options** find **Missing API baseline** -> If **Error** is selected change it to **Warning** or **Ignore** ->  **Apply** .

![1730300417701](image/1730300417701.png)

放弃解决dismatch的问题了，现在就设置选项，反正不要报Error就行。先跳过这个错误看是否能够正常运行使用。

![1730300492117](image/1730300492117.png)

现在至少看起来是没错误了。找一个看起来比较能体现embededcdt的插件功能界面的插件运行下试试看：

![1730300725913](image/1730300725913.png)

![1730300669464](image/1730300669464.png)

备忘：

eclipse：/home/phebe/eclipse-tools/eRCP202409R-CDT10.0.0-one/eclipse

ws：eRCP202409R-embed-cdt10.0.0-plugins-1

总结：

1. eclipese版本：202409R
2. eclipse安装的cdt插件版本：这里一定要搞清楚
   1. https://github.com/eclipse-embed-cdt/eclipse-plugins  ：cdt 9.2.1
   2. https://github.com/eclipse-embed-cdt/eclipse-plugins/tree/master/plugins 目录下的若干个插件工程/包： cdt 10.0.0

      这里还有没有搞清楚的：
   3. 通过 Eclipse Markerplace 安装插件，没找到如何选择非最新版本。怎么看都只能安装最新版本插件
   4. 通过 Install New Software 安装插件，选择下载到本地的cdt 10.0.0版本（其它版本同），似乎无效，都会自动更新很多软件包版本（通过对比，安装过程中的部分包信息版本比下载的高）；使用p2网址，也存在同样的问题。而且不管怎么设置过程中的选项似乎都不是很能达到效果。最后的操作方式是：先导入所有的eclipse-plugins/plugins 下的包，然后选项按照这个设置的：

      ![1730278296837](image/1730278296837.png)
3. API baseline：理论上应该是eclipse根下的plugins目录；但是换成cdt 10.0.0 也同样报mismatch。没有一个合理的能够让其不报错的版本。
   1. API Baseline 设置操作没问题，但是设置什么样的版本才能不报 mismatch 的错误呢？
   2. 不设置baseline 对项目又有什么影响呢？
