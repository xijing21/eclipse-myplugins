## 摸底项目下的图片情况，从图片样子看哪些图片需要替换

### 搜索图片

从图片名搜索源码，确定修改项目的位置

1. 查询所有的图片（还得加上.svg格式）

```
    find . -type f \( -name ".xpm" -o -name ".png" -o -name ".jpg" -o -name ".bmp" \) -exec cp {} /mnt/hgfs/vm-share/package-img/eclipse \;
    #find . -type f \(  -name "*.bmp" \) -exec cp {} /mnt/hgfs/vm-share/package-img/eclipse \;
    对照缩略图查看有eclipse明显标识的图片，拷贝到 /mnt/hgfs/vm-share/package-img/eclipse-yuantu-youyong ；观察文件名：eclipse 、icon、splash
```

2. 将上述图片名称、路径导出，对照1中的图片看2中的路径，方便查找图片位置和执行替换

   ```
   find . -type f \( -name ".xpm" -o -name ".png" -o -name ".jpg" -o -name ".bmp" \) >> /mnt/hgfs/vm-share/package-img/eclipse-images.txt
   ```
3. eclipse-images.txt中，删除所有路径中带：product/target/products  （这些是构建生成的包中的，不是源码中的图片）

   [源码中需要考虑替换的图片列表](/packaging/images.log)

   特别注意的有：

   - ./icons/icon.xpm  256*256px

     - 同目录下还有其它2个图片：

       - [X] icon.xpm	     256*256px 透明底  ：替换图标
       - [X] *eclipse.ico    256*256px  透明底 ：添加ruyisdk.ico，还需要在代码中找到对应位置并修改文件名
       - [ ] Eclipse.icns  512*512 px  白底  :.icns是苹果操作系统中用于图标的一种文件格式*
   - ./packages/org.eclipse.epp.package.common/splash.bmp

     - [X] splash.bmp   452*302px ：替换图片
   - 以下基本上每个包中都有重复的图片文件：(参考/mnt/hgfs/vm-share/package-img/eclipse-yuantu-youyong)

     - ./packages/org.eclipse.epp.package.{%packagename}/eclipse_lg.png    116*302px
     - ./packages/org.eclipse.epp.package.{%packagename}rcp/eclipse_lg@2x.png   232*604px
     - ~~./packages/org.eclipse.epp.package.{%packagename}rcp/epp32.png~~
     - 
     - ./packages/org.eclipse.epp.package.{%packagename}rcp/eclipse16.png
     - ./packages/org.eclipse.epp.package.{%packagename}rcp/eclipse16@2x.png
     - ./packages/org.eclipse.epp.package.{%packagename}rcp/eclipse32.png
     - ./packages/org.eclipse.epp.package.{%packagename}rcp/eclipse32@2x.png
     - ./packages/org.eclipse.epp.package.{%packagename}rcp/eclipse48.png
     - ./packages/org.eclipse.epp.package.{%packagename}rcp/eclipse48@2x.png
     - ./packages/org.eclipse.epp.package.{%packagename}rcp/eclipse256.png
     - ./packages/org.eclipse.epp.package.{%packagename}rcp/eclipse256@2x.png

       > 汇总整理到 /mnt/hgfs/vm-share/new-ruyiide-imgs/imgsV1.0/useful
       >

       拷贝/mnt/hgfs/vm-share/new-ruyiide-imgs/imgsV1.0/useful  下的图片到如下路径：

       - [X] org.eclipse.epp.package.embedcpp
       - [ ] org.eclipse.epp.package.rcp
       - [ ] org.eclipse.epp.package.committers
       - [ ] org.eclipse.epp.package.common
       - [ ] org.eclipse.epp.package.cpp
       - [ ] org.eclipse.epp.package.dsl
       - [ ] org.eclipse.epp.package.java
       - [ ] org.eclipse.epp.package.jee
       - [ ] org.eclipse.epp.package.modeling
       - [ ] org.eclipse.epp.package.php
       - [ ] org.eclipse.epp.package.scout
4. 替换图片：

   * ~/eclipse-build/packaging/packages/packages/org.eclipse.epp.package.common/splash.bmp
   * ~/eclipse-build/packaging/packages/icons/icon.xpm

### 搜索文件内容

上面的命名为eclipse* 的文件，都计划替换成ruyisdk*。

- 查询文件内容包含"eclipse*.png"的文件：
  ```
  grep -R "eclipse.png" /path/to/search
  grep -R "eclipse.*\.png" /path/to/search
  grep -R --include="*.java" "eclipse.*\.png" /path/to/search
  grep -R --include="*.java" --include="*.xml" --include="*.html" "eclipse.*\.png" /path/to/search

  ```

执行：

```
cd /home/phebe/eclipse-build/packaging/packages
grep -R -I --exclude-dir=target  "eclipse.*\.png" . >> /mnt/hgfs/vm-share/pngpath1.txt   # -I 可以忽略二进制；
```

或者利用脚本对日志进行数据过滤：

```
# Python代码示例
# 假设日志文件名为 'log.txt'

# 读取文件
with open('log.txt', 'r') as file:
    lines = file.readlines()

# 过滤并删除包含特定字符的行
filtered_lines = [line for line in lines if '.product/target/products' not in line]

# 写入新文件
with open('cleaned_log.txt', 'w') as file:
    file.writelines(filtered_lines)

```

目前扫描出来的结果详见：[包含eclipse*.png 的文件](imgpath.log)  过滤后 [非target下包含eclipse*.png 的文件](images.log)

针对主要关注对象先看看：
./packages/org.eclipse.epp.package.embedcpp/plugin.xml:               value="eclipse_lg.png">
./packages/org.eclipse.epp.package.embedcpp/plugin.xml:               value="eclipse16.png,eclipse32.png,eclipse48.png,eclipse256.png">
./packages/org.eclipse.epp.package.embedcpp/plugin.xml:            icon="platform:/plugin/org.eclipse.ui.intro.universal/themes/solstice/graphics/icons/ctool/start-cheatsheet.png"
./packages/org.eclipse.epp.package.embedcpp/plugin.xml:            icon="platform:/plugin/org.eclipse.ui.intro.universal/themes/solstice/graphics/icons/ctool/egit-checkout.png"
./packages/org.eclipse.epp.package.embedcpp/plugin.xml:            icon="platform:/plugin/org.eclipse.ui.intro.universal/themes/solstice/graphics/icons/ctool/import-existing-project.png"
./packages/org.eclipse.epp.package.embedcpp/plugin.xml:            icon="platform:/plugin/org.eclipse.ui.intro.universal/themes/solstice/graphics/icons/ctool/open-file.png"
./packages/org.eclipse.epp.package.embedcpp/plugin.xml:            icon="platform:/plugin/org.eclipse.ui.intro.universal/themes/solstice/graphics/icons/ctool/settings.png"
./packages/org.eclipse.epp.package.embedcpp/plugin.xml:            icon="platform:/plugin/org.eclipse.ui.intro.universal/themes/solstice/graphics/icons/ctool/new-project.png"
./packages/org.eclipse.epp.package.embedcpp/plugin.xml:            icon="platform:/plugin/org.eclipse.epp.mpc.ui/intro/css/marketplace.png">
./packages/org.eclipse.epp.package.embedcpp/build.properties:               eclipse16.png,
./packages/org.eclipse.epp.package.embedcpp/build.properties:               eclipse16@2x.png,
./packages/org.eclipse.epp.package.embedcpp/build.properties:               eclipse32.png,
./packages/org.eclipse.epp.package.embedcpp/build.properties:               eclipse32@2x.png,
./packages/org.eclipse.epp.package.embedcpp/build.properties:               eclipse48.png,
./packages/org.eclipse.epp.package.embedcpp/build.properties:               eclipse48@2x.png,
./packages/org.eclipse.epp.package.embedcpp/build.properties:               eclipse256.png,
./packages/org.eclipse.epp.package.embedcpp/build.properties:               eclipse256@2x.png,
./packages/org.eclipse.epp.package.embedcpp/build.properties:               eclipse_lg.png,
./packages/org.eclipse.epp.package.embedcpp/build.properties:               eclipse_lg@2x.png,
./packages/org.eclipse.epp.package.embedcpp/eclipse32.svg:   inkscape:export-filename="/Users/d021678/git/org.eclipse.epp.packages/packages/org.eclipse.epp.package.java/eclipse32.png"
./packages/org.eclipse.epp.package.embedcpp/eclipse48.svg:   inkscape:export-filename="/Users/d021678/git/org.eclipse.epp.packages/packages/org.eclipse.epp.package.java/eclipse48@2x.png"
./packages/org.eclipse.epp.package.embedcpp/about.ini:windowImage=eclipse16.png
./packages/org.eclipse.epp.package.embedcpp/about.ini:aboutImage=eclipse_lg.png
./packages/org.eclipse.epp.package.embedcpp.product/epp.product:      `<image path="/org.eclipse.epp.package.embedcpp/eclipse_lg.png"/>`
./packages/org.eclipse.epp.package.embedcpp.product/epp.product:   `<windowImages i16="/org.eclipse.epp.package.embedcpp/eclipse16.png" i32="/org.eclipse.epp.package.embedcpp/eclipse32.png" i48="/org.eclipse.epp.package.embedcpp/eclipse48.png" i256="/org.eclipse.epp.package.embedcpp/eclipse256.png"/>`

## 图片加工工具

> 备忘在线免费的图片工具。

- 在线ps：https://ps.gaoding.com/
  - 启动背景图psd文件：D:\RuyiSDK\eclipse-imgs\splash.psd  导出为bmp格式
- 抠图：佐糖 https://picwish.cn/remove-background
- 改图片大小：https://www.gaitubao.com
- 格式转换：推荐 convert 命令


基于linux 命令的 格式和尺寸转换：

```
# 修改尺寸
convert your-image.png -resize 16x16 icon_16x16.png
convert your-image.png -resize 32x32 icon_32x32.png
convert your-image.png -resize 128x128 icon_128x128.png
convert your-image.png -resize 256x256 icon_256x256.png
convert your-image.png -resize 512x512 icon_512x512.png
convert your-image.png -resize 1024x1024 icon_1024x1024.png

# png转ico
convert ruyisdk256.png -resize 256x256 image.ico
convert image.ico -compress none ruyisdk.ico  #解决图片不能预览问题
```
