from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Hr(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '未登陆'),
        (STATUS_DELETE, '已登录'),
    )
    name = models.CharField(max_length=11)
    statue = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Detail(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '未审核'),
        (STATUS_DELETE, '已审核'),
    )
    SALARY_ITEMS = [
        (0, "1000-3000"),
        (1, "3000-5000"),
        (2, "5000-7000"),
        (3, "7000-以上"),
    ]
    EDUCATION_ITEMS = [
        (0, "不限制"),
        (1, "本科生"),
        (2, "硕士"),
        (3, "博士"),
    ]
    EXPERIENCE_ITEM = [
        (0, "无经验"),
        (1, "一年以上"),
        (2, "两年以上"),
        (3, "三年以上"),
    ]
    post = models.CharField(max_length=20, verbose_name="岗位")
    company = models.CharField(max_length=55, verbose_name="公司", null=True)
    company_address = models.CharField(max_length=55, verbose_name="公司地址")
    salary = models.IntegerField(choices=SALARY_ITEMS, default=0, verbose_name="工资等级")
    education = models.IntegerField(choices=EDUCATION_ITEMS, default=0, verbose_name="学历")
    experience = models.IntegerField(choices=EXPERIENCE_ITEM, default=0, verbose_name="工作经验")
    pub_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")
    title = models.CharField(max_length=20, verbose_name="标题")
    statue = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    hr = models.ForeignKey(Hr, on_delete=models.CASCADE, verbose_name="发布人")
    context = RichTextField()

    def __str__(self):
        return self.title


class Applicant(models.Model):
    STATUS_ITEMS = (
        (1, '未登录'),
        (2, '已登录'),
    )
    SEX_ITEMS = (
        (1, '男'),
        (2, '女'),
    )
    SALARY_ITEMS = [
        (0, "1000-3000"),
        (1, "3000-5000"),
        (2, "5000-7000"),
        (3, "7000-以上"),
    ]
    name = models.CharField(max_length=11, verbose_name="姓名")
    sex = models.PositiveIntegerField(default=1, choices=SEX_ITEMS, verbose_name="性别")
    telephone = models.CharField(max_length=20, verbose_name="电话")
    statue = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    a_account = models.CharField(max_length=20, verbose_name="账号")
    password = models.CharField(max_length=20, verbose_name="密码")
    station = models.CharField(max_length=10, default="无", verbose_name="岗位")
    province = models.CharField(max_length=10, default="广东省", verbose_name="省份")
    city = models.CharField(max_length=3, default="广州市", verbose_name="城市")
    salary = models.IntegerField(choices=SALARY_ITEMS, default=0, verbose_name="工资等级")
    school = models.CharField(max_length=20, default="北京理工大学珠海学院", verbose_name="学校")
    specialty = models.CharField(max_length=20, default="信息系统与信息管理", verbose_name="专业")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class Business(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Comment(models.Model):
    context = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=20)


class Type(models.Model):
    name = models.CharField(max_length=255)


class Record(models.Model):
    STATUS_ITEMS = (
        (1, '投递成功'),
        (2, '简历被查看'),
        (3, '待沟通'),
        (4, '邀请面试'),
        (5, '已录用'),
        (6, '不合适'),
    )
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")
    statue = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name="状态")
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, verbose_name="文章")
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, verbose_name="应聘者")
    hr = models.ForeignKey(Hr, on_delete=models.CASCADE, verbose_name="发布人")
