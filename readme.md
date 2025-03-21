预览github仓库里面的html
http://htmlpreview.github.io/

http://htmlpreview.github.io/?https://github.com/sion567/words/blob/main/jp/20250305.html

#### 🔴🟠🟡🟢🔵 艾宾浩斯五阶色标方案

| 复习阶段 | 时间间隔      | 色标(HEX) | 视觉标记     | 应用场景示例       | 神经科学依据        |
| ---- | --------- | ------- | -------- | ------------ | ------------- |
| 即刻巩固 | 5分钟       | #FF4444 | 🔴 红底白字  | 课堂笔记即时标注重点词汇 | 海马体短期记忆编码关键期‌ |
| 短期强化 | 30分钟/12小时 | #FFA726 | 🟠 橙底黑字  | 午休前整理错题本     | 前额叶皮层信息整合阶段‌  |
| 中期稳定 | 1天/2天     | #FFF176 | 🟡 黄底黑条纹 | 次日早读卡片复习     | 杏仁核情绪记忆关联形成‌  |
| 长期固化 | 4天/7天     | #9CCC65 | 🟢 绿渐变图标 | 周计划表模块化复习区   | 新皮层神经网络重构完成‌  |
| 永久记忆 | 15天+      | #42A5F5 | 🔵 蓝底波浪线 | 月总结知识图谱节点标记  | 基底神经节程序性记忆存储‌ |

## 色标应用细则

#### ‌色阶过渡原理‌

暖色系（红→橙→黄）对应高遗忘风险期，需高频刺激‌15

冷色系（绿→蓝）反映记忆稳定度提升，降低复习密度‌8

#### ‌动态调整机制‌

连续三次正确回忆后，色标降阶处理（如🔴→🟠）‌57

错误率＞20%时逆向升阶（如🟢→🟡）‌6

#### ‌多场景适配‌

数字工具：

```css
/* Anki卡片模板示例 */
.eb-red {background: #FF4444; border-left: 5px solid #D32F2F}
.eb-blue {background: #42A5F5; box-shadow: 0 2px 4px rgba(66,165,245,0.3)}F5"  

```

多模态编码技术:

```python
# 自动色标生成算法示例  
def get_color_tag(review_count, error_rate):  
    if review_count < 3: return "#FF4444"  
    elif error_rate > 0.2: return "#FFA726"  
    elif review_count % 7 == 0: return "#9CCC65"  
    else: return "#42A5F5"  

```