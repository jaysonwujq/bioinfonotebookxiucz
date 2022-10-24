语句（声明语句，表达式语句）：1. 分号结尾；2无返回值
表达式： 1. 无结尾；返回一个值

expression -> statement 

fn add_one(x : u32) -> u32
{
    x + 1
}

在函数声明时，声明返回值是u32类型。而语句 x + 1; 的返回值是 ()。这会导致类型错误。所以，在函数返回时使用 表达式 x + 1 。不然，rust就会提醒你让你去掉分号啦。


数组
let a = [1,2,3];
println!("array 1st element = {}", a[0]); //# 下标访问
println!("array len = {}", a.len()); //数组长度

切片

loop { /* loop forever! */ }

while if_expression { /* do until expression become false */ }

for var in iterators_expression { /* do something */ }