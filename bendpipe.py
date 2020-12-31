import numpy as np

np.set_printoptions(formatter={'float': '{:.3f}'.format})


class BendPipe:
    def __init__(self, points, radius):
        self.points = points
        if len(self.points) < 3:
            raise ValueError("输入点数至少为3")
        self.length = len(self.points) - 2
        self.radius = radius
        self.p1 = self.points[0:-2]
        self.p2 = self.points[1:-1]
        self.p3 = self.points[2:]

    def fit(self):
        cos_alpha = [self.cos_alpha(self.p1[i], self.p2[i], self.p3[i]) if
                     self.cos_alpha(self.p1[i], self.p2[i], self.p3[i]) <= 1 else 1 for i in range(self.length)]
        self.alphas = np.arccos(np.array(cos_alpha))
        self.degrees = np.rad2deg(self.alphas)
        print('弯曲角度: ', end='')
        print(self.degrees)
        self.arcs = self.alphas * self.radius
        print('弧长: ', end='')
        print(self.arcs)
        self.degree_rotate = self.rotate_value()
        print('旋转角度: ', end='')
        print(self.degree_rotate)
        self.lines = self.line_length()
        print('直线段长度: ', end='')
        print(self.lines)
        self.total = self.total_length()
        print("下料长度: ", end='')
        print(self.total)
        max_length = len(self.lines)
        degrees = list(self.degrees) + [None] * (max_length - len(self.degrees))
        arcs = list(self.arcs) + [None] * (max_length - len(self.arcs))
        print(([list(self.lines), arcs, degrees, self.degree_rotate], self.total))
        return [list(self.lines), arcs, degrees, self.degree_rotate], self.total

    def cos_alpha(self, x1, x2, x3):
        a = np.linalg.norm(x1-x2)
        b = np.linalg.norm(x3-x2)
        if a == 0 or b ==0:
            raise ValueError("相邻的点不能相同")
        value = np.dot(x2 - x1, x3 - x2) / a / b
        return value

    def rotate_value(self):
        n_list = []
        for i in range(self.length):
            p1p2 = self.p2[i] - self.p1[i]
            p2p3 = self.p3[i] - self.p2[i]
           # a1 = p1p2[1] * p2p3[2] - p2p3[1] * p1p2[2]
           # b1 = p1p2[2] * p2p3[0] - p2p3[2] * p1p2[0]
           # c1 = p1p2[0] * p2p3[1] - p2p3[0] * p1p2[1]

            n = np.cross(p1p2, p2p3)
            #n = np.array((a1, b1, c1))
            n_list.append(n)
        degree_rotate_list = [0]
        for i in range(len(n_list) - 1):
            a = np.linalg.norm(n_list[i])
            b = np.linalg.norm(n_list[i+1])
            if a == 0 or b == 0:
                raise Warning('相邻四点共线!')
            else:
                cos_rotate = np.dot(n_list[i], n_list[i + 1]) / a / b
            radian_rotate = np.arccos(cos_rotate)
            degree_rotate = np.degrees(radian_rotate)
            degree_rotate_list.append(degree_rotate)
        # 判断旋转角度的正负
        d_list = [0]
        for i in range(self.length - 1):
            p4p1 = self.p3[i + 1] - self.p1[i]
            p2p1 = self.p2[i] - self.p1[i]
            p3p1 = self.p3[i] - self.p1[i]
            matrix = np.array((p4p1, p2p1, p3p1))
            d = np.linalg.det(matrix)
            isminus = -1 if d >= 0 else 1
            d_list.append(isminus)
        d_list = np.array(d_list)
        degree_rotate_list = degree_rotate_list * d_list
        degree_rotate_list = [None if not i else i for i in degree_rotate_list]
        return degree_rotate_list

    def line_length(self):
        def line_caculate(x1, x2, r, alpha):
            return np.linalg.norm(x1-x2) - r * np.tan(alpha / 2)

        l1_list = []
        for i in range(self.length):
            l1 = line_caculate(self.p1[i], self.p2[i], r=self.radius, alpha=self.alphas[i])
            if i != 0:
                l1 -= self.radius * np.tan(self.alphas[i - 1] / 2)
            l1_list.append(l1)
        l1_list.append(np.sqrt(np.sum((self.p3[self.length - 1] - \
                                       self.p2[self.length - 1]) ** 2)) - \
                       self.radius * np.tan(self.alphas[-1] / 2))
        return np.array(l1_list)

    def total_length(self):
        return np.sum(self.lines) + np.sum(self.arcs)

class Correct:
    def __init__(self, bendpipe, theory, reality):
        self.arcs = bendpipe.arcs
        self.degree_rotate = bendpipe.degree_rotate
        self.lines = bendpipe.lines
        self.degrees = bendpipe.degrees
        self.theory, self.reality = theory, reality
        self.radius = bendpipe.radius
    def fit(self):
        self.sections = self.section_choose()
        params = self.k_b_caculate(self.sections)
        return self.correct_cac(params)
    def section_choose(self):
        sections = []
        for degree in self.degrees:
            for i in range(len(self.theory)-1):
                if degree > self.theory[i] and degree <= self.theory[i+1]:
                    sections.append(i)
                else:
                    sections.append(None)
        return sections

    def k_b_caculate(self, sections):
        params = []
        for i in sections:
            if i is not None:
                k = (self.theory[i+1] - self.theory[i]) / (self.reality[i+1] - self.reality[i])
                b = (self.theory[i] * self.reality[i+1] - self.theory[i+1]*self.theory[i]) / \
                    (self.reality[i+1] - self.reality[i])
                params.append((k, b))
            else:
                params.append(None)
        return np.array(params)

    def correct_cac(self, params):
        self.correct_degrees = []
        for param, degree in zip(params, self.degrees):
            if param is not None:
                self.correct_degrees.append(param[0] * degree + param[1])
            else:
                self.correct_degrees.append(degree)
        degrees = np.array(self.correct_degrees)
        self.correct_arcs = self.radius * np.deg2rad(degrees - self.degrees)
        self.correct_arcs = list(self.correct_arcs)
        ls = [0]
        ls.extend(list(self.correct_arcs))
        self.correct_lines = list(self.lines - np.array(ls))
        self.correct_arcs += [None]
        self.correct_degrees += [None]
        return (self.correct_lines, self.correct_arcs, self.correct_degrees,)

if __name__ == '__main__':
    a = np.array([[0, 0, 0],
                  [0, 0, 100],
                  [0, 50, 100],

                  [200, 100, 150]])
    b = np.array([[0, 0, 0], [1, 1, 1], [3, 3, 3]])
    bend = BendPipe(b, radius=30)
    bend.fit()




