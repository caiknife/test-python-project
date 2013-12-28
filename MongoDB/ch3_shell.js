// 插入并保存文档
db.foo.insert({"bar": "baz"});

// 文档替换
db.users.insert({"name": "joe", "friends": 32, "enemies": 2});
var joe = db.users.findOne({"name": "joe"});
joe.relationships = {"friends": joe.friends, "enemies": joe.enemies};
joe.username = joe.name;
delete joe.friends;
delete joe.enemies;
delete joe.name;
db.users.update({"name": "joe"}, joe);
