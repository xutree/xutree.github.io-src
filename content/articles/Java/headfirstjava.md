Title: Head first Java 笔记
Category: 读书笔记
Date: 2019-09-16 22:30:04
Modified: 2019-09-18 11:10:13
Tags: Java

[TOC]

### 1. 基本概念

- `Java` 源代码编译成字节码，在不同平台上通过 `JVM` 执行字节码
- `System.out.print` 输出在同一行，`System.out.println` 输出会换行

### 2. 类与对象

- 任何变量只要加上 `public`、`static` 和 `final`，基本上都会变成全局取用的常数
- 可以把文件打包成 **.jar**，在其中加入 **manifest** 文件告知哪个文件中带有 `main()` 函数
- 所有的 `Java` 程序都定义在类中
- 面向对象设计不需要改动之前已经测试好的程序代码
- 类是蓝图描述对象如何创建
- 对象本身已知道的事务称为**实例变量**，他代表对象的**状态**
- 对象可执行的动作称为方法，他代表类的**行为**
- `Java` 的程序在执行期是一组会相互交谈的对象

### 3. `primitive` 主数据类型和引用

- 对于任意一个 `Java` 虚拟机来说，所有的引用大小都一样，但不同的虚拟机之间可能会以不同的方式表示引用
- 数组是对象
- `primitive` 主数据类型的值是该值的字节表示
- 引用变量的额值代表位于堆之对象的存取方法

### 4. 方法操作实例变量

- 类所描述的是对象知道什么与执行什么
- `Java` 是值传递，应用对象的值类似于对象的地址
- 将实例变量标记为私有的，并提供公有的 `getter` 和 `setter` 来控制存取动作
- 实例变量永远有默认值，局部变量没有默认值
- 实例变量声明在类内而不是方法中
- 局部变量声明在方法中
- 使用 **==** 来比较两个 `primitive` 主数据类型，或者判断两个引用是否引用同一个对象
- 使用 `equals()` 来判断两个对象是否在意义上相等

### 5. 超强力方法

- `Java` 程序应该从高层的设计开始
- 伪码、测试码、真实码
- 伪码描述要做什么事情而不是如何做
- 实现之前应该先编写测试码
- 使用 `Interger.parseInt()` 来取得 `String` 的整数值

### 6. 认识 `Java` 的 `API`

- `ArrayList` 方法
    - `add(Object elem)`
    - `remove(int index)`
    - `remove(Object elem)`
    - `contains(Object elem)`
    - `isEmpty()`
    - `indexOf(Object elem)`
    - `size()`
    - `get(int index)`
- `ArrayList` 自动调整大小
- 一般数组在创建时就必须确定大小
- 存放对象给一般数组时必须指定位置，`ArrayList` 直接 `add`
- 一般数组使用特殊的语法 `[]`
- `ArrayList` 类似于 `C++` 中的模板类
- 在 `Java` 中，类被包装在包中
- 数组用 `length` 这个变量取得大小
- 类有完整的名称，都是由包的名称与类的名称所组成的。`ArrayList` 实际上叫做 `java.util.ArrayList`

### 7. 继承与多态

- is-a：是一个对象
- has-a：是一个实例变量
- 继承概念下的 is-a 是个单向的关系
- 在子类可以不用完全覆盖掉父类的功能，只是再加上额外的行为，可以用 `super` 关键字取用父类，且必须是第一条语句
- `public` 类型的成员（实例变量和方法）会被继承
- `private` 类型的成员（实例变量和方法）不会被继承
- 子类是父类 `extends` 来的
- 继承下来的方法可以被覆盖掉，但实例变量不能被覆盖掉
- 继承避免了重复的程序代码，定义出共同的协议
- 运用多态时，引用类型可以是实际对象类型的父类
- 参数和返回类型也可以多态
- 非公有的类只能被同一个包的类继承
- 使用 `final` 修饰的类不能被继承
- 拥有 `private` 构造函数的类不能被继承
- 覆盖的规则：参数必须要一样，返回类型必须要兼容；不能减低方法的存取权限

### 8. 接口和抽象类

- `abstract class Myclass extends Object {}`
- `public abstract void eat();`
- 含有抽象方法的类一定是抽象类
- 抽象的类可以带有抽象的和非抽象的方法
- 抽象方法没有内容，他的声明以分号结束，只是为了标记多态而存在，在继承树结构下的第一个具体类必须要实现所有的抽象方法
- `Java` 所有类都是从 `Object` 类继承而来
    - `equals(Object c)`
    - `getClass()`
    - `hashCode()`
    - `toString()`
- 任何从 `ArrayList<Object>` 取出的东西都会被当做 `Object` 类型的引用而不管他原来是什么
- 不管实际上所引用的对象是什么类型，只有在引用变量的类型就是带有某方法的类型时才能调用该方法
- `Father father = new Son()` 是**父类引用指向子类对象**而不是父类对象指向子类引用
- **子类的引用不能指向父类的对象**
- **当使用多态方式调用方法时，首先检查父类中是否有该方法，如果没有，则编译错误；如果有，再去调用子类的同名方法**
- 多态：继承、重写、父类引用指向子类对象
- `a instanceOf b` 判断 a 是不是 b 的对象
- 多重继承，致命方块 ---> 接口
- 接口的定义 `public interface Pet {...}`
- 接口的实现 `public class Dog extends Canine implements Pet {...}`
- 接口的方法默认是 `public` 和 `abstract` 的
- 不同继承树的类也可以实现相同的接口
- **如果想要定义出类扮演的角色，使用接口**
- `Java` 不允许多重继承
- 接口就好像 100\% 纯天然抽象类
- `class` 可以实现多个接口
- 实现接口的类必须实现他的所有方法

### 9. 构造器与垃圾收集器

- 对象的生存空间是堆（heap），方法调用及变量的生存空间是栈（stack）
- 非 `primitive` 的变量只是保存了对象的引用而已，如果局部变量是对象的引用，只有变量本身会放在栈上，对象在堆上
- 实例变量存在于对象所属的堆空间上
- 如果实例变量全是主数据类型，`Java` 会依据主数据类型的大小为该实例变量留下空间
- 如果实例变量是个对象，`Java` 会给变量的值留下空间，至于所指的对象是否在堆上，要看此实例变量有没有被赋值
- 唯一能够调用构造函数的方法就是新建一个类
- 构造函数没有返回值
- `Java` 可以有与类同名的函数而不会变成构造函数，只要其有返回值即可
- 最好要有不带参数的构造函数，让人可以选择使用默认值
- 编译器只会在你完全没有设定构造函数时才会调用
- 可以使用 `this` 从某个构造函数调用同一个类的另一个构造函数，` this()` 只能用在构造函数中，且必须是第一条语句，`super()` 和 `this` 不可兼得

### 10. 数字与静态

- 在 `Math` 这个类中所有的方法都不需要实例变量值，因为这些方法都是静态的，所以你无须实例，你会用到的只有他的类本身
- `Math` 的构造函数是私有的，你不能创建他的实例
- 如果类只有静态的方法，你可以将构造函数标记为 `private` 以避免被初始化
- 静态方法是属于类本身的
- `static` 关键字
- 静态的方法不能调用非静态的变量和非静态的方法
- 虽然可以用类的实例调用静态方法，但是尽量避免
- 静态变量被所有的实例共享
- 静态变量会在该类的任何静态方法执行之前就初始化
- 静态变量的默认值等于该变量类型的默认值
- 静态的 `final` 变量是常数
- 常数变量的名称应该都大写
- 静态初始化程序是一段在加载类时会执行的程序代码，它会在其他程序可以使用该类之前就执行，所以很适合放静态 `final` 变量的初始程序
- 静态 `final` 变量的初始化：声明的时候、在静态初始化程序中
- `Math` 的方法
    - `Math.random()`：0.0~1.0 之间的双精度浮点数
    - `Math.abs()`：有重载的版本，传入整数会返回整数，双精度会返回双精度
    - `Math.round()`：有重载的版本，根据传入是浮点还是双精度，四舍五入返回整型或长整型
    - `Math.min()`：有 `int`、`long`、`float` 和 `double` 重载的版本
    - `Math.max()`：有 `int`、`long`、`float` 和 `double` 重载的版本
- 包装类
    - `Boolean`
    - `Character`
    - `Byte`
    - `Short`
    - `Integer`
    - `Long`
    - `Float`
    - `Double`
- + 是 `Java` 唯一重载过得运算符，`String str = "" + 12;`
- 数字格式化 `String.format()`
- `%[参数][标记][宽度][.精度]type`，标记比如数字逗号分隔或正负号，参数是指哪一个
- 完整的日期和时间 `String.format("%tc", new Date());`
- 只有时间 `String.format("%tr", new Date());`
- 周，月，日 `String.format("%tA, %<tB, %<td", new Date());`
- 用 `java.util.Calendar` 操作日期，是抽象类
- `Calendar cal = Calendar.getInstance();` 一般会返回一个 `java.util.GregorianCalendar` 实例
- 可以静态导入，类似于 C++ 的命名空间

### 11. 异常处理

- 异常是一种 `Exception` 类型的对象
- 除了 `RuntimeExceptions` 之外，编译器保证：如果你有抛出异常，一定要使用 `throw` 来声明这件事；如果你调用会抛出异常的方法，你必须的确认你知道异常的可能性（try catch 或者继续抛出）
- `finally` 块是用来存放不管有没有异常都得执行的程序，即使前面有 `return` 也要执行
- 有多个 `catch` 块时要从小到大排列

### 12. 图形用户接口

- GUI 从创建窗口开始 `JFrame frame = new JFrame();`
- 加入组件 `frame.getContenPane().add(button);`
- `JFrame` 与其他组件不同，不能直接加上组件，要用他的 content pane
- 显示窗口 `frame.setSize(300, 300); frame.setVisible(true);`
- 监听 GUI 事件才知道用户对接口做了什么事情
- 你必须要对事件源注册所要监听的时间。事件源是一种会根据用户操作而触发的机制
- 事件注册 add<EventType>Listener `button.addActionListener(this);`
- 内部类可以使用外部所有的方法与变量
- 内部类的实例一定会绑定外部类的实例上
- 你也可以从外部类以外的程序代码来初始化内部实例
```
    class Foo {
        public static void main (String[] args) {
            MyOuter outerObj = new MyOuter();
            MyOuter.MyInner innerObj = outerObj.new MyInner();
        }
    }
```
- 内部类提供了在一个类中实现同一接口的多次机会

### 13. swing

- 布局管理器：
    - `Borderlayout` 五个区域，框架默认
    - `Flowlayout` 书写顺序，面板默认
    - `Boxlayout` 垂直排列

### 14. 序列化和文件的输入输出

- 将序列化对象写入文件
```
    FileOutputStream fileStream = new FileOutputStream("filename");
    ObjectOutputStream os = new ObjectOutputStream(fileStream)
    os.writeObject(obj);
    os.close();
```
- 解序列化
```
    FileInputStream fileStream = new FileInputStream("filename");
    ObjectInputStream os = new ObjectInputStream(fileStream);
    Object obj = os.readObject();
    os.close();
```
- 当对象呗序列化时，该对象的实例变量也会被序列化，且所有被引用的对象也被序列化
- 如果想让类能够被序列化，就实现 `Serializable`，这是一个 tag 标记接口，没有任何方法需要实现，唯一的目的就是声明他的类是可以被序列化的
- 如果某实例变量是不能或不应该被序列化的，就把他标为 `transient`
- 解序列化时，新的对象会被放在堆上，但构造函数不会执行
- 如果对象在继承树上有个不可序列化的祖先类，则该类和之上类的构造函数就会执行
- 对象的实例变量会被还原成序列化时点的状态值，`transient` 变量会被赋值 `null` 的对象引用或主数据的默认值
- 静态变量属于类，不会被序列化
- 将字符串写入文本
```
    try {
        FileWriter writer = new FileWriter("filename");
        writer.write("hello world");
        writer.close();
    } catch(IOException ex) {
        ex.printStackTrace();
    }
```
- 读取文本文件
```
    try {
        File myFile = new File("filename");
        FileReader fileReader = new FileReader(myFile);
        BufferedReader reader = new BufferedReader(fileReader);
        String line = null;
        line = reader.readLine();
        reader.close();
    } catch(Exception ex) {
        ex.printStackTrace();
    }
```
- `java.io.File` 类代表磁盘上的文件
- 创建代表存盘文件的对象
```
    File f = new File("filename");
```
- 建立新目录
```
    File dir = new File("dirname");
    dir.mkdir();
```
- 列出目录下的内容
```
    if (dir.isDirectory()) {
        String[] dirContents = dir.list();
        for (Sting file : dirContents) {
            System.out.println(file);
        }
    }
```
- 每当对象被序列化时，该对象都会有一个版本 ID，可自己在类中定义
```
    static final long serialVersionUID = -7526832723882L;
```

### 15. 网络联机

- 读取数据
```
    Socket chatSocket = new Socket("196.164.1.103", 5000)`;
    InputStreamReader stream = new InputStreamReader(chatSocket.getInputStream());
    BufferedReader reader = new BufferedReader(stream);
    String message = reader.readLine();
```
- 写数据
```
    Socket chatSocket = new Socket("196.164.1.103", 5000)`;
    PrintWriter writer = new PrintWriter(chatSocket.getOutputStream());
    writer.println("message to send");
    writer.print("another message");
```
- TCP 端口是一个 16 位宽，用来识别服务器上特定程序的数字
- HTTP：80、Telnet：23、POP3：110、SMTP：25、FTP：20、HTTPS：443、Time：37
- 0~1023 的 TCP 端口号是留给已知的特定服务的
- 我们可以使用 1024~65535 之间的端口
- 通信
```
    ServerSocket serverSock = new ServerSocket(4242);
    Socket chatSocket = new Socket("196.164.1.103", 4242)`;
    Socket sock = serverSock.accept();
```
- 服务器可以使用 `ServerSocket` 来等待用户对特定端口的请求，当接受到请求后，他会做一个 `Socket` 连接来接受客户端的请求
- 启动新的线程
```
    Runnable threadJob = new MyRunnable();
    Thread myThread = new Thread(threadJob);
    myThread.start();
```
- `Runnable` 这个接口只有一个 `run()` 方法
- 线程的 `sleep()` 这个方法能够保证一件事，在指定的沉睡时间之前，昏睡的线程一定不会被唤醒
- `Java` 中每个线程都有独立的执行空间
- 要把 `Runnable` 传给 `Thread` 的构造函数才能启动新的线程
- `start()` 之前，线程处于新建立的状态
- 使用 `synchronized` 关键字来修饰方法使他每次只能被单一的线程存取
- `synchronized` 关键字代表线程需要一把钥匙来存取被同步化过的线程
- 要保护数据，就把作用在数据上的方法给同步化
- 锁是配在对象上的，锁住的是存取数据的方法
- 同步化一部分
```
    public void go() {
        doStuff();

        synchronized(this) {
            criticalStuff();
            moreCriticalStuff();
        }
    }
```
- `Java` 没有处理死锁的机制，他甚至不会知道死锁的发生
- `sleep()` 方法可能抛出 `InterruptedRxception` 异常，所以要包在 `try/cathc` 里或者把他声明出来
- 可以用 `setName()` 方法给线程命名
- 类本身也有锁，保护静态变量

### 16. 集合与泛型

- `TreeSet`、`LinkedHashList`、`HashSet`
- `ArrayList`、`LinkedList`、`Vector`
- `TreeMap`、`HashMap`、`LinkedHashMap`、`Hashtable`
- `Collections.sort(List list);`
- `TreeSet` 自动排序
- 在泛型中，`extend` 代表 `extend` 或 `implement`
- `sort()` 可以提供第二个比较器参数
- `List` 存储对象的引用，可重复引用相同对象
- `SET` 不允许重复
- `MAP` 键不可重复，值可重复
- `HashSet` 用 `hashCode()` 和 `equals()` 检查重复
- 数组的类型是在运行期检查的，集合的类型是在编译期检查的
- 万用字符
```
    public void takeAnimals(Array<? entends Animal> animals) {
        for (Animal a : animals) {
            a.eat();
        }
    }
```
- 在方法参数中使用万用字符时，编译器会阻止任何可能破坏引用参数所指集合的行为
- 下面的声明都对
```
    public <T extends Animal> void takeThing(ArrayList<T> list)
    public void takeThing(ArrayList<? extends Animal> list)
```

### 17. 包、jar 存档文件和部署

- 将源代码与类文件分离，一般建立 **source** 和 **classes** 目录，将源代码存储在 source 下，编译时加 **-d** 编译选项把类文件输出到 classes 目录
- 把程序包进 jar（Java Archive），这种文件是个 **pkzip** 格式文件，可执行的 JAR 代表用户不需要吧文件抽出来就能运行，方法是建立 **manifest** 文件，它会带有 JAR 的信息，告诉 JVM 哪个类含有 `main()` 方法
- manifest.txt 文件包括：`Main-Class: MyApp` 在此行要有换行，此文件放在 **classes** 目录下
```
    % cd MiniProject/classes
    % jar -cvmf manifest.txt app1.jar *.class
    // 或
    % jar -cvmf manifest.txt app1.jar MyApp.class
```
- 执行，直接双击 jar 文件或者 `% jave -jar app1.jar`
- 用包防止类名称冲突
- 反向域名.工程名.类名
- 你必须把类放在与包层级结构相同的目录下
- 把类加入到包中 `package 反向域名.工程名;`，一般让类位于完整名称的目录下
- 编译和执行包
```
    % javac -d ../classes com/headfirstjava/PackageExercise.java
    // 或编译包里的所有文件
    % javac -d ../classes com/headfirstjava/*.java
    // 执行
    % java ../classes/com.headfirstjava.PackageExercise
```
- -d 选项会要求编译器将结果根据包的结构来建立目录并输出，如果目录还没有建好，编译器会自动处理这些工作
- 从包创建可执行的 JAR
    - 包的第一层目录必须是 JAR 的第一层目录
    - 在 manifest 文件中加入完整的类名称 Main-Class: com.headfirstjava.PackageExercise
    - 执行 jar 工具，只要从 com 开始就行
    ```
        % cd MyProject/classes
        % jar -cvmf manifest.txt packEx,jar com
    ```
- 解压
```
    % jar -tf packEx.jar
    // 或
    % jar -xf packEx.jar
```
- **Java Web Start** 工作方式
    - 客户点击某个网页上 JWS 应用程序的链接（.jnlp 文件）
    ```
        <a href="MyApp.jnlp">Click</a>
    ```
