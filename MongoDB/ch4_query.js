// 普通查询
db.users.find({"age": 27});
db.users.find({"username": "joe"});
// AND查询
db.users.find({"username": "joe", "age": 27});

// 返回指定的key
db.users.find({}, {"username": 1, "email": 1});
// 不返回指定的key
db.users.find({}, {"fatal_weakness": 0});
db.users.find({}, {"username": 1, "_id": 0});

// 条件查询
db.users.find({"age": {"$gte": 18, "$lte", 30}});
// 日期条件查询
var start = new Date("01/01/2007");
db.users.find({"registered": {"$lt": start}});
// 不等查询
db.users.find({"username": {"$ne": "joe"}});
// IN查询
db.raffle.find({"ticket_no": {"$in": [725, 542, 390]}});
db.users.find({"user_id": {"$in"：[12345, "joe"]}});
// NOT IN查询
db.raffle.find({"ticket_no": {"$nin": [725, 542, 390]}});
// OR查询
db.raffle.find({"$or": [{"ticket_no": 725}, {"winner": true}]});
db.raffle.find({"$or": [{"ticket_no": {"$in": [725, 542, 390]}}, {"winner": true}]});
// $not查询
db.users.find({"id_num": {"$mod": [5, 1]}}); //返回被5取模余1的数据
db.users.find({"id_num": {"$not": {"$mod": [5, 1]}}}); //返回被5取模不余1的数据

// 特定类型查询
// null查询
db.c.find({"y": null}); //不仅匹配自身，还匹配所有不存在的数据
db.c.find({"z": {"$in": [null], "$exists": true}}); //要检查该键的值是否为null，还要检查该键是否存在

// 正则表达式
db.users.find({"username": /joe/i});
db.users.find({"username": /joey?/i});
// 把正则表达式插入到数据库内，还是可以自身匹配的
db.foo.insert({"bar": /baz/});
db.foo.find({"bar": /baz/});

// 查询数组
// $all查询，找到既有apple又有banana的文档
db.food.find({"fruit": {"$all": ["apple", "banana"]}});
// 精确匹配
db.food.find({"fruit": ["apple", "banana", "peach"]});
// 根据数组索引匹配
db.food.find({"fruit.2": "peach"});
// $size查询
db.food.find({"fruit": {"$size": 3}});
// 查询长度范围，增加一个size键，但是这种技巧不能和$addToSet同时使用
db.food.update({"$push": {"fruit": "strawberry"}, "$inc": {"size": 1}});
db.food.find({"size": {"$gt": 3}});

// $slice操作符
// 返回前10条评论
db.blog.posts.findOne(criteria, {"comments": {"$slice": 10}});
// 返回后10条评论
db.blog.posts.findOne(criteria, {"comments": {"$slice": -10}});
// 返回第24-33条评论
db.blog.posts.findOne(criteria, {"comments": {"$slice": [23, 10]}});

// 查询内嵌文档
// 查询整个文档
db.people.find({"name": {"first": "Joe", "last": "Schmoe"}});
// 只针对键值查询，对一个内嵌文档的多个键操作时才会用到
db.blog.find({"comments": {"$elemMatch": {"author": "joe", "score": {"$gte": 5}}}});

// $where查询
db.foo.insert({"apple": 1, "banana": 6, "peach": 3});
db.foo.insert({"apple": 8, "spinach": 4, "watermelon": 4});
db.foo.find({"$where": function() {
    for (var current in this) {
        for (var other in this) {
            if (current!=other && this[current]==this[other]) {
                return true;
            }
        }
    }
    return false;
}});

// limit
db.c.find.limit(3); //返回前3条数据
// skip
db.c.find.skip(3); // 略过前3条数据，返回剩下的数据
// sort
db.c.find.sort({"username": 1, "age": -1});
db.stock.find({"desc": "mp3"}).limit(50).sort({"price": -1});
db.stock.find({"desc": "mp3"}).limit(50).skip(50).sort({"price": -1});

