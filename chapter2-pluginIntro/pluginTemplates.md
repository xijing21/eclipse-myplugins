## Eclipse Plug-in Templates

```
Custom plug-in wizard
Editor contribution for XML files
Hello, world command
Incremental project builder
Menu contribution using 4.XAPI
Multi-page editor
Property page
RAP e4 Template
RAP Hello world
RAP Mail Template
Sample help content
Textual editor, relying on Generic Editor
Toolbar contribution using 4.xAPI
View contribution using 3.xAPI
View contribution using 4.xAPI
View using browser technology
```

1. Custom Plug-in Wizard

用于创建自定义插件的向导，帮助用户通过一系列步骤轻松生成插件项目的基本结构和必要文件。可以定制化配置项和模板。

2. Editor Contribution for XML Files

提供对 XML 文件的编辑支持的插件，允许用户在 Eclipse 中打开、编辑和验证 XML 文件。通常会实现特定的编辑功能，如语法高亮和代码完成。

3. Hello, World Command

一个简单的示例插件，演示如何创建一个命令并在 Eclipse 中执行。通常包含一个菜单项或按钮，点击后显示“Hello, World”消息。

4. Incremental Project Builder

实现增量构建的插件，允许 Eclipse 在文件更改时只重新构建受影响的部分，而不是整个项目。这可以提高构建效率。

5. Menu Contribution Using 4.XAPI

使用 Eclipse 4.x API 创建自定义菜单项的插件，允许在 Eclipse 界面中添加自定义功能。可以定义菜单的显示位置和行为。

6. Multi-page Editor

支持多页面编辑的插件，允许用户在同一个编辑器中打开多个标签页。适用于需要在多个视图之间切换的复杂编辑任务。

7. Property Page

为特定的项目或资源提供属性页面的插件，允许用户查看和编辑与特定项目或资源相关的设置。这通常在项目资源的上下文菜单中可见。

8. RAP e4 Template

用于 Rapid Application Platform (RAP) 的模板，帮助开发者创建基于 Eclipse 的 web 应用程序，使用 Eclipse 4.x 的架构。

9. RAP Hello World

一个简单的 RAP 示例，演示如何创建一个基本的 web 应用程序。通常包括一个简单的用户界面和基本的功能。

10. RAP Mail Template

为创建基于邮件功能的 RAP 应用程序提供的模板。可以用于构建与电子邮件相关的功能，如发送和接收邮件。

11. Sample Help Content

提供示例帮助内容的插件，通常用于演示如何在 Eclipse 中集成帮助系统。包括帮助文档、示例和导航。

12. Textual Editor, Relying on Generic Editor

一个文本编辑器插件，基于通用编辑器功能。提供基本的文本编辑功能，可以用于多种文本格式。

13. Toolbar Contribution Using 4.XAPI

使用 Eclipse 4.x API 创建自定义工具栏按钮的插件，允许用户在工具栏中添加特定功能的快捷方式。

14. View Contribution Using 3.XAPI

使用 Eclipse 3.x API 创建自定义视图的插件，允许在 Eclipse 界面中添加新的视图，以显示不同类型的信息。

15. View Contribution Using 4.XAPI

使用 Eclipse 4.x API 创建自定义视图的插件，类似于 3.x API 版本，但利用了更现代的架构和功能。

16. View Using Browser Technology

使用浏览器技术（如 HTML、JavaScript 和 CSS）创建的视图插件，允许在 Eclipse 中显示 web 内容或应用程序界面，适用于集成 web 技术的项目。

这些模板和贡献类型为 Eclipse 插件开发提供了丰富的功能和灵活性，帮助开发者实现各种需求。

## New plug-in project with custom templates

### 可用模板及说明

以下是一些可用模板及其扩展点的简要说明：

- **`template.browserView.name`** (`org.eclipse.ui.views`): 创建一个基于浏览器的视图，允许显示 web 内容。
- **`Project Builder and Nature`** (`org.eclipse.core.resources.builders`): 定义项目的构建方式和特性。
- **`template.commonNavigator.name`** (`org.eclipse.ui.navigator.commonNavigator`): 创建一个公共导航器视图，显示项目结构。
- **`Icon Decorator`** (`org.eclipse.ui.decorators`): 添加自定义图标装饰，用于在资源视图中标识特定资源。
- **`XML Editor`** (`org.eclipse.ui.editors`): 创建一个用于编辑 XML 文件的编辑器。
- **`Textual editor relying on Generic Editor`** (`org.eclipse.ui.editors`): 基于通用编辑器的文本编辑器。
- **`"Hello world" command contribution`** (`org.eclipse.ui.commands`): 创建一个简单的命令示例，通常用于学习目的。
- **`Help Table of contents`** (`org.eclipse.help.toc`): 定义帮助内容的目录结构。
- **`File import wizard`** (`org.eclipse.ui.importwizards`): 创建用于导入文件的向导。
- **`Multi-page Editor`** (`org.eclipse.ui.editors`): 支持多个页面的编辑器，适合复杂编辑任务。
- **`New File wizard`** (`org.eclipse.ui.newwizards`): 创建新的文件的向导。
- **`Release Engineering Perspective`** (`org.eclipse.ui.perspectives`): 定义新的视角，适合特定的开发任务。
- **`Preference Page`** (`org.eclipse.ui.preferencePages`): 创建用户首选项页面。
- **`Property Page`** (`org.eclipse.ui.propertyPages`): 定义特定资源或项目的属性页面。
- **`Splash Handler`** (`org.eclipse.ui.splashHandlers`): 定义启动时的欢迎界面。
- **`Universal welcome Contribution`** (`org.eclipse.ui.intro.configExtension`): 创建通用的欢迎页面。
- **`Example view extension`** (`org.eclipse.ui.views`): 提供一个示例视图扩展，通常用于学习或参考。

模板选择页面极大地简化了插件开发过程，使开发者能够快速选择所需的功能，避免从头开始构建每个组件。选择合适的模板后，Eclipse 会自动生成相应的代码和配置文件，帮助你更快地开始插件开发。

模板和扩展点在 Eclipse 插件开发中通常是固定搭配，并由模板的创建者定义。这意味着：

1. **固定搭配**: 每个模板都有与之关联的特定扩展点。这个关系是预先定义好的，确保插件能够正确集成到 Eclipse 平台中。
2. **不能修改**: 开发者在选择模板时，不能直接修改模板所关联的扩展点。模板的创建者设定了扩展点，以定义模板的功能和行为。
3. **自定义扩展**: 虽然你不能修改现有模板的扩展点，但你可以在生成的插件基础上进行自定义开发。这包括实现额外的功能、修改现有行为或添加新的扩展点。
