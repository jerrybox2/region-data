# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.functional import cached_property


def populate_tree(node, grade):
    """
    递归遍历树节点，遍历到层级为grade结束遍历
    Example：
        populate_tree(node(name="河北省"), grade="county")  # 省-市-县
        populate_tree(node(name="河北省"), grade="city")  # 省-市
        {
            "data": {
                "name": "河北省",
                "code": "130000",
                "children": [
                    {
                        "name": "石家庄市",
                        "code": "130100"
                    },
                    {
                        "name": "唐山市",
                        "code": "130200"
                    },
                    {
                        "name": "秦皇岛市",
                        "code": "130300"
                    },
                    {
                        "name": "邯郸市",
                        "code": "130400"
                    },
                    {
                        "name": "邢台市",
                        "code": "130500"
                    },
                    {
                        "name": "保定市",
                        "code": "130600"
                    },
                    {
                        "name": "张家口市",
                        "code": "130700"
                    },
                    {
                        "name": "承德市",
                        "code": "130800"
                    },
                    {
                        "name": "沧州市",
                        "code": "130900"
                    },
                    {
                        "name": "廊坊市",
                        "code": "131000"
                    },
                    {
                        "name": "衡水市",
                        "code": "131100"
                    }
                ]
            }
        }
    :param node:  区域节点对象
    :param grade: 最低的层级类型
    :return:
    """
    data = {"name": node.name,
            "code": node.code}
    if node.children.all().count() and not(node.grade == grade):
        data["children"] = []
        for child in node.children.all():
            data["children"].append(populate_tree(child, grade=grade))
    return data


class Region(models.Model):
    """
    省市县三级区域数据：
    0 整体是一个树形结构
    1 每个区域都是树上的一个节点
    2 外键关联节点间父子关系
    """
    GRADE_CHOICES = (
        ("province", 'Province'),
        ("city", 'City'),
        ("county", "County"),
    )

    code = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(to='self',
                               related_name="children",
                               related_query_name="child",
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL)
    grade = models.CharField(max_length=10, choices=GRADE_CHOICES, default="county")

    @cached_property
    def province(self):
        if self.grade == self.GRADE_CHOICES[0][0]:
            obj = self
        elif self.grade == self.GRADE_CHOICES[1][0]:
            obj = self.parent
        elif self.grade == self.GRADE_CHOICES[2][0]:
            obj = self.parent.parent
        else:
            raise Exception("Grade Error")
        data = {"obj": obj, "name": obj.name, "code": obj.code}
        return data

    @cached_property
    def city(self):
        if self.grade == self.GRADE_CHOICES[0][0]:
            data = []
            for city in self.children.all():
                obj = {"obj": city, "name": city.name, "code": city.code}
                data.append(obj)
            return data
        elif self.grade == self.GRADE_CHOICES[1][0]:
            obj = self
        elif self.grade == self.GRADE_CHOICES[2][0]:
            obj = self.parent
        else:
            raise Exception("Grade Error")
        data = {"obj": obj, "name": obj.name, "code": obj.code}
        return data

    @cached_property
    def county(self):
        if self.grade == self.GRADE_CHOICES[0][0]:
            raise Exception("Get city First")
        elif self.grade == self.GRADE_CHOICES[1][0]:
            data = []
            for county in self.children.all():
                obj = {"obj": county, "name": county.name, "code": county.code}
                data.append(obj)
            return data
        elif self.grade == self.GRADE_CHOICES[2][0]:
            obj = self
            data = {"obj": obj, "name": obj.name, "code": obj.code}
            return data

    def __str__(self):
        return self.name
