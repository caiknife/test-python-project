// count
db.foo.count(); // 0
db.foo.insert({"x": 1});
db.foo.count(); // 1
db.foo.insert({"x": 2});
db.foo.count(); // 2
db.foo.count({"x": 1}); // 1

// distinct
db.people.insert({"name": "Ada", "age": 20});
db.people.insert({"name": "Fred", "age": 35});
db.people.insert({"name": "Susan", "age": 40});
db.people.insert({"name": "Andy", "age": 35});
db.runCommand({"distinct": "people", "key": "age"}); // 会有详细的返回值
db.people.distinct("age"); // 只返回唯一数据

// group
db.stocks.insert({"day": "2010/10/03", "time": "2010/10/03 03:47:01 GMT-400", "price": 4.23});
db.stocks.insert({"day": "2010/10/04", "time": "2010/10/04 11:28:39 GMT-400", "price": 4.27});
db.stocks.insert({"day": "2010/10/03", "time": "2010/10/03 05:00:23 GMT-400", "price": 4.10});
db.stocks.insert({"day": "2010/10/06", "time": "2010/10/06 05:27:58 GMT-400", "price": 4.30});
db.stocks.insert({"day": "2010/10/04", "time": "2010/10/04 08:34:50 GMT-400", "price": 4.01});

db.runCommand({
    "group": {
        "ns": "stocks",
        "key": "day",
        "initial": {"time": 0},
        "$reduce": function (doc, prev) {
            if (doc.time > prev.time) {
                prev.price = doc.price;
                prev.time = doc.time;
            }
        }
    }
}); // 这里的用法是错误的

db.runCommand({
    "group": {
        "ns": "stocks",
        "key": {"day": true},
        "initial": {"time": "0"},
        "$reduce": function (doc, prev) {
            if (doc.time > prev.time) {
                prev.price = doc.price;
                prev.time = doc.time;
            }
        }
    }
}); // 用runCommand来处理

db.runCommand({
    "group": {
        "ns": "stocks",
        "key": {"day": true},
        "initial": {"price": 0},
        "$reduce": function (doc, prev) {
            prev.price += doc.price;
        }
    }
});

db.stocks.group({
    "key": {"day": true},
    "initial": {"time": "0"},
    "reduce": function (doc, prev) {
        if (doc.time > prev.time) {
            prev.price = doc.price;
            prev.time = doc.time;
        }
    },
    "condition": {"day": {"$gte": "2009/12/31"}}
}); // 用集合的group方法来处理

db.stocks.group({
    "key": {"day": true},
    "initial": {"price": 0},
    "reduce": function (doc, prev) {
        prev.price += doc.price;
    }
});

// 使用完成器
// 为标签计数
db.posts.group({
    "key": {"day": true},
    "initial": {"tags": {}},
    "$reduce": function (doc, prev) {
        for (i in doc.tags) {
            if (doc.tags[i] in prev.tags) {
                prev.tags[doc.tags[i]]++;
            } else {
                prev.tags[doc.tags[i]] = 1;
            }
        }
    }
});
// 使用finalizer
db.posts.group({
    "key": {"day": true},
    "initial": {"tags": {}},
    "$reduce": function (doc, prev) {
        for (i in doc.tags) {
            if (doc.tags[i] in prev.tags) {
                prev.tags[doc.tags[i]]++;
            } else {
                prev.tags[doc.tags[i]] = 1;
            }
        }
    },
    "finalize": function (prev) {
        var mostPopular = 0;
        for (i in prev.tags) {
            if (prev.tags[i] > mostPopular) {
                prev.tag = i;
                mostPopular = prev.tags[i];
            }
        }
        delete prev.tags;
    }
});

// 将函数作为键使用
db.posts.group({
    "$keyf": function (x) {
        return x.category.toLowerCase();
    } // 根据posts的category小写名称来group
});

// map reduce
map = function () {
    for (var key in this) {
        emit(key, {"count": 1});
    }
};

reduce = function (key, emits) {
    total = 0;
    for (var i in emits) {
        total += emits.count;
    }
    return {"count": total};
};

