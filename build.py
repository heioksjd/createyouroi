# -*- coding: utf-8 -*-
"""把 template.html 编译成 index.html：
从旧 index.html 提取注入数据（PAL 调色板 / WOLF 小狼底图 / TPL 示例模板），
替换新模板里的占位符后写回 index.html。数据只增不减，避免手工维护。"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
old = open(os.path.join(HERE, "index.html"), encoding="utf-8").read()


def grab(name):
    key = "const %s = " % name
    i = old.index(key) + len(key)
    data, _ = json.JSONDecoder().raw_decode(old[i:])
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"))


for ph, name in (("__PALETTE_JSON__", "PAL"),
                 ("__WOLF_JSON__", "WOLF"),
                 ("__TEMPLATES_JSON__", "TPL")):
    tpl = tpl.replace(ph, grab(name))


# 站点 logo：由 logo_pattern.json（用户画板 8x8 图案）生成珠子 SVG 与 favicon
def build_logo():
    pat = json.load(open(os.path.join(HERE, "logo_pattern.json"), encoding="utf-8"))
    pal = json.loads(grab("PAL"))
    s = 10  # 每格像素
    parts = []
    for i, row in enumerate(pat):
        for j, v in enumerate(row):
            if v == ".":
                continue
            cx, cy = j * s + s / 2, i * s + s / 2
            col = pal.get(v, "#ccc")
            parts.append(f"<circle cx='{cx}' cy='{cy}' r='4.2' fill='{col}'/>")
            parts.append(f"<circle cx='{cx - 1.3}' cy='{cy - 1.5}' r='1.4' fill='rgba(255,255,255,.45)'/>")
    h = len(pat) * s
    w = len(pat[0]) * s
    svg = f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}'>" + "".join(parts) + "</svg>"
    from urllib.parse import quote
    favicon = "data:image/svg+xml," + quote(svg, safe="'" + " /=:.,()-")
    return svg, favicon


logo_svg, favicon_uri = build_logo()
tpl = tpl.replace("__FAVICON__", favicon_uri).replace("__LOGO_SVG__", logo_svg)

open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(tpl)
print("index.html 已生成，%d 字符" % len(tpl))
