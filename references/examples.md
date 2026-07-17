# Before / After Examples

Each keeps every number and citation intact and never invents a source. The point of each pair is called out.

## 1. Paper — introduction opener (English)

**Before (AI-sounding):**
> In recent years, tabular deep learning has attracted increasing attention. Additionally, an enduring testament
> to the method's value is its ability to delve into intricate dependencies, showcasing a seamless integration
> that underscores its pivotal role in the evolving landscape of the field.

**After:**
> Tabular deep learning has a structural limitation: most models discard feature-type metadata and must relearn
> it from data. Our encoder conditions on that metadata directly and recovers the higher-order dependencies the
> baselines miss (Table 2).

*Fixes: formulaic opener, AI-vocab cluster (delve/intricate/seamless/pivotal/landscape), copula avoidance,
significance hype → a concrete limitation anchored to a table.*

## 2. Paper — over-claim → evidence-matched (English)

**Before:**
> We prove that our method significantly outperforms all prior approaches, demonstrating its universal superiority.

**After:**
> Our method improves held-out accuracy by 4–7 points over the strongest prior approach (Table 3); the gain is
> significant at p < 0.01 by a paired test. We did not test domains outside the three benchmarks, so we make no
> universal claim.

*Fixes: "prove/demonstrate/universal" downgraded to match the evidence; the number and p-value are preserved
verbatim; the scope limit is stated rather than hidden.*

## 3. 摘要 opener (中文)

**Before（AI 腔）：**
> 随着人工智能技术的快速发展，图神经网络已经成为备受关注的研究热点。本文创新性地提出了一种全新的框架，
> 大量实验充分证明了该方法的显著优越性，为该领域的发展提供了重要的参考价值。

**After：**
> 图神经网络在长程依赖上仍存在信息过压缩（over-squashing）问题。本文提出一种基于曲率重连的框架，在三个基准
> （ogbn-arxiv、Cora、PubMed）上将节点分类准确率相对最强基线提升 1.8–3.2 个百分点（表 2），在长程任务上的
> 增益更明显。

*修复：套话开场、"创新性/全新/大量/充分证明/显著/重要参考价值" 拔高 → 具体问题 + 具体数据集 + 带表引用的
数值范围；数字与括注保持原样，不新增来源。*

## 4. 长文 `bounded` scope — deletion list (中文)

**输入段落：**
> 我们的方法在多个数据集上都取得了很好的效果。值得注意的是，这充分说明了该方法的有效性。总的来说，
> 该方向是非常有前景的。

**输出（正文，句内洗）：**
> 我们的方法在 CIFAR-100、iNaturalist 和 ImageNet 上分别取得 X/Y/Z 的准确率（表 3）。

**建议删除（待确认）：**
- `值得注意的是，这充分说明了该方法的有效性。` — 空句：剥掉引导词后只剩无源论断，删了不丢信息点。
- `总的来说，该方向是非常有前景的。` — 价值拔高收尾，无独有事实，删了不丢信息点。

*（`bounded` 不擅自删整句，只进清单交作者拍板；数字位 X/Y/Z 为占位，需作者填真实结果。）*

## 5. Reviewer response (English)

**Before:**
> We thank the reviewer for the excellent and insightful comment. We have significantly improved the paper and
> fully addressed this concern.

**After:**
> On the reviewer's point about baseline strength: we added GraphGPS as a stronger baseline (new Table 4). Our
> method still leads by 1.4 points on ogbn-arxiv; on Cora the gap narrows to 0.3 points, within one standard
> deviation, which we now state in Section 5.2.

*Fixes: sycophancy and the unverifiable "fully addressed" → a specific change tied to a named baseline, a table,
and an honest statement of where the advantage is small.*

## 6. Grant — vague importance → cost-of-the-gap (proposal register kept)

**Before:**
> Understanding this problem is critically important and has many potential applications.

**After:**
> Without bounds on how measurement noise propagates to diagnosis, clinical models are tuned by trial and error.
> This proposal removes that inefficiency, and our preliminary result (Fig. 1) shows the bound is achievable on
> two of the three target assays.

*Fixes: vague importance → concrete cost of the gap; ambition/vision is kept (proposal register), and it is now
tied to a real preliminary result rather than left as an assertion.*
