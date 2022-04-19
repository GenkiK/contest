class UnionFind:
    """
    ・各要素は番号で管理
    ・par[x] == x ならば x は木の根
    """

    def __init__(self, num: int):
        self.par = [0] * num
        for i in range(num):
            self.par[i] = i
        self.rank = [0] * num

    # 木の根を求める
    def find(self, x: int) -> int:
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])  # 縮約
            return self.par[x]

    # xとyの属する集合をマージ
    def unite(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:  # rankが同じときのみ根となった木のrankが大きくなる
                self.rank[x] += 1

    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
