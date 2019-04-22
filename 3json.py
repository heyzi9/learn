# 导入库
import json

# json例子
json_data = {
    "results":[
        {
            "location":{
                "id":"123456",
                "name":"厦门",
                "country":"CN",
                "path":"福建，厦门",
                "timezone":"Asia/Shanghai",
                "timezone_offset":"+08:00"
            }
        }
    ]
}

b = json.dumps(json_data)
print(b,type(b))
c = json.loads(b)
print(c,type(c))