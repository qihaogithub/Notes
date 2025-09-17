scheduler

学习率调度器，有以下几种

["cosine_with_restarts", "cosine", "polynomial", "constant", "constant_with_warmup", "linear"]

不妨搜索学习率调整策略。推荐使用 cosine_with_restarts，它会使学习率从高到低下降，变化速度先慢后快再慢。restarts 表示余弦退火的热重启次数，有助于逃脱平坦区域。