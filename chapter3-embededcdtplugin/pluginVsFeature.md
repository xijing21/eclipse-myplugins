## Feature 与 Plugin 区别与联系

请参考：https://blog.csdn.net/m0_47406832/article/details/130606046

> plugin-in project 和 feature project 分别是什么？有那些相同点和不同点。分别用在什么样的场景中，解决怎么样的需求？

eclipse plugin-in project 和 feature project 都是用来构建eclipse插件的。

### 不同点:

* plugin-in project 是 lowest-level 的插件,主要实现特定功能。
* feature project 包含多个 plugin-in project ,代表一组相关功能。

### 相同点:

* 都是基于OSGi框架构建的。
* 都可以包含java代码,xml配置文件。

### 使用场景:

* 当你需要实现一个独立功能时,可以使用plugin-in project。比如实现一个简单的代码编辑器插件。
* 当你需要实现一组相关功能时,可以使用feature project。比如实现一个包括UML编辑器、代码生成器等多种功能的UML工具插件。
* 通过plugin-in project实现基本功能,将相关 plugin-in 通过feature project 整合到一起,提供完整的功能集合。

### 小节:

* plugin-in project 适合实现独立功能
* feature project 适合整合相关 plugin-in ,提供一个完整的功能集。

## plugin-in project 何如整合为 feature project ?

将多个plugin-in project整合为一个feature project主要有以下步骤:

1. 创建feature project。右击项目→New →Feature Project。
2. 定义feature.xml文件。指定feature id和name,用来定义该feature提供的功能。

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <feature
         id="com.mycompany.myfeature"
         label="My Feature" 
         version="1.0.0" 
         provider-name="MyCompany">
   </feature>

   ```
3. 在feature.xml中include对应的plugin-in projects。

   ```xml
   <plugin 
        id="com.mycompany.plugin1" 
        download-size="500"
        install-size="200" 
        version="1.0.0"/>

   <plugin 
        id="com.mycompany.plugin2"  
        download-size="1000"
        install-size="500"
        version="1.0.0"/>

   ```
4. 利用Eclipse Plugin Dependency Analysis Tool(PDE Dependencies)检查依赖关系。确保所有依赖都被 resolver。
5. 编译(Build) feature project,生成feature.jar,包含所有包含的plugin-in项目。
6. 发布feature.jar,用户就可以通过安装该feature来获得所有相关的功能。
7. 主要就是通过在feature项目的feature.xml中包含多个plugin-in的id,并指定版本号,从而将它们整合到一个feature中。
8. 创建feature.jar后,就可以作为一个整体发布和安装。



在Eclipse中，`features`对于插件功能的影响主要体现在它们能够将多个相关的插件（plugin-in projects）组合成一个完整的功能集合。具体来说，`feature project`包含了多个 `plugin-in project`，每个 `plugin-in project`实现特定的功能。通过这种方式，`feature project`允许开发者将相关的插件整合在一起，提供一个更为全面和模块化的功能集。

例如，如果要实现一个UML工具插件，可以创建多个 `plugin-in projects`，分别实现UML图的查看和编辑功能、类图功能、时序图功能等。然后，通过一个 `feature project`将这些插件整合在一起，提供一个完整的UML图建模功能。这样，用户就可以通过安装这个 `feature project`来获得一整套相关的功能，而无需分别安装每个独立的插件。

总的来说，`features`通过提供一种组织和管理插件的方式，使得插件的功能更加模块化和易于管理。它们能够将多个相关的插件组合成一个完整的功能集合，使用户能够更方便地获取和安装一系列相关的功能.
