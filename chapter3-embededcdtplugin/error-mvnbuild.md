## 构建与错误

### Error1：

```shell
[ERROR] Cannot resolve target definition:
[ERROR]   Software being installed: org.eclipse.cdt.feature.group 10.0.0.202009071455
[ERROR]   Missing requirement: org.eclipse.cdt.gdb 7.1.0.202008310002 requires 'osgi.ee; (&(osgi.ee=JavaSE)(version=11))' but it could not be found
[ERROR]   Cannot satisfy dependency: org.eclipse.cdt.feature.group 10.0.0.202009071455 depends on: org.eclipse.equinox.p2.iu; org.eclipse.cdt.gdb.feature.group [10.0.0.202008310002,10.0.0.202008310002]
[ERROR]   Cannot satisfy dependency: org.eclipse.cdt.gdb.feature.group 10.0.0.202008310002 depends on: org.eclipse.equinox.p2.iu; org.eclipse.cdt.gdb [7.1.0.202008310002,7.1.0.202008310002]
[ERROR] 
[ERROR] Failed to resolve target definition /home/phebe/eclipse-build/trybuild/eclipse-plugins.git/target-platform/org.eclipse.embedcdt.target-platform.target: See log for details -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MavenExecutionException

```

java版本不对，检查java版本，通过设置环境变量解决。


### Error2: Could not read feature descriptor

执行 `mvn clean verify` 会报错，为了更详细的了解原因，执行：

`mvn clean verify -X` 输出调试信息：

```
[ERROR] Failed to execute goal org.eclipse.tycho:tycho-packaging-plugin:1.7.0:package-feature (default-package-feature) on project org.eclipse.embedcdt: Execution default-package-feature of goal org.eclipse.tycho:tycho-packaging-plugin:1.7.0:package-feature failed: Could not read feature descriptor at /home/phebe/.m2/repository/org/eclipse/license/org.eclipse.license/2.0.2-SNAPSHOT/org.eclipse.license-2.0.2-SNAPSHOT.jar -> [Help 1]
org.apache.maven.lifecycle.LifecycleExecutionException: Failed to execute goal org.eclipse.tycho:tycho-packaging-plugin:1.7.0:package-feature (default-package-feature) on project org.eclipse.embedcdt: Execution default-package-feature of goal org.eclipse.tycho:tycho-packaging-plugin:1.7.0:package-feature failed: Could not read feature descriptor at /home/phebe/.m2/repository/org/eclipse/license/org.eclipse.license/2.0.2-SNAPSHOT/org.eclipse.license-2.0.2-SNAPSHOT.jar
```

在我的环境中，是因为缺少了 /home/phebe/.m2/repository/org/eclipse/license/org.eclipse.license/2.0.2-SNAPSHOT/org.eclipse.license-2.0.2-SNAPSHOT.jar 文件，在网上找了近似的 [jar包](https://eclipse.c3sl.ufpr.br/cbi/updates/license/2.0.2-SNAPSHOT/features/) ，完全与ERROR信息中提示的路径和文件名保持一致补充缺失的依赖（找不到完全一样的jar包，用近似版本改名后替代）。

人为填补上述依赖缺失后，再次构建则通过了。

### Error3：One of setGitDir or setWorkTree must be called

在 Eclispe IDE 中执行 Maven Build 报错：

```
Failed to execute goal org.eclipse.tycho:tycho-packaging-plugin:1.7.0:package-plugin (default-package-plugin)  on project  org.eclipse.embedcdt :
Execution default-package-plugin of goal org.eclipse.tycho:tycho-packaging-plugin:1.7.0:package-plugin failed: One of setGitDir or setWorkTree must be called.  ->  [Help 1]
```

解决问题：
When you build a project through gradle, and get the error message One of setGitDir or setWorkTree must be called, that normally means, no git metadata was found for a project that already had git set up. This could be that you downloaded the project as a .zip. To fix it just clone the project either through the GUI or git bash like below:

```
git clone your-project-url
```
