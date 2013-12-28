// 创建索引
db.people.ensureIndex({"username": 1});
// 索引的方向
db.people.ensureIndex({"username": 1, "age": -1}); // 用户名严格按照升序排列，相同的用户名下，按年龄降序排列

// 扩展索引
db.status.ensureIndex({"user": 1, "date": -1}); // 对用户和日期的查询很快，但不是最好的方式
db.status.ensureIndex({"date": -1, "user": 1}); // 改变索引的顺序，把日期排在前面，可以减少内存的交换

// 索引内嵌文档的键
db.blog.ensureIndex({"comments.date": 1});

// 索引名称
db.foo.ensureIndex({"a": 1, "b": 1, "c": 1}, {"name": "alphabet"}); // 第二个参数就是索引的名字

// 唯一索引
db.people.ensureIndex({"username", 1}, {"unique": true});

// 唯一索引消除重复
db.people.ensureIndex({"username", 1}, {"unique": true, "dropDups": true});

// 修改索引
db.people.ensureIndex({"username": 1}, {"background": true}); // background参数表示在后台创建索引，不会引起阻塞

// 删除索引
db.runCommand({"dropIndexes": "foo", "index": "alphabet"}); // 删除foo集合下的alphabet索引
db.runCommand({"dropIndexes": "foo", "index": "*"}); // 删除foo集合下的所有索引

// 地理空间索引
db.map.ensureIndex({"gps": "2d"}); //创建地理空间索引
// gps的格式
{"gps": [0, 100]};
{"gps": {"x": -30, "y":30}};
{"gps": {"latitude": -180, "longtitude": 180}} // 默认情况下，地理空间索引的范围是-180到180，对经纬度来说很方便
// 创建一个2000光年见方的空间索引
db.star.trek.ensureIndex({"light-years": "2d"}, {"min": -1000, "max": 1000});

// 地理空间查询
db.map.find({"gps": {"$near": [40, -73]}}); // 离点[40, -73]由远及近的方式返回map集合的所有文档，默认返回100个
db.map.find({"gps": {"$near": [40, -73]}}).limit(10); // find() near查询不会返回每个文档到查询点的距离，但是如果返回结果大于4MB，这是唯一的选择
db.runCommand({"geoNear": "map", "near": [40, -73], "num": 10}); // geoNear会返回每个文档到查询点的距离
// 查找指定形状内的文档
db.map.find({"gps": {"$within": {"$box": [[10, 20], [15, 30]]}}}); // 矩形
db.map.find({"gps": {"$within": {"$center": [[12, 25], 5]}}}); // 圆形

// 复合地理空间索引
db.map.ensureIndex({"location": "2d", "desc": 1}); // 建立索引
db.map.find({"location": {"$near": [-80, 30]}, "desc": "coffeeshop"}).limit(1); // 查找离目标点最近的咖啡馆

