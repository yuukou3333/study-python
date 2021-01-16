# モジュールのインポート =====================

import math

# θ=π2
theta = math.pi / 2

# sinθ2+ cosθ2=1.0
ans = math.sin(theta)**2 + math.cos(theta)**2
print(ans)

# エイリアス =============================
# import後にasをつけることで別名を付けれる。

import math as m

# θ=π2
theta = m.pi / 2

# sinθ2+ cosθ2=1.0
ans = m.sin(theta)**2 + m.cos(theta)**2
print(ans)
