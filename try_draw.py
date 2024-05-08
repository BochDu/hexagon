import turtle

import math

side_pixel = 20
gap_pixel_x = int (side_pixel * math.sqrt(3))
gap_pixel_x_offset = int (side_pixel * math.sqrt(3) / 2) 
gap_pixel_y = int (1.5 * side_pixel)

# 创建Turtle对象
t = turtle.Turtle()
t.speed(0)  # 设置绘制速度为最快

# 定义函数来绘制六边形
def draw_hexagon(x, y, color_index):
    colors = ['grey', 'black', 'blue']  # 三种颜色
    heading = t.heading()  # 保存当前朝向
    t.penup()  # 抬起画笔
    t.goto(x, y)  # 移动到指定位置
    t.pendown()  # 落下画笔
    t.fillcolor(colors[color_index])  # 填充颜色
    t.begin_fill()  # 开始填充
    for _ in range(6):
        t.forward(side_pixel)  # 向前移动100个像素
        t.right(60)  # 向右旋转60度
    t.end_fill()  # 结束填充
    t.setheading(heading)  # 恢复到原始朝向

t.right(30)

random_blue_array = [
    [1, 1, 2, 1, 1, 2, 2, 1, 1, 2],
    [2, 1, 1, 1, 2, 1, 2, 1, 1, 2],
    [2, 2, 2, 1, 1, 2, 1, 1, 1, 1],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [2, 1, 0, 1, 1, 0, 1, 1, 1, 2],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [2, 1, 1, 0, 1, 0, 1, 1, 1, 2],
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 1]
]

m = len(random_blue_array)
n = len(random_blue_array[0])  # 假设所有行都有相同数量的列

print(f"m: {m}")
print(f"n: {n}")

for i in range(0,m,1):
    for j in range(0,n,1):
        if i % 2 == 0:
            draw_hexagon(gap_pixel_x * j , - gap_pixel_y * i ,random_blue_array[i][j])
        else:
            draw_hexagon(gap_pixel_x_offset + gap_pixel_x * j , - gap_pixel_y * i ,random_blue_array[i][j])

# 绘制网状结构
# for i in range(0, gap_pixel_x*m, gap_pixel_x):
#     for j in range(0, gap_pixel_y*n, gap_pixel_y):
#         if 
#         draw_hexagon(i, j,2)  # 绘制一个六边形

# 隐藏Turtle箭头
t.hideturtle()

# 保持窗口打开
turtle.done()







