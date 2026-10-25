# 敖董的拼豆工坊

在线拼豆图纸绘制工具 —— 纯前端单文件应用，打开即用，数据保存在浏览器本地。
ai辅助产物

**在线使用**：https://你的用户名.github.io/pinzhu-gongfang/（开启 Pages 后生效）

## 功能

- 画板绘图：画笔 / 橡皮 / 吸色 / 直线 / 填充，支持 Ctrl+Z 撤销、Ctrl+Y 重做
- 色号调色板（Mard 拼豆色系），自动用料清单统计
- 编码导入 / 导出（纯文本格式，可直接粘贴到微信分享）
- PNG 效果图导出
- 内置示例模板、小狼崽底图
- 本地作品库（localStorage 自动保存）

## 文件说明

| 文件 | 说明 |
|---|---|
| `index.html` | 成品（单文件，包含全部功能与数据，直接打开即用） |
| `template.html` | 源码模板（占位符版本，改功能用这个） |
| `build.py` | 构建脚本：`python build.py` 把调色板/底图/模板/logo 注入模板生成 index.html |
| `logo_pattern.json` | 站点 logo 图案（8×8 珠子矩阵） |

## 本地开发

```bash
# 修改 template.html 或 logo_pattern.json 后重新构建
python build.py
```

## License

MIT
