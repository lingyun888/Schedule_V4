import matplotlib.pyplot as plt


class ResourceUsagePlot:
    def __init__(self, num_links):
        self.num_links = num_links

    def draw_grid_lines(self, ax):
        # 画16条线
        for row in range(self.num_links + 1):
            ax.axhline(y=row, color='black', linewidth=2)
        # 画16条线
        for col in range(self.num_links + 1):
            ax.axvline(x=col, color='black', linewidth=2)

    def plot_resource_usage_top_row(self):
        fig, ax = plt.subplots()

        self.draw_grid_lines(ax)

        # 绘制位于第一列的蓝色矩形，其中 row = 14 的矩形会被上色
        for row in range(self.num_links):
            color = 'blue' if row == 14 else 'white'
            ax.add_patch(plt.Rectangle((0, row), 1, 1, color=color))

        # 设置 x 和 y 轴的刻度
        ax.set_xticks(range(self.num_links))
        ax.set_yticks(range(self.num_links))

        # 设置 x 轴刻度标籤，并进行旋转和对齐
        ax.set_xticklabels([f'Time {i + 1}' for i in range(self.num_links)], rotation=45, ha='center')
        ax.set_yticklabels([f'Link {i}' for i in range(self.num_links, 0, -1)], va='center')

        ax.set_xlim(0, self.num_links)
        ax.set_ylim(0, self.num_links)
        # 默认情况下，Matplotlib 的坐标轴纵横比是 "auto"，这意味著 Matplotlib 会根据图形的数据范围和绘图区域的尺寸自动调整纵横比。
        # 使用ax.set_aspect('equal') 来保持纵横比为 1，从而确保在绘制时不会有形状的变形。
        # 总之，ax.set_aspect() 方法可以根据您的需求设定坐标轴的纵横比，以确保绘制的图形在输出时保持正确的形状。
        ax.set_aspect('equal')

        ax.set_xlabel('Time')
        ax.set_ylabel('Links')

        ax.set_title('Resource Usage')

        plt.tight_layout()
        plt.show()


resource_plot = ResourceUsagePlot(num_links=15)  # 创建XY各15个格子
resource_plot.plot_resource_usage_top_row()
